====================
concurrent
====================


.. post:: 2024-02-21 21:55:17
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: `<https://docs.python.org/zh-cn/3/library/concurrent.html>`_

目前就一个包:

- ``concurrent.futures`` —— 启动并行任务

concurrent.futures
====================

模块提供异步执行可调用对象高层接口。

异步执行可以由 ThreadPoolExecutor_ 使用线程或由 ProcessPoolExecutor_ 使用单独的进程来实现。
两者都是实现抽像类 Executor 定义的接口。

.. _concurrent-Executor-funs:

Executor
====================

class concurrent.futures.Executor
  抽象类提供异步执行调用方法。要通过它的子类调用，而不是直接调用。

  .. function:: submit(fn, /, *args, **kwargs)

    调度可调用对象 fn，以 ``fn(*args, **kwargs)`` 方式执行并返回一个代表该可调用对象的执行的 Future 对象::

      with ThreadPoolExecutor(max_workers=1) as executor:
          future = executor.submit(pow, 323, 1235)
          print(future.result())

  .. function:: map(func, *iterables, timeout=None, chunksize=1)

    类似于 ``map(func, *iterables)`` 函数，除了以下两点:

    - iterables 是立即执行而不是延迟执行的；
    - func 是异步执行的，对 func 的多个调用可以并发执行。

    timeout: Union[int, float, None]
      当超时时, 将会触发 超时 异常(raises TimeoutError)

    如果 func 调用引发一个异常，当从迭代器中取回它的值时这个异常将被引发。

    使用 ProcessPoolExecutor 时，这个方法会将 iterables 分割任务块并作为独立的任务并提交到执行池中。
    这些块的大概数量可以由 chunksize 指定正整数设置。
    对很长的迭代器来说，使用大的 chunksize 值比默认值 1 能显著地提高性能。 chunksize 对 ThreadPoolExecutor 没有效果。

    返回的是执行结果的生成器迭代, 保持于 iterables 的顺序一致::

      from concurrent.futures import ThreadPoolExecutor

      with ThreadPoolExecutor(max_workers=3) as t:
          d = t.map(lambda x: x**2, [1, 2, 3, 8])
          print(type(d))
          for x in d:
              print(x, type(x))

    输出::

      <class 'generator'>
      1 <class 'int'>
      4 <class 'int'>
      9 <class 'int'>
      64 <class 'int'>

    在 3.5 版更改: 加入 chunksize 参数。

  .. function:: shutdown(wait=True, *, cancel_futures=False)

    当待执行的 future 对象完成执行后向执行者发送信号，它就会释放正在使用的任何资源。
    在关闭后调用 Executor.submit() 和 Executor.map() 将会引发 RuntimeError。

    wait: bool = True
      wait 为 True, 则此方法只有在所有待执行的 future 对象完成执行且释放已分配的资源后才会返回。

      wait 为 False，方法立即返回，所有待执行的 future 对象完成执行后会释放已分配的资源。

      不管 wait 的值是什么，整个 Python 程序将等到所有待执行的 future 对象完成执行后才退出。
    cancel_futures: bool=False
      cancel_futures 为 True，此方法将取消所有执行器还未开始运行的挂起的 Future。
      任何已完成或正在运行的 Future 将不会被取消，无论 cancel_futures 的值是什么？

    如果 cancel_futures 和 wait 均为 True，则执行器已开始运行的所有 Future 将在此方法返回之前完成。 其余的 Future 会被取消。

    如果使用 with 语句，你就可以避免显式调用这个方法，
    它将会停止 Executor (就好像 Executor.shutdown() 调用时 wait 设为 True 一样等待)::

      import shutil
      with ThreadPoolExecutor(max_workers=4) as e:
          e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
          e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
          e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
          e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

    在 3.9 版更改: 增加了 cancel_futures。

ThreadPoolExecutor
====================

concurrent.futures.ThreadPoolExecutor

ThreadPoolExecutor 是 Executor_ 的子类，它使用线程池来异步执行调用。

当可调用对象已关联了一个 Future 然后在等待另一个 Future 的结果时就会导致死锁情况。例如::

  import time
  def wait_on_b():
      time.sleep(5)
      print(b.result())  # b will never complete because it is waiting on a.
      return 5

  def wait_on_a():
      time.sleep(5)
      print(a.result())  # a will never complete because it is waiting on b.
      return 6

  executor = ThreadPoolExecutor(max_workers=2)
  a = executor.submit(wait_on_b)
  b = executor.submit(wait_on_a)

