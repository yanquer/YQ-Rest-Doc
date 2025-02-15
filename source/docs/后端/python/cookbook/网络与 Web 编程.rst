=================================
网络与 Web 编程
=================================

本章是关于在网络应用和分布式应用中使用的各种主题。主题划分为使用 Python
编写客户端程序来访问已有的服务，以及使用 Python 实现网络服务端程序。也给出了
一些常见的技术，用于编写涉及协同或通信的的代码。

作为客户端与 HTTP 服务交互
=================================

问题
  你需要通过 HTTP 协议以客户端的方式访问多种服务。例如，下载数据或者与基
  于 REST 的 API 进行交互。

解决方案
  对于简单的事情来说，通常使用 urllib.request 模块就够了。例如，发送一个简
  单的 HTTP GET 请求到远程的服务上，可以这样做::

    from urllib import request, parse

    # Base URL being accessed
    url = 'http://httpbin.org/get'

    # Dictionary of query parameters (if any)
    parms = { 'name1' : 'value1', 'name2' : 'value2' }

    # Encode the query string
    querystring = parse.urlencode(parms)

    # Make a GET request and read the response
    u = request.urlopen(url+'?' + querystring)
    resp = u.read()

  如果你需要使用 POST 方法在请求主体中发送查询参数，可以将参数编码后作为
  可选参数提供给 urlopen() 函数，就像这样::

    # Make a POST request and read the response
    u = request.urlopen(url, querystring.encode('ascii'))
    resp = u.read()

  如果你需要在发出的请求中提供一些自定义的 HTTP 头，例如修改 user-agent 字 段,
  可以创建一个包含字段值的字典，并创建一个 Request 实例然后将其传给 urlopen()
  ，如下::

    from urllib import request, parse
    ...
    # Extra headers
    headers = { 'User-agent' : 'none/ofyourbusiness', 'Spam' : 'Eggs' }
    req = request.Request(url, querystring.encode('ascii'), headers=headers)
    # Make a request and read the response
    u = request.urlopen(req)
    resp = u.read()

  如果需要交互的服务比上面的例子都要复杂，也许应该去看看 requests 库::

    resp = requests.post(url, data=parms, headers=headers)

  关于 requests 库，一个值得一提的特性就是它能以多种方式从请求中返回响应结
  果的内容。

  - resp.text 带给我们的是以 Unicode 解码的响应文本
  - resp.content ，就会得到原始的二进制数据
  - resp.json ，那么就会得到 JSON 格式的响应内容

  利用 requests 通过基本认证登录 Pypi ::

    import requests
    resp = requests.get('http://pypi.python.org/pypi?:action=login',
                        auth=('user','password'))

  利用 requests 将 HTTP cookies 从一个请求传递到另一个的例子::

    import requests
    # First request
    resp1 = requests.get(url)
    ...
    # Second requests with cookies received on first requests
    resp2 = requests.get(url, cookies=resp1.cookies)

  最后但并非最不重要的一个例子是用 requests 上传内容::

    import requests
    url = 'http://httpbin.org/post'
    files = { 'file': ('data.csv', open('data.csv', 'rb')) }
    r = requests.post(url, files=files)

讨论
  对于真的很简单 HTTP 客户端代码，用内置的 urllib 模块通常就足够了。但是，
  如果你要做的不仅仅只是简单的 GET 或 POST 请求，那就真的不能再依赖它的功能
  了。这时候就是第三方模块比如 requests 大显身手的时候了。

  request 库还对许多高级的 HTTP 客户端协议提供了支持，
  比如 OAuth。requests 模块的文档（http://docs.python-requests.org) 质量很高

创建 TCP 服务器
=================================

问题
  你想实现一个服务器，通过 TCP 协议和客户端通信。

