=========================
socket
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/socket.html

| 底层网络接口

提供了访问 BSD 套接字 的接口。在所有现代 Unix 系统、Windows、macOS 和其他一些平台上可用。


套接字协议簇
=========================

| 仅介绍常用的 ipv4与ipv6相关地址协议簇

- 一对 (host, port) 被用作 AF_INET 地址族，其中 host 是一个表示互联网域名标记形式的主机名例如 'daring.cwi.nl'
  或者 IPv4 地址例如 '100.50.200.5' 的字符串，而 port 是一个整数值。

  - 对于 IPv4 地址，有两种可接受的特殊形式被用来代替一个主机地址：'' 代表 INADDR_ANY，用来绑定到所有接口；
    字符串 '<broadcast>' 代表 INADDR_BROADCAST。
    此行为不兼容 IPv6，因此，如果你的 Python 程序打算支持 IPv6，则可能需要避开这些。
- 对于 AF_INET6 地址族，使用一个四元组 (host, port, flowinfo, scope_id)，
  其中 flowinfo 和 scope_id 代表了 C 库 struct sockaddr_in6
  中的 sin6_flowinfo 和 sin6_scope_id 成员。
  对于 socket 模块中的方法， flowinfo 和 scope_id 可以被省略，只为了向后兼容。
  注意，省略 scope_id 可能会导致操作带有领域 (Scope) 的 IPv6 地址时出错。

setsockopt
=========================

setsockopt()方法用来设置套接字选项,它有以下参数:

- level:选项级别,用于区分是针对套接字级别的选项还是某个具体协议级别的选项。socket.SOL_SOCKET表示套接字级别。
- optname:选项名称, 如socket.SO_BROADCAST,表示广播选项。
  支持的值:

  - level为SOL_SOCKET:设置套接字级别的选项。包括:

    - SO_REUSEADDR:允许重用本地地址和端口。
      比如当上一个套接字关闭时立即再启动, 会发现报错端口已占用.
      这是因为上一次关闭时, 其处于 TIME_WAIT 状态，无法立即重用, 设置此选项即可立即重用.
    - SO_REUSEPORT: 允许多个套接字绑定到同一个地址和端口。
      普通的套接字绑定要求地址和端口必须是唯一的。如果有两个套接字尝试绑定到同一地址和端口,第二个绑定调用将失败。
    - SO_KEEPALIVE:开启TCP keepalive机制。
    - SO_SNDBUF / SO_RCVBUF:设置发送/接收缓冲区大小。
    - SO_LINGER:控制套接字关闭时未发送的数据。
    - SO_OOBINLINE:允许接收带外数据。
    - SO_BROADCAST: 允许套接字发送广播数据包。这在编写基于UDP的广播程序时需要设置
    - SO_ERROR: 获取或设置套接字的错误状态。当一个套接字出现错误时，它将返回一个非零值，表示该套接字上发生了错误。
      这个错误状态可以通过 socket.getsockopt() 和 socket.setsockopt() 来获取和设置。
      常见的错误状态包括连接被拒绝、超时、主机名无法解析等

  - level为IPPROTO_IP / IPPROTO_TCP:设置IP/TCP级别的选项。包括:

    - IP_TOS:设置IP数据包的服务类型。
    - TCP_NODELAY:禁用Nagle算法,立即发送数据。
    - IP_MULTICAST_TTL: 设置IP多播数据包的存活时间TTL。它控制多播数据包可以跨过的路由器数量.
      IP_MULTICAST_TTL选项的值确实只能在0到255之间。
      它表示IP多播数据包可以跨越的路由器数量。每个路由器跨越时,该值减一。当值减至0时,该数据包将不再被转发。
      所以,该选项的值越大,多播数据包可以传输的距离越远。常用的值有:

      - 1:同一子网内。只允许多播数据包在本地网络内传输。
      - 32:同一站点内。允许跨越较大范围,可覆盖大多数机房或校园网。
      - 64:同一地域内。可以覆盖较大范围的地区网络。
      - 128或更大:更广范围的覆盖,甚至跨洲际。

      而0值表示禁止多播数据包转发,它将被丢弃而不离开本地主机。
      所以,对于这个选项,推荐的值一般为:

      - 1-32:局域网/机房内多播。
      - 64-128:广域网多播。
      - 0:禁止多播数据包转发,本地回环。

      正确设置这个值,可以控制多播数据包的传播范围,实现我们想要的多播覆盖面。

      eg, 当值为2时: 表示多播数据包可以在当前子网及直接相邻的一个子网传输,但不允许传输到更远的网络。
      它允许包括第一个跨路由器跳跃在内的两次路由。当IP多播数据包离开源主机后,它可以跨越第一个路由器,此时TTL值减一变为1。
      然后在第二个路由器,TTL值再减一变为0。此时,该路由器将不再转发这个数据包,且将其丢弃。

    - IP_MULTICAST_LOOP: 控制是否向本地套接字发送回环多播数据包。
      默认情况下,IP多播数据包会回环到本地,但在某些情况下我们需要禁用此功能。

  - IPPROTO_IPV6:设置IPv6相关的选项。

