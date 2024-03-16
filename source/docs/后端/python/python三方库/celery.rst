====================
celery
====================


.. post:: 2024-03-09 18:21:01
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


安装::

  pip install celery[librabbitmq,redis,auth,msgpack]

详细见: :doc:`/docs/后端/python/python三方库/celery_more/option_install`

简介
====================

分布式任务队列

一个简单、灵活、可靠的分布式系统，可用于处理大量消息的消息队列, 可用于处理实时数据以及任务调度

任务队列: 一般用于线程或计算机之间分配工作的一种机制

Celery 通过消息机制进行通信:

- Broker 中间人
- Worker 职程

客户端向消息队列发送消息, 实际就是给到了 Broker,
然后 Broker 将消息发给 Worker, 由 Worker 执行.

Celery 可以在一台机器上运行，也可以在多台机器上运行，甚至可以跨数据中心运行。

优点:

- 分布式, 可多机运行
- 跨语言(协议)
- 自定义消息队列(Broker), 如: rabbitmq, redis
- 高可用, 如果出现丢失连接或连接失败，职程（Worker）和客户端会自动重试，并且中间人通过 主/主 主/从 的方式来进行提高可用性。
- 快速, 单个 Celery 进行每分钟可以处理数以百万的任务，而且延迟仅为亚毫秒（使用 RabbitMQ、 librabbitmq 在优化过后）。
- 灵活, Celery 的每个部分几乎都可以自定义扩展和单独使用.
  例如自定义连接池、序列化方式、压缩方式、日志记录方式、任务调度、生产者、消费者、中间人（Broker）等。
- 支持 Crontab 定时任务
- 内存保护, --max-tasks-per-child 参数适用于可能会出现资源泄漏（例如：内存泄漏）的任务
- 时间和速率的限制, 可以控制每秒/分钟/小时执行任务的次数，或者任务执行的最长时间，也将这些设置为默认值，针对特定的任务或程序进行定制化配置

相关说明:

- Celery Beat: 任务调度器，Beat 进程会读取配置文件的内容，周期性的将配置中到期需要执行的任务发送给任务队列
- Celery Worker: 执行任务的消费者，通常会在多台服务器运行多个消费者来提高运行效率
- Broker: 消息代理，也是任务队列本身（通常是消息队列或者数据库），通常称为消息中间件，
  接收任务生产者发送过来的任务消息，存进队列再按序分发给任务消费方
- Producer: 任务生产者，调用 Celery API 的函数或者装饰器而产生任务并交给任务队列处理的都是任务生产者

中间件配置
====================

Celery 需要消息中间件来进行发送和接收消息。

RabbitMQ 和 Redis 中间人的功能比较齐全，但也支持其它的实验性的解决方案，其中包括 SQLite 进行本地开发。

应用设计(编码)
====================

task.py::

  from celery import Celery
  app = Celery('tasks', broker='amqp://guest@localhost//')
  @app.task
  def add(x, y):
      return x + y

- 第一个参数为当前模块的名称，只有在 ``__main__`` 模块中定义任务时才会生产名称。
- 第二个参数为中间人（Broker）的链接 URL。

app的传递
--------------------

即 Celery 实例 的共享, 一般不建议使用全局的 app 变量, 而是以参数传递的形式替代::

  class Scheduler(object):
      def __init__(self, app):
          self.app = app

在celery内部实现中，使用 celery.app_or_default() 函数使得模块级别的 API 也能正常使用::

  from celery.app import app_or_default

  class Scheduler(object):
      def __init__(self, app=None):
          self.app = app_or_default(app)

在开发环境中，可以通过设置 CELERY_TRACE_APP 环境变量在应用实例链被打破时抛出一个异常::

  $ CELERY_TRACE_APP=1 celery worker -l info

中文翻译文档称其为 `打破链式操作：Breaking the chain <https://www.celerycn.io/v/4.4.0/yong-hu-zhi-nan/ying-yong-application/da-po-lian-shi-cao-zuo-breaking-the-chain>`_

不是怎么理解是何含义

启动Worker
========================================

启动/运行 Celery 职程（Worker）服务

命令行启动
--------------------

code::

  celery -A tasks worker --loglevel=info
  # celery -A src.time_schedule --workdir ./  worker -l info -E

.. note::

  可以查看帮助信息::

    celery --help

直接在 python 中启动
--------------------

调试时使用比较方便, 或者是一些需要在代码内部启动时

 启动一个职程（Worker）:::

  from celery import Celery
  app = Celery()

  @app.task
  def add(x, y): return x + y

  if __name__ == '__main__':
      app.worker_main()

手动调用任务
====================

命令行
--------------------

使用命令行的方式, 详情可参考 :doc:`/docs/后端/python/python三方库/celery_more/命令行工具` ::

  例::

  celery -A src.time_schedule call -a '[2, 2]'  src.time_schedule.pre_tasks.add
  7506ef60-5621-460a-8219-7a97f6e96f4e

代码使用方式
--------------------

调用我们创建的实例任务，可以通过 delay() 进行调用。

delay() 是 apply_async() 的快捷方法，可以更好的控制任务的执行（详情：调用任务：Calling Tasks）::

  >>> from tasks import add
  >>> add.delay(4, 4)

该任务已经有职程（Worker）开始处理，可以通过控制台输出的日志进行查看执行情况。

调用任务会返回一个 AsyncResult 的实例，用于检测任务的状态，等待任务完成获取返回值（如果任务执行失败，会抛出异常）。
默认这个功能是不开启的，如果开启则需要配置 Celery 的结果后端，见 保存任务结果_ 。