解决方案
  创建一个 TCP 服务器的一个简单方法是使用 socketserver 库。例如，下面是一
  个简单的应答服务器::

    from socketserver import BaseRequestHandler, TCPServer

    class EchoHandler(BaseRequestHandler):
      def handle(self):
        print('Got connection from', self.client_address)
        while True:
          msg = self.request.recv(8192)
          if not msg:
            break
          self.request.send(msg)

    if __name__ == '__main__':
      serv = TCPServer(('', 20000), EchoHandler)
      serv.serve_forever()

  使用另一个客户端测试::

    >>> from socket import socket, AF_INET, SOCK_STREAM
    >>> s = socket(AF_INET, SOCK_STREAM)

    >>> s.connect(('localhost', 20000))
    >>> s.send(b'Hello') 5
    >>> s.recv(8192)
    b'Hello'
    >>>

  很 多 时 候， 可 以 很 容 易 的 定 义 一 个 不 同 的 处 理 器。 下 面 是 一 个 使 用
  StreamRequestHandler 基类将一个类文件接口放置在底层 socket 上的例子::

    from socketserver import StreamRequestHandler, TCPServer
    class EchoHandler(StreamRequestHandler):
      def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
          # self.wfile is a file-like object for writing
          self.wfile.write(line)

    if __name__ == '__main__':
      serv = TCPServer(('', 20000), EchoHandler)
      serv.serve_forever()

讨论
  socketserver 可以让我们很容易的创建简单的 TCP 服务器。但是，你需要注意
  的是，默认情况下这种服务器是单线程的，一次只能为一个客户端连接服务。如果你想
  处理多个客户端，可以初始化一个 ForkingTCPServer 或者是 ThreadingTCPServer 对
  象。例如::

    from socketserver import ThreadingTCPServer
    if __name__ == '__main__':
      serv = ThreadingTCPServer(('', 20000), EchoHandler)
      serv.serve_forever()

  使用 fork 或线程服务器有个潜在问题就是它们会为每个客户端连接创建一个新的
  进程或线程。由于客户端连接数是没有限制的，因此一个恶意的黑客可以同时发送大量
  的连接让你的服务器奔溃。

  如果你担心这个问题，你可以创建一个预先分配大小的工作线程池或进程池。你先
  创建一个普通的非线程服务器，然后在一个线程池中使用 serve_forever() 方法来启
  动它们::

    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
      t = Thread(target=serv.serve_forever)
      t.daemon = True
      t.start()
    serv.serve_forever()

  一般来讲，一个 TCPServer 在实例化的时候会绑定并激活相应的 socket
  。不过，有时候你想通过设置某些选项去调整底下的 socket‘ ，可以设置参数
  bind_and_activate=False 。如下::

    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    # Set up various socket options
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # Bind and activate
    serv.server_bind()
    serv.server_activate()
    serv.serve_forever()

  上面的 socket 选项是一个非常普遍的配置项，它允许服务器重新绑定一个之前使
  用过的端口号。由于要被经常使用到，它被放置到类变量中，可以直接在 TCPServer 上
  面设置。在实例化服务器的时候去设置它的值，如下所示::

    TCPServer.allow_reuse_address = True
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()

  在上面示例中，我们演示了两种不同的处理器基类（BaseRequestHandler 和
  StreamRequestHandler ）。StreamRequestHandler 更加灵活点，能通过设置其他的类
  变量来支持一些新的特性。

  最后，还需要注意的是巨大部分 Python 的高层网络模块（比如 HTTP、XML-RPC
  等）都是建立在 socketserver 功能之上。也就是说，直接使用 socket 库来实现服务
  器也并不是很难。

创建 UDP 服务器
=================================

问题
  你想实现一个基于 UDP 协议的服务器来与客户端通信。

解决方案
  跟 TCP 一样，UDP 服务器也可以通过使用 socketserver 库很容易的被创建。例
  如，下面是一个简单的时间服务器::

    from socketserver import BaseRequestHandler, UDPServer
    import time
    class TimeHandler(BaseRequestHandler):
      def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

    if __name__ == '__main__':
      serv = UDPServer(('', 20000), TimeHandler)
      serv.serve_forever()

  来测试下这个服务器::

    >>> from socket import socket, AF_INET, SOCK_DGRAM
    >>> s = socket(AF_INET, SOCK_DGRAM)
    >>> s.sendto(b'', ('localhost', 20000))
    0
    >>> s.recvfrom(8192)
    (b'Wed Aug 15 20:35:08 2012', ('127.0.0.1', 20000))
    >>>

