=================
filter
=================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

- Python2.7 返回列表
- Python3.x 返回迭代器对象

.. function:: filter(function, iterable)

  function -- 判断函数。
  iterable -- 可迭代对象。

  该接收两个参数，第一个为函数，第二个为序列，
  序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

过滤出列表中的所有奇数::

  def is_odd(n):
      return n % 2 == 1

  newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  print(newlist)


