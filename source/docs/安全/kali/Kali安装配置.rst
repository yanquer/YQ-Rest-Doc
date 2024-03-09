=============================
Kali安装、配置
=============================

`下载地址 <https://www.kali.org/get-kali/>`_ ,
选择自己合适的版本下载即可，下载后，直接解压打开（需提前准备好环境如虚拟机）

默认账户密码::

	kali
	kali
	# 旧版本是 root 跟 toor

一些其他工具默认账密
=============================

BeEF-XSS::

	Username: beef
	Password: beef
	Configuration File: /etc/beef-xss/config.yaml

MySQL::

	User: root
	Password: (blank)
	Setup Program: mysql_secure_installation

OpenVAS::

	Username: admin
	Password: <Generated during setup>
	Setup Program: openvas-setup

Metasploit-Framework::

	Username: postgres
	Password: postgres
	Configuration File: /usr/share/metasploit-framework/config/database.yml

参考： `<https://www.kali.org/docs/introduction/default-credentials/>`_

换源
=============================

.. code-block:: sh

	# 备份
	mv /etc/apt/sources.list /etc/apt/sources.list.bak

	# 写入
	echo "deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
	deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
	" >/etc/apt/sources.list

安装vim, ssh
=============================

.. code-block:: sh

	apt update
	apt install vim ssh

启动ssh
=============================

.. code-block:: sh

	# 或者 service ssh start
	/etc/init.d/ssh start

	# 可以通过 netstat -anutp 查看是否在监听22端口

	# 设置开机启动
	update-rc.d ssh enable

