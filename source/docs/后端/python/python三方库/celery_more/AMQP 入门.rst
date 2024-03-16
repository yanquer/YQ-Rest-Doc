==================
AMQP 入门
==================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库, celery_more
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


celery 基本上全部兼容了 AMQP 的实现, 所以此处对此作一个了解说明.

消息
==================

一个消息由消息头和消息体组成。

Celery 使用消息头来存储消息的内容类型以及内容的编码。
内容类型通常是用来序列化消息的序列化格式，
消息体包含要执行的任务的名称，任务ID(UUID)，执行任务的参数以及一些额外的元数据(比如重试次数和ETA(下次执行任务的时间))。

这是通过一个 Python 的字典来表示的示例任务消息::

  {'task': 'myapp.tasks.add',
  'id': '54086c5e-6193-4575-8308-dbab76798756',
  'args': [4, 4],
  'kwargs': {}}

生产者，消费者和中间人
====================================

发送消息的客户端通常被称为一个发布者，或一个生产者，而接收消息的实体被称为消费者。

中间人是将消息从生产者路由到消费者的消息服务器。

你可能在与AMQP相关的材料中看到这些术语被大量使用。

交换机，队列和路由键
====================================

- 消息将被发送到交换机
- 交换机将消息路由到一个或者多个队列。存在多种交换机类型来提供不同的消息路由方式，或实现不同的消息发送方案。
- 消息将在队列中等待直到有人消费它。
- 一旦消息被确认消费，将会从队列中删除。

发送和接收消息所需要的步骤如下:

- 创建一个交换机
- 创建一个队列
- 绑定队列到交换机。

为了使 task_queues 中的队列工作， Celery 将会自动创建所需要的实体(除非队列的 auto_declare 选项被设置为 False )。

下方是一个包含三个队列的示例队列配置; 一个用于视频，一个用于图片，另一个用于其他消息的默认队列::

  from kombu import Exchange, Queue

  app.conf.task_queues = (
      Queue('default', Exchange('default'), routing_key='default'),
      Queue('videos',  Exchange('media'),   routing_key='media.video'),
      Queue('images',  Exchange('media'),   routing_key='media.image'),
  )
  app.conf.task_default_queue = 'default'
  app.conf.task_default_exchange_type = 'direct'
  app.conf.task_default_routing_key = 'default'

交换机类型
==================

- 直连交换机
- 主题交换机

交换机的类型定义了交换机将会如何路由消息。
在正常情况下交换机被定义为 direct, topic, fanout。
此外也可以通过 RabbitMQ 的插件来使用非标准的交换机类型，
比如由 Michael Bridgen 实现的 last-value-cache plug-in 。

直连交换机
------------------
直连交换机通过精确的路由键来进行匹配，所以被路由键 video 绑定的队列只接收具有该路由键的消息。

主题交换机
------------------

主题交换机通过以点分隔的单词和通配符来匹配路由键::

  *(匹配单个单词)
  #(匹配零或多个单词)。

假如有如下路由键::

  usa.news
  usa.weather
  norway.news
  norway.weather

可以通过绑定 ``*.news`` 来接收所有的新闻，
绑定 ``usa.#`` 来接收与 USA 有关的所有消息，
或绑定 ``usa.weather`` 来接收所有与 USA 天气有关的消息。

相关的API命令
==================

- declare_ 通过名称声明交换机


declare
------------------

.. function:: exchange.declare(exchange_name, type, passive, durable, auto_delete, internal)

  通过名称声明交换机

  passive:
    被动意味着不会创建交换机，但是你可以通过这个参数来检查交换机是否被创建。
  durable:
    交换机将被持久化(也就是说，中间人(Broker)重启后，交换机仍然存在)
  auto_delete:
    指定该参数意味着如果没有队列使用该交换机，那么交换机将被中间人(Broker)删除。

  详情见 `<https://docs.celeryq.dev/projects/amqp/en/latest/reference/amqp.channel.html#amqp.channel.Channel.exchange_declare>`_

.. function:: queue.declare(queue_name, passive, durable, exclusive, auto_delete)

  通过名称声明一个队列

  exclusive:
    专有队列只能通过当前的连接进行消费，专有队列也同时是自动删除的


.. function:: queue.bind(queue_name, exchange_name, routing_key)

  通过路由键(routing_key)将队列绑定到交换机

  队列如果没有被绑定将不会接收消息，因为绑定是必须的