讨论
  一个典型的 UDP 服务器接收到达的数据报 (消息) 和客户端地址。如果服务器需
  要做应答，它要给客户端回发一个数据报。对于数据报的传送，你应该使用 socket 的
  sendto() 和 recvfrom() 方法。尽管传统的 send() 和 recv() 也可以达到同样的效果，
  但是前面的两个方法对于 UDP 连接而言更普遍。

  由于没有底层的连接，UPD 服务器相对于 TCP 服务器来讲实现起来更加简单。不
  过，UDP 天生是不可靠的（因为通信没有建立连接，消息可能丢失）。因此需要由你自
  己来决定该怎样处理丢失消息的情况。

  通常来
  说，如果可靠性对于你程序很重要，你需要借助于序列号、重试、超时以及一些其他方
  法来保证。UDP 通常被用在那些对于可靠传输要求不是很高的场合。例如，在实时应
  用如多媒体流以及游戏领域，无需返回恢复丢失的数据包（程序只需简单的忽略它并
  继续向前运行）。

  UDPServer 类是单线程的，也就是说一次只能为一个客户端连接服务。实际使用
  中，这个无论是对于 UDP 还是 TCP 都不是什么大问题。如果你想要并发操作，可以
  实例化一个 ForkingUDPServer 或 ThreadingUDPServer 对象

通过 CIDR 地址生成对应的 IP 地址集
==================================================================

问题
  你有一个 CIDR 网络地址比如“123.45.67.89/27”，你想将其转换成它所代表的所
  有 IP （比如，“123.45.67.64”, “123.45.67.65”, …, “123.45.67.95”)）

解决方案
  可以使用 ipaddress 模块很容易的实现这样的计算。例如::

    >>> import ipaddress
    >>> net = ipaddress.ip_network('123.45.67.64/27')
    >>> net
    IPv4Network('123.45.67.64/27')
    >>> for a in net:
    ...   print(a)
    ...
    123.45.67.64
    123.45.67.65
    123.45.67.66
    123.45.67.67
    123.45.67.68
    ...
    123.45.67.95
    >>>
    >>> net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
    >>> net6
    IPv6Network('12:3456:78:90ab:cd:ef01:23:30/125')
    >>> for a in net6:
    ...   print(a)
    ...
    12:3456:78:90ab:cd:ef01:23:30
    12:3456:78:90ab:cd:ef01:23:31
    12:3456:78:90ab:cd:ef01:23:32
    12:3456:78:90ab:cd:ef01:23:33
    12:3456:78:90ab:cd:ef01:23:34
    12:3456:78:90ab:cd:ef01:23:35
    12:3456:78:90ab:cd:ef01:23:36
    12:3456:78:90ab:cd:ef01:23:37
    >>>

  Network 也允许像数组一样的索引取值

  还可以执行网络成员检查之类的操作::

    >>> a = ipaddress.ip_address('123.45.67.69')
    >>> a in net
    True
    >>> b = ipaddress.ip_address('123.45.67.123')
    >>> b in net
    False

  一个 IP 地址和网络地址能通过一个 IP 接口来指定，例如::

    >>> inet = ipaddress.ip_interface('123.45.67.73/27')
    >>> inet.network
    IPv4Network('123.45.67.64/27')
    >>> inet.ip
    IPv4Address('123.45.67.73')
    >>>

讨论
  ipaddress 模块有很多类可以表示 IP 地址、网络和接口。当你需要操作网络地址
  （比如解析、打印、验证等）的时候会很有用。
  要注意的是，ipaddress 模块跟其他一些和网络相关的模块比如 socket 库交集很
  少。所以，你不能使用 IPv4Address 的实例来代替一个地址字符串，你首先得显式的
  使用 str() 转换它。

创建一个简单的 REST 接口
=================================

问题
  你想使用一个简单的 REST 接口通过网络远程控制或访问你的应用程序，但是你
  又不想自己去安装一个完整的 web 框架。

解决方案
  构建一个 REST 风格的接口最简单的方法是创建一个基于 WSGI 标准（PEP
  3333）的很小的库.

通过 XML-RPC 实现简单的远程调用
=================================

问题
  你想找到一个简单的方式去执行运行在远程机器上面的 Python 程序中的函数或方
  法

解决方案
  实现一个远程方法调用的最简单方式是使用 XML-RPC。下面我们演示一下一个
  实现了键-值存储功能的简单服务器::

    from xmlrpc.server import SimpleXMLRPCServer
    class KeyValueServer:
      _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

      def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
          self._serv.register_function(getattr(self, name))

      def get(self, name):
        return self._data[name]

      def set(self, name, value):
        self._data[name] = value

      def delete(self, name):
        del self._data[name]

      def exists(self, name):
        return name in self._data

      def keys(self):
        return list(self._data)

      def serve_forever(self):
        self._serv.serve_forever()

    # Example
    if __name__ == '__main__':
      kvserv = KeyValueServer(('', 15000))
      kvserv.serve_forever()

  从一个客户端机器上面来访问服务器::

    >>> from xmlrpc.client import ServerProxy
    >>> s = ServerProxy('http://localhost:15000', allow_none=True)
    >>> s.set('foo', 'bar')
    >>> s.set('spam', [1, 2, 3])
    >>> s.keys()
    ['spam', 'foo']
    >>> s.get('foo')
    'bar'
    >>> s.get('spam')
    [1, 2, 3]
    >>> s.delete('spam')
    >>> s.exists('spam')
    False
    >>>

