==============
math
==============

官网: `math --- 数学函数 <https://docs.python.org/zh-cn/3/library/math.html>`_

该模块提供了对C标准定义的数学函数的访问。

这些函数不适用于复数；如果你需要计算复数，请使用 :doc:`/docs/后端/python/python标准库/cmath` 模块中的同名函数。
将支持计算复数的函数区分开的目的，来自于大多数开发者并不愿意像数学家一样需要学习复数的概念。
得到一个异常而不是一个复数结果使得开发者能够更早地监测到传递给这些函数的参数中包含复数，进而调查其产生的原因。

该模块提供了以下函数。除非另有明确说明，否则所有返回值均为浮点数。

数论与表示函数
============================

.. function:: math.ceil(x)

  返回 x 的向上取整，即大于或等于 x 的最小的整数。如果 x 不是浮点数，委托给 x.__ceil__ ，它应该返回一个 Integral 的值。

.. function:: math.comb(n, k)

  返回不重复且无顺序地从 n 项中选择 k 项的方式总数。

  当 k <= n 时取值为 n! / (k! * (n - k)!)；当 k > n 时取值为零。

  Also called the binomial coefficient because it is equivalent to the coefficient of k-th term in polynomial expansion of (1 + x)ⁿ.

  如果任一参数不为整数则会引发 TypeError。 如果任一参数为负数则会引发 ValueError。

  3.8 新版功能.

.. function:: math.copysign(x, y)

  返回一个基于 x 的绝对值和 y 的符号的浮点数。在支持带符号零的平台上，copysign(1.0, -0.0) 返回 -1.0.

.. function:: math.fabs(x)

  返回 x 的绝对值。

.. function:: math.factorial(n)

  Return n factorial as an integer. Raises ValueError if n is not integral or is negative.

  3.9 版后已移除: 接受具有整数值的浮点数 (例如 5.0) 的行为已被弃用。

.. function:: math.floor(x)

  返回 x 的向下取整，小于或等于 x 的最大整数。如果 x 不是浮点数，则委托给 x.__floor__ ，它应返回一个 Integral 值。

.. function:: math.fmod(x, y)

  返回 fmod(x, y) ，由平台C库定义。请注意，Python表达式 x % y 可能不会返回相同的结果。
  C标准的目的是 fmod(x, y) 完全（数学上；到无限精度）等于 x - n*y 对于某个整数 n ，使得结果具有 与 x 相同的符号和小于 abs(y) 的幅度。
  Python的 x % y 返回带有 y 符号的结果，并且可能不能完全计算浮点参数。
  例如， fmod(-1e-100, 1e100) 是 -1e-100 ，但Python的 -1e-100 % 1e100 的结果是 1e100-1e-100 ，
  它不能完全表示为浮点数，并且取整为令人惊讶的 1e100 。
  出于这个原因，函数 fmod() 在使用浮点数时通常是首选，而Python的 x % y 在使用整数时是首选。

.. function:: math.frexp(x)

  以 (m, e) 对的形式返回 x 的尾数和指数。
  m 是一个浮点数， e 是一个整数，正好是 x == m * 2**e 。

  如果 x 为零，则返回 (0.0, 0) ，否则返回 0.5 <= abs(m) < 1 。这用于以可移植方式“分离”浮点数的内部表示。

.. function:: math.fsum(iterable)

  返回迭代中的精确浮点值。通过跟踪多个中间部分和来避免精度损失::

    sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    0.9999999999999999
    fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    1.0

  该算法的准确性取决于IEEE-754算术保证和舍入模式为半偶的典型情况。在某些非Windows版本中，底层C库使用扩展精度添加，并且有时可能会使中间和加倍，导致它在最低有效位中关闭。

  有关待进一步讨论和两种替代方法，参见 ASPN cookbook recipes for accurate floating point summation。

.. function:: math.gcd(*integers)

  返回给定的整数参数的最大公约数。 如果有一个参数非零，则返回值将是能同时整除所有参数的最大正整数。 如果所有参数为零，则返回值为 0。 不带参数的 gcd() 返回 0。

  3.5 新版功能.

  在 3.9 版更改: 添加了对任意数量的参数的支持。 之前的版本只支持两个参数。

