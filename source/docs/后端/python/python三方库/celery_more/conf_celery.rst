====================
配置
====================

支持的一种配置形式::

  输入端 -> Broker
  输出端 -> 结果后端

支持的配置
====================

- task_serializer , 序列化方式_
- result_serializer 结果后端的序列化方式
- timezone, 时区_
- task_annotations, 详细指定多个任务配置, 如 任务限速_
- task_routes, 路由_
- broker_transport_options, 可见性超时_
- result_backend, 结果后端配置: 返回结果_
- task_publish_retry, 是否失败重试, 默认为 True
- task_publish_retry_policy, 失败重试策略_
- task_compression, 压缩_

序列化方式
--------------------

task_serializer, 默认为json

在客户端和工作人员之间传输的数据需要进行序列化，
因此 Celery 中的每条消息都有一个 content_type 标头，
该标头描述了用于对其进行编码的序列化方法。

默认的序列化器是JSON，但是您可以使用 task_serializer 设置更改此设置，或者针对每个任务，甚至针对每条消息进行更改。

有内置的支持JSON，pickle，YAML 和msgpack

每个序列化器都有其优点和缺点:

- json - JSON 被大多数的编程语言支持，并且现在是 Python 标准的一部分（自2.6开始），
  并且现代 Python 库（例如 simplejson）具有非常快的 json 解析速度。

  JSON 的缺点是会限制你使用如下的数据类型：字符串、Unicode、字典和列表。小数和日期明显缺失。
  二进制数据使用 Base64 编码进行传输，这与支持纯二进制传输的相比，数据传输量增长了34%。
  但如果你的数据满足上述限制，并且你需要跨语言支持，则 JSON 可能是你的最佳选择。
  有关更多信息，请参见 http://json.org
- pickle - 如果你除了 Python 外，并不需要支持其他语言，
  那么使用 pickle 编码将让你获得对所有 Python 内建类型的支持（类实例除外）。

  相比 JSON，使用 pickle 序列化的二进制文件更小，传输速度更快。
  请参阅 pickle 获得更多信息
- yaml - YAML 和 JSON 有许多相似的特征，yaml 支持包括日期、递归引用在内的更多数据类型。
  然而，Python 的 YMAL 库相比 JSON 库 要慢很多。

  如果你需要更具表现能力的数据集合，则 YMAL 比上面的序列化方式更适合。
  有关更多信息，请参见 http://yaml.org/
- msgpack - msgpack 是一种接近 JSON 的二进制序列化格式。但是，它还很年轻，因此此时应该将支持视为实验性的
  有关更多信息，请参见 http://msgpack.org/

编码类型可以用作消息头，因此 workers 知道如何反序列化所有的任务。如果你使用自定义序列方案，则该序列化必须被 workers 支持。
发送任务时的序列化配置优先级如下（从高到低）:

- serializer 执行选项。
- Task.serializer 属性。
- task_serializer 属性。

为单个任务调用设置序列化方式::

  >>> add.apply_async((10, 10), serializer='json')

任务限速
--------------------

任务限速除了::

  task_annotations = {
      'tasks.add': {'rate_limit': '10/m'}
  }

还可以在启动时设置(仅适用 RabbitMQ 或 Redis)::

  $ celery -A tasks control rate_limit tasks.add 10/m
  worker@example.com: OK
      new rate limit set successfully

时区
--------------------

内部和消息中的所有的时间和日期使用的都是 UTC 时区。

当职程（Worker）收到消息时，例如倒计时设置，会将 UTC 时间转换为本地时间。
如果需要使用与系统不同的时区，可以通过 timezone进行配置::

  app.conf.timezone = 'Europe/London'

路由
--------------------

Celery 支持 AMQP 中提供的所有路由，可以将消息发送到指定的任务队列路由。

通过 task_routes 可以设置一个按名称分配的路由任务队列，将所有的内容集中存放在一个位置::

  app.conf.update(
      task_routes = {
          'proj.tasks.add': {'queue': 'hipri'},
      },
  )

可以在程序是使用 queue 参数进行指定队列::

>>> from proj.tasks import add
>>> add.apply_async((2, 2), queue='hipri')

可以通过设置运行职程（Worker）时指定职程（Worker）从某个队列中进行消费（celery worker -Q）::

  $ celery -A proj worker -Q hipri

