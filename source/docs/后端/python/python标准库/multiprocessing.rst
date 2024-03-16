======================
multiprocessing
======================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


:官网文档::
  `multiprocessing <https://docs.python.org/zh-cn/3/library/multiprocessing.html?#module-multiprocessing>`_

Python中多进程是相互执行互不干扰的，但是如果多进程之间需要对同一资源对象进行操作或者多个进程之间有相互依赖的，
那就需要一个共享变量供多进程使用。

Python multiprocessing 多进程之间相互协调的方式有如下几种:

- Lock: 锁
- Queue: 队列
- Semaphore: 信号量
- Event: 事件
- Pipe: 管道


Process
======================

.. function::  Process(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

  开启一个新的进程, 仅介绍常用的几个

  target=None
    子进程执行的代码, 一般是一个函数
  args: tuple = ()
    target传递的函数, 需要用的参数列表
  kwargs: dict = {}
    target传递的函数, 需要用的关键字参数字典
  daemon=None
    bool, 是否设置为守护线程. 详细见: daemon_

支持三种启动进程的方法

- spawn

  父进程启动一个新的Python解释器进程。
  子进程将只继承运行Process对象的run()方法所需的资源。
  不会继承来自父进程的不必要的文件描述符和句柄。与使用fork或forkserver相比，使用此方法启动进程相当慢。

  可在 Unix 和 Windows 上使用。 Windows 和 macOS 上的默认设置。

- fork

  父进程使用 os.fork() 来产生 Python 解释器分叉。子进程在开始时实际上与父进程相同。父进程的所有资源都由子进程继承。请注意，安全分叉多线程进程是棘手的。

  只存在于 Unix。 Unix 中的默认值。

- forkserver

  程序启动并选择 forkserver 启动方法时，将启动服务器进程。 从那时起，每当需要一个新进程时，父进程就会连接到服务器并请求它分叉一个新进程。 分叉服务器进程是单线程的，因此使用 os.fork() 是安全的。 没有不必要的资源被继承。

  可在Unix平台上使用，支持通过Unix管道传递文件描述符。

如要更改, 在执行之前使用::

  import multiprocessing as mp

  mp.set_start_method('spawn')

进程之间交换对象
======================

multiprocessing 支持进程之间的两种通信通道：

- 队列_
- 管道_

队列
----------------------

Queue 类是一个近似 queue.Queue 的克隆。 例如::

  from multiprocessing import Process, Queue

  def f(q):
      q.put([42, None, 'hello'])

  if __name__ == '__main__':
      q = Queue()
      p = Process(target=f, args=(q,))
      p.start()
      print(q.get())    # prints "[42, None, 'hello']"
      p.join()

队列是线程和进程安全的。

管道
----------------------

Pipe() 函数返回一个由管道连接的连接对象，默认情况下是双工（双向）。例如::

  from multiprocessing import Process, Pipe

  def f(conn):
      conn.send([42, None, 'hello'])
      conn.close()

  if __name__ == '__main__':
      parent_conn, child_conn = Pipe()
      p = Process(target=f, args=(child_conn,))
      p.start()
      print(parent_conn.recv())   # prints "[42, None, 'hello']"
      p.join()

返回的两个连接对象 Pipe() 表示管道的两端。每个连接对象都有 send() 和 recv() 方法（相互之间的）。请注意，如果两个进程（或线程）同时尝试读取或写入管道的 同一 端，则管道中的数据可能会损坏。当然，在不同进程中同时使用管道的不同端的情况下不存在损坏的风险。

进程间同步
======================

multiprocessing 包含来自 threading 的所有同步原语的等价物。例如，可以使用锁来确保一次只有一个进程打印到标准输出::

  from multiprocessing import Process, Lock

  def f(l, i):
      l.acquire()
      try:
          print('hello world', i)
      finally:
          l.release()

  if __name__ == '__main__':
      lock = Lock()

      for num in range(10):
          Process(target=f, args=(lock, num)).start()

不使用锁的情况下，来自于多进程的输出很容易产生混淆。

进程间共享状态
======================

如上所述，在进行并发编程时，通常最好尽量避免使用共享状态。使用多个进程时尤其如此。

但是，如果你真的需要使用一些共享数据，那么 multiprocessing 提供了两种方法。

共享内存
----------------------

可以使用 Value 或 Array 将数据存储在共享内存映射中。例如，以下代码::

  from multiprocessing import Process, Value, Array

  def f(n, a):
      n.value = 3.1415927
      for i in range(len(a)):
          a[i] = -a[i]

  if __name__ == '__main__':
      num = Value('d', 0.0)
      arr = Array('i', range(10))

      p = Process(target=f, args=(num, arr))
      p.start()
      p.join()

      print(num.value)
      print(arr[:])

将打印::

  3.1415927
  [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

创建 num 和 arr 时使用的 'd' 和 'i' 参数是 array 模块使用的类型的 typecode ： 'd' 表示双精度浮点数， 'i' 表示有符号整数。这些共享对象将是进程和线程安全的。

为了更灵活地使用共享内存，可以使用 multiprocessing.sharedctypes 模块，该模块支持创建从共享内存分配的任意ctypes对象。

服务进程
----------------------

由 Manager() 返回的管理器对象控制一个服务进程，该进程保存Python对象并允许其他进程使用代理操作它们。

Manager() 返回的管理器支持类型:

- list
- dict
- Namespace
- Lock
- RLock
- Semaphore
- BoundedSemaphore
- Condition
- Event
- Barrier
- Queue
- Value
- Array

例如::

  from multiprocessing import Process, Manager

  def f(d, l):
      d[1] = '1'
      d['2'] = 2
      d[0.25] = None
      l.reverse()

  if __name__ == '__main__':
      with Manager() as manager:
          d = manager.dict()
          l = manager.list(range(10))

          p = Process(target=f, args=(d, l))
          p.start()
          p.join()

          print(d)
          print(l)

将打印::

  {0.25: None, 1: '1', '2': 2}
  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

使用服务进程的管理器比使用共享内存对象更灵活，因为它们可以支持任意对象类型。
此外，单个管理器可以通过网络由不同计算机上的进程共享。但是，它们比使用共享内存慢。

使用工作进程
======================



Process对象的一些属性/方法
============================

.. topic:: start()

  启动进程活动。

  这个方法每个进程对象最多只能调用一次。它会将对象的 run() 方法安排在一个单独的进程中调用。

.. topic:: join([timeout])

  如果可选参数 timeout 是 None （默认值），则该方法将阻塞，直到调用 join() 方法的进程终止。如果 timeout 是一个正数，它最多会阻塞 timeout 秒。请注意，如果进程终止或方法超时，则该方法返回 None 。检查进程的 exitcode 以确定它是否终止。

  一个进程可以被 join 多次。

  进程无法join自身，因为这会导致死锁。尝试在启动进程之前join进程是错误的。

.. topic:: name

  进程的名称。该名称是一个字符串，仅用于识别目的。它没有语义。可以为多个进程指定相同的名称。

  初始名称由构造器设定。 如果没有为构造器提供显式名称，则会构造一个形式为 'Process-N1:N2:...:Nk' 的名称，其中每个 Nk 是其父亲的第 N 个孩子。

.. topic:: is_alive()

  返回进程是否还活着。

  粗略地说，从 start() 方法返回到子进程终止之前，进程对象仍处于活动状态。

.. topic:: daemon
  :name: daemon

  进程的守护标志，一个布尔值。这必须在 start() 被调用之前设置。

  初始值继承自创建进程。

  当进程退出时，它会尝试终止其所有守护进程子进程。

  请注意，不允许在守护进程中创建子进程。这是因为当守护进程由于父进程退出而中断时，其子进程会变成孤儿进程。
  另外，这些 不是 Unix 守护进程或服务，它们是正常进程，如果非守护进程已经退出，它们将被终止（并且不被合并）。

.. topic:: pid

  返回进程ID。在生成该进程之前，这将是 None 。

.. topic:: exitcode

  子进程的退出代码。如果该进程尚未终止则为 None 。

  如果子进程的 run() 方法正常返回，退出代码将是 0 。 如果它通过 sys.exit() 终止，并有一个整数参数 N ，退出代码将是 N 。

  如果子进程由于在 run() 内的未捕获异常而终止，退出代码将是 1 。 如果它是由信号 N 终止的，退出代码将是负值 -N 。

.. topic:: sentinel

  系统对象的数字句柄，当进程结束时将变为 "ready" 。

  如果要使用 multiprocessing.connection.wait() 一次等待多个事件，可以使用此值。否则调用 join() 更简单。

  在Windows上，这是一个操作系统句柄，可以与 WaitForSingleObject 和 WaitForMultipleObjects 系列API调用一起使用。在Unix上，这是一个文件描述符，可以使用来自 select 模块的原语。

  3.3 新版功能.

.. topic:: terminate()

  终止进程。 在Unix上，这是使用 SIGTERM 信号完成的；在Windows上使用 TerminateProcess() 。 请注意，不会执行退出处理程序和finally子句等。

  请注意，进程的后代进程将不会被终止 —— 它们将简单地变成孤立的。

  .. warning::

    如果在关联进程使用管道或队列时使用此方法，则管道或队列可能会损坏，并可能无法被其他进程使用。
    类似地，如果进程已获得锁或信号量等，则终止它可能导致其他进程死锁。

.. topic:: kill()

  与 terminate() 相同，但在Unix上使用 SIGKILL 信号。

.. topic:: close()

  关闭 Process 对象，释放与之关联的所有资源。如果底层进程仍在运行，则会引发 ValueError 。一旦 close() 成功返回， Process 对象的大多数其他方法和属性将引发 ValueError 。

.. note::

  注意 start() 、 join() 、 is_alive() 、 terminate() 和 exitcode 方法只能由创建进程对象的进程调用。



