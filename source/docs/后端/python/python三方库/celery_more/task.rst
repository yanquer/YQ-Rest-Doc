===============
Celery的Task
===============

:参考::
  `[Celery 中文手册] 任务: Tasks <https://www.celerycn.io/v/4.4.0/yong-hu-zhi-nan/ren-wu-tasks>`_

概念与 异步 的任务类似

基础
===============

使用 task() 装饰器轻松的创建任何可被调用的任务::

  from .models import User

  @app.task
  def create_user(username, password):
      User.objects.create(username=username, password=password)

支持指定参数::

  @app.task(serializer='json')
  def create_user(username, password):
      User.objects.create(username=username, password=password)

注意, 若存在多个装饰器, ``app.task`` 需要放在首位.

还有一个 ``app.shared_task`` 待...

一些属性/方法
===============

app.task装饰器支持的参数
------------------------------

name:
  任务注册的名称。

  可以手动设置任务名称，也可以通过模块名和类名进行自动生成(默认行为)。
backend:
  结果后端的实例，用于任务结果后端，默认为 app.backend，可以通过 result_backend 进行配置。
acks_late:
  如果设置为 True，任务执行后（而不是执行前，默认为执行前）才会确认该任务的消息。

  注意：如果职程（Worker）执行过程中崩溃，任务可能会执行多次。
  可以通过 task_acks_late 参数来进行全局配置。
track_started:
  如果设置为 True，当职程（Worker）执行任务时，任务状态为 stared。

  默认为 False，因为在正常情况下是不需要该颗粒度级别的。
  任务要么挂起、完成要么等待重试。
  如果有长时间运行的任务，并且需要报告任当任务状态时，stared比较有用。

  任务执行的职程（Worker）和进程 id 可以通过状态的元数据中进行查看（例如：result.info['pid']）。

  可以通过 task_track_started 进行全局配置。
rate_limit: Union[int, float, None]
  配置任务的频率.

  限制指定任务类型的速率（限制在指定时间内运行的任务数量）。当速率限制生效时，任务仍然会完成，但是可能需要一些时间才能开始。

  如果限制速率为 None，表示速率限制无效.

  速率可以为 int 也可以为 float 类型，则被表示为“每秒任务数”。
bind: bool=False
  为 Trur 时表示设置第一个参数为 self (task实例)
serializer: str
  设置序列化方式, 会覆盖掉初始配置.

  默认为 task_serializer，
  也可以为 pickle、json、yaml 或者通过 kombu.serialization.registry 注册的自定义序列化方法。
request:
  如果该任务正处于执行状态，该信息包含该任务的请求信息。使用多线程本地存储。
  见: request_
throws: tuple
  预期内的异常，如果在元组中含有该异常类，将不会被视为异常。 但是日志会记录到结果后端.
time_limit:
  该任务的硬时间限制（以秒为单位），如果没有设置职程（Worker）时，使用默认值。
soft_time_limit:
  该任务的软时间限制（以秒为单位），如果没有设置职程（Worker）时，使用默认值。
ignore_result:
  不存储任务状态信息，如果配置该选项 AsyncResult 将失效，无法进行检测任务情况以及返回内容。

  如果你并不关心任务的结果，请务必确定设置 ignore_result 选项，因为存储结果会浪费时间和资源。
store_errors_even_if_ignored:
  如果设置为 True ，即使任务被忽略，也会存储错误信息。
compression:
  标识需要使用默认压缩方法的字符串。

  默认为 task_compression，可以设置为 gzip、bzip2或通过 kombu.compression 注册的自定义压缩方案。
max_retries: int = 3
  当前任务调用 self 或使用 autoretry_for 参数时才会启用。

  如果重试的次数超过最大限制，会引发 MaxRetriesExceededError 异常。在异常时不会自动重试，所以必须手动调用 retry()。

  默认值重试次数为3次，如果设置为 None 会关闭重试限制，直到任务执行成功为止。

  速率限制也可以在数值后面添加 "/s"、"/m" 或 "/h"，以秒、分钟或以小时为单位。任务将在指定的时间内平均分配。

  例如: "100/m" （每分钟100个任务）。则强制会在同一个职程（Worker）实例上启动俩个任务之间至少 600ms 的延迟。

  默认值通过 task_default_rate_limit 进行设定：如果未指定，表示默认情况禁用任务的速率限制。

  注意，该速率限制为每一个职程（Worker）实例的限制，并非全局速率限制。配置全局速率限制（例如，API每秒最多请求的次数），必须制定队列。