也可以通过“,”作为分割符进行设置多个队列，
例如，可以将默认队列和 hipri 队列一起通过职程（Worker）进行消费，
其中默认队列 celery 由于历史原因被命名::

  $ celery -A proj worker -Q hipri,celery

队列名称的顺序不分前后，职程（Worker）给予队列分配的权重是相同的。
相关路由的信息以及使用 AMQP 路由的全部功能，详情请参考路由任务: `官网中文翻译文档-路由`_

自动路由
++++++++++++++++++++


最简单的路由方式是使用选项 task_create_missing_queues 进行设置(默认情况下，此设置为打开状态)。

如果启用了该参数，将会自动创建没有在 task_queues 选项中定义的命名队列。这样可以更加容易的执行简单的路由任务。

假如你有两个处理常规任务的服务器 x 和 y ，以及一个只处理与 feed 相关的任务的服务器 z 。那么你可以使用这样的配置::

  task_routes = {'feed.tasks.import_feed': {'queue': 'feeds'}}

启用这样的路由设置后，import_feed 的任务将会被路由到 feeds 队列中，
而其他的任务将会被路由到默认的队列(因为历史原因被命名为celery)。

另外，你还可以使用通配符，甚至正则表达式来匹配所有在 feed.tasks 命名空间内的所有任务::

  app.conf.task_routes = {'feed.tasks.*': {'queue': 'feeds'}}

如果匹配模式的顺序很重要，你应该使用列表的方式指定路由的次序::

  task_routes = ([
      ('feed.tasks.*', {'queue': 'feeds'}),
      ('web.tasks.*', {'queue': 'web'}),
      (re.compile(r'(video|image)\.tasks\..*'), {'queue': 'media'}),
  ],)

安装完路由之后，你可以按照如下方式启动服务器 z 来只处理 feeds 队列的消息::

  user@z:/$  celery -A proj worker -Q feeds

你可以指定任意数量的队列，所以你也可以让这个服务器去处理来自默认队列的消息::

  user@z:/$  celery -A proj worker -Q feeds,celery

修改默认队列的名称
____________________

你可以使用如下的配置来修改默认队列的名称::

  app.conf.task_default_queue = 'default'

定义队列
____________________

这部分的特性主要是隐藏复杂的 AMPQ 协议实现，只对用户暴露出需要的基础用法。但是，你可能仍然对队列是如何被声明的原理感兴趣。
使用如下的配置将会创建一个名为 video 的队列::

  {
    'exchange': 'video',
    'exchange_type': 'direct',
    'routing_key': 'video'
  }

对于那些非 AMPQ 的后端组件如 Redis 或者 SQS 并不支持交换机，所以他们要求交换机的名称与队列的名称一致。
使用这种设计可以确保正常的处理不同的情况。

手动路由
++++++++++++++++++++

假设你有两台处理常规任务的服务器，x 和 y，以及另一台只处理与 feed 相关的任务，你可以使用如下的配置::

  from kombu import Queue

  app.conf.task_default_queue = 'default'
  app.conf.task_queues = (
      Queue('default',    routing_key='task.#'),
      Queue('feed_tasks', routing_key='feed.#'),
  )
  task_default_exchange = 'tasks'
  task_default_exchange_type = 'topic'
  task_default_routing_key = 'task.default'

task_queues 是一个包含 Queue 实例的列表。如果你不想指定 exchange 和 exchange_type 的值。
这些变量将会被 task_default_exchange 和 task_default_exchange_type 来设置。

要将一个任务路由到 feed_tasks 队列中，你可以在task_routes配置中添加一个入口::

  task_routes = {
          'feeds.tasks.import_feed': {
              'queue': 'feed_tasks',
              'routing_key': 'feed.import',
          },
  }

还可以使用 Task.apply_async() 或者 send_task() 中的 routing_key 参数来重载这些设置::

  >>> from feeds.tasks import import_feed
  >>> import_feed.apply_async(args=['http://cnn.com/rss'],
  ...                         queue='feed_tasks',
  ...                         routing_key='feed.import')

要使服务器 z 只处理来自 feed 队列的消息，你可以使用 celery worker -Q 来启动服务::

  user@z:/$ celery -A proj worker -Q feed_tasks --hostname=z@%h

服务器 x 和 y 需要配置为从默认的队列中消费消息::

  user@x:/$ celery -A proj worker -Q default --hostname=x@%h
  user@y:/$ celery -A proj worker -Q default --hostname=y@%h

