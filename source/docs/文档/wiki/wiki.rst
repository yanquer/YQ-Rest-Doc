================
wiki
================


.. post:: 2023-02-20 22:06:49
  :tags: wiki
  :category: 文档
  :author: YanQue
  :location: CD
  :language: zh-cn


目前是直接使用的sphinx, 写rst文档, 然后通过build编译称html.

感觉差点意思, 于是找了一下有哪些开源的wiki实现.


wiki.js


部署::

  docker run -d -p 8080:3000 --name wiki --restart unless-stopped -e "DB_TYPE=mysql" -e "DB_HOST=db" -e "DB_PORT=3306" -e "DB_USER=yanque" -e "DB_PASS=wikijsrocks_yanque" -e "DB_NAME=yanque_wiki" ghcr.io/requarks/wiki:2





