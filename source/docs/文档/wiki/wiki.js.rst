====================
wiki.js
====================

一个开源的 wiki 框架, 支持数据库...

:官网/gitthub::
  `docs-wiki.js <https://docs.requarks.io>`_
  `github-wiki.js <https://github.com/requarks/wiki>`_

本地docker部署
====================

部署mysql, 可参考 :doc:`/docs/容器与集群/docker/docker_store/mysql` ::

  docker run -d --name mymysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=yanque_wiki -e MYSQL_PASSWORD=yanque_wiki -e MYSQL_DATABASE=yanque_wiki mysql

部署wiki.js::

  docker run -d -p 8080:3000 --name wiki --restart unless-stopped -e "DB_TYPE=mysql" -e "DB_HOST=172.17.0.1" -e "DB_PORT=3306" -e "DB_USER=yanque_wiki" -e "DB_PASS=yanque_wiki" -e "DB_NAME=yanque_wiki" ghcr.io/requarks/wiki

注意:

- 这里的 DB_HOST , 一开始只想着数据库已经映射到本地, 脑子抽了写了个 127.0.0.1 , 一直连不上数据库.
- 如果要设置中文, 不要使用官网文档建议的2的tag(2只有英文), 使用最新的.


待补充...