与::

  def wait_on_future():
      f = executor.submit(pow, 5, 2)
      # This will never complete because there is only one worker thread and
      # it is executing this function.
      print(f.result())

  executor = ThreadPoolExecutor(max_workers=1)
  executor.submit(wait_on_future)

ProcessPoolExecutor
====================

ProcessPoolExecutor 类是 Executor_ 的子类，它使用进程池来异步地执行调用。
ProcessPoolExecutor 会使用 :doc:`/docs/后端/python/python标准库/multiprocessing` 模块，
这允许它绕过 全局解释器锁 但也意味着只可以处理和返回可封存的对象。

``__main__`` 模块必须可以被工作者子进程导入。这意味着 ProcessPoolExecutor 不可以工作在交互式解释器中。

从可调用对象中调用 Executor_ 或 Future_ 的方法提交给 ProcessPoolExecutor 会导致死锁。

class concurrent.futures.ProcessPoolExecutor(max_workers=None, mp_context=None, initializer=None, initargs=(), max_tasks_per_child=None)
  异步地执行调用的 Executor_ 子类使用最多具有 max_workers 个进程的进程池。

  max_workers:
    如果 max_workers 为 None 或未给出，它将默认为机器的处理器个数。
    如果 max_workers 小于等于 0，则将引发 ValueError。

    在 Windows 上，max_workers 必须小于等于 61，否则将引发 ValueError。
    如果 max_workers 为 None，则所选择的默认值最多为 61，即使存在更多的处理器。
  mp_context:
    可以是一个多进程上下文或是 None。 它将被用来启动工作进程。

    如果 mp_context 为 None 或未给出，则将使用默认的多进程上下文。
  initializer:
    一个可选的可调用对象，它会在每个工作进程启动时被调用；
  initargs:
    传给 initializer 的参数元组。
    如果 initializer 引发了异常，则所有当前在等待的任务以及任何向进程池提交更多任务的尝试都将引发 BrokenProcessPool。
  max_tasks_per_child: = None
    可选参数, 表示单个进程可执行的最大任务数. 超出将会使用新的进程(刷新).

    默认 None 表示工作进程将会一直存活到进程池终止.

    在默认情况,缺少MP_CONTEXT参数, 且指定了最大值时，将使用 spawn() 多进程启动方法.

    与 fork() 启动方式不兼容.

  在 3.3 版更改:
  如果其中一个工作进程被突然终止，BrokenProcessPool 就会马上触发。
  可预计的行为没有定义，但执行器上的操作或它的 future 对象会被冻结或死锁。

  在 3.7 版更改: 添加 mp_context 参数允许用户控制由进程池创建给工作者进程的开始方法 。

  加入 initializer 和*initargs* 参数。

  在 3.11 版更改: The max_tasks_per_child argument was added to allow users
  to control the lifetime of workers in the pool.

.. _concurrent-Future:

Future
====================

Future 类将可调用对象封装为异步执行。Future 实例由 ``Executor.submit()`` 创建。

