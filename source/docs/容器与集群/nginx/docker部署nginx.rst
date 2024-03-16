==========================
docker部署nginx
==========================


.. post:: 2023-02-20 22:06:49
  :tags: nginx
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


大概指令::

	docker pull nginx
	docker run --name mynginx -d -p 80:80 -v /Users/yanque/project/new_doc_rst/build/html:/usr/share/nginx/html nginx

首先本地目录要有html项目, 我的在 `/Users/yanque/project/new_doc_rst/build/html` , 映射上去.

然后本地打开 localhost访问即可, 局域网内可用内网ip打开.