也可以让 feed 消息的处理职程去处理常规消息，比如在某个时间出现很多任务需要去做::

  user@z:/$ celery -A proj worker -Q feed_tasks,default --hostname=z@%h

如果你想添加配置了另一个交换机的队列，只需要指定自定义的 exchange 和 exchange_type ::

  from kombu import Exchange, Queue

  app.conf.task_queues = (
      Queue('feed_tasks',    routing_key='feed.#'),
      Queue('regular_tasks', routing_key='task.#'),
      Queue('image_tasks',   exchange=Exchange('mediatasks', type='direct'),
                            routing_key='image.compress'),
  )

如果你对这些术语感到迷惑，你应该阅读一下 AMPQ.

.. note::

  此处建议看一下: `Redis Message Priorities <https://docs.celeryq.dev/en/latest/userguide/routing.html#amqp-primer>`_

特殊的路由选项
++++++++++++++++++++

RabbitMQ 消息优先级
____________________

支持的中间人(Broker)::

  RabbitMQ

从 4.0 版本开始引入。

队列可以通过设置 x-max-priority 参数来支持优先级::

  from kombu import Exchange, Queue

  app.conf.task_queues = [
      Queue('tasks', Exchange('tasks'), routing_key='tasks',
            queue_arguments={'x-max-priority': 10}),
  ]

可以通过指定参数 task_default_priority 来设置所有队列的默认最大优先级::

  app.conf.task_queue_max_priority = 10

可以通过指定参数 task_default_priority 来设置所有任务的默认优先级::

  app.conf.task_default_priority = 5

Redis 消息优先级
____________________

支持的中间人(Broker)::

  Redis

虽然 Celery 的 Redis 中间人(Broker) 支持了优先级的字段，但是 Redis 本身并没有优先级的概念。
所以在尝试使用 Redis 来实现优先级之前，请阅读下方的说明，因为你可能遇到一些意想不到的行为。

优先级的支持是通过为每个队列创建 n 个列表来实现的。
也就是说即使存在 10(0-9) 个优先级别，在默认情况下也会被合并成 4 个级别来节省资源。
也就是说一个名为 celery 的队列将会分成 4 个队列::

  ['celery0', 'celery3', 'celery6', 'celery9']

如果你想要更多的优先级别，你可以通过设置中间人(Broker)参数 priority_steps 来实现::

  app.conf.broker_transport_options = {
      'priority_steps': list(range(10)),
  }

这就是说，要注意到这样的实现永远不如在服务器端实现优先级别，只能近似说是最佳的实现。但是这对于你的应用来说也足够好了。

可见性超时
--------------------

可见性超时为将消息重新下发给另外一个程序之前等待确认的任务秒数

可以通过 broker_transport_options 选项进行修改::

  app.conf.broker_transport_options = {'visibility_timeout': 3600} # 一个小时

默认的可见性超时时间为1个小时。

返回结果
--------------------

如果您想保存任务执行返回结果保存到Redis，您需要进行以下配置::

  app.conf.result_backend = 'redis://localhost:6379/0'

有关 Redis 保存结果的完整选项列表，请查阅 Redis后端配置。
如果您使用的是 Redis 哨兵默认是，则需要使用 result_backend_transport_options 进行指定 master_name::

  app.conf.result_backend_transport_options = {'master_name': "mymaster"}

.. note::

  可以通过配置 ``task_ignore_result`` 来全局禁用结果/返回值

  单个禁用直接 ``@app.task(ignore_result=True)`` 即可

在调用apply_async和delay执行任务时, 通过传递ignore_result参数, 可以在每次执行的基础上设置开启/禁用任务结果::

  @app.task
  def mytask(x, y):
      return x + y

  # No result will be stored
  result = mytask.apply_async(1, 2, ignore_result=True)
  print result.get() # -> None

  # Result will be stored
  result = mytask.apply_async(1, 2, ignore_result=False)
  print result.get() # -> 3

**默认情况下， 当配置了 backend ，任务将不会忽略结果( ignore_result=False )**

选项优先顺序如下(从低到高):

- 全局选项 task_ignore_result
- 任务配置 ignore_result
- 任务执行时选项 ignore_result

失败重试策略
--------------------

task_publish_retry_policy

支持的键为:

max_retries: int = 3
  最大重试次数，在这种情况下，将抛出重试失败的异常。

  值为None意味着它将永远重试。
