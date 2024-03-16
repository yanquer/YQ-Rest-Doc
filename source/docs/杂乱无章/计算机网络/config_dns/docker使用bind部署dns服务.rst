==================================
docker使用ubuntu/bind部署dns服务
==================================


.. post:: 2024-03-09 18:21:01
  :tags: config_dns
  :category: 计算机网络
  :author: YanQue
  :location: CD
  :language: zh-cn


使用的镜像: `ubuntu/bind9 <https://hub.docker.com/r/ubuntu/bind9>`_

创建容器::

	mkdir -p dns_config
	docker run -d --name bind9-dns-server -e TZ=UTC -p 30053:53 -v dns_config:/data  ubuntu/bind9:9.18-22.04_beta

后面方式基本与 ::doc:`ubuntu配置dns` 一致

其他
===============================

具有管理面板的docker-bind: `使用Docker搭建自己的DNS服务器 <https://cloud.tencent.com/developer/article/2027134>`_

