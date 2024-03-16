=================
mysql
=================


.. post:: 2023-02-20 22:06:49
  :tags: docker, docker_store
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


:hub地址::
  `docker-mysql <https://hub.docker.com/_/mysql>`_


一些环境变量:

- MYSQL_ROOT_PASSWORD
- MYSQL_DATABASE
- MYSQL_USER, MYSQL_PASSWORD
- MYSQL_ALLOW_EMPTY_PASSWORD
- MYSQL_RANDOM_ROOT_PASSWORD
- MYSQL_ONETIME_PASSWORD
- MYSQL_INITDB_SKIP_TZINFO

运行::

  docker run --name mymysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=yanque_wiki -e MYSQL_PASSWORD=yanque_wiki -d mysql:tag


