==================
可选安装工具
==================


安装::

  pip install celery[librabbitmq,redis,auth,msgpack]

中括号中表示可选拓展, 部分拓展说明:

- librabbitmq 使用 librabbitmq 的 C 库
- redis       使用 Redis 作为消息传输方式或结果后端
- mongodb     使用 MongoDB 作为消息传输方式（ 实验性 ），或是结果后端（ 已支持 ）。
- auth        序列化工具
- msgpack     序列化工具
- yaml        序列化工具
- eventlet    使用 eventlet 池
- gevent      使用 gevent 池
- threads     使用 线程 池

