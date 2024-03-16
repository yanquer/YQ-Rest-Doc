================================
list
================================


.. post:: 2024-03-06 23:40:36
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


index()方法
  检测 **字符串** 中是否包含子字符串 str，并返回索引值；
  从 **列表** 中找出某个值第一个匹配项的索引位置。

list 求交集并集差集
================================

不建议的::

  # 假设有两个集合 a,b
  # 交集
  [val for val in a if val in b]
  # 并集
  list(set(a+b))
  # 差集
  [val for val in b if val not in a]	# b中有而a中没有的

建议的高效的::

  # 假设有两个集合 a,b
  # 交集
  list(set(a).intersection(set(b)))
  # 并集
  list(set(a).union(set(b)))
  # 差集
  list(set(b).difference(set(a)))	# b中有而a中没有的

见 :doc:`/docs/后端/python/内置函数/set`

求其中某值的个数
================================

使用 count, 如::

  In [23]: [1, 2, 3].count(3)
  Out[23]: 1




