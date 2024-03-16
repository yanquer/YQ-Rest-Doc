=====================
enumerate
=====================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


enumerate() 函数返回的是一个 enumerate 对象实例，它是一个迭代器，返回连 续的包含一个计数和一个值的元组，
元组中的值通过在传入序列上调用 next() 返回。

接受一个参数作为起始序号, 默认为0::

  >>> my_list = ['a', 'b', 'c']
  >>> for idx, val in enumerate(my_list, 1):
  ...   print(idx, val)
  ...
  1a
  2b
  3c


