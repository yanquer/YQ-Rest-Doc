========================
ssl
========================

官网: `<https://docs.python.org/zh-cn/3/library/ssl.html>`_

套接字对象的TLS/SSL封装

该模块提供了对传输层安全（通常称为 "安全套接字层"）加密和网络套接字的对等认证设施的访问，
包括客户端和服务器端。 该模块使用 OpenSSL 库。
它可以在所有现代 Unix 系统、 Windows 、 macOS 和可能的其他平台上使用，只要 OpenSSL 安装在该平台上。

主要的一个API

.. function:: SSLContext.wrap_socket(sock, server_side=False, do_handshake_on_connect=True, suppress_ragged_eofs=True, server_hostname=None, session=None)

  包装一个现有的 Python 套接字 sock 并返回一个
  SSLContext.sslsocket_class 的实例 (默认为 SSLSocket)。
  返回的 SSL 套接字会绑定上下文、设置以及证书。
  sock 必须是一个 SOCK_STREAM 套接字；其他套接字类型不被支持。

  server_side: bool
    标明希望从该套接字获得服务器端行为还是客户端行为

    对于客户端套接字，上下文的构造会延迟执行；
    如果下层的套接字尚未连接，上下文的构造将在对套接字调用 connect() 之后执行。

    对于服务器端套接字，如果套接字没有远端对等方，它会被视为一个监听套接字，
    并且服务器端 SSL 包装操作会在通过 accept() 方法所接受的客户端连接上自动执行。
    此方法可能会引发 SSLError。
  server_hostname:
    用在客户端连接上，指定所要连接的服务的主机名。
    这允许单个服务器托管具有单独证书的多个基于 SSL 的服务，
    很类似于 HTTP 虚拟主机。
    如果 server_side 为真值则指定 server_hostname 将引发 ValueError。
  do_handshake_on_connect:
    指明是否要在调用 socket.connect() 之后自动执行 SSL 握手，
    还是要通过发起调用 SSLSocket.do_handshake() 方法让应用程序显式地调用它。
    显式地调用 SSLSocket.do_handshake() 可给予程序对握手中所涉及的套接字 I/O 阻塞行为的控制。
  suppress_ragged_eofs:
    形参 suppress_ragged_eofs 指明 SSLSocket.recv() 方法
    应当如何从连接的另一端发送非预期的 EOF 信号。
    如果指定为 True (默认值)，它将返回正常的 EOF (空字节串对象)
    来响应从下层套接字引发的非预期的 EOF 错误；
    如果指定为 False，它将向调用方引发异常。

  session，参见 session。

  在 3.5 版更改: 总是允许传送 server_hostname，即使 OpenSSL 没有 SNI。

  在 3.6 版更改: 增加了 session 参数。

  在 3.7 版更改: The method returns an instance of SSLContext.sslsocket_class instead of hard-coded SSLSocket.


