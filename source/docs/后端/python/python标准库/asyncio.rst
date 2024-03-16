===========================
asyncio
===========================


.. post:: 2023-02-20 22:18:59
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


- 官网: https://docs.python.org/zh-cn/3/library/asyncio.html
- 低层api索引: https://docs.python.org/zh-cn/3/library/asyncio-llapi-index.html

这部分属于协程, 相关介绍可见: :doc:`/docs/后端/python/概念相关/协程`

包问题
===========================

如果尝试用pip安装过, 会发现asyncio目前同时存在于Python标准库和三方包中, 这是因为:

- Python 3.4引入了asyncio模块,这是asyncio最初出现在Python标准库的形式。
- 在Python 3.5中,asyncio模块被重构,并更名为asyncio package。这是目前Python标准库中推荐使用的asyncio形式。
- 此外,还存在三方包asyncio和trolly,它们在Python 3.3之前实现了asyncio功能。

所以,目前asyncio主要有这三种形式:

- Python 3.4中的asyncio模块(已过时)
- Python 3.5+中的asyncio package(推荐)
- 三方包asyncio和trolly(仅用于Python 3.3之前)

应该关注并使用的是Python 3.5+中的asyncio package。它是官方支持和推荐的asyncio形式,具有更丰富的功能和更高的性能。
三方包asyncio和trolly由于兼容性问题,已经很少再被使用。而asyncio模块由于设计问题,已在Python 3.5中被更名和重构。

await和create_task的区别
===========================

await:
  当前代码在此处挂起(阻塞), 等待await的语句执行完成. 程序中时间循环中的其他语句可以在这时候执行.
  直到await的语句执行完成(如果一下就执行完了, 那么可以说没有等待)

  但只能用在 async 方法体内
create_task:
  创建一个任务, 提交给事件循环队列(上下文环境复制一份给事件循环), 事件循环自动调度, 不阻塞

  同步异步方法内皆可用

可等待对象
===========================

可等待对象有 coroutine/future/task

其中task是future的子类

任务回调
===========================

task.add_done_callback 完成后的回调如何自定义参数,

使用 functools.partial 偏函数来插入参数，
此处正常情况的参数只有一个 future 对象表示它本身这个 task::

  # 插入参数后， 实际回调的参数列表为 (_num, task), 也就是 (10, task)
  task.add_done_callback(functools.partial(cls._set_num1, 10))

多线程的事件循环
===========================

一般而言, 只能是主线程拥有自己的事件循环, 子线程无法获取主线程的loop, 若子线程需要, 可以在新建一个loop给子线程使用,

尤其是gui编程的时候, 一般gui线程只能在主线程跑(除非提供了特殊支持),
那么当存在全局的非gui能处理的实时监听时, 那么就只能在子线程跑了(或者新建一个进程, 至少目前我是没有其他办法)

事件循环增加信号监听
===========================

code::

  import signal
  loop.add_signal_handler(signal.SIGTERM, hander)

与socket协作
===========================

code::

  _sock: socket.socket
  loop.sock_recv(_sock, 1024)

并发执行(假并发)
===========================

使用 **asyncio.gather** 同时运行两个协程任务::

  tasks = [task1(), task2()]
  loop.run_until_complete(asyncio.gather(*tasks))

创建socket-udp事件
===========================

使用 **loop.create_datagram_endpoint**

.. function:: loop.create_datagram_endpoint(protocol_factory, local_addr=None, remote_addr=None, *, family=0, proto=0, flags=0, reuse_port=None, allow_broadcast=None, sock=None)

  创建一个数据报连接。

  套接字族可以是 AF_INET, AF_INET6 或 AF_UNIX，具体取决于 host (或 family 参数，如果有提供的话)。

  socket类型将是 SOCK_DGRAM 。

  protocol_factory:
    必须为一个返回 协议 实现的可调用对象。

    成功时返回一个 (transport, protocol) 元组。
  local_addr:
    如果指定，它应当是一个用来在本地绑定套接字的 (local_host, local_port) 元组。
    local_host 和 local_port 是使用 getaddrinfo() 来查找的。
  remote_addr:
    如果指定的话，就是一个 (remote_host, remote_port) 元组，
    用于同一个远程地址连接。remote_host 和 remote_port 是使用 getaddrinfo() 来查找的。

  family, proto, flags 是可选的地址族，协议和标志，其会被传递给 getaddrinfo() 来完成 host 的解析。
  如果要指定的话，这些都应该是来自于 socket 模块的对应常量。

  reuse_port:
    告知内核，只要在创建时都设置了这个旗标，就允许此端点绑定到其他现有端点所绑定的相同端口上。
    这个选项在 Windows 和某些 Unix 上不受支持。 如果 SO_REUSEPORT 常量未定义则此功能就是不受支持的。
  allow_broadcast:
    告知内核允许此端点向广播地址发送消息。
  sock:
    可选择通过指定此值用于使用一个预先存在的，已经处于连接状态的 socket.socket 对象，
    并将其提供给此传输对象使用。如果指定了这个值， local_addr 和 remote_addr 就应该被忽略 (必须为 None)。

  当具有不同 UID 的多个进程将套接字赋给具有 SO_REUSEADDR 的相同 UDP 套接字地址时，传入的数据包可能会在套接字间随机分配。

  对于受支持的平台，reuse_port 可以被用作类似功能的替代。 通过 reuse_port 将改用 SO_REUSEPORT，
  它能够防止具有不同 UID 的进程将套接字赋给相同的套接字地址。

eg::

  loop.create_datagram_endpoint(
              lambda: OrdinaryProtocol(),
              local_addr=('0.0.0.0', 0),
          )

注意 protocol_factory 必须为一个返回 协议 实现的可调用对象,
协议 实现是指实现 asyncio.protocols 下的需要的协议, 协议的基类是 asyncio.protocols.BaseProtocol
如udp编程使用 协议 实现asyncio.protocols.DatagramProtocol
这里是 OrdinaryProtocol() 就是实现的 DatagramProtocol::

  class DatagramProtocol(DatagramProtocol):
      def __init__(self):
          self._transport: Optional[DatagramTransport] = None
          self._udp_socket: Optional[DatagramTransport] = None

      def connection_made(self, transport: transports.DatagramTransport) -> None:
          self._transport = transport

      def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None:
          _LOGGER.debug(f'datagram_received:: addr: {addr} ; data: {data}')

      def connection_lost(self, exc: Optional[Exception]) -> None:
          ...

      async def close(self):
          self._transport.close()

判断是否是协程
===========================

可使用 asyncio 的 iscoroutinefunction::

  async def async_func(): ...
  asyncio.iscoroutinefunction(async_func)     # True

或者inspect 的检查::

  inspect.iscoroutinefunction(async_func))    # True

如果要使用类型注解, 参见 :ref:`CR_Callable`

