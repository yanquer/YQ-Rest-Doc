==================
operator
==================

两个便捷使用的操作::

  import operator
  operator.itemgetter
  <class 'operator.itemgetter'>
  operator.attrgetter
  <class 'operator.attrgetter'>

- itemgetter, 便捷获取字典属性
- attrgetter, 便捷获取对象属性

itemgetter
==================

有一个字典列表，你想根据某个或某几个字典字段来排序这个列表::

  rows = [
      {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
      {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
      {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
      {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
  ]

  from operator import itemgetter

  rows_by_fname = sorted(rows, key=itemgetter('fname'))
  rows_by_uid = sorted(rows, key=itemgetter('uid'))

也支持多个 keys，比如下面的代码::

  rows_by_lfname = sorted(rows, key=itemgetter('lname','fname')) print(rows_by_lfname)

也可以用 lambda 表达式代替，比如:

  rows_by_fname = sorted(rows, key=lambda r: r['fname'])
  rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))

但是效率较低

attrgetter
==================

与上类似. 支持的是自定义对象


总览
==================

部分总览::

  operator.lt(a, b)
  operator.le(a, b)
  operator.eq(a, b)
  operator.ne(a, b)
  operator.ge(a, b)
  operator.gt(a, b)
  operator.__lt__(a, b)
  operator.__le__(a, b)
  operator.__eq__(a, b)
  operator.__ne__(a, b)
  operator.__ge__(a, b)
  operator.__gt__(a, b)

