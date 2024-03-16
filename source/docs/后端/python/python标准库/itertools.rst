================
itertools
================


.. post:: 2024-03-10 20:49:14
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: `<https://docs.python.org/zh-cn/3/library/itertools.html>`_

groupby
================

根据某个记录分组::

  rows = [
      {'address': '5412 N CLARK', 'date': '07/01/2012'},
      {'address': '5148 N CLARK', 'date': '07/04/2012'},
      {'address': '5800 E 58TH', 'date': '07/02/2012'},
      {'address': '2122 N CLARK', 'date': '07/03/2012'},
      {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
      {'address': '1060 W ADDISON', 'date': '07/02/2012'},
      {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
      {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
  ]

根据日期分组::

  from operator import itemgetter
  from itertools import groupby

  # Sort by the desired field first
  rows.sort(key=itemgetter('date'))
  # Iterate in groups
  for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
      print(' ', i)

一个非常重要的准备步骤是要根据指定的字段将数据排序。
因为 groupby() 仅仅 检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。

compress
================

itertools.compress

以一个 iterable 对象和一个相对应的Boolean选择器序列作为输入参数。
然后输出iterable对象中对 应选择器为 True 的元素::

  addresses = [
      '5412 N CLARK',
      '5148 N CLARK',
      '5800 E 58TH',
      '2122 N CLARK',
      '5645 N RAVENSWOOD',
      '1060 W ADDISON',
      '4801 N BROADWAY',
      '1039 W GRANVILLE',
  ]
  counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

操作::

  >>> from itertools import compress
  >>> more5 = [n > 5 for n in counts]
  >>> more5
  [False, False, True, False, False, True, True, False]
  >>> list(compress(addresses, more5))
  ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
  >>>

关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。
然后 compress() 函数根据这个序列去选择输出对应位置为 True 的元素。

和 filter() 函数类似，compress() 也是返回的一个迭代器。

permutations
================

排列函数, 比如获取某个迭代的全排列

如, 从num中抽2个获取全排列::

  permutations('ABCD', 2)

结果::

  AB AC AD BA BC BD CA CB CD DA DB DC

combinations
================

组合函数, 从某个迭代中抽取指定的不重复元素个数组合

如, 从num中抽2个组合(不重复)::

  combinations('ABCD', 2)

  AB AC AD BC BD CD

combinations_with_replacement
================================

组合函数, 从某个迭代中抽取指定的重复元素个数组合

如, 从num中抽2个组合(可重复)::

  combinations_with_replacement('ABCD', 2)

  AA AB AC AD BB BC BD CC CD DD

.. _Python_zip_longest:

zip_longest
================================

与 zip 类似, 不过 zip 返回的结果以最短的序列为准, zip_longest以最长的序列为准::

  In [18]: from itertools import zip_longest

  In [19]: list(zip('ABC', range(5), [10, 20, 30, 40]))
  Out[19]: [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]

  In [20]: list(zip_longest('ABC', range(5), [10, 20, 30, 40]))
  Out[20]: [('A', 0, 10), ('B', 1, 20), ('C', 2, 30), (None, 3, 40), (None, 4, None)]

  In [21]:

starmap
================================

乘法运算符可以被映射到两个向量之间执行高效的点积::

  sum(starmap(operator.mul, zip(vec1, vec2, strict=True)))。

.. note::

  operator 见 :doc:`operator`

再如统计两个数组a, b中索引与元素都相等的个数::

  starmap(operator.eq, zip(a, b))






