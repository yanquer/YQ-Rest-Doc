==============
ord
==============

ord() 函数是 chr() 函数（对于8位的ASCII字符串, 见 :doc:`/docs/后端/python/内置函数/chr` ）
或 unichr() 函数（对于Unicode对象）的配对函数，
它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。


.. function:: ord(c)
  :noindex:

  c:
    字符

  返回值是对应的十进制整数::

    >>>ord('a')
    97
    >>> ord('b')
    98
    >>> ord('c')
    99