讨论
  XML-RPC 可以让我们很容易的构造一个简单的远程调用服务。你所需要做的仅
  仅是创建一个服务器实例，通过它的方法 register_function() 来注册函数，然后使
  用方法 serve_forever() 启动它。在上面我们将这些步骤放在一起写到一个类中，不
  够这并不是必须的。比如你还可以像下面这样创建一个服务器::

    from xmlrpc.server import SimpleXMLRPCServer
    def add(x,y):
      return x+y

    serv = SimpleXMLRPCServer(('', 15000))
    serv.register_function(add)
    serv.serve_forever()

  XML-RPC 暴露出来的函数只能适用于部分数据类型，比如字符串、整形、列表和
  字典。对于其他类型就得需要做些额外的功课了。例如，如果你想通过 XML-RPC 传
  递一个对象实例，实际上只有他的实例字典被处理.

  类似的，对于二进制数据的处理也跟你想象的不太一样::

    >>> s.set('foo', b'Hello World')
    >>> s.get('foo')
    <xmlrpc.client.Binary object at 0x10131d410>
    >>> _.data
    b'Hello World'
    >>>

  一般来讲，你不应该将 XML-RPC 服务以公共 API 的方式暴露出来。对于这种情
  况，通常分布式应用程序会是一个更好的选择。

  XML-RPC 的一个缺点是它的性能。SimpleXMLRPCServer 的实现是单线程的，所
  以它不适合于大型程序

  另外，由于 XML-RPC 将所有数据都序列化为 XML 格式，所以它会比其他的方式运
  行的慢一些。但是它也有优点，这种方式的编码可以被绝大部分其他编程语言支持。通
  过使用这种方式，其他语言的客户端程序都能访问你的服务。

  虽然 XML-RPC 有很多缺点，但是如果你需要快速构建一个简单远程过程调用系
  统的话，它仍然值得去学习的。有时候，简单的方案就已经足够了。

在不同的 Python 解释器之间交互
=================================

问题
  你在不同的机器上面运行着多个 Python 解释器实例，并希望能够在这些解释器之
  间通过消息来交换数据。

解决方案
  通过使用 multiprocessing.connection 模块可以很容易的实现解释器之间的通
  信。下面是一个简单的应答服务器例子::

    from multiprocessing.connection import Listener

    import traceback

    def echo_client(conn):
      try:
        while True:
          msg = conn.recv()
          conn.send(msg)
      except EOFError:
        print('Connection closed')

    def echo_server(address, authkey):
      serv = Listener(address, authkey=authkey)
      while True:
        try:
          client = serv.accept()
          echo_client(client)
        except Exception:
          traceback.print_exc()

    echo_server(('', 25000), authkey=b'peekaboo')

  然后客户端连接服务器并发送消息的简单示例::

    >>> from multiprocessing.connection import Client
    >>> c = Client(('localhost', 25000), authkey=b'peekaboo')
    >>> c.send('hello')
    >>> c.recv()
    'hello'
    >>> c.send([1, 2, 3, 4, 5])
    >>> c.recv()
    [1, 2, 3, 4, 5]
    >>>

  跟底层 socket 不同的是，每个消息会完整保存（每一个通过 send() 发送的对象能
  通过 recv() 来完整接受）。另外，所有对象会通过 pickle 序列化。因此，任何兼容 pickle
  的对象都能在此连接上面被发送和接受。

