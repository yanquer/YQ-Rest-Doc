====================
types
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


types --- 动态类型创建和内置类型名称

官网: https://docs.python.org/zh-cn/3/library/types.html

此模块定义了一些工具函数，用于协助动态创建新的类型。

它还为某些对象类型定义了名称，这些名称由标准 Python 解释器所使用，但并不像内置的 int 或 str 那样对外公开。

最后，它还额外提供了一些类型相关但重要程度不足以作为内置对象的工具类和函数。

动态类型创建
====================

.. function:: types.new_class(name, bases=(), kwds=None, exec_body=None)

  使用适当的元类动态地创建一个类对象。

  前三个参数是组成类定义头的部件：类名称，基类 (有序排列)，关键字参数 (例如 metaclass)。

  exec_body 参数是一个回调函数，用于填充新创建类的命名空间。
  它应当接受类命名空间作为其唯一的参数并使用类内容直接更新命名空间。
  如果未提供回调函数，则它就等效于传入 lambda ns: None。

  3.3 新版功能.

.. function:: types.prepare_class(name, bases=(), kwds=None)

  计算适当的元类并创建类命名空间。

  参数是组成类定义头的部件：类名称，基类 (有序排列) 以及关键字参数 (例如 metaclass)。

  返回值是一个 3 元组: metaclass, namespace, kwds

  metaclass 是适当的元类，namespace 是预备好的类命名空间而 kwds 是所传入 kwds 参数移除每个 'metaclass' 条目后的已更新副本。 如果未传入 kwds 参数，这将为一个空字典。

  3.3 新版功能.

  在 3.6 版更改: 所返回元组中 namespace 元素的默认值已被改变。 现在当元类没有 __prepare__ 方法时将会使用一个保留插入顺序的映射。

.. function:: types.resolve_bases(bases)

  动态地解析 MRO 条目

  3.7 新版功能.

标准解释器类型
====================

此模块为许多类型提供了实现 Python 解释器所要求的名称。
它刻意地避免了包含某些仅在处理过程中偶然出现的类型，例如 listiterator 类型。

此种名称的典型应用如 isinstance() 或 issubclass() 检测。

如果你要实例化这些类型中的任何一种，请注意其签名在不同 Python 版本之间可能出现变化。

以下类型有相应的标准名称定义：

types.NoneType
  None 的类型。

  3.10 新版功能.
types.FunctionType
  \.
types.LambdaType
  用户自定义函数以及由 lambda 表达式所创建函数的类型。

  引发一个 审计事件 function.__new__，附带参数 code。

  此审计事件只会被函数对象的直接实例化引发，而不会被普通编译所引发。
types.GeneratorType
  generator 迭代器对象的类型，由生成器函数创建。
types.CoroutineType
  coroutine 对象的类型，由 async def 函数创建。

  3.5 新版功能.
types.AsyncGeneratorType
  asynchronous generator 迭代器对象的类型，由异步生成器函数创建。

  3.6 新版功能.

.. function:: class types.CodeType(**kwargs)

  代码对象的类型，例如 compile() 的返回值。

  引发 审计事件 code.__new__ 附带参数 code, filename, name, argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize, flags。

  请注意被审计的参数可能与初始化代码所要求的名称或位置不相匹配。 审计事件只会被代码对象的直接实例化引发，而不会被普通编译所引发。

.. function:: replace(**kwargs)

  返回代码对象的一个副本，使用指定的新字段值。

  3.8 新版功能.

types.CellType
  单元对象的类型：这种对象被用作函数中自由变量的容器。

  3.8 新版功能.
types.MethodType
  用户自定义类实例方法的类型。
types.BuiltinFunctionType
  .
types.BuiltinMethodType
  内置函数例如 len() 或 sys.exit() 以及内置类方法的类型。 （这里所说的“内置”是指“以 C 语言编写”。）
types.WrapperDescriptorType
  某些内置数据类型和基类的方法的类型，例如 object.__init__() 或 object.__lt__()。
types.MethodWrapperType
  某些内置数据类型和基类的 绑定 方法的类型。 例如 object().__str__ 所属的类型。
types.NotImplementedType
  NotImplemented 的类型。
types.MethodDescriptorType
  某些内置数据类型方法例如 str.join() 的类型。
types.ClassMethodDescriptorType
  某些内置数据类型 非绑定 类方法例如 dict.__dict__['fromkeys'] 的类型。
class types.ModuleType(name, doc=None)
  模块 的类型。 构造器接受待创建模块的名称并以其 docstring 作为可选参数。

  备注: 如果你希望设置各种由导入控制的属性，请使用 importlib.util.module_from_spec() 来创建一个新模块。
__doc__
  模块的 docstring。 默认为 None。
__loader__
  用于加载模块的 loader。 默认为 None。

  This attribute is to match importlib.machinery.ModuleSpec.
  loader as stored in the __spec__ object.

  .. note::

    未来的 Python 版本可能会停止默认设置此属性。
    为了避免这个潜在变化的影响，如果你明确地需要使用此属性则推荐改从 __spec__ 属性读取
    或是使用 getattr(module, "__loader__", None)。

  在 3.4 版更改: 默认为 None。 之前该属性为可选项。
__name__
  模块的名称。 应当能匹配 importlib.machinery.ModuleSpec.name。
