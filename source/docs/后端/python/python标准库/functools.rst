====================
functools
====================

官网

wraps
====================

.. function:: functools.wraps()

  用于自定义装饰器, 刷新名称

partial
====================

也叫偏函数

.. function:: functools.partial()

  用于包装函数, 可用于函数回调的时候, 增加参数, 或者说固定参数::

    def show(name, age):
        print("my name is {} and age is {}".format(name, age))


    # 相当于生成一个新的函数
    # def new_fun():
    #   show("x x x",1)
    # 如果
    # showP = functools.partial(show, "xxx")	# 固定第一个参数为 xxx
    # showP(20)
    # 结果一样
    showP = functools.partial(show, "xxx", 20)	# 固定前两个参数为 xxx, 20, 也适用于关键字参数


    def test(callback):
        print("do some opt…………")
        callback()


    test(showP)

    # do some opt…………
    # my name is xxx and age is 19

用途: 有些回调函数不支持传入参数, 可以使用此函数来支持参数.

total_ordering
====================

装饰器, 实现比较方法

.. function:: @functools.total_ordering

  给定一个声明一个或多个全比较排序方法的类，这个类装饰器实现剩余的方法。这减轻了指定所有可能的全比较操作的工作。

  此类必须包含以下方法之一：__lt__() 、__le__()、__gt__() 或 __ge__()。另外，此类必须支持 __eq__() 方法。

  例如::

    @total_ordering
    class Student:
        def _is_valid_operand(self, other):
            return (hasattr(other, "lastname") and
                    hasattr(other, "firstname"))
        def __eq__(self, other):
            if not self._is_valid_operand(other):
                return NotImplemented
            return ((self.lastname.lower(), self.firstname.lower()) ==
                    (other.lastname.lower(), other.firstname.lower()))
        def __lt__(self, other):
            if not self._is_valid_operand(other):
                return NotImplemented
            return ((self.lastname.lower(), self.firstname.lower()) <
                    (other.lastname.lower(), other.firstname.lower()))

.. note::

  虽然此装饰器使得创建具有良好行为的完全有序类型变得非常容易，
  但它 确实 是以执行速度更缓慢和派生比较方法的堆栈回溯更复杂为代价的。
  如果性能基准测试表明这是特定应用的瓶颈所在，则改为实现全部六个富比较方法应该会轻松提升速度。

  这个装饰器不会尝试重载类 或其上级类 中已经被声明的方法。
  这意味着如果某个上级类定义了比较运算符，则 total_ordering 将不会再次实现它，即使原方法是抽象方法。

3.2 新版功能.

在 3.4 版更改: 现在已支持从未识别类型的下层比较函数返回 NotImplemented 异常。






