===============================
threading模块
===============================

:官网文档::
  `threading <https://docs.python.org/zh-cn/3/library/threading.html#threading.Thread>`_

.. threading.Thread的 run, start, join方法

threading.Thread的常见方法

run()
  线程的主要执行体, 用于子类重写, 直接调用不会触发多线程
start()
  启动新线程的方式, 开启一个新线程去执行run方法(实现多线程),
  每个定义的线程只能start一次, 如果调用多次，则会报RuntimeError错误
join(timeout=None)
  阻塞当前线程, 等待子进程执行结束
setDaemon(True)
  将线程设置为守护线程, 如果主线程退出, 那么子线程也退出(若需要等待则使用join)
is_alive()
  线程是否存活，返回True或者False。
  在线程的run()运行之后直到run()结束，该方法返回True。
threading.Condition(lock=None)
  一个条件变量对象允许一个或多个线程等待，直到被另一个线程通知。
  lock参数必须是一个Lock对象或者RLock对象，
  并且会作为底层锁使用，默认使用RLock。
acquire(\*args)
  请求底层锁。此方法调用底层锁对应的方法和返回对应方法的返回值。
release()
  释放底层锁。此方法调用底层所对应的方法，没有返回值。
wait(timeout=None)
  释放锁，等待直到被通知（再获取锁）或者发生超时事件。
  如果线程在调用此方法时本身并没有锁（即线程首先得有锁），
  则会报RuntimeError错误。这个方法释放底层锁，然后阻塞线程，
  直到另一个线程中的同一个条件变量使用notify()或notify_all()唤醒，
  或者超时事件发生，一旦被唤醒或者超时，
  则会重新去获取锁并返回（成功返回True，否则返回False）。
  timeout参数为浮点类型的秒数。
  在RLock中使用一次release方法，可能并不能释放锁，
  因为锁可能被acquire()了多次，但是在条件变量对象中，
  它调用了RLock类的内部方法，可以一次就完全释放锁，
  重新获取锁时也会重置锁的递归等级。
wait_for(predicate, timeout=None)
  与wait方法相似，等待，直到条件计算为True，
  返回最后一次的predicate的返回值。
  predicate参数为一个返回值为布尔值的可调用对象。
  调用此方法的时候会先调用predicate对象，
  如果返回的就是True，则不会释放锁，直接往后执行。
  另一个线程通知后，在它释放锁时，
  才会触发wait_for方法等待事件，
  这时如果predicate结果为True，则尝试获取锁，
  获取成功后则继续往后执行，
  如果为False，则会一直阻塞下去。此方法如果忽略timeout参数，
  就相当于：while not predicate(): condition_lock.wait()。
notify(n=1)
  唤醒一个等待这个条件的线程，
  如果调用这个方法的线程在没有获得锁的情况下调用这个方法，
  会报RuntimeError错误。
  默认唤醒一个线程，可以通过参数n设置唤醒n个正在等待这个条件变量的线程，
  如果没有线程在等待，调用这个方法不会发生任何事。
  如果等待的线程中正好有n个线程，那么这个方法可以准确的唤醒这n个线程，
  但是等待的线程超过指定的n个，有时候可能会唤醒超过n个的线程，
  所以依赖参数n是不安全的行为。
notify_all()
  唤醒所有等待这个条件的线程。
  这个方法与notify()不同之处在于它唤醒所有线程，而不是特定n个。

.. todo: 看有些地方写的是 False 则 主线程会等待子线程退出后再退出

默认为False(换而言之, 默认, 主线程,子线程互不影响)

同时个人建议设置为True, 可以保证对子线程的控制权, 否则可能会出现, 主线程结束后, 子线程成为孤儿进程, 被托管给系统的init进程, 直到完成后被回收

其他变量:

name
  线程的名称字符串，并没有什么实际含义，多个线程可以赋予相同的名称，
  初始值由初始化方法来设置。
ident
  线程的标识符，如果线程还没有启动，
  则为None。ident是一个非零整数，
  参见threading.get_ident()函数。
  当线程结束后，它的ident可能被其他新创建的线程复用，
  当然就算该线程结束了，它的ident依旧是可用的。
daemon
  表示该线程是否是守护线程，True或者False。设置一个线程的daemon必须在线程的start()方法之前，否则会报RuntimeError错误。这个值默认继承自创建它的线程，主线程默认是非守护线程的，所以在主线程中创建的线程默认都是非守护线程的，即daemon=False。


Lock()
===============================

互斥锁

获取一个互斥锁, 用于多线程时互斥访问.

不过会降低效率(类似写成了单任务)

Semaphore()
===============================

信号量Semaphore

与 Lock()_ 的区别是, Semaphore 支持同时对多个使用.

Semaphore 内部维护了一个计数器.

获取锁的时候, 计数器减一, 释放锁的时候加一

一些坑
===============================

__new__方法是支持多线程的，
所以对于使用__new__实现的单例对象, 不存在多线程的线程安全问题,
更详细的说明, 知识在 __new__内部的操作没有线程安全问题, 可以保证多线程环境下返回的都是同一个对象, 但是其他方法, 存在同时访问的对象, 该加锁还是要加锁

.. code-block::

  class Single(object):

    """
        single instance, attention son class's __init__ will exec once
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, )
        return cls.__instance


  if __name__ == '__main__':

    class P(Single):
        p = 0
        # _instance = None

        # @classmethod
        # def instance(cls,):
        #     if cls._instance is None:
        #         cls._instance = cls()
        #     return cls._instance

        def __init__(self):
            time.sleep(random.randint(0, 5))

        def set_p(self):
            self.p += 1
            print(f'p={self.p}', )

    def set_p():
        time.sleep(random.randint(0, 5))
        pp = P()
        print(pp)
        pp.set_p()

    t_list = []
    for _ in range(20):
        t_list.append(threading.Thread(target=set_p))
    for t in t_list:
        t.start()


输出(某些顺序 kennel不一样)::

  <__main__.P object at 0x1107de4c0>
  p=1
  <__main__.P object at 0x1107de4c0><__main__.P object at 0x1107de4c0>

  p=2
  p=3
  <__main__.P object at 0x1107de4c0>
  <__main__.P object at 0x1107de4c0>
  p=4
  p=5
  <__main__.P object at 0x1107de4c0>
  p=6
  <__main__.P object at 0x1107de4c0>
  p=7
  <__main__.P object at 0x1107de4c0><__main__.P object at 0x1107de4c0>
  p=8
  <__main__.P object at 0x1107de4c0>
  p=9

  p=10
  <__main__.P object at 0x1107de4c0><__main__.P object at 0x1107de4c0>
  <__main__.P object at 0x1107de4c0>
  p=11<__main__.P object at 0x1107de4c0>
  p=12
  <__main__.P object at 0x1107de4c0>
  p=13

  p=14

  p=15
  <__main__.P object at 0x1107de4c0>
  p=16
  <__main__.P object at 0x1107de4c0><__main__.P object at 0x1107de4c0>
  p=17

  p=18
  <__main__.P object at 0x1107de4c0>
  p=19
  <__main__.P object at 0x1107de4c0>
  p=20