__package__
  一个模块所属的 package。
  如果模块为最高层级的（即不是任何特定包的组成部分）则该属性应设为 ''，
  否则它应设为特定包的名称 (如果模块本身也是一个包则名称可以为 __name__)。 默认为 None。

  This attribute is to match importlib.machinery.ModuleSpec.parent as stored in the __spec__ object.

  .. note::

    未来的 Python 版本可能停止默认设置此属性。
    为了避免这个潜在变化的影响，如果你明确地需要使用此属性则推荐改从 __spec__ 属性读取或是使用 getattr(module, "__package__", None)。

  在 3.4 版更改: 默认为 None。 之前该属性为可选项。
__spec__
  模块的导入系统相关状态的记录。 应当是一个 importlib.machinery.ModuleSpec 的实例。
types.EllipsisType
  Ellipsis 的类型。
class types.GenericAlias(t_origin, t_args)
  形参化泛型 的类型，例如 list[int]。

  t_origin 应当是一个非形参化的泛型类，例如 list, tuple 或 dict。
  t_args 应当是一个形参化 t_origin 的 tuple (长度可以为 1)::

    >>>
    from types import GenericAlias

    list[int] == GenericAlias(list, (int,))
    True
    dict[str, int] == GenericAlias(dict, (str, int))
    True

  在 3.9.2 版更改: 此类型现在可以被子类化。
class types.UnionType
  合并类型表达式 的类型。

.. function:: class types.TracebackType(tb_next, tb_frame, tb_lasti, tb_lineno)

  The type of traceback objects such as found in sys.exception().__traceback__.

types.FrameType
  帧对象的类型，例如 tb.tb_frame 中的对象，其中 tb 是一个回溯对象。
types.GetSetDescriptorType
  使用 PyGetSetDef 在扩展模块中定义的对象的类型，例如 FrameType.f_locals 或 array.array.typecode。
  此类型被用作对象属性的描述器；它的目的与 property 类型相同，但专门针对在扩展模块中定义的类。
types.MemberDescriptorType
  使用 PyMemberDef 在扩展模块中定义的对象的类型，例如 datetime.timedelta.days。
  此类型被用作使用标准转换函数的简单 C 数据成员的描述器；它的目的与 property 类型相同，但专门针对在扩展模块中定义的类。

  CPython 实现细节： 在 Python 的其它实现中，此类型可能与 GetSetDescriptorType 完全相同。
class types.MappingProxyType(mapping)
  一个映射的只读代理。 它提供了对映射条目的动态视图，这意味着当映射发生改变时，视图会反映这些改变。

  在 3.9 版更改: 更新为支持 PEP 584 所新增的合并 (|) 运算符，它会简单地委托给下层的映射。

.. function:: key in proxy

  如果下层的映射中存在键 key 则返回 True，否则返回 False。

proxy[key]
  返回下层的映射中以 key 为键的项。 如果下层的映射中不存在键 key 则引发 KeyError。
iter(proxy)
  返回由下层映射的键为元素的迭代器。 这是 iter(proxy.keys()) 的快捷方式。
len(proxy)
  返回下层映射中的项数。
copy()
  返回下层映射的浅拷贝。
get(key[, default])
  如果 key 存在于下层映射中则返回 key 的值，否则返回 default。
  如果 default 未给出则默认为 None，因而此方法绝不会引发 KeyError。
items()
  返回由下层映射的项 ((键, 值) 对) 组成的一个新视图。
keys()
  返回由下层映射的键组成的一个新视图。
values()
  返回由下层映射的值组成的一个新视图。
reversed(proxy)
  返回一个包含下层映射的键的反向迭代器。

附加工具类/函数
====================

.. function:: class types.SimpleNamespace

  一个简单的 object 子类，提供了访问其命名空间的属性，以及一个有意义的 repr。

  不同于 object，对于 SimpleNamespace 你可以添加和移除属性。 如果一个 SimpleNamespace 对象使用关键字参数进行初始化，这些参数会被直接加入下层命名空间。

  此类型大致等价于以下代码::

    class SimpleNamespace:
        def __init__(self, /, **kwargs):
            self.__dict__.update(kwargs)

        def __repr__(self):
            items = (f"{k}={v!r}" for k, v in self.__dict__.items())
            return "{}({})".format(type(self).__name__, ", ".join(items))

        def __eq__(self, other):
            if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
              return self.__dict__ == other.__dict__
            return NotImplemented

  SimpleNamespace 可被用于替代 class NS: pass。 但是，对于结构化记录类型则应改用 namedtuple()。

  在 3.9 版更改: repr 中的属性顺序由字母顺序改为插入顺序 (类似 dict)。

.. function:: types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)

  在类上访问 __getattr__ 的路由属性。

  这是一个描述器，用于定义通过实例与通过类访问时具有不同行为的属性。 当实例访问时保持正常行为，但当类访问属性时将被路由至类的 __getattr__ 方法；这是通过引发 AttributeError 来完成的。

  这允许有在实例上激活的特性属性，同时又有在类上的同名虚拟属性 (一个例子请参见 enum.Enum)。

协程工具函数
====================

.. function:: types.coroutine(gen_func)

  This function transforms a generator function into a coroutine function which returns a generator-based coroutine.
  The generator-based coroutine is still a generator iterator,
  but is also considered to be a coroutine object and is awaitable.
  However, it may not necessarily implement the __await__() method.

  如果 gen_func 是一个生成器函数，它将被原地修改为异步生成器函数。

  如果 gen_func 不是一个生成器函数，则它会被包装。 如果它返回一个 collections.abc.Generator 的实例，该实例将被包装在一个 awaitable 代理对象中。 所有其他对象类型将被原样返回。

  3.5 新版功能.




