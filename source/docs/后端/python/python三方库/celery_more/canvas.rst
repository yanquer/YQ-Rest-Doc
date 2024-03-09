===================
canvas
===================

celery 的 canvas 应当值得是一种设计流程, 目前不是很理解.

签名
====================

有时候可能希望将任务调用的签名传递给另外一个进程或其他函数的参数，Celery 提供了签名。
**签名通过一种方式进行封装任务调用的参数以及执行选项，便于传递给他的函数，甚至通过序列化通过网络传送。**
可以将 add 使用的参数作为任务创建的签名，倒计时为 10 秒，如下所示（2,2）::

  >>> add.signature((2, 2), countdown=10)
  tasks.add(2, 2)

也可以通过一个快捷的方式进行操作::

  >>> add.s(2, 2)
  tasks.add(2, 2)

签名实例支持调用API：这就意味着可以使用 delay 和 apply_async 方法。
但区别就在于签名实例已经指定了参数签名，该 add 任务有两个参数，需要指定两个参数的签名才能够成一个完整的签名实例::

  >>> s1 = add.s(2, 2)
  >>> res = s1.delay()
  >>> res.get()
  4

也可以创建不完整的签名来进行创建::

  # incomplete partial: add(?, 2)
  >>> s2 = add.s(2)

也可以设置新的参值，新设置的参数会覆盖原有的参数值::

  >>> s3 = add.s(2, 2, debug=True)
  >>> s3.delay(debug=False)   # debug is now False.

不变签名
--------------------

不变性(Immutability)

部分参数通常在回调中使用，父任务的结果将会作为参数传递给链接或chord的回调任务。

有时你希望指明一个不需要参数的回调，这时你可以设置签名为不变的::

  >>> add.apply_async((2, 2), link=reset_buffers.signature(immutable=True))

快捷方式 .si() 也能创建不变签名::

  >>> add.apply_async((2, 2), link=reset_buffers.si())

对于不变签名，只有执行选项可以进行设置，并无法使用部分参数和关键词参数。

回调
--------------------

任务可以使用 apply_async 的 link 参数来添加回调::

  add.apply_async((2, 2), link=other_task.s())

只有当任务成功退出，回调函数才能被执行，并且将父任务的结果作为参数传递给回调的任务。
如前所述，新传递的参数将会添加在签名指定的参数前。
如果你有一个签名::

  >>> sig = add.s(10)

接着 sig.delay(result) 将变为::

  >>> add.apply_async(args=(result, 10))

现在，让我们调用 add 任务，并设置回调::

  >>> add.apply_async((2, 2), link=add.s(8))

正如预期，首先第一个任务将会计算 2 + 2，接着回调任务将会计算 4 + 8。


组
====================

组：Groups

一个 group 并行调用任务列表，返回一个特殊的结果实例，可以将结果作为一个列表进行查看，并且通过索引进去获取返回值::

  >>> from celery import group, add
  >>> group(add.s(i, i) for i in xrange(10))().get()
  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

Partial group::

  >>> g = group(add.s(i) for i in xrange(10))
  >>> g(10).get()
  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

链
====================

链：Chains

可以将任务链接在一起，在一个人返回后进行调用另外一个任务::

  >>> from celery import chain
  >>> from proj.tasks import add, mul

  # (4 + 4) * 8
  >>> chain(add.s(4, 4) | mul.s(8))().get()
  64

或 partial chain::

  >>> # (? + 4) * 8
  >>> g = chain(add.s(4) | mul.s(8))
  >>> g(4).get()
  64

链也可以这样写::

  >>> (add.s(4, 4) | mul.s(8))().get()
  64

和弦
====================

和弦：Chords
和弦是一个带有回调的组::

  >>> from celery import chord
  >>> from proj.tasks import add, xsum

  >>> chord((add.s(i, i) for i in xrange(10)), xsum.s())().get()
  90

链接到其他任务的组将自动转换为和弦::

  >>> (group(add.s(i, i) for i in xrange(10)) | xsum.s())().get()
  90

这些原语都是签名的类型，可以根据需要进行组合，例如::

  >>> upload_document.s(file) | group(apply_filter.s() for filter in filters)