.. function:: math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

  若 a 和 b 的值比较接近则返回 True，否则返回 False。

  根据给定的绝对和相对容差确定两个值是否被认为是接近的。

  rel_tol 是相对容差 —— 它是 a 和 b 之间允许的最大差值，相对于 a 或 b 的较大绝对值。例如，要设置5％的容差，请传递 rel_tol=0.05 。默认容差为 1e-09，确保两个值在大约9位十进制数字内相同。 rel_tol 必须大于零。

  abs_tol 是最小绝对容差 —— 对于接近零的比较很有用。 abs_tol 必须至少为零。

  如果没有错误发生，结果将是： abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol) 。

  IEEE 754特殊值 NaN ， inf 和 -inf 将根据IEEE规则处理。具体来说， NaN 不被认为接近任何其他值，包括 NaN 。 inf 和 -inf 只被认为接近自己。

  3.5 新版功能.

  参见 PEP 485 —— 用于测试近似相等的函数

.. function:: math.isfinite(x)

  如果 x 既不是无穷大也不是NaN，则返回 True ，否则返回 False 。 （注意 0.0 被认为 是 有限的。）

  3.2 新版功能.

.. function:: math.isinf(x)

  如果 x 是正或负无穷大，则返回 True ，否则返回 False 。

.. function:: math.isnan(x)

  如果 x 是 NaN（不是数字），则返回 True ，否则返回 False 。

.. function:: math.isqrt(n)

  返回非负整数 n 的整数平方根。 这就是对 n 的实际平方根向下取整，或者相当于使得 a² ≤ n 的最大整数 a。

  对于某些应用来说，可以更适合取值为使得 n ≤ a² 的最小整数 a ，或者换句话说就是 n 的实际平方根向上取整。
  对于正数 n，这可以使用 a = 1 + isqrt(n - 1) 来计算。

  3.8 新版功能.

.. function:: math.lcm(*integers)

  返回给定的整数参数的最小公倍数。 如果所有参数均非零，则返回值将是为所有参数的整数倍的最小正整数。 如果参数之一为零，则返回值为 0。 不带参数的 lcm() 返回 1。

  3.9 新版功能.

.. function:: math.ldexp(x, i)

  返回 x * (2**i) 。 这基本上是函数 frexp() 的反函数。

.. function:: math.modf(x)

  返回 x 的小数和整数部分。两个结果都带有 x 的符号并且是浮点数。

.. function:: math.nextafter(x, y)

  返回 x 趋向于 y 的最接近的浮点数值。

  如果 x 等于 y 则返回 y。

  示例::

    math.nextafter(x, math.inf) 的方向朝上：趋向于正无穷。
    math.nextafter(x, -math.inf) 的方向朝下：趋向于负无穷。
    math.nextafter(x, 0.0) 趋向于零。
    math.nextafter(x, math.copysign(math.inf, x)) 趋向于零的反方向。

  另请参阅 math.ulp()。

  3.9 新版功能.

.. function:: math.perm(n, k=None)

  返回不重复且有顺序地从 n 项中选择 k 项的方式总数。

  当 k <= n 时取值为 n! / (n - k)!；当 k > n 时取值为零。

  如果 k 未指定或为 None，则 k 默认值为 n 并且函数将返回 n!。

  如果任一参数不为整数则会引发 TypeError。 如果任一参数为负数则会引发 ValueError。

  3.8 新版功能.

.. function:: math.prod(iterable, *, start=1)

  计算输入的 iterable 中所有元素的积。 积的默认 start 值为 1。

  当可迭代对象为空时，返回起始值。 此函数特别针对数字值使用，并会拒绝非数字类型。

  3.8 新版功能.

.. function:: math.remainder(x, y)

  返回 IEEE 754 风格的 x 相对于 y 的余数。对于有限 x 和有限非零 y ，这是差异 x - n*y ，其中 n 是与商 x / y 的精确值最接近的整数。
  如果 x / y 恰好位于两个连续整数之间，则将最接近的 偶数 用作 n 。 余数 r = remainder(x, y) 因此总是满足 abs(r) <= 0.5 * abs(y)。

  特殊情况遵循IEEE 754：特别是 remainder(x, math.inf) 对于任何有限 x 都是 x ，
  而 remainder(x, 0) 和 remainder(math.inf, x) 引发 ValueError 适用于任何非NaN的 x 。
  如果余数运算的结果为零，则该零将具有与 x 相同的符号。

  在使用IEEE 754二进制浮点的平台上，此操作的结果始终可以完全表示：不会引入舍入错误。

  3.7 新版功能.

.. function:: math.trunc(x)

  返回去除小数部分的 x ，只留下整数部分。
  这样就可以四舍五入到0了： trunc() 对于正的 x 相当于 floor() ，对于负的 x 相当于 ceil() 。
  如果 x 不是浮点数，委托给 x.__trunc__ ，它应该返回一个 Integral 值。

