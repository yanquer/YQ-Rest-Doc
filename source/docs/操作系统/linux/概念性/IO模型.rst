===============================
IO模型
===============================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 概念性
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


epoll
===============================

好处
  epoll是单线程, 基于回调; 减少多线程切换的开销

epoll_create
  函数::

    int epoll_create(int size);

  关于更多信息, 可以通过查看::

    man epoll_create

  .. note::

    文件描述符（file descriptor），
    Linux内核为高效管理已被打开的“文件”所创建的索引，用该索引可以找到文件
epoll_ctl
  对于指定的文件描述符epfd引用的epoll实例,
  监听相关事件event

  函数::

    int epoll_ctl (int epfd, int op, int fd, struct epoll_event *event);

  op
    - EPOLL_CTL_ADD： 注册新的fd到epfd中，并关联事件event；
    - EPOLL_CTL_MOD：修改已经注册的fd的监听事件；
    - EPOLL_CTL_DEL：从epfd中移除fd，并且忽略掉绑定的event，这时event可以为null;
  events
    有很多可选值，这里只举例最常见的几个

    - EPOLLIN ：表示对应的文件描述符是可读的；
    - EPOLLOUT：表示对应的文件描述符是可写的；
    - EPOLLERR：表示对应的文件描述符发生了错误；

  成功则返回0，失败返回-1
epoll_wait
  等待 epoll_ctl 的事件

  当socket收到数据后，
  操作系統的中断程序调用回调函数会给epoll实例的
  事件就緒列表rdlist里添加该socket引用（这块是操作系统实现的），
  当程序执行到epoll_wait 时，如果rdllist已经引用了socket，
  那么 epoll_wait 直接返回，如果rdllist为空，阻塞进程

  rdllist
    就绪事件列表

  再底层就是操作系统的 ** 中断** 实现




