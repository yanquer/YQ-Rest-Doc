==============
random
==============


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/random.html

**生成伪随机数**

该模块实现了各种分布的伪随机数生成器。

对于整数，从范围中有统一的选择。 对于序列，存在随机元素的统一选择、用于生成列表的随机排列的函数、以及用于随机抽样而无需替换的函数。

在实数轴上，有计算均匀、正态（高斯）、对数正态、负指数、伽马和贝塔分布的函数。 为了生成角度分布，可以使用 von Mises 分布。

这个模块提供的函数实际上是 random.Random 类的隐藏实例的绑定方法。 你可以实例化自己的 Random 类实例以获取不共享状态的生成器。

random 模块还提供 SystemRandom 类，它使用系统函数 os.urandom() 从操作系统提供的源生成随机数。

.. warning::

  不应将此模块的伪随机生成器用于安全目的。 有关安全性或加密用途，请参阅 :doc:`/docs/后端/python/python标准库/secrets` 模块。

功能/状态
==============

.. function:: random.seed(a=None, version=2)

  初始化随机数生成器。

  如果 a 被省略或为 None ，则使用当前系统时间。
  如果操作系统提供随机源，则使用它们而不是系统时间（有关可用性的详细信息，请参阅 os.urandom() 函数）。

  如果 a 是 int 类型，则直接使用。

  对于版本2（默认的），str 、 bytes 或 bytearray 对象转换为 int 并使用它的所有位。

  对于版本1（用于从旧版本的Python再现随机序列），用于 str 和 bytes 的算法生成更窄的种子范围。

  在 3.2 版更改: 已移至版本2方案，该方案使用字符串种子中的所有位。

  在 3.11 版更改: The seed must be one of the following types: NoneType, int, float, str, bytes, or bytearray.

.. function:: random.getstate()

  返回捕获生成器当前内部状态的对象。 这个对象可以传递给 setstate() 来恢复状态。

.. function:: random.setstate(state)

  state 应该是从之前调用 getstate() 获得的，并且 setstate() 将生成器的内部状态恢复到 getstate() 被调用时的状态。

用于字节数据的函数
============================

.. function:: random.randbytes(n)

  生成 n 个随机字节。

  此方法不可用于生成安全凭据。 那应当使用 secrets.token_bytes()。

  3.9 新版功能.

整数用函数
==============

.. function:: random.randrange(stop)

.. function:: random.randrange(start, stop[, step])
  :noindex:

  从 range(start, stop, step) 返回一个随机选择的元素。
  这相当于 choice(range(start, stop, step)) ，但实际上并没有构建一个 range 对象。

  位置参数模式匹配 range() 。不应使用关键字参数，因为该函数可能以意外的方式使用它们。

  在 3.2 版更改: randrange() 在生成均匀分布的值方面更为复杂。
  以前它使用了像``int(random()*n)``这样的形式，它可以产生稍微不均匀的分布。

  3.10 版后已移除: 非整数类型到相等整数的自动转换已被弃用。
  目前 randrange(10.0) 会无损地转换为 randrange(10)。 在未来，这将引发 TypeError。

  3.10 版后已移除: 针对非整数值例如 randrange(10.5) 或 randrange('10') 引发的异常将从 ValueError 修改为 TypeError。

.. function:: random.randint(a, b)

返回随机整数 N 满足 a <= N <= b。相当于 randrange(a, b+1)。

.. function:: random.getrandbits(k)

  返回具有 k 个随机比特位的非负 Python 整数。
  此方法随 MersenneTwister 生成器一起提供，其他一些生成器也可能将其作为 API 的可选部分提供。
  在可能的情况下，getrandbits() 会启用 randrange() 来处理任意大的区间。

  在 3.9 版更改: 此方法现在接受零作为 k 的值。
