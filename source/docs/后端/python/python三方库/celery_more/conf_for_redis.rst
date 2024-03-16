====================
基于redis的配置
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库, celery_more
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


此处只介绍redis相关配置, 更多配置见 :doc:`/docs/后端/python/python三方库/celery_more/conf_celery`

redis相关配置
====================

默认使用的 rabbitmq, 所以用 redis 需要先安装以来库(若没安装)::

  pip install celery[redis]

代码里的配置::

  app.conf.broker_url = 'redis://localhost:6379/0'

此url格式为::

  redis://:password@hostname:port/db_number

默认使用的是 localhost 的 6379 端口中 0 数据库。（ Redis 默认有 16 个数据库）

可以通过 Uninx 套接字进行连接，URl 格式如下::

  redis+socket:///path/to/redis.sock

可以通过设置 virtual_host参数添加到URL上进行指定使用时 Uninx 套接字连接的数据库编号::

  redis+socket:///path/to/redis.sock?virtual_host=db_number

Celery 也可以连接 Redis 哨兵也是非常简单的::

  app.conf.broker_url = 'sentinel://localhost:26379;sentinel://localhost:26380;sentinel://localhost:26381'
  app.conf.broker_transport_options = {'master_name':'cluster1'}


