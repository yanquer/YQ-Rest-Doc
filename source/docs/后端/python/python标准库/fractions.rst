====================
fractions
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


支持分数运算, 如::

  >>> from fractions import Fraction
  >>> a = Fraction(5, 4)
  >>> b = Fraction(7, 16)
  >>> print(a + b)
  27/16

  >>> # Getting numerator/denominator >>> c = a * b
  >>> c.numerator
  35
  >>> c.denominator 64
