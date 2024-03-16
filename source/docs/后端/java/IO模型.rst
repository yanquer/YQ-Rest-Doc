==============================
IO模型
==============================


.. post:: 2023-02-27 21:24:23
  :tags: java
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


BIO
  阻塞IO
NIO
  非阻塞IO

  Java有提供一个Selector的多路复用机制

Selector多路复用
==============================

不会阻塞

在Linux下, 是基于epoll实现

会维护一个epoll数组, 底层调用C的本地方法返回一个文件描述符::

  epoll_create(256)

其他相关可参考 :doc:`/docs/后端/java/IO模型`

Netty线程模型
==============================

基于NIO做了一系列封装,
性能高于 :doc:`/docs/数据库/redis/redis`

