===========================
dataclasses
===========================

官网: https://docs.python.org/zh-cn/3/library/dataclasses.html

提供了一个装饰器和一些函数，用于自动添加生成的 special method，例如 __init__() 和 __repr__() 到用户定义的类。

装饰器使用
===========================

.. function:: @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)

  dataclass() 装饰器会检查类以查找 具有 **类型标注** 的 **类变量**

类属性的默认值

.. function:: dataclasses.field(*, default=MISSING, default_factory=MISSING, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=MISSING)

  对于被 dataclasses 装饰的数据类, 有时候 类变量的默认值 是较复杂的类型, 这时候就可以使用 field 方式来定义其默认值

  default:
    可选, 表示此变量的默认值
  default_factory
    可选, 必须是一个零参数可调用对象，当该字段需要一个默认值时，它将被调用。可以用于指定具有可变默认值的字段

    与 default 的区别是:

    - default 与 default_factory 仅可显示指定一个
    - default 制定的值将会在多个对象之间共享; default_factory 指定的工程, 每个对象生成的值是独立的, 仅用于可变类型
    - default可以是“任何可调用对象”，包括函数、lambda表达式、staticmethod等; 而default_factory必须是一个函数。

  注意: 同时指定 default 和 default_factory 将产生错误。

  init: bool = True
    如果为true（默认值），则该字段作为参数包含在生成的 __init__() 方法中。
  repr: bool = True
    如果为true（默认值），则该字段包含在生成的 __repr__() 方法返回的字符串中。
  hash: bool = None
    如果为true，则此字段包含在生成的 __hash__() 方法中。如果为 None （默认值），请使用 compare 的值，这通常是预期的行为。如果字段用于比较，则应在 hash 中考虑该字段。不鼓励将此值设置为 None 以外的任何值。

    设置 hash=False 但 compare=True 的一个可能原因是，如果一个计算 hash 的代价很高的字段是检验等价性需要的，但还有其他字段可以计算类型的 hash 。 即使从 hash 中排除某个字段，它仍将用于比较。
  compare: bool = True
    如果为true（默认值），则该字段包含在生成的相等性和比较方法中（ __eq__() ， __gt__() 等等）。
  metadata: dict = None
    这可以是映射或 None 。 None 被视为一个空的字典。这个值包含在 MappingProxyType() 中，使其成为只读，并暴露在 Field 对象上。数据类根本不使用它，它是作为第三方扩展机制提供的。多个第三方可以各自拥有自己的键值，以用作元数据中的命名空间。
  kw_only:
    如果为真值，则此字段将被标记为仅限关键字。 这将在当计算出所生成的 __init__() 方法的形参时被使用。

如果通过调用 field() 指定字段的默认值，则该字段的类属性将替换为指定的 default 值。
如果没有提供 default ，那么将删除类属性。目的是在 dataclass() 装饰器运行之后，类属性将包含字段的默认值，就像指定了默认值一样。
例如::

  @dataclass
  class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20

类属性 C.z 将是 10 ，类属性 C.t 将是 20，类属性 C.x 和 C.y 将不设置(因为 **没设置默认值** )。

.. class:: class dataclasses.Field

  Field 对象描述每个定义的字段。这些对象在内部创建，并由 fields() 模块级方法返回（见下文）。用户永远不应该直接实例化 Field 对象。 其有文档的属性是：

  name ：字段的名字。
  type ：字段的类型。
  default, default_factory, init, repr, hash, compare, metadata 和 kw_only 具有与 field() 函数中对应参数相同的含义和值。
  可能存在其他属性，但它们是私有的，不能被审查或依赖。

.. function:: dataclasses.fields(class_or_instance)

  返回 Field 对象的元组，用于定义此数据类的字段。 接受数据类或数据类的实例。如果没有传递一个数据类或实例将引发 TypeError 。 不返回 ClassVar 或 InitVar 的伪字段。

.. function:: dataclasses.asdict(obj, *, dict_factory=dict)

  将数据类``obj``转换为一个字典（通过使用工厂函数``dict_factory``）。 每个数据类被转换为其字段的字典，作为``name: value``键值对。数据类、字典、列表和元组被递归到。 其他对象用 copy.deepcopy() 来复制。

  在嵌套的数据类上使用 asdict() 的例子::

    @dataclass
    class Point:
      x: int
      y: int

    @dataclass
    class C:
      mylist: list[Point]

    p = Point(10, 20)
    assert asdict(p) == {'x': 10, 'y': 20}

    c = C([Point(0, 0), Point(10, 4)])
    assert asdict(c) == {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}

  要创建一个浅拷贝，可以使用以下方法::

    dict((field.name, getattr(obj, field.name)) for field in fields(obj))

  如果 obj 不是一个数据类实例, asdict() 引发 TypeError 。

