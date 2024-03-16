==================
divmod
==================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)

.. function:: divmod(a, b)

  a: 数字
  b: 数字

例::

  >>>divmod(7, 2)
  (3, 1)
  >>> divmod(8, 2)
  (4, 0)
  >>> divmod(1+2j,1+0.5j)
  ((1+0j), 1.5j)



