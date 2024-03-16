========================
netstat
========================


.. post:: 2023-02-26 21:30:12
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


Ubuntu安装::

	apt install net-tools -y

.. note::

	net-tools包含arp, ifconfig, netstat, rarp, nameif and route命令，如果使用这些命令报错，可以尝试安装。

功能
========================

查看网络状态

Linux netstat 命令用于显示网络状态。利用 netstat 指令可让你得知整个 Linux 系统的网络情况。

使用::

	netstat [-acCeFghilMnNoprstuvVwx][-A<网络类型>][--ip]

选项参数
========================

.. csv-table:: netstat选项参数
	:header: 选项, 含义

	-a/--all	, 显示所有连线中的Socket
	-n/--numeric	, 以ip形式显示当前建立的有效连接和端口.直接使用IP地址，而不通过域名服务器
	-u/--udp	, 显示UDP传输协议的连线状况。
	-t/--tcp	, 显示TCP传输协议的连线状况。
	-p/--programs	, 显示对应PID与程序名. 显示正在使用Socket的程序识别码和程序名称。
	A<网络类型>或--<网络类型>	, 列出该网络类型连线中的相关地址。
	-c/--continuous	, 持续列出网络状态。
	-C/--cache	, 显示路由器配置的快取信息。
	-e/--extend	, 显示网络其他相关信息。
	-F/--fib	, 显示路由缓存。
	-g/--groups	, 显示多重广播功能群组组员名单。
	-h/--help	, 在线帮助。
	-i,--interfaces	, 显示网络界面信息表单。
	-l/--listening	, 显示监控中的服务器的Socket。
	-M/--masquerade	, 显示伪装的网络连线。
	-N/--netlink/--symbolic	, 显示网络硬件外围设备的符号连接名称。
	-o/--timers	, 显示计时器。
	-r/--route	, 显示Routing Table。
	-s/--statistics	, 显示网络工作信息统计表。
	-v/--verbose	, 显示指令执行过程。
	-V/--version	, 显示版本信息。
	-w/--raw	, 显示RAW传输协议的连线状况。
	-x/--unix	, 此参数的效果和指定"-A unix"参数相同。
	--ip/--inet	, 此参数的效果和指定"-A inet"参数相同。


.. note::

	常用: ``netstat -anutp``

常用::

	#列出所有端口 (包括监听和未监听的)
	netstat -a     #列出所有端口
	netstat -at    #列出所有tcp端口
	netstat -au    #列出所有udp端口
	#列出所有处于监听状态的 Socket
	netstat -l        #只显示监听端口
	netstat -lt       #只列出所有监听 tcp 端口
	netstat -lu       #只列出所有监听 udp 端口
	netstat -lx       #只列出所有监听 UNIX 端口

	netstat -antup    #显示所有 及 占用程序名

内容解释::

	Proto        该联机的封包协议
	Recv-Q        非由用户程序连接所复制而来的总 bytes
	Send-Q        由远程主机所传送而来，但不具有ACK标志的总bytes数，意指主动联机SYN或其他标志的封包所占的bytes数
	Local Address    本地地址
	Foreign Address    远程主机地址
	stat        状态栏，有以下
			ESTABLISED    已建立的联机的状态
			SYNC_SENT    发出主动联机的联机封包
			SYNC_RECV    接收到一个要求联机的主动联机封包
			FIN_WAIT1    该插槽服务socket已中断，该联机正在断线中
			FIN_WAIT2    该联机已挂断，但正在等待对方主机响应断线确认的封包
			TIME_WAIT    该联机已挂断，但socket还在网络上等待结束
			LISTEN        通常在服务的监听port，可使用 -l查询