**详细说明**

使用 delay() 方法进行调用::

  >>> add.delay(2, 2)

delay() 实际上为 apply_async() 的快捷使用::

  >>> add.apply_async((2, 2))

apply_async() 可以指定调用时执行的参数，例如运行的时间，使用的任务队列等::

  >>> add.apply_async((2, 2), queue='lopri', countdown=10)

上面的实例中，任务被下发到 lopri 队列中，任务下发之后会在最早10秒内执行。 直接调用任务函数进行执行任务，不会发送任何任务消息::

  >>> add(2, 2)
  4

每一个任务被调用时会赋值一个的任务ID（UUIID）::

  res = add.delay(2, 2)
  res.id

如果任务执行引发异常，可以进行检查异常以及溯源，默认情况下 result.get() 会抛出异常::

  >>> res = add.delay(2)
  >>> res.get(timeout=1)
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/devel/celery/celery/result.py", line 113, in get
      interval=interval)
  File "/opt/devel/celery/celery/backends/rpc.py", line 138, in wait_for
      raise meta['result']
  TypeError: add() takes exactly 2 arguments (1 given)

如果不希望 Celery 抛出异常，可以通过设置 propagate 来进行禁用::

  >>> res.get(propagate=False)
  TypeError('add() takes exactly 2 arguments (1 given)',)

在这种情况下，他可以返回引发错误的实例，需要检查任务是否执行成功还是失败，可以通过在结果实例中使用对应的方法::

  >>> res.failed()
  True

  >>> res.successful()
  False

如何知道任务是否执行失败？可以通过查看任务的 state 进行查看::

  >>> res.state
  'FAILURE'

一个任务只能有当前只能有一个状态，但他的执行过程可以为多个状态，一个典型的阶段是::

  PENDING -> STARTED -> SUCCESS

启动状态是一种比较特殊的状态，仅在 task_track_started 启用设置或 @task(track_started=True)的情况下才会进行记录。
挂起状态实际上不是记录状态，而是未知任务ID的默认状态，可以从此实例中看到::

  >>> from proj.celery import app

  >>> res = app.AsyncResult('this-id-does-not-exist')
  >>> res.state
  'PENDING'

重试任务比较复杂，为了证明，一个任务会重试两次，任务的阶段为::

  PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS

保存任务结果
====================

如使用Redis作为Celery结果后端和中间人, ::

  app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

已经配置结果后端，重新调用执行任务。会得到调用任务后返回的一个 AsyncResult 实例::

  >>> result = add.delay(4, 4)

ready() 可以检测是否已经处理完毕::

  >>> result.ready()
  False

整个任务执行过程为异步的，如果一直等待任务完成，会将异步调用转换为同步调用::

  >>> result.get(timeout=1)
  8

如果任务出现异常，get() 会再次引发异常，可以通过 propagate 参数进行覆盖::

  >>> result.get(propagate=False)

如果任务出现异常，可以通过以下命令进行回溯::

  >>> result.traceback

.. note::

  也可以使用配置文件进行配置, 见 :doc:`/docs/后端/python/python三方库/celery_more/conf_celery`

  如果后端使用资源进行存储结果，必须要针对调用任务后返回每一个 AsyncResult 实例调用 get() 或 forget() ，进行资源释放。

远程控制
====================

使用 RabbitMQ（AMQP）、Redis 或 Qpid 作为中间人（Broker），可以在运行时控制和检查职程（Worker）。

例如，当前职程（Worker）正在处理的任务::

  $ celery -A proj inspect active

这是通过广播消息实现的，集群中所有职程（Worker）都会所有收到远程控制发出的指令。
也可以通过 --destination 选项指定一个或多个职程（Worker）进行操作，使用“,”进行分割职程（Worker）主机列表::

  $ celery -A proj inspect active --destination=celery@example.com

如果没有提供目的地，那么每个工作人员都将采取行动并回复请求。

celery inspect 命令不能修改程序，只能进行查看职程（Worker）概况以及统计信息，可以通过 help 进行查看::

  $ celery -A proj inspect --help

celery control 命令可以查看实际上改变了工作在运行时的状况::

  $ celery -A proj control --help

例如，可以强制职程（Worker）启用事件消息（用于监控任务以及职程（Worker））::

  $ celery -A proj control enable_events

启动事件后，可以启动事件转储程序，进行查看职程（Worker）目前执行的状况::

  $ celery -A proj events --dump

或者可以启动 curses 接口::

  $ celery -A proj events

当监控完毕之后，可以禁用事件::

  $ celery -A proj control disable_events

celery status 命令可以远程控制并且显示集群中职程（Worker）的列表::

  $ celery -A proj status

查看所有任务
====================

调用 Celery 实例的 tasks ::

  app = Celery()
  app.tasks

仅当导入定义的模块时任务才会被注册。

默认加载程序导入配置 imports 列出的所有模块。
app.task() 装饰器负责在应用任务注册表中注册你的任务。

详细说明
====================

.. toctree::
  :maxdepth: 1

  ./celery_more/option_install
  ./celery_more/conf_celery
  ./celery_more/conf_for_redis
  ./celery_more/命令行工具
  ./celery_more/load_celery
  ./celery_more/canvas
  ./celery_more/task
  ./celery_more/exception
  ./celery_more/logging
  ./celery_more/应用设计拓展
  ./celery_more/优化
  ./celery_more/AMQP 入门
  ./celery_more/调试
  ./celery_more/并发
  ./celery_more/信号
  ./celery_more/一些问题