.. function:: queue.delete(name. If_unused=False, if_empty=False)

  删除队列及其绑定


.. function:: exchange.delete(name. If_unused=False)

  删除交换机


.. note::

  声明并不代表创建，在你声明的时候，你可以断定这个实体已经存在，并且是可操作的。
  这里并没有规定消费者或生产者中的哪一方需要最先创建交换机/队列/绑定。

  通常来说，最先需要它的哪一方就会创建它。

使用 API
==================

Celery 自带了一个名为 celery amqp 的工具，用于通过命令行来操作 AMQP API 去管理任务，
比如说创建或者删除队列或交换机，清理队列或发送消息。
该工具也可以用于 非 AMQP 的中间人，但是不一定实现了所有的命令操作。

你可以直接在`celery amqp 的命令里写参数，或者无参数启动命令模式::

  $ celery -A proj amqp
  -> connecting to amqp://guest@localhost:5672/.
  -> connected.
  1>

这里的 1> 是命令提示。数字 1 表示到目前为止指定的命令数。

输入 help 可以得到所有可用的命令列表。工具还支持自动补全，所以你可以输入一个命令然后按 tab 键来显示可能匹配到的命令列表。
让我们创建一个你可以发送消息的队列::

  1> exchange.declare testexchange direct
  ok.
  2> queue.declare testqueue
  ok. queue:testqueue messages:0 consumers:0.
  3> queue.bind testqueue testexchange testkey
  ok.

上方的命令创建了一个直连交换机 testexchange 和一个名为 testqueue 的队列。该队列通过路由键 testkey 绑定到直连交换机。
从现在开始，所有发送到 testexchange 交换机的带有路由键testkey 的消息将被移动到队列 testqueue 中。
你可以通过 basic.publish 命令发送一条消息::

  4> basic.publish 'This is a message!' testexchange testkey
  ok.

现在消息已经发送出去，你可以去获取消息了。
你可以在这里使用 basic.get 命令，该命令将会以同步轮询的方式去获取队列中的新消息
(这种方式对于维护任务来说是还可以的，但是对于服务来说，你需要使用 basic.consume命令来代替它)
从队列中弹出一条消息::

  {'body': 'This is a message!',
  'delivery_info': {'delivery_tag': 1,
                    'exchange': u'testexchange',
                    'message_count': 0,
                    'redelivered': False,
                    'routing_key': u'testkey'},
  'properties': {}}

AMQP 使用确认来表明一条消息已经被接收并且成功处理。
如果消息没有被确认并且消费者的通道关闭了，消息将被传递给另一个消费者。
请注意上方结构中列出来的传递标记 delivery_tag ;
再每个连接通道中，每个接收到的消息都有一个唯一的传递标记，这个标记用来确认消息。
但是要注意，传递标记并不是跨连接唯一的，所以在另一个客户端中，传递标记为 1 的消息可能与当前连接中的消息是不一致的。

你可以通过 basic.ack 命令来确认你收到的消息::

  6> basic.ack 1
  ok.

在我们的测试回话结束后，你应该清除你创建的实体::

  7> queue.delete testqueue
  ok. 0 messages deleted.
  8> exchange.delete testexchange
  ok.

路由任务
==================

队列声明
------------------

在 Celery 存在的队列可以通过 task_queues 来设置。

下方是一个包含三个队列的示例队列配置; 一个用于视频，一个用于图片，另一个用于其他消息的默认队列::

  default_exchange = Exchange('default', type='direct')
  media_exchange = Exchange('media', type='direct')

  app.conf.task_queues = (
      Queue('default', default_exchange, routing_key='default'),
      Queue('videos', media_exchange, routing_key='media.video'),
      Queue('images', media_exchange, routing_key='media.image')
  )
  app.conf.task_default_queue = 'default'
  app.conf.task_default_exchange = 'default'
  app.conf.task_default_routing_key = 'default'

在这里 task_default_queue 指定队列将被用于路由那些没有显示指定队列的任务。

task_default_exchange，exchange type 以及routing key 将被用作于任务的默认值，
并且也被用作于 task_queues 中的实体的默认值。

对单个队列的多个绑定也是被支持的。如下一个两个路由键同时绑定于同一个队列的例子::

  from kombu import Exchange, Queue, binding

  media_exchange = Exchange('media', type='direct')

  CELERY_QUEUES = (
      Queue('media', [
          binding(media_exchange, routing_key='media.video'),
          binding(media_exchange, routing_key='media.image'),
      ]),
  )

指定任务目标
------------------

任务的目标是通过如下的(按顺序)的方式决定的:

- Task.apply_async 的路由参数
- 在任务本身定义的路由参数
- 在 task_routes 中定义的 Routers

最好的做法是不在配置中进行硬编码，而是将其作为 Routers 的配置。这是最灵活的，并且合理的默认值仍然可以设置为任务的属性。

路由器
==================

路由器是决定任务的路由选项的函数。

定义一个新的路由器，你所需要做的是通过签名 ``(name, args, kwargs, options, task=None, **kw)``
定义一个函数::

  def route_task(name, args, kwargs, options, task=None, **kw):
          if name == 'myapp.tasks.compress_video':
              return {'exchange': 'video',
                      'exchange_type': 'topic',
                      'routing_key': 'video.compress'}

如果你返回队列的键值，它将会带着在task_queues 中定义的配置展开::

  {'queue': 'video', 'routing_key': 'video.compress'}

变成 -> ::

  {'queue': 'video',
  'exchange': 'video',
  'exchange_type': 'topic',
  'routing_key': 'video.compress'}

你可以通过将路由器的类添加到 task_routes 的配置中来安装路由器::

  task_routes = (route_task,)

路由器方法也可以通过名称添加::

  task_routes = ('myapp.routers.route_task',)

对于类似上方示例的简单的任务名称->路由映射，你可以简单地将字典放置在 task_routes 中来过的同样的行为效果::

  task_routes = {
      'myapp.tasks.compress_video': {
          'queue': 'video',
          'routing_key': 'video.compress',
      },
  }

将会按照顺序遍历路由器，直到在第一个返回真的路由器处停止，并将该路由器用作为任务的最终路由器。
你也可以将多个路由器定义在一个序列中::

  task_routes = [
      route_task,
      {
          'myapp.tasks.compress_video': {
              'queue': 'video',
              'routing_key': 'video.compress',
      },
  ]

路由器将会被按顺序访问，并选择第一个返回的值。
如果你使用的是 Redis 或 RabbitMQ ，你也可以在路由器中指定队列的默认优先级::

  task_routes = {
      'myapp.tasks.compress_video': {
          'queue': 'video',
          'routing_key': 'video.compress',
          'priority': 10,
      },
  }

类似的，对任务使用 apply_async 调用时，传递的参数将会覆盖默认的优先级::

  task.apply_async(priority=0)

**优先级顺序和集群响应**

需要重视的是，因为职程(worker) 的预取机制，如果同一时间提交了一堆任务，那么它们的优先级顺序可能发生混乱。
禁用职程的预取可以防止该问题，但是对于小而快的任务，这么做会导致达不到理想的性能。
在大多数情况下，简单的将 worker_prefetch_multiplier 参数减少到 1，
是一个简单而清晰的方式来提升系统的灵敏性，并且不会存在禁用预取带来的成本。
要注意的是优先级的顺序是按照值的反序来排列的：0 是最高优先级。

广播
==================

Celery 也支持广播路由。下面是一个 broadcast_tasks 交换机的示例, 它将任务分发给所有连接到它的职程::

  from kombu.common import Broadcast

  app.conf.task_queues = (Broadcast('broadcast_tasks'),)
  app.conf.task_routes = {
      'tasks.reload_cache': {
          'queue': 'broadcast_tasks',
          'exchange': 'broadcast_tasks'
      }
  }

现在任务 tasks.reload_cache 将会被被发送给从当前队列中消费的所有职程。
如下是另一个关于广播路由的任务，这次使用了 celery beat 定时器::

  from kombu.common import Broadcast
  from celery.schedules import crontab

  app.conf.task_queues = (Broadcast('broadcast_tasks'),)

  app.conf.beat_schedule = {
      'test-task': {
          'task': 'tasks.reload_cache',
          'schedule': crontab(minute=0, hour='*/3'),
          'options': {'exchange': 'broadcast_tasks'}
      },
  }

**广播和结果**

注意 Celery 结果并没有定义如果有两个任务使用同一个任务 ID 时会发生什么。
如果同一个人任务被派发到多于一个职程，该任务的状态历史将不被保留。
在这种情况下设置 task.ignore_result 属性忽略任务结果将会是个好主意。