default_retry_delay: Union[int, float] = 30 * 60
  如果任务需要重试, 设置每次重试之间的间隔时间. 单位: 秒(s)
autoretry_for:
  任务失败时重试, 相关的配置.
  异常类的列表或元组，如果任务在执行的过程中引发异常，任务将自动重试。默认情况下不会自动重试任何异常。

  见 autoretry_for_
retry_kwargs: dict
  任务失败重试时相关配置. 自定义配置自动重试参数。

  注意，如果使用下面的 exponential backoff 选项是，
  countdown 任务选项将由 Celery 的自动重试系统决定，字典中包含 countdown 会被忽略。

  见 retry_kwargs_
retry_backoff: Union[int, bool] = False
  如果将此选项设置为True，则自动重试将按照 exponential backoff 规则延迟。
  第一次重试延迟 1 秒，第二次重试延迟 2 秒，第三次延迟 4 秒，第四次延迟 8 秒，以此类推。
  （如果启用了 retry_jitter 会修改延迟值）。

  如果该选项设置为数字，则作为延迟因子.
  例如，该选项设置为 3，那么第一次重试将延迟 3 秒，第二次将延迟 6 秒，第三次延迟 12 秒，第四次延迟 24秒，以此类推。

  默认情况下，该选项设置为 False，自动重试不会延迟。
retry_backoff_max: int = 600
  如果启动了 retry_backoff，该选项在任务自动重试之间设置以秒为单位的最大延迟。

  默认情况，该选项默认值为 600，即 10分钟。
retry_jitter: bool = True
  Jitter 用于随机性引入指数回退延迟，防止队列中所有任务同时执行.

  如果该选项设置为 True，则将 retry_backoff 计算的延迟作为最大值，实际的延迟值为一个介于 0 和最大值之间的一个随机数。


retry
---------------

任务失败时的重试

当调用 retry 时，会发送与原始任务相同的ID发送一条消息，将该消息发送到原始任务的对列中。
当任务被重试时，也会被记录为一个任务状态，便于通过 result 实例来跟踪任务。

例::

  @app.task(bind=True)
  def send_twitter_status(self, oauth, tweet):
      try:
          twitter = Twitter(oauth)
          twitter.update_status(tweet)
      except (Twitter.FailWhaleError, Twitter.LoginError) as exc:
          raise self.retry(exc=exc)

exc 参数主要用传递日志和存储任务结果时的使用的异常信息。exception 和 traceback 都将在任务状态中可用(如果启用了结果后端)。

任务如果有一个 max_retries 值，超出了重试的最大次数，则会重新引发当前的异常信息，但如果:

- exc 参数没有设置
  该情况会引发 MaxRetriesExceededError 异常
- 没有异常
  如果没有初始异常来重新引发exc参数，可以使用::

    self.retry(exc=Twitter.LoginError())

  设置 exc 参数值

request
---------------

`任务请求：Task Request <https://www.celerycn.io/v/4.4.0/yong-hu-zhi-nan/ren-wu-tasks/ren-wu-qing-qiu-task-request>`_

app.Task.request 包含与当前执行任务相关的信息和状态。
该请求定义了以下属性:

.. csv-table::
  :header: 属性名称,  说明

  id,         执行任务的唯一ID
  group,      任务组的唯一ID（该任务是组成员的情况下）
  chord,      此任务所属的和弦的惟一id(如果该任务是标题的一部分)
  correlation_id, 用于重复数据删除的自定义ID
  args,       选项参数
  kwargs,     关键字参数
  origin,     发送任务的主机名
  retries,    任务重试次数，默认是从 0 开始的
  is_eager,   如果任务是由客户端执行，并非职程（Worker）执行，设置 True
  expires,    任务预计时间（如果已经设置的情况下），时间为 UTC 格式（取决于 enable_utc 设置）
  hostname,   执行任务的职程（Worker）实例的节点名
  delivery_info,  添加附加传递消息，主要用于包含交付任务的交换和路由键的映射，retry() 主要用于重新讲任务下发到队列中，该 dict 中的键可用取决于使用的消息中间人（Broker）。
  reply-to,   回复的发送的队列名称（例如，与 RPC 结果后端一起使用）
  called_directly,  如果职程（Worker）未执行任务，则此标志设置为true
  timelimit,  当前(软、硬)时间限制的元组(如果有的话)
  callbacks,  如果此任务成功返回，将调用的签名列表
  errback,    如果此任务失败，将调用的签名列表
  utc,        设置为 true ，启用 UTC

  headers,    与任务消息一起发送的消息头的映射（可以为 None）
  reply_to,   回复的地址（队列名称）
  correlation_id,   一般与任务的ID相同，通常用于AMQP中跟踪回复的内容

  root_id,    此任务所属工作流中的第一个任务的唯一ID（如果有）
  parent_id,  调用此任务的任务的惟一id（如果有）
  chain,      反转形成链的任务列表（如果有）。列表中最后一个任务是当前任务执行成功之后的下一个任务。如果使用任务协议的第一个版本，则链任务将位于 request.callbacks 中

案例
访问上下文访问信息的一个任务案例::

  @app.task(bind=True)
  def dump_context(self, x, y):
      print('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(
              self.request))

bind 参数表示该函数绑是一个绑定方法，可以通过访问任务类型实例中的属性和方法。

任务重试
===============

使用装饰器参数的方式
------------------------------

.. _autoretry_for:

有时，您只想在引发特定异常时重试任务。 可也通过 Celery 中 task() 装饰器中的 autoretry_for 参数进行自动重试任务::

  from twitter.exceptions import FailWhaleError

  @app.task(autoretry_for=(FailWhaleError,))
  def refresh_timeline(user):
      return twitter.refresh_timeline(user)

.. _retry_kwargs:

可以通过 task() 中的 retry_kwargs 参数来指定 retry() 内部调用参数::

  @app.task(autoretry_for=(FailWhaleError,),
            retry_kwargs={'max_retries': 5})
  def refresh_timeline(user):
      return twitter.refresh_timeline(user)

上面的示例与在 try ... except 语句中包含的代码块使用 retry_ 效果一致::

  @app.task
  def refresh_timeline(user):
      try:
          twitter.refresh_timeline(user)
      except FailWhaleError as exc:
          raise div.retry(exc=exc, max_retries=5)

如果你想自动重试任何错误，只需使用::

  @app.task(autoretry_for=(Exception,))
  def x():
      ...

手动捕获的方式
---------------

见 retry_

任务状态
===============

内置状态
---------------

PENDING
  任务正在等待执行或未知。任何未知的任务 ID 都默认处于挂起状态。
STARTED
  任务已经开始。默认情况下不会记录，需要启用，请参阅 app.Task.track_started.。

  meta-data：正在执行任务的职程（Worker） pid 和主机名。
SUCCESS
  任务执行成功。

  meta-data：任务结果返回值 propagates：Yes ready: Yes
FAILURE
  任务执行失败。
  meta-data：执行异常时的任务信息，其中 traceback 包含引发错误的堆栈信息。 propagates：Yes
RETRY
  任务处于重试状态。

  meta-data：结果信息包含导致重试的异常信息，traceback 包含引发异常时堆栈的回溯。 propagates：No
REVOKED
  任务被撤销。

  propagates：Yes

自定义状态
---------------

**使用 update_state() 更新任务状态**

只需要设置一个位置的名称，就可以轻松的自定义状态，状态名通常是大写的字符串。

例如，您可以查看定义自定义中止状态的可中止任务::

  @app.task(bind=True)
  def upload_files(self, filenames):
      for i, file in enumerate(filenames):
          if not self.request.called_directly:
              self.update_state(state='PROGRESS',
                  meta={'current': i, 'total': len(filenames)})

在这里，创建了一个名称为“ PROGRESS”的状态，通过 current 和 total 作为元数据的一部分，
计算任务当前正在进行状态的任何应用程序以及任务在进程中位置。可以通过该方法来创建任务进度条。

自定义任务类
===============

所有的任务都继承 app.Task 类，run() 方法为任务体。
例如::

  @app.task
  def add(x, y):
      return x + y

在内部大概会是这样::

  class _AddTask(app.Task):

      def run(self, x, y):
          return x + y
  add = app.tasks[_AddTask.name]

任务调用
===============