讨论
  目前有很多用来实现各种消息传输的包和函数库，比如 ZeroMQ、Celery 等。你还
  有另外一种选择就是自己在底层 socket 基础之上来实现一个消息传输层。但是你想要
  简单一点的方案，那么这时候 multiprocessing.connection 就派上用场了。仅仅使用
  一些简单的语句即可实现多个解释器之间的消息通信。

  如果你的解释器运行在同一台机器上面，那么你可以使用另外的通信机制，比如
  Unix 域套接字或者是 Windows 命名管道。要想使用 UNIX 域套接字来创建一个连接，
  只需简单的将地址改写一个文件名即可::

    s = Listener('/tmp/myconn', authkey=b'peekaboo')

  要想使用 Windows 命名管道来创建连接，只需像下面这样使用一个文件名::

    s = Listener(r'\\.\pipe\myconn', authkey=b'peekaboo')

  一个通用准则是，你不要使用 multiprocessing 来实现一个对外的公共服务。
  Client() 和 Listener() 中的 authkey 参数用来认证发起连接的终端用户。如果密钥
  不对会产生一个异常。此外，该模块最适合用来建立长连接（而不是大量的短连接），
  例如，两个解释器之间启动后就开始建立连接并在处理某个问题过程中会一直保持连
  接状态。

  如果你需要对底层连接做更多的控制，比如需要支持超时、非阻塞 I/O 或其他类
  似的特性，你最好使用另外的库或者是在高层 socket 上来实现这些特性。

实现远程方法调用
=================================

问题
  你想在一个消息传输层如 sockets 、multiprocessing connections 或 ZeroMQ 的
  基础之上实现一个简单的远程过程调用（RPC）。

