=====================
str/repr
=====================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


str 与 repr 函数的效果差不多, 所以就放到一起说了.

对于继承了 object 的类(新式类)而言, 可以通过重写::

  __str__()
  __repr__()

来更改默认行为.

一般而言,

- repr 用于 开发/测试,
- str 用于正式场景
- 若没有定义 ``__str__`` 而定义了 ``__repr__`` , 则使用 str, 会调用 ``__repr__``

可以看看默认的例子::

  In [7]: @dataclass
   ...: class MTest(object):
   ...:     name: str
   ...:     age: int
   ...:

  In [8]: m = MTest('tt', 12)

  In [9]: str(m)
  Out[9]: "MTest(name='tt', age=12)"

  In [10]: repr(m)
  Out[10]: "MTest(name='tt', age=12)"

可以发现默认实现的没有什么差别. 这时候如果需要不一致, 就需要自己重写了...

理想的情况::

  In [14]: import datetime

  In [15]: d = datetime.datetime.now()

  In [16]: d
  Out[16]: datetime.datetime(2023, 4, 13, 9, 37, 55, 887361)

  In [17]: str(d)
  Out[17]: '2023-04-13 09:37:55.887361'

  In [18]: repr(d)
  Out[18]: 'datetime.datetime(2023, 4, 13, 9, 37, 55, 887361)'