interval_start: int = 0
  定义两次重试之间要等待的秒数（浮点数或整数）。默认值为0（第一次重试是瞬时的）。
interval_step: float = 0.2
  在每次连续重试时，此数字将被添加到重试延迟中（浮点数或整数）。默认值为0.2。
interval_max: float=0.2
  重试之间等待的最大秒数（浮点数或整数）。默认值为0.2。

例::

  add.apply_async((2, 2), retry=True, retry_policy={
      'max_retries': 3,
      'interval_start': 0,
      'interval_step': 0.2,
      'interval_max': 0.2,
  })

重试的最长时间为0.4秒。
默认情况下将其设置为相对较短，因为如果代理连接断开，连接失败可能导致重试堆效应–
例如，许多 Web 服务器进程正在等待重试，从而阻止了其他传入请求。

压缩
--------------------

task_compression

Celery 可以使用以下内建方案压缩消息。

- brotli_
- bzip2_
- gzip_
- lzma_
- zlib_
- zstd_

你还可以创建自己的压缩方式，并在kumbo压缩注册中注册它们。
发送任务时的压缩方案配置优先级如下（从高到低）:

- compression 执行选项。
- Task.compression 属性。
- task_compression 属性。

任务调用时指定压缩方法的示例::

  >>> add.apply_async((2, 2), compression='zlib')

brotli
++++++++++++++++++++

brotli 针对 web 进行了优化，尤其是小型文档。该压缩对诸如字体、html页面等静态内容最有效。
要使用 brotli，请用以下命令进行安装::

  $ pip install celery[brotli]

bzip2
++++++++++++++++++++

bzip2 创建的文件比 gzip 小，但是压缩和解压的速度明显慢于 gzip。

要使用 bzip2，请确保 bzip2 已经编译到你的 Python 可执行文件中。
如果你得到以下错误 ImportError::

  >>> import bz2
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ImportError: No module named 'bz2'

这意味着你应该重新编译支持 bzip2 的 Python 版本。

gzip
++++++++++++++++++++

gzip 适用于内存占用较小的系统，因此 gzip 非常适合内存有限的系统。该压缩常用语生成带有 “.tar.gz” 后缀的文件。

要使用 gzip，请确保 gzip 已经编译到你的 Python 可执行文件中。

如果你得到以下错误::

  >>> import gzip
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ImportError: No module named 'gzip'

这意味着你应该重新编译支持 gzip 的 Python 版本。

lzma
++++++++++++++++++++

lzma 具有较好的压缩效率以及压缩解压速度，但内存消耗更大。
要使用 lzma，请确保 gzip 已经编译到你的 Python 可执行文件中，并且你的 Python 版本为3.3或更高版本。
如果你得到以下错误 ImportError::

  >>> import lzma
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ImportError: No module named 'lzma'

这意味着你应该重新编译支持 lzam 的 Python 版本。
也可以通过以下的方式进行安装::

  $ pip install celery[lzma]

zlib
++++++++++++++++++++

zlib 是 Deflate 算法的抽象，它的 API 支持包括 gzip 格式和轻量级流格式文件的支持。
zlib 是许多软件系统的重要组成部分，例如 Linux 内核以及 Git VCS。

要使用 zlib，请确保 zlib 已经编译到你的 Python 可执行文件中。
如果你得到以下错误 ImportError::

  >>> import zlib
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ImportError: No module named 'zlib'

这意味着你应该重新编译支持 zlib 的 Python 版本。

zstd
++++++++++++++++++++

zstd是一个针对 zlib 的实时压缩方案，且有着更好的压缩效率。zstd 由 Huff0 和 FSE 库提供快速算法。
要使用zstd，请用以下命令进行安装::

  $ pip install celery[zstd]

支持的配置方式
====================

- 硬编码_
- 使用配置文件_

硬编码
--------------------

指定序列化方式为json::

  app.conf.task_serializer = 'json'

多个配置使用 update::

  app.conf.update(
      task_serializer='json',
      accept_content=['json'],  # Ignore other content
      result_serializer='json',
      timezone='Europe/Oslo',
      enable_utc=True,
  )

使用配置文件
--------------------

配置py模块的方式
++++++++++++++++++++

