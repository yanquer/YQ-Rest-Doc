=================
bytearray
=================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。

.. function:: class bytearray([source[, encoding[, errors]]])

  source:
    如果 source 为整数，则返回一个长度为 source 的初始化数组；
    如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
    如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
    如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
    如果没有输入任何参数，默认就是初始化数组为0个元素。

  返回值:
    返回新字节数组。


bytearray() 的使用方法::

  >>>bytearray()
  bytearray(b'')
  >>> bytearray([1,2,3])
  bytearray(b'\x01\x02\x03')
  >>> bytearray('runoob', 'utf-8')
  bytearray(b'runoob')
  >>>








