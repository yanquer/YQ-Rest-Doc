=========================
mac下应用运行管理
=========================


.. post:: 2024-03-09 18:21:01
  :tags: 
  :category: 常用工具使用
  :author: YanQue
  :location: CD
  :language: zh-cn


前言
=========================

.. topic:: 相关的指令

	- launchctl

.. code-block:: sh
	:caption: 用法

	# 显示当前的启动脚本
	launchctl list

	# 开机时自动启动Apache服务器
	sudo launchctl load -w /System/Library/LaunchDaemons/org.apache.httpd.plist

	# 设置开机启动并立即启动改服务
	launchctl load -w   **.pist

	# 设置开机启动但不立即启动服务
	launchctl load **.pist

	# 停止正在运行的启动脚本
	sudo launchctl unload [path/to/script]
	# 再加上-w选项即可去除开机启动
	sudo launchctl unload -w [path/to/script]

.. note::

	launchctl 管理 MacOS 的启动脚本, 控制启动计算机时需要开启的服务。也可以设置定时执行特定任务的脚本, 就像Linux cron一样。

	launchctl需要 root 权限。

参考: `MacOS launchctl 启动进程控制 <https://www.jianshu.com/p/baa23cc820d2>`_

使用
=========================

直接举例, 例如要停止Docker

.. code-block:: sh
	:caption: mac停止Docker
	:emphasize-lines: 1, 4

	yanque@yanquedembp ~ % launchctl list | grep docker
	-	0	com.docker.helper
	1333	0	application.com.docker.docker.25263488.25263866
	yanque@yanquedembp ~ % launchctl stop application.com.docker.docker.25263488.25263866