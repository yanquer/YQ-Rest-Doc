=========================
ntpq
=========================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


ntpq指令使用NTP模式6数据包与NTP服务器通信,能够在允许的网络上查询的兼容的服务器。它以交互模式运行,或者通过命令行参数运行。

此命令的适用范围：RedHat、RHEL、Ubuntu、CentOS、Fedora。

语法格式::

  ntpq [参数]

常用参数

-4
  使用ipv4解析
-6
  使用ipv6解析
-d
  打开调试模式
-i
  使用交互模式
-n
  以十进制格式显示主机地址
-p
  显示服务器同级设备的列表

-c [command]
  添加执行的命令到指定主机的命令列表

.. note::

  设置ntp的时候，server表示对时服务器，restrict表示对服务器做限制

restrict选项
=========================

restrict选项格式::

  restrict [ 客户端IP ]  mask  [ IP掩码 ]  [参数]

“客户端IP” 和 “IP掩码” 指定了对网络中哪些范围的计算机进行控制，
如果使用default关键字，则表示对所有的计算机进行控制，参数指定了具体的限制内容，常见的参数如下：

◆ ignore
  拒绝连接到NTP服务器
◆ nomodiy
  忽略所有改变NTP服务器配置的报文，但可以查询配置信息
◆ noquery
  忽略所有mode字段为6或7的报文，客户端不能改变NTP服务器配置，也不能查询配置信息
◆ notrap
  不提供trap远程登录功能，trap服务是一种远程时间日志服务。
◆ notrust
  不作为同步的时钟源。
◆ nopeer
  提供时间服务，但不作为对等体。
◆ kod
  向不安全的访问者发送Kiss-Of-Death报文。

server选项
=========================

server选项格式::

  server host  [ key n ] [ version n ] [ prefer ] [ mode n ] [ minpoll n ] [ maxpoll n ] [ iburst ]

其中host是上层NTP服务器的IP地址或域名，随后所跟的参数解释如下所示：

◆ key
  表示所有发往服务器的报文包含有秘钥加密的认证信息，n是32位的整数，表示秘钥号。
◆ version
  表示发往上层服务器的报文使用的版本号，n默认是3，可以是1或者2。
◆ prefer
  如果有多个server选项，具有该参数的服务器有限使用。
◆ mode
  指定数据报文mode字段的值。
◆ minpoll
  指定与查询该服务器的最小时间间隔为2的n次方秒，n默认为6，范围为4-14。
◆ maxpoll
  指定与查询该服务器的最大时间间隔为2的n次方秒，n默认为10，范围为4-14。
◆ iburst
  当初始同步请求时，采用突发方式接连发送8个报文，时间间隔为2秒。

参考: `ntp服务器restrict和server选项格式 <https://blog.csdn.net/wjciayf/article/details/51396144>`_


