================
any
================

any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False

元素除了是 0、空、FALSE 外都算 TRUE。

函数等价于::

  def any(iterable):
      for element in iterable:
          if element:
              return True
      return False

.. function:: any(iterable)

  iterable:
    元组或列表

  如果都为空、0、false，则返回false，
  如果不都为空、0、false，则返回true


