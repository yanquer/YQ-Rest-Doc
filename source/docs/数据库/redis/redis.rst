============
redis
============

.. _redis官网: http://www.redis.cn/download.html

Redis 常用五大数据类型:

- String
- List (比如消息队列)
- Set (比如关注列表)
- Hash (复杂最想存储)
- Zset（有序集合）SortSet (比如排行榜)

aof文件：记录redis数据的变动情况

.. note::

  redis的key支持设置过期策略.

按照性能分类

- 单机
- 主从
- 高可用 (Redis集群)

待看:

- `美团万亿级 KV 存储架构与实践 <https://tech.meituan.com/2020/07/01/kv-squirrel-cellar.html>`_
- `阿里云Redis <https://help.aliyun.com/product/26340.html>`_

好处?
  距离, 电商为什么会用redis做消息系统，微服务下的高并发架构
  (作为消息中心, 生产者消费者中介)

  单机就能支持10w并发(标准8核16G)

docker 部署
========================

先去 `redis官网`_ 下载一个配置文件, 因为官方docker镜像内没有

按需修改配置文件, 注意默认不设置守护线程::

  daemonize no

这个不要改, 改了docker启动不了...

启动::

  docker run --name myredis -p 6379:6379 -d \
  -v /Users/yanque/project/code/moment-management/src/conf:/usr/local/etc/redis \
  redis redis-server /usr/local/etc/redis/redis.conf

``redis-server /usr/local/etc/redis/redis.conf`` 表示使用此配置文件.

也可以后面进入shell手动执行