.. function:: dataclasses.astuple(obj, *, tuple_factory=tuple)

  将数据类``obj``转换为一个元组（通过使用工厂函数``tuple_factory``）。 每个数据类被转换为其字段值的元组。数据类、字典、列表和元组被递归到。其他对象用 copy.deepcopy() 来复制。

  继续前一个例子::

    assert astuple(p) == (10, 20)
    assert astuple(c) == ([(0, 0), (10, 4)],)

  要创建一个浅拷贝，可以使用以下方法::

    tuple(getattr(obj, field.name) for field in dataclasses.fields(obj))

  如果``obj``不是一个数据类实例， astuple() 引发 TypeError 。

.. function:: dataclasses.make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)

  与使用装饰器 @dataclasses 的效果一致

  此函数不是严格要求的，因为用于任何创建带有 __annotations__ 的新类的 Python 机制都可以应用 dataclass() 函数将该类转换为数据类。提供此功能是为了方便。例如::

    C = make_dataclass('C',
            [('x', int),
              'y',
              ('z', int, field(default=5))],
            namespace={'add_one': lambda self: self.x + 1})

  等价于::

    @dataclass
    class C:
      x: int
      y: 'typing.Any'
      z: int = 5

      def add_one(self):
        return self.x + 1

.. function:: dataclasses.replace(obj, /, **changes)

  创建一个与``obj``类型相同的新对象，将字段替换为来自``changes``的值。如果``obj``不是数据类，则引发 TypeError 。如果``changes``里面的值没有指定字段，引发 TypeError 。

  新返回的对象通过调用数据类的 __init__() 方法创建。这确保了如果存在 __post_init__() ，其也被调用。

  如果存在没有默认值的仅初始化变量，必须在调用 replace() 时指定，以便它们可以传递给 __init__() 和 __post_init__() 。

  changes 包含任何定义为 init=False 的字段是错误的。在这种情况下会引发 ValueError 。

  提前提醒 init=False 字段在调用 replace() 时的工作方式。如果它们完全被初始化的话，它们不是从源对象复制的，而是在 __post_init__() 中初始化。估计 init=False 字段很少能被正确地使用。如果使用它们，那么使用备用类构造函数或者可能是处理实例复制的自定义 replace() （或类似命名的）方法可能是明智的。

.. function:: dataclasses.is_dataclass(obj)

  如果其形参为 dataclass 或其实例则返回 True，否则返回 False。

  如果你需要知道一个类是否是一个数据类的实例（而不是一个数据类本身），那么再添加一个 not isinstance(obj, type) 检查


.. note::

  使用 @dataclasses 时, __init__() 方法将会调用 __post_init__() 方法

  且具有继承关系的类时, __init__() 不会实现基类的 __init__(), 故有需求可以在 __post_init__() 里调用

  具有继承关系时, 参数为其变量声明顺序(变量类型默认值会被覆盖). 关键字字段具有重新排序: 先顺序普通字段, 再顺序关键字字段.

类属性
===========================

dataclasses.MISSING
  一个表示缺失 default 或 default_factory 的监视值。
dataclasses.KW_ONLY
  .. _KW_ONLY:

  一个用作类型标注的监视值。 任何在伪字段之后的类型为 KW_ONLY 的字段会被标记为仅限关键字字段。
  请注意在其他情况下 KW_ONLY 类型的伪字段会被完全忽略。
  这包括此类字段的名称。 根据惯例，名称 _ 会被用作 KW_ONLY 字段。
  仅限关键字字段指明当类被实例化时 __init__() 形参必须以关键字形式来指定。
  可用于 关键字字段重排序_ .

  在这个例子中，字段 y 和 z 将被标记为仅限关键字字段::

    @dataclass
    class Point:
        x: float
        _: KW_ONLY
        y: float
        z: float

    p = Point(0, y=1.5, z=2.0)

  在单个数据类中，指定一个以上 KW_ONLY 类型的字段将导致错误。

继承时顺序
===========================

继承时, 顺序按照定义顺序, 但是类型会被覆盖(Python继承MRO机制)::

  @dataclass
  class Base:
      x: Any = 15.0
      y: int = 0

  @dataclass
  class C(Base):
      z: int = 10
      x: int = 15

最后的字段列表依次是 x 、 y 、 z 。 x 的最终类型是 int ，如类 C 中所指定的那样。
类似::

  def __init__(self, x: int = 15, y: int = 0, z: int = 10): ...

关键字字段重排序
===========================

仅限关键字字段的重新排序-使用 KW_ONLY_

在计算出 __init__() 所需要的形参之后，任何仅限关键字形参会被移至所有常规（非仅限关键字）形参的后面。
这是 Python 中实现仅限关键字形参所要求的：它们必须位于非仅限关键字形参之后。

在这个例子中，Base.y, Base.w, and D.t 是仅限关键字字段，而 Base.x 和 D.z 是常规字段::

  @dataclass
  class Base:
      x: Any = 15.0
      _: KW_ONLY
      y: int = 0
      w: int = 1

  @dataclass
  class D(Base):
      z: int = 10
      # 注意这里也有 kw_only 参数
      t: int = field(kw_only=True, default=0)

结果近似::

  def __init__(self, x: Any = 15.0, z: int = 10, *, y: int = 0, w: int = 1, t: int = 0): ...

