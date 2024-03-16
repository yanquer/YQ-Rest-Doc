=============
ip
=============


.. post:: 2023-02-26 21:30:12
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


若无则安装::

    apt install iproute2

查看网络状态

语法::

    ip [option] [动作] [指令]

选项与参数
=============

支出的选项/命令:

- \-s    : s_
- link  : link_
- address, a    : address_
- route, r      :route_

s
------------

说明::

    ip -s   # 显示该装置的统计数据

    # 后面可跟参数
        link            # 关于设备的相关设定，包括MTU Mac地址等
        addr/address    # 关于额外的ip协议。例如多ip的达成
        route           # 与路由相关的设定

link
------------

说明::

    ip link

    # 后面可跟参数
        show        # 仅显示出与这个装置相关的内容
        set         # 可以开始设定项目，device指的是eth0等界面代号
                    # set支持参数
                    up|down     # 启动或者关闭某个接口
                    address     # 如果这个装置可以修改mac地址，用这个修改
                    name        # 命名
                    mtu         # 最大传输单元

address
------------

查看网卡信息

说明::

    # 或者 ip a
    ip address

    # 后面可跟参数
    show        # 显示接口ip信息. 默认就是此参数
    add|del     # 添加/删除相关设定
                # 支持参数
                ip      # 主要就是网域的设定
                dev     # 这个ip参数设定的接口 如eth0，
                    # 包含的参数如下
                    broadcast    # 设定广播地址，如果设定值是+，表示自动设置
                    label        # 装置的别名 例如 eth0:0
                    scope        # 这个界面的领域，
                        # 有以下几类
                        global          # 允许来自所有来源的联机
                        site            # 仅支持ipv6    仅允许本主机的联机
                        link            # 仅允许本装置自我联机
                        host            # 仅允许主机内部联机

输出参数详解：

lo
  全称loopback，是回环地址，经常被分配到127.0.0.1地址上，用于本机通信，经过内核处理后直接返回，不会在任何网络中出现。
eth0
  网卡名，如果有多块网卡，会有多个eth 或其它名称。
link/ether
  这个是MAC地址，唯一的，一块网卡一个MAC。
inet
  网卡上绑定的IP地址，通常所说的IPV4，一块网卡可以绑定多个IP地址。在绑定IP地址时注意：windows主机会提示IP地址冲突，而linux主机无任何提示，在添加新的IP地址时务必检测一下新地址是否和原有地址冲突，避免造成访问不可用。常用检测命令：ping或arping IP；
inet6
  IPV6地址，暂时没有，预留。

网络设备状态标识::

  <BROADCAST,MULTICAST,UP,LOWER_UP>

UP
  网卡处于启动状态。
BROADCAST
  网卡有广播地址，可以发生广播包。
MULTICAST
  网卡可以发生多播包。
LOWER_UP
  L1是启动的，即网线是插着的。

`<BROADCAST,MULTICAST,UP,LOWER_UP>` 这个配置串告诉我们：

  BROADCAST   该接口支持广播
  MULTICAST   该接口支持多播
  UP          网络接口已启用
  LOWER_UP    网络电缆已插入，设备已连接至网络

列出的其他值也告诉了我们很多关于接口的知识，
但我们需要知道 `brd` 和 `qlen` 这些词代表什么意思。
所以，这里显示的是上面展示的 `ip` 信息的其余部分的翻译::

  mtu 1500                                    最大传输单位（数据包大小）为1,500字节
  qdisc pfifo_fast                            用于数据包排队
  state UP                                    网络接口已启用
  group default                               接口组
  qlen 1000                                   传输队列长度
  link/ether 00:1e:4f:c8:43:fc                接口的 MAC（硬件）地址
  brd ff:ff:ff:ff:ff:ff                       广播地址
  inet 192.168.0.24/24                        IPv4 地址
  brd 192.168.0.255                           广播地址
  scope global                                全局有效
  dynamic enp0s25                             地址是动态分配的
  valid_lft 80866sec                          IPv4 地址的有效使用期限
  preferred_lft 80866sec                      IPv4 地址的首选生存期
  inet6 fe80::2c8e:1de0:a862:14fd/64          IPv6 地址
  scope link                                  仅在此设备上有效
  valid_lft forever                           IPv6 地址的有效使用期限
  preferred_lft forever                       IPv6 地址的首选生存期


route
------------

查看路由信息

说明::

    # 或者 ip r
    ip route

    # 后面可跟参数

    show            # 单纯显示路由表，也可以使用list. 默认就是此参数
    add|del
        # 支持参数
        IP|网域     # 可以使用192.168.170.0/24这样的网域或者单纯的ip
        via        # 从那个gateway出去，不一定需要
        dev        # 由那个装置连接出去，需要
        mtu        # 额外设定MTU的数值

输出详解
=============

- lo：全称loopback，是回环地址，经常被分配到127.0.0.1地址上，用于本机通信，经过内核处理后直接返回，不会在任何网络中出现。
- eth0：网卡名，如果有多块网卡，会有多个eth 或其它名称。
- link/ether：这个是MAC地址，唯一的，一块网卡一个MAC。
- inet：网卡上绑定的IP地址，通常所说的IPV4，一块网卡可以绑定多个IP地址。在绑定IP地址时注意：windows主机会提示IP地址冲突，而linux主机无任何提示，在添加新的IP地址时务必检测一下新地址是否和原有地址冲突，避免造成访问不可用。常用检测命令：ping或arping IP；
- inet6：IPV6地址，暂时没有，预留。
- 网络设备状态标识：<BROADCAST,MULTICAST,UP,LOWER_UP>
    - UP：网卡处于启动状态。
    - BROADCAST：网卡有广播地址，可以发生广播包。
    - MULTICAST：网卡可以发生多播包。
    - LOWER_UP：L1是启动的，即网线是插着的。

    `<BROADCAST,MULTICAST,UP,LOWER_UP` 这个配置串告诉我们::

        BROADCAST   该接口支持广播
        MULTICAST   该接口支持多播
        UP          网络接口已启用
        LOWER_UP    网络电缆已插入，设备已连接至网络


列出的其他值也告诉了我们很多关于接口的知识，但我们需要知道 `brd` 和 `qlen` 这些词代表什么意思。 所以，这里显示的是上面展示的 `ip` 信息的其余部分的翻译::

    mtu 1500                                    最大传输单位（数据包大小）为1,500字节
    qdisc pfifo_fast                            用于数据包排队
    state UP                                    网络接口已启用
    group default                               接口组
    qlen 1000                                   传输队列长度
    link/ether 00:1e:4f:c8:43:fc                接口的 MAC（硬件）地址
    brd ff:ff:ff:ff:ff:ff                       广播地址
    inet 192.168.0.24/24                        IPv4 地址
    brd 192.168.0.255                           广播地址
    scope global                                全局有效
    dynamic enp0s25                             地址是动态分配的
    valid_lft 80866sec                          IPv4 地址的有效使用期限
    preferred_lft 80866sec                      IPv4 地址的首选生存期
    inet6 fe80::2c8e:1de0:a862:14fd/64          IPv6 地址
    scope link                                  仅在此设备上有效
    valid_lft forever                           IPv6 地址的有效使用期限
    preferred_lft forever                       IPv6 地址的首选生存期

例::

    root@6378b4ca047d:/# ip address show to 172.17.0.3/16
    76: eth0@if77: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default  link-netnsid 0
        inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
        valid_lft forever preferred_lft forever
