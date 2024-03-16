===================================
nmap
===================================


.. post:: 2024-03-04 22:04:43
  :tags: kali, kali渗透专用指令
  :category: 安全
  :author: YanQue
  :location: CD
  :language: zh-cn


Network Mapper, Linux下的网络扫描和嗅探工具包(比如IP/端口扫描)

用法::

	nmap [Scan Type(s)] [Options] {target specification}

.. 不带任何参数, 限制Ping时, 在Ubuntu上默认功能为网络地址发现.

- target可以是单一 IP, 或主机名，或域名，或子网

选项参数
===================================

--interactive
	打开交互模式
-v
	输出详细信息
-O
	尝试识别远程操作系统
-sS
	TCP SYN 扫描 (又称半开放,或隐身扫描)
-sV
	打开系统版本检测
-A
	同时打开操作系统指纹和版本检测
-sn, -sP
	不扫描端口, 发送imcp和一个TCP报文到80端口

其他::

	-P0
		允许你关闭 ICMP pings.
	-Pn
		无ping, 跳过主机发现阶段，把每个都IP当成存活主机
	-P0 <协议号列表>
		IP 协议 ping,
	-sT
		TCP connect()扫描
	-sU
		UDP 扫描

示例
===================================

扫描局域网主机::

	nmap -sP 192.168.1.0/24

扫描主机端口::

	nmap -sT 192.168.1.101
	# 貌似其他非Kali机器自行安装的得 nmap -sT -Pn 192.168.1.101

匿名扫描::

	nmap -sS 192.168.1.101

.. code-block:: sh

	┌──(yanque㉿kali)-[~]
	└─$ nmap 192.168.179.129
	Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-02 17:24 CST
	Nmap scan report for 192.168.179.129
	Host is up (0.000042s latency).
	Not shown: 999 closed tcp ports (conn-refused)
	PORT   STATE SERVICE
	22/tcp open  ssh

	Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds

	┌──(yanque㉿kali)-[~]
	└─$

查看 192.168.179.129 的 22 端口状态::

	┌──(yanque㉿3675b5ebb8ce)-[~/test]
	└─$ nmap -p22 192.168.179.129
	Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-25 06:48 UTC
	Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
	Nmap done: 1 IP address (0 hosts up) scanned in 3.06 seconds

伪装MAC地址11:11:11:11:11:11 ::

	┌──(yanque㉿3675b5ebb8ce)-[~/test]
	└─$ nmap --spoof-mac 11:11:11:11:11:11 192.168.100.1 -Pn -p 80
	Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-25 07:35 UTC
	Spoofing MAC address 11:11:11:11:11:11 (Private)
	You have specified some options that require raw socket access.
	These options will not be honored without the necessary privileges.
	Nmap scan report for 192.168.100.1
	Host is up.

	PORT   STATE    SERVICE
	80/tcp filtered http

	Nmap done: 1 IP address (1 host up) scanned in 2.14 seconds