- apply_async_ , 发送一个任务消息
- delay_ ,       直接发送一个任务消息,但是不支持运行参数
- calling_ ,     应用一个支持调用接口（例如，add(2,2)）的对象,
  意味着任务不会被一个 worker 执行,但是会在当前线程中执行(但是消息不会被发送)

apply_async
---------------

.. function:: apply_async(args[, kwargs[, ...]])

  发送一个任务消息。

  T.apply_async((arg,), {'kwarg': value})

  从现在起, 十秒内执行::

    T.apply_async(countdown=10)

  从现在起十秒内执行，指明使用eta::

    T.apply_async(eta=now + timedelta(seconds=10))

  从现在起一分钟执行，但在两分钟后过期::

    T.apply_async(countdown=60, expires=120)

  两天内过期，使用datetime对象::

    T.apply_async(expires=now + timedelta(days=2))

  一些位置参数:

  link: Union[Callable, list]
    Celery支持任务链，一个任务在另一个任务之后。回调任务将用父任务的结果作为一部分参数::

      res = add.apply_async((2, 2), link=add.s(16))

      # 译者注
      # res.get() --> 4 # 2+2 = 4
      # res.children[0].get() --> 20 # 4 + 16
  link_error: Union[Callable, list]
    添加错误回调签名

    例子::

      @app.task
      def error_handler(uuid):
          result = AsyncResult(uuid)
          exc = result.get(propagate=False)
          print('Task {0} raised exception: {1!r}\n{2!r}'.format(
                uuid, exc, result.traceback))

    可以使用 link_error 执行选项将其添加到任务中::

      add.apply_async((2, 2), link_error=error_handler.s())

    此外，link 和 link_error 选项都可以是list::

      add.apply_async((2, 2), link=[add.s(16), other_task.s()])

    然后将依次调用回调/错误返回，并且将使用父任务的返回值作为部分参数来调用所有回调
  countdown: int
    在某个时间之前结束, 见 countdown_
  eta: datatime
    在某个时间之前结束, 见 eta_
  expires: Union[int, datetime]
    任务有效期, 与上基本一致, 见 expires_
  retry: bool = True
    是否失败重试, 对应配置为: task_publish_retry
  retry_policy: dict
    重试策略, 对应配置为: task_publish_retry_policy.

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


delay
---------------

.. function:: delay(*args, **kwargs)

  直接发送一个任务消息,但是不支持运行参数。

  ``T.delay(arg, kwarg=value)`` 调用 apply_async 的快捷方式::

    .delay(_args, *_kwargs)

  等价于调用::

    .apply_async(args, kwargs)

  例如, delay 版::

    task.delay(arg1, arg2, kwarg1='x', kwarg2='y')

  apply_async版::

    task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})

  尽管运行十分方便，但是如果像设置额外的行参数，必须用 apply_async_

calling
---------------

.. function:: calling(__call__)

  应用一个支持调用接口（例如，add(2,2)）的对象,意味着任务不会被一个 worker 执行,但是会在当前线程中执行(但是消息不会被发送)。

任务回调
===============

task支持的函数回调

- after_return_  任务返回后调用的处理程序
- on_failure_    任务执行失败时，由职程（Worker）调用。
- on_retry_      任务重试时，由职程（Worker）调用。
- on_success_    任务成功时，由职程（Worker）调用。

after_return
---------------

.. function:: after_return(self, status, retval, task_id, args, kwargs, einfo)

  任务返回后调用的处理程序

  位置参数::

    status  – 当前任务状态
    retval  – 任务返回值/异常
    task_id – 唯一的任务ID
    args    – 返回任务的原始参数
    kwargs  – 返回任务的原始关键字

  关键字参数::

    einfo   – 异常信息实例，包含 traceback （有的情况下）

  此处理程序的返回值将被忽略。

on_failure
---------------

.. function:: on_failure(self, exc, task_id, args, kwargs, einfo)

  任务执行失败时，由职程（Worker）调用。

  位置参数::

    exc     – 任务引发的异常。
    task_id – 执行失败任务的唯一 ID。
    args    – 任务失败的原始参数。
    kwargs  – 任务失败的原始关键字。

  关键字参数::

    einfo   – 异常信息实例，包含 traceback （有的情况下）。

  此处理程序的返回值将被忽略。

on_retry
---------------