解决方案
  将函数请求、参数和返回值使用 pickle 编码后，在不同的解释器直接传送 pickle 字
  节字符串，可以很容易的实现 RPC。下面是一个简单的 PRC 处理器，可以被整合到一
  个服务器中去::

    # rpcserver.py
    import pickle
    class RPCHandler:

      def __init__(self):
        self._functions = { }

      def register_function(self, func):
        self._functions[func.__name__] = func

      def handle_connection(self, connection):
        try:
          while True:

            # Receive a message
            func_name, args, kwargs = pickle.loads(connection.recv())

            # Run the RPC and send a response
            try:
              r = self._functions[func_name](*args,**kwargs)
              connection.send(pickle.dumps(r))
            except Exception as e:
              connection.send(pickle.dumps(e))
        except EOFError:
          pass

  要使用这个处理器，你需要将它加入到一个消息服务器中。你有很多种选择，但是
  使用 multiprocessing 库是最简单的。下面是一个 RPC 服务器例子::

    from multiprocessing.connection import Listener
    from threading import Thread

    def rpc_server(handler, address, authkey):
      sock = Listener(address, authkey=authkey)
      while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

    # Some remote functions
    def add(x, y):
      return x + y

    def sub(x, y):
      return x - y

    # Register with a handler
    handler = RPCHandler()
    handler.register_function(add)
    handler.register_function(sub)

    # Run the server
    rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')

  为了从一个远程客户端访问服务器，你需要创建一个对应的用来传送请求的 RPC
  代理类。例如::

    import pickle

    class RPCProxy:
      def __init__(self, connection):
        self._connection = connection

      def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
          self._connection.send(pickle.dumps((name, args, kwargs)))
          result = pickle.loads(self._connection.recv())
          if isinstance(result, Exception):
            raise result
          return result
        return do_rp

  要使用这个代理类，你需要将其包装到一个服务器的连接上面，例如::

    >>> from multiprocessing.connection import Client
    >>> c = Client(('localhost', 17000), authkey=b'peekaboo')
    >>> proxy = RPCProxy(c)
    >>> proxy.add(2, 3) 5
    >>> proxy.sub(2, 3)
    -1
    >>> proxy.sub([1, 2], 4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "rpcserver.py", line 37, in do_rpc
        raise result
    TypeError: unsupported operand type(s) for -: 'list' and 'int'
    >>>

  要注意的是很多消息层（比如 multiprocessing ）已经使用 pickle 序列化了数据。
  如果是这样的话，对 pickle.dumps() 和 pickle.loads() 的调用要去掉。

讨论
  由于底层需要依赖 pickle，那么安全问题就需要考虑了（因为一个聪明的黑客可以
  创建特定的消息，能够让任意函数通过 pickle 反序列化后被执行）。因此你永远不要允
  许来自不信任或未认证的客户端的 RPC。特别是你绝对不要允许来自 Internet 的任意
  机器的访问，这种只能在内部被使用，位于防火墙后面并且不要对外暴露。

  实现 RPC 的一个比较复杂的问题是如何去处理异常。至少，当方法产生异常时服
  务器不应该奔溃。因此，返回给客户端的异常所代表的含义就要好好设计了。如果你使
  用 pickle，异常对象实例在客户端能被反序列化并抛出。如果你使用其他的协议，那得
  想想另外的方法了。不过至少，你应该在响应中返回异常字符串。

简单的客户端认证
=================================

问题
  你想在分布式系统中实现一个简单的客户端连接认证功能，又不想像 SSL 那样的
  复杂。

解决方案
  可以利用 hmac 模块实现一个连接握手，从而实现一个简单而高效的认证过程。下
  面是代码示例::

    import hmac
    import os
    def client_authenticate(connection, secret_key):
      '''
      Authenticate client to a remote service.
      connection represents a network connection.
      secret_key is a key known only to both client/server.
      '''
      message = connection.recv(32)
      hash = hmac.new(secret_key, message)
      digest = hash.digest()
      connection.send(digest)

    def server_authenticate(connection, secret_key):
      '''
      Request client authentication.
      '''
      message = os.urandom(32)
      connection.send(message)
      hash = hmac.new(secret_key, message)
      digest = hash.digest()
      response = connection.recv(len(digest))
      return hmac.compare_digest(digest,response)

  基本原理是当连接建立后，服务器给客户端发送一个随机的字节消息（这里例子
  中使用了 os.urandom() 返回值）。客户端和服务器同时利用 hmac 和一个只有双方知
  道的密钥来计算出一个加密哈希值。然后客户端将它计算出的摘要发送给服务器，服务
  器通过比较这个值和自己计算的是否一致来决定接受或拒绝连接。摘要的比较需要使
  用 hmac.compare_digest() 函数。使用这个函数可以避免遭到时间分析攻击，不要用
  简单的比较操作符（==）。为了使用这些函数，你需要将它集成到已有的网络或消息
  代码中。

讨论
  hmac 认证的一个常见使用场景是内部消息通信系统和进程间通信。例如，如果你
  编写的系统涉及到一个集群中多个处理器之间的通信，你可以使用本节方案来确保只
  有被允许的进程之间才能彼此通信。事实上，基于 hmac 的认证被 multiprocessing 模
  块使用来实现子进程直接的通信。

  还有一点需要强调的是连接认证和加密是两码事。认证成功之后的通信消息是以
  明文形式发送的，任何人只要想监听这个连接线路都能看到消息（尽管双方的密钥不
  会被传输）

  hmac 认证算法基于哈希函数如 MD5 和 SHA-1，

在网络服务中加入 SSL
=================================

问题
  你想实现一个基于 sockets 的网络服务，客户端和服务器通过 SSL 协议认证并加
  密传输的数据。

解决方案
  ssl 模块能为底层 socket 连接添加 SSL 的支持。ssl.wrap_socket() 函数接受一
  个已存在的 socket 作为参数并使用 SSL 层来包装它。例如，下面是一个简单的应答服
  务器，能在服务器端为所有客户端连接做认证。

  例子::

    from socket import socket, AF_INET, SOCK_STREAM
    import ssl

    KEYFILE = 'server_key.pem' # Private key of the server
    CERTFILE = 'server_cert.pem' # Server certificate (given to client)

    def echo_client(s):
      while True:
        data = s.recv(8192)
        if data == b'':
          break
        s.send(data)
        s.close()
        print('Connection closed')

    def echo_server(address):
      s = socket(AF_INET, SOCK_STREAM)
      s.bind(address)
      s.listen(1)

      # Wrap with an SSL layer requiring client certs
      s_ssl = ssl.wrap_socket(s,
                              keyfile=KEYFILE,
                              certfile=CERTFILE,
                              server_side=True
                              )
      # Wait for connections
      while True:
        try:
          c,a = s_ssl.accept()
          print('Got connection', c, a)
          echo_client(c)
        except Exception as e:
          print('{}: {}'.format(e.__class__.__name__, e))

    echo_server(('', 20000))

  客户端连接服务器::

    >>> from socket import socket, AF_INET, SOCK_STREAM
    >>> import ssl
    >>> s = socket(AF_INET, SOCK_STREAM)
    >>> s_ssl = ssl.wrap_socket(s,
                  cert_reqs=ssl.CERT_REQUIRED,
                  ca_certs = 'server_cert.pem')
    >>> s_ssl.connect(('localhost', 20000))
    >>> s_ssl.send(b'Hello World?')
    12
    >>> s_ssl.recv(8192)
    b'Hello World?'
    >>>

  这种直接处理底层 socket 方式有个问题就是它不能很好的跟标准库中已存在的
  网络服务兼容。例如，绝大部分服务器代码（HTTP、XML-RPC 等）实际上是基于
  socketserver 库的。客户端代码在一个较高层上实现。我们需要另外一种稍微不同的
  方式来将 SSL 添加到已存在的服务中

  创建自签名证书::

     openssl req -new -x509 -days 365 -nodes -out server_cert.pem -keyout server_key.pem

  在创建证书的时候，各个值的设定可以是任意的，但是”Common Name“的值通
  常要包含服务器的 DNS 主机名。如果你只是在本机测试，那么就使用”localhost“，否
  则使用服务器的域名。

进程间传递 Socket 文件描述符
=================================

问题
  你有多个 Python 解释器进程在同时运行，你想将某个打开的文件描述符从一个解
  释器传递给另外一个。比如，假设有个服务器进程相应连接请求，但是实际的相应逻辑
  是在另一个解释器中执行的。

解决方案
  为了在多个进程中传递文件描述符，你首先需要将它们连接到一起。在 Unix 机器
  上，你可能需要使用 Unix 域套接字，而在 windows 上面你需要使用命名管道。不过你
  无需真的需要去操作这些底层，通常使用 multiprocessing 模块来创建这样的连接会
  更容易一些。

  一 旦 一 个 连 接 被 创 建， 你 可 以 使 用 multiprocessing.reduction 中 的
  send_handle() 和 recv_handle() 函数在不同的处理器直接传递文件描述符。下面
  的例子演示了最基本的用法::

    import multiprocessing
    from multiprocessing.reduction import recv_handle, send_handle
    import socket

    def worker(in_p, out_p):
      out_p.close()
      while True:
        fd = recv_handle(in_p)
        print('CHILD: GOT FD', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as s:
          while True:
            msg = s.recv(1024)
            if not msg:
              break
            print('CHILD: RECV {!r}'.format(msg))
            s.send(msg)

    def server(address, in_p, out_p, worker_pid):
      in_p.close()
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True) s.bind(address)
      s.listen(1)
      while True:
        client, addr = s.accept()
        print('SERVER: Got connection from', addr)
        send_handle(out_p, client.fileno(), worker_pid)
        client.close()

    if __name__ == '__main__':
      c1, c2 = multiprocessing.Pipe()
      worker_p = multiprocessing.Process(target=worker, args=(c1,c2))
      worker_p.start()
      server_p = multiprocessing.Process(target=server,
      args=(('', 15000), c1, c2, worker_p.pid))
      server_p.start()
      c1.close()
      c2.close()

  在这个例子中，两个进程被创建并通过一个 multiprocessing 管道连接起来。服
  务器进程打开一个 socket 并等待客户端连接请求。工作进程仅仅使用 recv_handle()
  在管道上面等待接收一个文件描述符。当服务器接收到一个连接，它将产生的 socket
  文件描述符通过 send_handle() 传递给工作进程。工作进程接收到 socket 后向客户端
  回应数据，然后此次连接关闭。

讨论
  对于大部分程序员来讲在不同进程之间传递文件描述符好像没什么必要。但是，有
  时候它是构建一个可扩展系统的很有用的工具。例如，在一个多核机器上面，你可以有
  多个 Python 解释器实例，将文件描述符传递给其它解释器来实现负载均衡。

  send_handle() 和 recv_handle() 函数只能够用于 multiprocessing 连接。

理解事件驱动的 IO
=================================

问题
  你应该已经听过基于事件驱动或异步 I/O 的包，但是你还不能完全理解它的底层
  到底是怎样工作的，或者是如果使用它的话会对你的程序产生什么影响。

解决方案
  事件驱动 I/O 本质上来讲就是将基本 I/O 操作（比如读和写）转化为你程序需要
  处理的事件。例如，当数据在某个 socket 上被接受后，它会转换成一个 receive 事件，
  然后被你定义的回调方法或函数来处理。作为一个可能的起始点，一个事件驱动的框架
  可能会以一个实现了一系列基本事件处理器方法的基类开始::

    class EventHandler:
      def fileno(self):
        'Return the associated file descriptor'
        raise NotImplemented('must implement')

      def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False

      def handle_receive(self):
        'Perform the receive operation'
        pass

      def wants_to_send(self):
        'Return True if sending is requested'
        return False

      def handle_send(self):
        'Send outgoing data'
        pass

  这个类的实例作为插件被放入类似下面这样的事件循环中::

    import select
    def event_loop(handlers):
    while True:
      wants_recv = [h for h in handlers if h.wants_to_receive()]
      wants_send = [h for h in handlers if h.wants_to_send()]
      can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
      for h in can_recv:
        h.handle_receive()
      for h in can_send:
        h.handle_send()

  事件循环的关键部分是 select() 调用，它会不断轮询文件描述符从而激活它。在
  调用 select() 之前，时间循环会询问所有的处理器来决定哪一个想接受或发生。然后
  它将结果列表提供给 select() 。然后 select() 返回准备接受或发送的对象组成的列
  表。然后相应的 handle_receive() 或 handle_send() 方法被触发。

讨论
  实际上所有的事件驱动框架原理跟上面的例子相差无几。实际的实现细节和软件
  架构可能不一样，但是在最核心的部分，都会有一个轮询的循环来检查活动 socket，并
  执行响应操作.

  事件驱动 I/O 的一个可能好处是它能处理非常大的并发连接，而不需要使用多线
  程或多进程。也就是说，select() 调用（或其他等效的）能监听大量的 socket 并响应
  它们中任何一个产生事件的。在循环中一次处理一个事件，并不需要其他的并发机制。

  事件驱动 I/O 的缺点是没有真正的同步机制。如果任何事件处理器方法阻塞或执
  行一个耗时计算，它会阻塞所有的处理进程。调用那些并不是事件驱动风格的库函数也
  会有问题，同样要是某些库函数调用会阻塞，那么也会导致整个事件循环停止。

  对于阻塞或耗时计算的问题可以通过将事件发送个其他单独的线程或进程来处理。
  不过，在事件循环中引入多线程和多进程是比较棘手的，下面的例子演示了如何使用
  concurrent.futures 模块来实现::

    self.pool = ThreadPoolExecutor(nworkers)
    r = self.pool.submit(func, *args, **kwargs)
    r.add_done_callback(lambda r: self._complete(callback, r))

  工作被提交给 ThreadPoolExecutor 实例。不过一个难点是协调计算结果和事件循环::

    # Callback that executes when the thread is done
    def _complete(self, callback, r):
      self.pending.append((callback, r.result()))
      self.signal_done_sock.send(b'x')

发送与接收大型数组
=================================

问题
  你要通过网络连接发送和接受连续数据的大型数组，并尽量减少数据的复制操作

解决方案
  下面的函数利用 memoryviews 来发送和接受大数组::

    # zerocopy.py
    def send_from(arr, dest):
      view = memoryview(arr).cast('B')
      while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

    def recv_into(arr, source):
      view = memoryview(arr).cast('B')
      while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]

