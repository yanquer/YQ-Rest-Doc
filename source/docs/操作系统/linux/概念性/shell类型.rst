==========================
shell类型
==========================


.. post:: 2023-02-27 21:24:23
  :tags: linux, 概念性
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


.. shell基础了解

大致与 :doc:`/docs/操作系统/linux/概念性/linux系统环境加载顺序` 一致

登录shell
==========================

交互式登陆
	直接通过终端输入用户信息登陆系统

	如::

		su - username
		#或
		su -l username

	配置文件读取过程::

		/etc/profile --> /etc/profile.d/*.sh --> ~/.bash_profile --> /etc/bashrc

	交互式登录shell::

		Bash reads and executes the /etc/profile (if it exists).

		After reading that file, it looks for ~/.bash_profile, ~/.bash_login, and ~/.profile in that order, and reads and executes the first one (that exists and is readable).  When a login shell exits: Bash reads and executes ~/.bash_logout (if it exists).

非交互式登陆
	图形界面的终端 执行脚本

	如::

		su username

	配置文件读取过程::

		~/.bashrc/ --> /etc/bash_rc --> /etc/profile.d/*.sh

	交互式非登陆shell::

		Bash reads and executes ~/.bashrc (if it exists)

登陆Linux的时候执行的文件过程::

	/etc/profile --> (~/.bash_profile | ~/.bash_login | ~/.profile) --> ~/.bashrc --> /etc/bashrc --> ~/.bash_logout

参考: `<http://groups.google.com/group/linux.debian.user/browse_thread/thread/2b71ecfc45789958/7bff24e3bae74b36?lnk=raot>`_

详加载顺序可见 :doc:`/docs/操作系统/linux/概念性/linux系统环境加载顺序`

选项/参数
==========================

- 短选项(参数)
	短横线加字母, 如::

		-h
		-a $option_arg
- 长选项(参数)
	双短横线加单词, 如::

		--help
		--add $option_arg
- 普通参数
	直接跟在后面的, 如::

		'commit msg'

	或者直接以双短横线开始作为分隔符的, 如::

		# 两个横线后面的部分都会被认为是参数了，而不再是前面的命令的选项了
		-- 'commit msg'

		# 单横线也可以其实
		- 'commit msg'

.. note::

	bash的man page::

		A -- signals the end of options and disables further option
		processing. Any arguments after the -- are treated as filenames and
		arguments. An argument of - is equivalent to --.


