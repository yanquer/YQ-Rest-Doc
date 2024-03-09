=========================
signal
=========================

:官网文档::
  `signal <https://docs.python.org/zh-cn/3/library/signal.html>`_

:部分参考::
  `python进程间通信--信号Signal <https://www.cnblogs.com/thomson-fred/p/9502497.html>`_

python的信号处理模块

信号是 Unix 系统中常见的一种进程间通信方式（IPC）, 也叫软中断信号

作用是通知进程发生了异步事件。进程之间可以调用系统来传递信号, 本身内核也可以发送信号给进程, 告诉该进程发生了某个事件.

.. note::

  注意，信号只是用来通知某进程发生了什么事件，并不给该进程传递任何数据。

  **Python 信号处理程序总是会在主 Python 主解释器的主线程中执行，即使信号是在另一个线程中接收的。 这意味着信号不能被用作线程间通信的手段。 你可以改用 threading 模块中的同步原语。**

  此外，只有主解释器的主线程才被允许设置新的信号处理程序。

接收信号的进程对不同的信号有三种处理方法:

- 指定处理函数
- 忽略
- 根据系统默认值处理, 大部分信号的默认处理是终止进程


linux相关信号可见: :doc:`/docs/操作系统/linux/概念性/linux系统信号`

signal函数
=========================

.. function:: signal.signal(signalnum, handler)

  信号中最关键的一个方法, 用于声明一个信号。
  当进程运行过程中出现故障异常或者需要进程间通信时, 由操作系统内核中的进程或者应用中的进程发出处理信号, 通知注册了信号的进程进行处理。

  sig: int
    要处理的信号名称
  handler:
    信号处理方法,

    可选值:

    SIG_DFL    表示默认方法处理

    SIG_IGN    表示忽略这个信号(一般为了避免父进程和子进程的互相干扰而使用)

    handler    自定义回调函数handler_

.. topic:: 自定义handler
  :name: 自定义回调函数handler

  用于在进程捕捉到其他进程发送的信号时调用的函数. 当此函数返回时, 进程继续按原来的逻辑顺序执行。

  此函数在定义时python普通函数的定义没有区别。
  函数名不一定是handler, 但作为作为参数传入signal()方法的参数名一定是与定义handler函数的函数相同::

    def  handler(signum,frame):

        do  something…

    sig:
      接收到的信号编号, signal模块内部定义了一些常用的内核信号, 并为它们进行了编号。

      注意: windows操作系统没有SIGUSR1和SIGUSR2这两个型号类型, linux操作系统才有
    frame:
      信号结构对象(可以通过结构对象查看信号信息,基本不用)

      signal函数实际上是一个异步的回调函数, 只要执行了该函数, 则进程任意时候接收到相应信号都会处理。

      这里的异步就是上文提到的异步机制, 是计算机内核程序与本进程间同时运行, 互相不干扰的一种机制, 对于进程的正常执行有着关键的作用。
      这种异步机制在任何后端编程语言中都是存在的, 只不过实现的方式和细节不一样而已。

alarm
=========================

.. function:: signal.alarm(sec)

  非阻塞函数

  设置时钟信号,在一定时间后给自身发送一个 SIGALRM 信号

  原理: 时钟的创建是进程交由操作系统内核(kernal)帮助创建的

  时钟和进程之间是异步执行的, 当时钟到时,内核会发送信号给进程, 进程接收信号进行相应的响应操作。

  注意: 如果设置多个时钟, 后面的时钟会覆盖前面的时钟,一个进程只有一个挂起的时钟。

pause
=========================

.. function:: signal.pause()

  阻塞进程,等待一个信号.当接收到信号时就会停止阻塞

  例如: 等待signal()函数的发送

getsignal
=========================

.. function:: signal.getsignal(signalnum)

  获取某个 signalnum 对应的 handler


信号举例
=========================

windows操作系统下, SIGNALINT编号为2::

  >>>signal.SIGINT
  <Signals.SIGINT: 2>

SIGBREAK编号为21::

  >>>signal.SIGBREAK
  <Signals.SIGBREAK: 21>

常用信号类型解析::

  SIGHUP   断开连接
  SIGINT    ctrl-C
  SIGUIT    ctrl-\
  SIGTSTP   ctrl-z
  SIGKILL    终止进程且不能被处理
  SIGSTOP   暂停进程且不能被处理
  SIGALRM   时钟进程
  SIGCHLD   子进程状态改变发送给父进程信息号(但一般父进程不会处理)

linux系统信号可参考: :doc:`/docs/操作系统/linux/概念性/linux系统信号`

.. tip::

  在系统中, SIGKILL 和 SIGSTOP 两种信号, 进程是无法捕获的.

  所以对于需要人为杀死的进程, 可使用SIGTERM信号，SIGTERM表示终止信号，是kill命令传送的系统默认信号，
  它与SIGKIIL的区别是，SIGTERM更为友好，进程可以捕捉SIGTERM信号，进而根据需要来做一些清理工作.

  手动触发就是::

    kill -15 pid

.. warning::

  多线程环境下使用信号，只有 main thread 可以设置 signal 的 handler