讨论
  在数据密集型分布式计算和平行计算程序中，自己写程序来实现发送/接受大量数
  据并不常见。不过，要是你确实想这样做，你可能需要将你的数据转换成原始字节，以
  便给低层的网络函数使用。你可能还需要将数据切割成多个块，因为大部分和网络相关
  的函数并不能一次性发送或接受超大数据块。

  一种方法是使用某种机制序列化数据——可能将其转换成一个字节字符串。不过，
  这样最终会创建数据的一个复制。就算你只是零碎的做这些，你的代码最终还是会有大
  量的小型复制操作。

  本质上，一个内存视图就是一个已存
  在数组的覆盖层。内存视图还能以不同的方式转换成不同类型来表现数据::

    view = memoryview(arr).cast('B')

  它接受一个数组 arr 并将其转换为一个无符号字节的内存视图。这个视图能被传递
  给 socket 相关函数，比如 socket.send() 或 send.recv_into() 。在内部，这些方法
  能够直接操作这个内存区域。例如，sock.send() 直接从内存中发生数据而不需要复
  制。send.recv_into() 使用这个内存区域作为接受操作的输入缓冲区

  剩下的一个难点就是 socket 函数可能只操作部分数据。通常来讲，我们得使用很
  多不同的 send() 和 recv_into() 来传输整个数组。不用担心，每次操作后，视图会通
  过发送或接受字节数量被切割成新的视图。新的视图同样也是内存覆盖层。因此，还是
  没有任何的复制操作.

  这里有个问题就是接受者必须事先知道有多少数据要被发送，以便它能预分配一
  个数组或者确保它能将接受的数据放入一个已经存在的数组中。如果没办法知道的话，
  发送者就得先将数据大小发送过来，然后再发送实际的数组数据。