- value:选项值,1表示允许,0表示禁止。

如允许UDP套接字udp_server发送和接收广播数据包::

  udp_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

如果不设置这个选项,默认情况下套接字是不允许广播的。设置后,套接字可以:

- 使用udp_server.sendto(data, ("<broadcast>", port)) 发送广播
- 使用udp_server.recvfrom(bufsize) 接收广播

.. sidebar::

  .. function:: socket.setsockopt(level, optname, value: int)
    :noindex:
  .. function:: socket.setsockopt(level, optname, value: buffer)
    :noindex:
  .. function:: socket.setsockopt(level, optname, None, optlen: int)
    :noindex:

    设置给定套接字选项的值（参阅 Unix 手册页 setsockopt(2) ）。
    所需的符号常量（ SO_* 等）已定义在本 socket 模块中。
    该值可以是整数、None 或表示缓冲区的 字节类对象。
    在后一种情况下，由调用者确保字节串中包含正确的数据位
    （关于将 C 结构体编码为字节串的方法，请参阅可选的内置模块 struct ）。
    当 value 设置为 None 时，必须设置 optlen 参数。
    这相当于调用 setsockopt() C 函数时使用了 optval=NULL 和 optlen=optlen 参数。

eg::

  # 设置socket选项，开启广播模式
  # 允许地址重用, 可以在同一个端口上绑定多个套接字
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
  # 启用广播模式，可以向本地网络中的所有主机发送广播消息
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  # 值设置为2，表示传输范围为本地子网，
  # 也就是说，UDP数据包只会被发送到与本地网络相连的主机
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
  # 值设置为1, 启用IP多播回送功能，允许主机接收自己发送的IP多播数据报
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

  # 绑定IP地址和端口号
  sock.bind(cls._SSDP_Addr)

  # 加入多播组
  # group变量存储多播地址, inet_aton()方法将其转换为二进制格式
  group = socket.inet_aton(cls._SSDP_Addr[0])
  # 将该地址和INADDR_ANY一起打包
  mreq = struct.pack('4sL', group, socket.INADDR_ANY)
  # 将socket加入到指定的多播组中
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

inet_aton
=========================

.. function:: socket.inet_aton(ip_string)

  将给定的地址字符串转换为32位二进制格式返回

  inet_aton() 也接受句点数少于三的字符串，详情请参阅 Unix 手册 inet(3)。

  如果传入本函数的 IPv4 地址字符串无效，则抛出 OSError。注意，具体什么样的地址有效取决于 inet_aton() 的底层 C 实现。

  inet_aton() 不支持 IPv6，在 IPv4/v6 双协议栈下应使用 inet_pton() 来代替。

一些常量
=========================

- socket.INADDR_ANY: 一个常用的特殊值,它表示: 0.0.0.0, 即所有本地IP地址。
- socket.IP_ADD_MEMBERSHIP: 让套接字加入指定的IP多播组,从而接收该组的数据包
- socket.SOCK_DGRAM表示使用UDP数据报套接字。
- socket.AF_INET表示使用IPv4地址族。

将udp-socket加入多播组
=========================

加入多播组

group变量存储多播地址, inet_aton()方法将其转换为二进制格式::

  group = socket.inet_aton(cls._SSDP_Addr[0])

将该地址和INADDR_ANY一起打包成一个4字节字符串加一个4/8字节整数,总长度为8/12字节::

  mreq = struct.pack('4sL', group, socket.INADDR_ANY)

- 4s:4个字符,使用s表示。这将打包成4个字节的字符串
- L:1个长整型(long integer),使用L表示。这将打包成4字节(32位)或8字节(64位)的整数,取决于平台

将socket加入到指定的多播组中::

  sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

socket的recvfrom与recv区别
==================================================

**参数个数**

- recvfrom(bufsize, flags) 接收数据并包含发送方地址信息。
- recv(bufsize, flags) 仅接收数据,不包含发送方地址信息。

**返回值**

- recvfrom() 返回值是(data, address)。包含接收的数据和发送方地址。
- recv() 返回值只有接收的数据data。

**使用场景**

- recvfrom() Typically used on UDP sockets where sender address matters.
  通常用于UDP套接字,需要获取发送方地址信息。
- recv() Typically used on TCP sockets where sender address does not matter.
  通常用于TCP套接字,不需要获取发送方地址信息。

**总结**

- 如果是TCP套接字,或者发送方地址信息不重要,使用recv()。
- 如果是UDP套接字,或者需要获取发送方地址信息,使用recvfrom()。


参考: `socket-底层网络接口 <https://docs.python.org/zh-cn/3/library/socket.html?#module-socket>`_

说明
==================================================

recv(bufsize, flags) 的bufsize决定一次能接受多少数据, send也是, 如果数据量大
建议将大数据分成多次循环发送.
