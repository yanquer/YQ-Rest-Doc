===================
collections
===================

deque
===================

队列

.. function:: deque(maxlen)

  maxlen: int
    设置队列的长度

- 在队列两端插入或删除元素时间复杂度都是 O(1)
- 在列表的开头插入或删除元 素的时间复杂度为 O(N)

defaultdict
===================

具有默认值的字典

OrderedDict
===================

自排序的字典(保持插入时顺序)

OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
每次当一个新的 元素插入进来的时候，它会被放到链表的尾部。
对于一个已经存在的键的重复赋值不会改变键的顺序。

需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，
因为它内部维 护着另外一个链表。
所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的 时候
(比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去)，
那么你就得仔 细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。

Counter
===================

计算出现次数

下面有一个 most_common() 返回出现次数最多的::

  words = [
      'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
      'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
      'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
      'my', 'eyes', "you're", 'under'
  ]
  from collections import Counter
  word_counts = Counter(words)
  # 出现频率最高的 3 个单词
  top_three = word_counts.most_common(3)
  print(top_three)
  # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

作为输入，Counter 对象可以接受任意的由可哈希(hashable)元素构成的序列 对象。
在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数 上。比如::

  >>> word_counts['not'] 1
  >>> word_counts['eyes'] 8
  >>>

同时也支持数学运算操作

Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的 工具。
在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。

Counter求交集
-------------------

**求交集(且保留最小值)**

假设 `secret = "1123"` 且 `guess = "0111"`，
那么 `Counter(secret)` 会得到::

  Counter({'1': 2, '2': 1, '3': 1})

而 `Counter(guess)` 会得到::

  Counter({'0': 1, '1': 3})

取它们的交集后得到::

  # 交集只有 1, 取其中小的个数 2
  Counter({'1': 2})

表示在 `secret` 和 `guess` 中都有的数字 `1` 的数量为 2。

total
-------------------

Counter().total()表示当前总的个数, 比如::

  Counter({'1': 2, '2': 3}).total() == 5

namedtuple
===================

映射元组到对象::

  >>> from collections import namedtuple
  >>> Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
  >>> sub = Subscriber('jonesy@example.com', '2012-10-19')
  >>> sub
  Subscriber(addr='jonesy@example.com', joined='2012-10-19')
  >>> sub.addr
  'jonesy@example.com'
  >>> sub.joined
  '2012-10-19'
  >>>

跟元组类型是可交换 的，支持所有的普通元组操作，比如索引和解压。比如::

  >>> len(sub)
  2
  >>> addr, joined = sub >>> addr 'jonesy@example.com' >>> joined '2012-10-19'

命名元组的一个主要用途是将你的代码从下标操作中解脱出来。

命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存空间。

注意一个命名元组是不可更改的, 如有特殊需要, 使用 ``_replace`` ::

  >>> s = Stock('ACME', 100, 123.45)
  >>> s
  Stock(name='ACME', shares=100, price=123.45)
  >>> s.shares = 75
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  AttributeError: can't set attribute
  >>>
  >>> s = s._replace(shares=75)
  >>> s
  Stock(name='ACME', shares=75, price=123.45)
  >>>

ChainMap
===================

链式合并字典.

假如你有如下两个字典::

  a = {'x': 1, 'z': 3 }
  b = {'y': 2, 'z': 4 }

现在假设你必须在两个字典中执行查找操作(比如先从 a 中找，如果找不到再在 b 中找)。
一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类。比如::

  from collections import ChainMap c = ChainMap(a,b)
  print(c['x']) # Outputs 1 (from a) print(c['y']) # Outputs 2 (from b) print(c['z']) # Outputs 3 (from a)
  >>> len(c)
  3
  >>> list(c.keys()) ['x', 'y', 'z']
  >>> list(c.values()) [1, 2, 3]
  >>>


一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。
然后，这些字典并 不是真的合并在一起了，ChainMap 类只是在内部创建了一个容纳这些字典的列表并重 新定义了一些常见的字典操作来遍历这个列表。
大部分字典操作都是可以正常使用的， 比如:
如果出现重复键，那么第一次出现的映射值会被返回。

因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值。
对于字典的更新或删除操作总是影响的是列表中第一个字典。比如::

  >>> c['z'] = 10
  >>> c['w'] = 40
  >>> del c['x']
  >>> a
  {'w': 40, 'z': 10}
  >>> del c['y']
  Traceback (most recent call last): ...
      KeyError: "Key not found in the first mapping: 'y'"
  >>>