配置模块例 celeryconfig.py ::

  broker_url = 'pyamqp://'
  result_backend = 'rpc://'

  task_serializer = 'json'
  result_serializer = 'json'
  accept_content = ['json']
  timezone = 'Europe/Oslo'
  enable_utc = True

  # 其他配置

  # 任务执行错误时的专用队列
  task_routes = {
      'tasks.add': 'low-priority',
  }

  # 任务限速, 每分钟内允许执行的10个任务
  task_annotations = {
      'tasks.add': {'rate_limit': '10/m'}
  }

配置好后加载配置模块 celeryconfig::

  app.config_from_object('celeryconfig')

可以通过以下命令来进行验证配置模块是否配置正确::

  $ python -m celeryconfig

配置py类的方式
++++++++++++++++++++

可以将其写做一个类::

  from celery import Celery

  app = Celery()

  class Config:
      enable_utc = True
      timezone = 'Europe/London'

  app.config_from_object(Config)
  # or using the fully qualified name of the object:
  #   app.config_from_object('module:Config')

配置环境变量的方式
++++++++++++++++++++

还可以将配置文件写入环境变量, 后面直接从环境变量读(app.config_from_envvar)::

  import os
  from celery import Celery

  #: Set default configuration module name
  os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')

  app = Celery()
  app.config_from_envvar('CELERY_CONFIG_MODULE')

然后通过指定的环境变量进行配置使用的配置模块：
$ CELERY_CONFIG_MODULE="celeryconfig.prod" celery worker -l info

task_routes涉及到自定义队列处理任务,
详情见: `官网中文翻译文档-路由`_

部分说明见: 路由_

配置的获取/过滤
====================

将配置作为调试信息或类似信息打印出来，那么您也可能希望过滤掉敏感信息，如密码和API密钥。
Celery 提供了集中打印配置信息工具，其中一个为 humanize()::

  >>> app.conf.humanize(with_defaults=False, censored=True)

该方法将配置信息转换为列表字符串返回，默认情况下，仅包含修改的键值，可以通过 with_defaults 参数进行包含默认的配置信息。
可以通过 table() 方法将返回结果转换为字典::

  >>> app.conf.table(with_defaults=False, censored=True)

注意：Celery 不会删除所有的敏感配置信息，通过正则表达式来进行检索通常命名的信息，
如果包含敏感信息的自定义配置，Celery 会标识为机密的名称来下进行命名秘钥。
如果命名中含有子字符串，将会进行过滤::

  API、TOKEN、KEY、SECRET、PASS、SIGNATURE、DATABASE

注意事项
====================

广播前缀
--------------------

默认情况下，所有的虚拟机都可以看到广播的消息。

您必须为消息进行设置前缀，以便它们由仅活动的虚拟机接收::

  app.conf.broker_transport_options = {'fanout_prefix': true}

注意：该选项仅是向后兼容的，老版本不支持。集群中所有的职程都必须要开启设置，否则无法进行通信。

该设置在将来以后的版本是默认配置，所以请尽早进行迁移。

广播模式
--------------------

默认情况下， 职程（Worker）收到所有与任务相关的事件。

为了避免该情况发生，需要进行配置 fanout_patterns 广播模式，以便职程（Worker）只能订阅相关的事件::

  app.conf.broker_transport_options = {'fanout_patterns': true}

该设置在将来以后的版本是默认配置。

可见性超时-注意
--------------------

如果在 可见性超时_ 内没有完成任务，该任务会重新分配给另外一个职程（Worker）进行执行。

这可能会出现在预计时间超出可见性超时时间的问题，如果出现该问题，任务将重新循环执行。

因此您必须要增加可见性超时时间用于用于匹配最长的执行时间。

注意：Celery会在职程（Worker）关闭的重新分配消息，如果可见性超时时间过长在断电或者强制终止职程（Worker）的情况会“丢失“重新分配的任务。

定期执行任务不会被可见性超时影响，因为这是俩个不同的概念。

您可以通过配置同名的配置选项来扩增可见性超时时间::

  app.conf.broker_transport_options = {'visibility_timeout': 432000}

对应的值必须为 int 类型。

驱逐Key
--------------------

在某些情况下，Redis会根据（驱逐策略）进行驱逐一些key

可能会出现已经错误问题::

  InconsistencyError: Probably the key ('_kombu.binding.celery') has been removed from the Redis database.

您可以在Redis服务器的 time_out 参数设置为0进行避免key被驱逐。


.. _官网中文翻译文档-路由: https://www.celerycn.io/v/4.4.0/yong-hu-zhi-nan/lu-you-ren-wu-routing-tasks


