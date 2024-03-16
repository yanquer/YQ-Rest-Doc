=====================
chr
=====================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。

.. function:: chr(i)

  i:
    十进制/十六进制 整数

  返回值是当前整数对应的 ASCII 字符::

    >>>print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
    0 1 a
    >>> print chr(48), chr(49), chr(97)         # 十进制
    0 1 a