class concurrent.futures.Future
  将可调用对象封装为异步执行。Future 实例由 Executor.submit() 创建，除非测试，不应直接创建。

  .. function:: cancel()

    尝试取消调用。 如果调用正在执行或已结束运行不能被取消则该方法将返回 False，否则调用会被取消并且该方法将返回 True。

  .. function:: cancelled()

    如果调用成功取消返回 True。

  .. function:: running()

    如果调用正在执行而且不能被取消那么返回 True 。

  .. function:: done()

    如果调用已被取消或正常结束那么返回 True。

  .. function:: result(timeout=None)

    Return the value returned by the call.
    If the call hasn't yet completed then this method will wait up to timeout seconds.
    If the call hasn't completed in timeout seconds, then a TimeoutError will be raised.
    timeout can be an int or float.
    If timeout is not specified or None, there is no limit to the wait time.

    如果 futrue 在完成前被取消则 CancelledError 将被触发。

    如果调用引发了一个异常，这个方法也会引发同样的异常。

  .. function:: exception(timeout=None)

    Return the exception raised by the call.
    If the call hasn't yet completed then this method will wait up to timeout seconds.
    If the call hasn't completed in timeout seconds, then a TimeoutError will be raised.
    timeout can be an int or float.
    If timeout is not specified or None, there is no limit to the wait time.

    如果 futrue 在完成前被取消则 CancelledError 将被触发。

    如果调用正常完成那么返回 None。

  .. function:: add_done_callback(fn)

    附加可调用 fn 到 future 对象。
    当 future 对象被取消或完成运行时，将会调用 fn，而这个 future 对象将作为它唯一的参数。

    加入的可调用对象总被属于添加它们的进程中的线程按加入的顺序调用。
    如果可调用对象引发一个 Exception 子类，它会被记录下来并被忽略掉。
    如果可调用对象引发一个 BaseException 子类，这个行为没有定义。

    如果 future 对象已经完成或已取消，fn 会被立即调用。

  **下面这些 Future 方法用于单元测试和 Executor 实现.**

  .. function:: set_running_or_notify_cancel()

    这个方法只可以在执行关联 Future 工作之前由 Executor 实现调用或由单测试调用。

    线程将会等待 Future实例 执行完成. 类似执行 as_completed() or wait()

    Return:
      False:
        Future实例被退出. 类似 Future.cancel() == True
      True:
        Future实例不可退出, 处于 running 状态. Future.running() == True.

    这个方法只可以被调用一次并且不能在调用 Future.set_result() 或 Future.set_exception() 之后再调用。

  .. function:: set_result(result)

    设置将 Future 关联工作的结果给 result 。

    这个方法只可以由 Executor 实现和单元测试使用。

    在 3.8 版更改: 如果 Future 已经完成则此方法会引发 concurrent.futures.InvalidStateError。

  .. function:: set_exception(exception)

    设置 Future 关联工作的结果给 Exception exception 。

    这个方法只可以由 Executor 实现和单元测试使用。

    在 3.8 版更改: 如果 Future 已经完成则此方法会引发 concurrent.futures.InvalidStateError。


模块函数
====================

- wait
- as_completed

.. function:: concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED)

  等待由 fs 指定的 Future 实例（可能由不同的 Executor 实例创建）完成。
  重复传给 fs 的 future 会被移除并将只返回一次。

  返回一个由集合组成的具名 2 元组。

  - 第一个集合的名称为 done，包含在等待完成之前已完成的 future（包括正常结束或被取消的 future）。
  - 第二个集合的名称为 not_done，包含未完成的 future（包括挂起的或正在运行的 future）。

  timeout: Union[int, float, None]
    timeout 可以用来控制返回前最大的等待秒数。

    如果 timeout 未指定或为 None ，则不限制等待时间。
  return_when:
    指定此函数应在何时返回。它必须为以下常数之一:

    .. csv-table::
      :header: 常量, 描述

      FIRST_COMPLETED,    函数将在任意可等待对象结束或取消时返回。
      FIRST_EXCEPTION,    函数将在任意可等待对象因引发异常而结束时返回。当没有引发任何异常时它就相当于 ALL_COMPLETED。
      ALL_COMPLETED,      函数将在所有可等待对象结束或取消时返回。

.. function:: concurrent.futures.as_completed(fs, timeout=None)

  返回多个已执行完成的 Future_ 对象的迭代器(状态: 执行完成或退出)

  调用之前就完成的回最先返回.

  fs:
    多个 Future_ 对象的列表
  timeout: Union[int, float, None]
    .

Exception 类
====================

- CancelledError
- TimeoutError
- BrokenExecutor
- InvalidStateError
- BrokenThreadPool
- BrokenProcessPool


.. function:: exception concurrent.futures.CancelledError

  future 对象被取消时会触发。

.. function:: exception concurrent.futures.TimeoutError

  A deprecated alias of TimeoutError, raised when a future operation exceeds the given timeout.

  在 3.11 版更改: This class was made an alias of TimeoutError.

.. function:: exception concurrent.futures.BrokenExecutor

  当执行器被某些原因中断而且不能用来提交或执行新任务时就会被引发派生于 RuntimeError 的异常类。

  3.7 新版功能.

.. function:: exception concurrent.futures.InvalidStateError

  当某个操作在一个当前状态所不允许的 future 上执行时将被引发。

  3.8 新版功能.

.. function:: exception concurrent.futures.thread.BrokenThreadPool

  当 ThreadPoolExecutor 中的其中一个工作者初始化失败时会引发派生于 BrokenExecutor 的异常类。

  3.7 新版功能.

.. function:: exception concurrent.futures.process.BrokenProcessPool

  当 ThreadPoolExecutor 中的其中一个工作者不完整终止时(比如，被外部杀死)
  会引发派生于 BrokenExecutor ( 原名 RuntimeError ) 的异常类。

  3.3 新版功能.






