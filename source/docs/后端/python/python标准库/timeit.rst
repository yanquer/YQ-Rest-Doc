====================
timeit
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: `timeit --- 测量小代码片段的执行时间 <https://docs.python.org/zh-cn/3/library/timeit.html?highlight=timeit#module-timeit>`_

此模块提供了一种简单的方法来计算一小段 Python 代码的耗时。
它有 命令行接口 以及一个 可调用 方法。
它避免了许多测量时间的常见陷阱。
另见 Tim Peter 在 O'Reilly 出版的 Python Cookbook 第二版中“算法”章节的概述。


看语句的执行时间

如::

  print(timeit.timeit('set([x for x in [1, 3, 5]])'))
  print(timeit.timeit('set(x for x in [1, 3, 5])'))

源码，主要有两个方法::

  def timeit(stmt="pass", setup="pass", timer=default_timer,
            number=default_number, globals=None):
      """Convenience function to create Timer object and call timeit method."""
      return Timer(stmt, setup, timer, globals).timeit(number)

  def repeat(stmt="pass", setup="pass", timer=default_timer,
            repeat=default_repeat, number=default_number, globals=None):
      """Convenience function to create Timer object and call repeat method."""
      return Timer(stmt, setup, timer, globals).repeat(repeat, number)

参数解析：

- stmt	statement，需要计算的代码字符串。（本地测的时候，不支持外部的变量）
- setup	statement的前置执行，比如可以在这里import或者定义变量
- timer	默认是 default_timer = time.perf_counter ，使用的计时器
- number	指定执行的次数，默认是1000000（3.6的源码默认是100w）
- globals	执行的命名空间
- repeat	重复次数，3.6源码默认是3


