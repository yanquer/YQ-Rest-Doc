================
zip
================


.. post:: 2024-03-06 23:40:36
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. note::

  相似的函数见 :doc:`/docs/后端/python/python标准库/itertools`
  的 :ref:`zip_longest <Python_zip_longest>`

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

zip 方法在 Python 2 和 Python 3 中的不同：
在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。

.. function:: zip([iterable, ...])

  iterable -- 一个或多个迭代器;

  返回元组列表


如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表::

  >>> a = [1,2,3]
  >>> b = [4,5,6]
  >>> c = [4,5,6,7,8]
  >>> zipped = zip(a,b)     # 返回一个对象
  >>> zipped
  <zip object at 0x103abc288>
  >>> list(zipped)  # list() 转换为列表
  [(1, 4), (2, 5), (3, 6)]
  >>> list(zip(a,c))              # 元素个数与最短的列表一致
  [(1, 4), (2, 5), (3, 6)]

  >>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
  >>> list(a1)
  [1, 2, 3]
  >>> list(a2)
  [4, 5, 6]
  >>>
