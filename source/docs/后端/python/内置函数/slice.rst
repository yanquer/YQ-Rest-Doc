================
slice
================

切片操作

slice() 函数返回 slice 对象（切片）。

slice 对象用于指定如何对序列进行裁切。
您可以指定在哪里开始裁切以及在哪里结束裁切。
您还可以指定步进，例如只切每隔一个项目。

.. function:: slice(start, end, step)

  start: int = 0
    指定在哪个位置开始裁切
  end: int
    指定在哪个位置结束裁切
  step: int = 1
    指定裁切的步长

支持有趣的操作::

  >>> items = [0, 1, 2, 3, 4, 5, 6]
  >>> a = slice(2, 4)
  >>> items[2:4]
  [2, 3]
  >>> items[a]
  [2, 3]
  >>> items[a] = [10,11]
  >>> items
  [0, 1, 10, 11, 4, 5, 6]
  >>> del items[a]
  >>> items
  [0, 1, 4, 5, 6]

可以分别调用它的 a.start , a.stop , a.step 属性 来获取更多的信息。比如::

  >>> a = slice(5, 50, 2)
  >>> a.start
  5
  >>> a.stop
  50
  >>> a.step 2
  >>>

还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序 列上，
这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以 满足边界限制，
从而使用的时候避免出现 IndexError 异常。比如::

  >>> s = 'HelloWorld'
  >>> a.indices(len(s))
  (5, 10, 2)
  >>> for i in range(*a.indices(len(s))): ... print(s[i])
  ...
  W
  r
  d
  >>>