.. function:: math.ulp(x)

  返回浮点数 x 的最小有效比特位的值:

  如果 x 是 NaN (非数字)，则返回 x。
  如果 x 为负数，则返回 ulp(-x)。
  如果 x 为正数，则返回 x。
  如果 x 等于零，则返回 去正规化的 可表示最小正浮点数 (小于 正规化的 最小正浮点数 sys.float_info.min)。
  如果 x 等于可表示最大正浮点数，则返回 x 的最低有效比特位的值，使得小于 x 的第一个浮点数为 x - ulp(x)。
  在其他情况下 (x 是一个有限的正数)，则返回 x 的最低有效比特位的值，使得大于 x 的第一个浮点数为 x + ulp(x)。
  ULP 即 "Unit in the Last Place" 的缩写。

  另请参阅 math.nextafter() 和 sys.float_info.epsilon。

    3.9 新版功能.

注意 frexp() 和 modf() 具有与它们的C等价函数不同的调用/返回模式：
它们采用单个参数并返回一对值，而不是通过 '输出形参' 返回它们的第二个返回参数（Python中没有这样的东西）。

对于 ceil() ， floor() 和 modf() 函数，请注意 所有 足够大的浮点数都是精确整数。
Python浮点数通常不超过53位的精度（与平台C double类型相同），在这种情况下，任何浮点 x 与 abs(x) >= 2**52 必然没有小数位。

幂函数与对数函数
============================

.. function:: math.cbrt(x)

  Return the cube root of x.

  3.11 新版功能.

.. function:: math.exp(x)

  返回 e 次 x 幂，其中 e = 2.718281... 是自然对数的基数。这通常比 math.e ** x 或 pow(math.e, x) 更精确。

.. function:: math.exp2(x)

  Return 2 raised to the power x.

  3.11 新版功能.

.. function:: math.expm1(x)

  返回 e 的 x 次幂，减1。这里 e 是自然对数的基数。
  对于小浮点数 x ， exp(x) - 1 中的减法可能导致 significant loss of precision；
  expm1() 函数提供了一种将此数量计算为全精度的方法::

    from math import exp, expm1
    exp(1e-5) - 1  # gives result accurate to 11 places
    1.0000050000069649e-05
    expm1(1e-5)    # result accurate to full precision
    1.0000050000166668e-05

  3.2 新版功能.

.. function:: math.log(x[, base])

  使用一个参数，返回 x 的自然对数（底为 e ）。

  使用两个参数，返回给定的 base 的对数 x ，计算为 log(x)/log(base) 。

.. function:: math.log1p(x)

  返回 1+x 的自然对数（以 e 为底）。 以对于接近零的 x 精确的方式计算结果。

.. function:: math.log2(x)

  返回 x 以2为底的对数。这通常比 log(x, 2) 更准确。

  3.3 新版功能.

  参见 int.bit_length() 返回表示二进制整数所需的位数，不包括符号和前导零。

.. function:: math.log10(x)

  返回 x 底为10的对数。这通常比 log(x, 10) 更准确。

.. function:: math.pow(x, y)

  Return x raised to the power y. Exceptional cases follow the IEEE 754 standard as far as possible. In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.

  与内置的 ** 运算符不同， math.pow() 将其参数转换为 float 类型。使用 ** 或内置的 pow() 函数来计算精确的整数幂。

  在 3.11 版更改: The special cases pow(0.0, -inf) and pow(-0.0, -inf) were changed to return inf instead of raising ValueError, for consistency with IEEE 754.

.. function:: math.sqrt(x)

  返回 x 的平方根。

三角函数
============================

.. function:: math.acos(x)

 返回以弧度为单位的 x 的反余弦值。 结果范围在 0 到 pi 之间。

.. function:: math.asin(x)

  返回以弧度为单位的 x 的反正弦值。 结果范围在 -pi/2 到 pi/2 之间。

.. function:: math.atan(x)

  返回以弧度为单位的 x 的反正切值。 结果范围在 -pi/2 到 pi/2 之间。.

.. function:: math.atan2(y, x)

  以弧度为单位返回 atan(y / x) 。结果是在 -pi 和 pi 之间。从原点到点 (x, y) 的平面矢量使该角度与正X轴成正比。 atan2() 的点的两个输入的符号都是已知的，因此它可以计算角度的正确象限。 例如， atan(1) 和 atan2(1, 1) 都是 pi/4 ，但 atan2(-1, -1) 是 -3*pi/4 。

.. function:: math.cos(x)

  返回 x 弧度的余弦值。

