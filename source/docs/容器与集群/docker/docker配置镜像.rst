====================
docker配置镜像
====================


.. post:: 2023-02-20 22:06:49
  :tags: docker
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


.. sidebar::

	后面看到github上有: https://gist.github.com/y0ngb1n/7e8f16af3242c7815e7ca2f0833d3ea6

镜像配置概述
====================

由于网络原因官方镜像下载很慢, 所以需要配置镜像加速.

配置成功后都是执行 `docker info` ,查看输出是否有自己配置的镜像地址.

linux
_______________________

适用于linux, 将配置加到 `/etc/docker/daemon.json`

.. code-block:: sh
	:caption: 适用于linux的配置

	mkdir -p /etc/docker
	tee /etc/docker/daemon.json <<-'EOF'
	{
	"registry-mirrors": [
		"https://0b27f0a81a00f3560fbdc00ddd2f99e0.mirror.swr.myhuaweicloud.com",
		"https://ypzju6vq.mirror.aliyuncs.com",
		"https://registry.docker-cn.com",
		"http://hub-mirror.c.163.com",
		"https://docker.mirrors.ustc.edu.cn"
	]
	}
	EOF
	systemctl daemon-reload
	systemctl restart docker

mac
_______________________

#. 右键点击桌面顶栏的 docker 图标,
#. 选择 Preferences (偏好) ,
#. 在 Docker Engine 标签下的 Registry mirrors 列表中将镜像地址的数组: ``"registry-mirrors": ["https://你的前缀地址.http://mirror.aliyuncs.com"]``
#. 点击 Apply & Restart 按钮, 等待Docker重启并应用配置的镜像加速器。

.. note::

	原以为mac也是跟linux类似, 结果在 `/etc/docker/daemon.json` 加入了配置不生效.
	思索了一下可能有两个原因:

		- *Docker for Mac* 跟命令行安装的docker不一致
		- mac下安装的docker只能在应用内配置

	更正, 是这两个原因也不是, mac下一般都是用的用户安装的, 所以默认的配置地址为 `~/.docker/daemon.json`, 而非 etc 下的目录.

镜像参考
_______________________

.. code-block:: json
	:caption: docker镜像地址参考

	{
	"registry-mirrors": [
		"https://0b27f0a81a00f3560fbdc00ddd2f99e0.mirror.swr.myhuaweicloud.com",
		"https://ypzju6vq.mirror.aliyuncs.com",
		"https://registry.docker-cn.com",
		"http://hub-mirror.c.163.com",
		"https://docker.mirrors.ustc.edu.cn"
	]
	}

- 官方国区docker `"https://registry.docker-cn.com"`
- 网易 `"http://hub-mirror.c.163.com"`
- 中科大 `"https://docker.mirrors.ustc.edu.cn"``


不同系统容器与镜像位置
========================

.. topic:: linux

	- `cd /var/lib/docker` - 容器与镜像存放在此目录下
	- 镜像位置: /var/lib/docker/image
	- 容器位置: /var/lib/docker/containers

.. topic:: mac, 不同版本或许可能文件版本不一样

	- `/Users/xxxxmyname/Library/Containers/com.docker.docker/Data` ,可以到上面的目录中, 查看文件大小, du -sh *
	- 本机存放位置如下: `/Users/xxxxmyname/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw`


.. note::

	设置docker清华源可参考: `Docker Community Edition 镜像使用帮助 <https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/>`_

	另外一般 apt 更新提示校验不一致的, 一般就是国内镜像源没有更新.


补充一个自己 Ubuntu 服务器配置Docker的命令集
================================================

.. code-block:: sh

	# 如果你过去安装过 docker，先删掉:

	sudo apt-get remove docker docker-engine docker.io containerd runc

	# 首先安装依赖:

	sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common

	# 根据你的发行版，下面的内容有所不同。你使用的发行版：
	# Ubuntu
	# 信任 Docker 的 GPG 公钥:


	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

	# 添加软件仓库:


	echo \
	"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
	$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

	# 最后安装

	sudo apt-get update
	sudo apt-get install docker-ce