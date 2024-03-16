===============================
windows安装Ubuntu
===============================


.. post:: 2023-02-20 22:06:49
  :tags: docker
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


环境
===============================

- 系统: windows11

安装概述
===============================

安装虚拟机
_______________________________

windows上一般都是用的 `Wmware Woprkstation` ,

官网下载地址: `Wmware Woprkstation下载页面 <https://www.vmware.com/cn/products/workstation-pro/workstation-pro-evaluation.html>`_ ,

截至2022-12-11, 最新版为17Pro, 安装包下载地址: `Wmware Woprkstation安装包 <https://download3.vmware.com/software/WKST-1700-WIN/VMware-workstation-full-17.0.0-20800274.exe>`_ .

jihuo: `许可证密钥 <https://www.kejihub.com/16647.html#:~:text=VMware%20Workstation%2017,Pro%E8%AE%B8%E5%8F%AF%E8%AF%81%E5%AF%86%E9%92%A5%EF%BC%88Linux%2FMac%E9%80%9A%E7%94%A8%EF%BC%89%204A4RR-813DK-M81A9-4U35H-06KND%20NZ4RR-FTK5H-H81C1-Q30QH-1V2LA%204C21U-2KK9Q-M8130-4V2QH-CF810>`_ .


安装Ubuntu
_______________________________

`官网 <https://cn.ubuntu.com/download/desktop>`_ 下载镜像安装.

设置
===============================

.. topic:: 换源

	我使用的是清华源, 备份原来内容, 将新地址写入即可

	.. code-block:: sh
		:caption: 清华源地址

		# 默认注释了源码镜像以提高 apt update 速度, 如有需要可自行取消注释
		deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
		# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
		deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
		# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
		deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
		# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
		deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
		# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse

		# 预发布软件源, 不建议启用
		# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
		# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse

	- 备份: ``mv /etc/apt/sources.list /etc/apt/sources.list.bak``
	- 写入: ``echo "上面源地址" >/etc/apt/sources.list`` ,或者直接vi进去修改(第一次安装的系统没有vim)

.. note::

	注意源地址后面的 ``jammy`` 代表了当前版本是 Ubuntu 22, 可以通过 ``lsb_release -a`` 查看

	.. figure:: ../../../resources/images/2022-12-11-20-18-46.png
		:align: center
		:width: 480px

		查看当前已安装Ubuntu版本

	不是安装的22版本的注意换成自己对应版本的代号.

docker run时候配置映射路径
===============================

windows与linux路径分隔符不一样，不过还是可以使用linux的分隔符传入， 比如我本地的路径是::

	D:\project\rst-document\build

可以这样传入::

	docker run --name mynginx -p80:80 -v "/D/project/rst-document/build/html:/usr/share/nginx/html" -d nginx

