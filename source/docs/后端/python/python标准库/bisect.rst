===========================
bisect
===========================


.. post:: 2023-02-24 22:59:42
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


bisect --- 数组二分查找算法

官网: `<https://docs.python.org/zh-cn/3/library/bisect.html>`_

这个模块对有序列表提供了支持，使得他们可以在插入新数据仍然保持有序。
对于长列表，如果其包含元素的比较操作十分昂贵的话，这可以是对更常见方法的改进。
这个模块叫做 bisect 因为其使用了基本的二分（bisection）算法。源代码也可以作为很棒的算法示例（边界判断也做好啦！）

支持的函数

.. function:: bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)

  a:
    需要插入的序列
  x:
    需要插入的值
  lo:
    序列a的起始位置
  hi:
    序列a的结束位置. 实际只从 a[lo: hi] 这个子集中找
  key:
    指定带有单个参数的 key function 用来从数组的每个元素中提取比较键。
    为了支持搜索复杂记录，键函数不会被应用到 x 值。

    如果 key 为 None，则将直接进行元素比较而不需要中间的函数调用。

  在 a 中找到 x 合适的插入点以维持有序。
  参数 lo 和 hi 可以被用于确定需要考虑的子集；默认情况下整个列表都会被使用。
  如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。
  如果 a 是列表（list）的话，返回值是可以被放在 list.insert() 的第一个参数的。

  返回的插入点 i 将数组 a 分成两半，使得 ``all(val < x for val in a[lo : i])`` 在左半边
  而 ``all(val >= x for val in a[i : hi])`` 在右半边。

  在 3.10 版更改: 增加了 key 形参。

.. function:: bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)

  bisect_right 与 bisect_left 的区别
    - 如果有序列表a没有元素x, 那么两者返回的索引相同,
      返回的索引地址, 使得arr的insert插入该值还是有序的
    - 如果有序列表a包含元素x,
      left返回已包含元素x的索引,
      right返回的索引值是在left的基础上加一

  如::

    data = [2, 5, 6, 9]

    print(f'数组: {data}')
    for x in (0, 2, 5, 8, 9, 10):
        l = bisect.bisect_left(data, x)
        r = bisect.bisect_right(data, x)

        print(f"查找: {x},  left结: {l}, right结: {r}")

  输出::

    数组: [2, 5, 6, 9]
    查找: 0,  left结: 0, right结: 0
    查找: 2,  left结: 0, right结: 1
    查找: 5,  left结: 1, right结: 2
    查找: 8,  left结: 3, right结: 3
    查找: 9,  left结: 3, right结: 4
    查找: 10,  left结: 4, right结: 4

.. function:: bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)

  类似于 bisect_left()，但是返回的插入点是 a 中已存在元素 x 的右侧。

  返回的插入点 i 将数组 a 分成两半，使得
  左半边为 ``all(val <= x for val in a[lo : i])``
  而右半边为 ``all(val > x for val in a[i : hi])``

  key 指定带有单个参数的 key function 用来从数组的每个元素中提取比较键。
  为了支持搜索复杂记录，键函数不会被应用到 x 值。

  如果 key 为 None，则将直接进行元素比较而不需要中间的函数调用。

  在 3.10 版更改: 增加了 key 形参。

.. function:: bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)

  按照已排序顺序将 x 插入到 a 中。

  此函数首先会运行 bisect_left() 来定位一个插入点。 然后，它会在 a 上运行 insert() 方法在正确的位置插入 x 以保持排序顺序。

  为了支持将记录插入到表中，key 函数（如果存在）将被应用到 x 用于搜索步骤但不会用于插入步骤。

  请记住 O(log n) 搜索是由缓慢的 O(n) 抛入步骤主导的。

  在 3.10 版更改: 增加了 key 形参。

.. function:: bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)

  .

.. function:: bisect.insort(a, x, lo=0, hi=len(a), *, key=None)

  类似于 insort_left()，但是把 x 插入到 a 中已存在元素 x 的右侧。

  此函数首先会运行 bisect_right() 来定位一个插入点。 然后，它会在 a 上运行 insert() 方法在正确的位置插入 x 以保持排序顺序。

  为了支持将记录插入到表中，key 函数（如果存在）将被应用到 x 用于搜索步骤但不会用于插入步骤。

  请记住 O(log n) 搜索是由缓慢的 O(n) 抛入步骤主导的。

  在 3.10 版更改: 增加了 key 形参。

当使用 bisect() 和 insort() 编写时间敏感的代码时，请记住以下概念:

- 二分法对于搜索一定范围的值是很高效的。 对于定位特定的值，则字典的性能更好。
- insort() 函数的时间复杂度为 O(n) 因为对数时间的搜索步骤被线性时间的插入步骤所主导。
  这些搜索函数都是无状态的并且会在它们被使用后丢弃键函数的结果。
  因此，如果在一个循环中使用搜索函数，则键函数可能会在同一个数据元素上被反复调用。
  如果键函数速度不快，请考虑用 functools.cache() 来包装它以避免重复计算。
  另外，也可以考虑搜索一个预先计算好的键数组来定位插入点。