.. function:: on_retry(self, exc, task_id, args, kwargs, einfo)

  任务重试时，由职程（Worker）调用。

  位置参数::

    exc     – 发送给 retry() 函数的异常
    task_id – 任务重试唯一 ID。
    args    – 任务重试的原始参数。
    kwargs  – 任务重试的原始关键字。 Keyword Arguments:
    einfo   – 异常信息实例，包含 traceback （有的情况下）。

  此处理程序的返回值将被忽略。

on_success
---------------

.. function:: on_success(self, retval, task_id, args, kwargs)

  任务成功时，由职程（Worker）调用。

  位置参数::

    retval  – 任务的返回值
    task_id – 执行成功唯一 ID。
    args    – 任务执行成功时的原始参数。
    kwargs  – 任务执行成功时的原始关键字。

  此处理程序的返回值将被忽略。

获取回调改变/状态-on_message
==============================

Celery 可以通过消息回调获取所有状态的改变。例如对于长时任务发送人任务进程，你可以这样做::

  @app.task(bind=True)
  def hello(self, a, b):
      time.sleep(1)
      self.update_state(state="PROGRESS", meta={'progress': 50})
      time.sleep(1)
      self.update_state(state="PROGRESS", meta={'progress': 90})
      time.sleep(1)
      return 'hello world: %i' % (a+b)

  def on_raw_message(body):
      print(body)

  r = hello.apply_async(4, 6)
  print(r.get(on_message=on_raw_message, propagate=False))

将生成如下输出::

  {'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
  'result': {'progress': 50},
  'children': [],
  'status': 'PROGRESS',
  'traceback': None}
  {'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
  'result': {'progress': 90},
  'children': [],
  'status': 'PROGRESS',
  'traceback': None}
  {'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
  'result': 'hello world: 10',
  'children': [],
  'status': 'SUCCESS',
  'traceback': None}
  hello world: 10

限制时间-ETA and Countdown
==============================

.. _eta:

**ETA** (estimated time of arrival, 预计到底时间) 让你设置一个日期和时间，在这个时间之前任务将被执行。

.. _countdown:

**countdown** 是一种以秒为单位设置ETA的快捷方式::

  >>> result = add.apply_async((2, 2), countdown=3)
  >>> result.get()    # this takes at least 3 seconds to return
  20

确保任务在指定的日期和时间之后的某个时间执行，但不一定在该时间执行。
可能原因可能包括许多项目在队列中等待，或者严重的网络延迟。为了确保您的任务及时执行，你应该监视队列中的拥塞情况。
使用Munin或类似工具来接收警报，因此可以采取适当的措施来减轻负载。点击查看Munin。

尽管 countdown 是整数，但eta必须是一个 datetime 对象，并指定确切的日期和时间（包括毫秒精度和时区信息）::

  >>> from datetime import datetime, timedelta

  >>> tomorrow = datetime.utcnow() + timedelta(days=1)
  >>> add.apply_async((2, 2), eta=tomorrow)

.. _expires:

**expries** 参数定义了一个可选的到期时间，既可以作为任务之后秒发布，或在特定日期和时间使用 datetime::

  >>> # Task expires after one minute from now.
  >>> add.apply_async((10, 10), expires=60)

  >>> # Also supports datetime
  >>> from datetime import datetime, timedelta
  >>> add.apply_async((10, 10), kwargs,
  ...                 expires=datetime.now() + timedelta(days=1)

当 worker 收到过期的任务时，它将任务标记为REVOKED

创建连接池
==============================

自动池支持

从2.3版开始，支持自动连接池，因此您不必手动处理连接和发布者即可重用连接。

从2.5版开始，默认情况下启用连接池。

您可以通过创建发布者来手动处理连接::

  results = []
  with add.app.pool.acquire(block=True) as connection:
      with add.get_publisher(connection) as publisher:
          try:
              for args in numbers:
                  res = add.apply_async((2, 2), publisher=publisher)
                  results.append(res)
  print([res.get() for res in results])

尽管这是个特定示例，但是可以更好的展现一组::

  >>> from celery import group

  >>> numbers = [(2, 2), (4, 4), (8, 8), (16, 16)]
  >>> res = group(add.s(i, j) for i, j in numbers).apply_async()

  >>> res.get()
  [4, 8, 16, 32]