.. function:: math.dist(p, q)

  返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。

  大致相当于::

    sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

  3.8 新版功能.

.. function:: math.hypot(*coordinates)

  返回欧几里得范数，sqrt(sum(x**2 for x in coordinates))。 这是从原点到坐标给定点的向量长度。

  对于一个二维点 (x, y)，这等价于使用毕达哥拉斯定义 sqrt(x*x + y*y) 计算一个直角三角形的斜边。

  在 3.8 版更改: 添加了对 n 维点的支持。 之前的版本只支持二维点。

  在 3.10 版更改: 改进了算法的精确性，使得最大误差在 1 ulp (最后一位的单位数值) 以下。 更为常见的情况是，结果几乎总是能正确地舍入到 1/2 ulp 范围之内。

.. function:: math.sin(x)

  返回 x 弧度的正弦值。

.. function:: math.tan(x)

  返回 x 弧度的正切值。

角度转换
============================

.. function:: math.degrees(x)

  将角度 x 从弧度转换为度数。

.. function:: math.radians(x)

  将角度 x 从度数转换为弧度。

双曲函数
============================

双曲函数 是基于双曲线而非圆来对三角函数进行模拟。

.. function:: math.acosh(x)

  返回 x 的反双曲余弦值。

.. function:: math.asinh(x)

  返回 x 的反双曲正弦值。

.. function:: math.atanh(x)

  返回 x 的反双曲正切值。

.. function:: math.cosh(x)

  返回 x 的双曲余弦值。

.. function:: math.sinh(x)

  返回 x 的双曲正弦值。

.. function:: math.tanh(x)

  返回 x 的双曲正切值。

特殊函数
============================

.. function:: math.erf(x)

  返回 x 处的 error function 。

  The erf() function can be used to compute traditional statistical functions such as the cumulative standard normal distribution::

    def phi(x):
        'Cumulative distribution function for the standard normal distribution'
        return (1.0 + erf(x / sqrt(2.0))) / 2.0

  3.2 新版功能.

.. function:: math.erfc(x)

  返回 x 处的互补误差函数。 互补错误函数 定义为 1.0 - erf(x)。 它用于 x 的大值，从其中减去一个会导致 有效位数损失。

  3.2 新版功能.

.. function:: math.gamma(x)

  返回 x 处的 伽马函数 值。

  3.2 新版功能.

.. function:: math.lgamma(x)

  返回Gamma函数在 x 绝对值的自然对数。

  3.2 新版功能.

常量
============================

math.pi:
  数学常数 π = 3.141592...，精确到可用精度。
math.e:
  数学常数 e = 2.718281...，精确到可用精度。
math.tau:
  数学常数 τ = 6.283185...，精确到可用精度。
  Tau 是一个圆周常数，等于 2π，圆的周长与半径之比。
  更多关于 Tau 的信息可参考 Vi Hart 的视频 Pi is (still) Wrong。吃两倍多的派来庆祝 Tau 日 吧！

  3.6 新版功能.
math.inf:
  浮点正无穷大。 （对于负无穷大，使用 -math.inf 。）相当于 float('inf') 的输出。

  3.5 新版功能.
math.nan:
  一个浮点的 "非数字"（NaN）值。相当于 float('nan') 的输出。
  由于 IEEE-754标准 的要求， math.nan 和 float('nan') 不被认为等于任何其他数值，包括其本身。
  要检查一个数字是否为NaN，请使用 isnan() 函数来测试 NaN ，而不是 is 或 == 。

  例子::

    >>>
    import math
    math.nan == math.nan
    False
    float('nan') == float('nan')
    False
    math.isnan(math.nan)
    True
    math.isnan(float('nan'))
    True

  在 3.11 版更改: It is now always available.

  3.5 新版功能.

CPython 实现细节
============================

math 模块主要包含围绕平台C数学库函数的简单包装器。
特殊情况下的行为在适当情况下遵循C99标准的附录F。
当前的实现将引发 ValueError 用于无效操作，如 sqrt(-1.0) 或 log(0.0) （其中C99附件F建议发出无效操作信号或被零除），
和 OverflowError 用于溢出的结果（例如， exp(1000.0) ）。
除非一个或多个输入参数是NaN，否则不会从上述任何函数返回NaN；
在这种情况下，大多数函数将返回一个NaN，但是（再次遵循C99附件F）这个规则有一些例外，
例如 pow(float('nan'), 0.0) 或 hypot(float('nan'), float('inf')) 。

请注意，Python不会将显式NaN与静默NaN区分开来，并且显式NaN的行为仍未明确。典型的行为是将所有NaN视为静默的。



