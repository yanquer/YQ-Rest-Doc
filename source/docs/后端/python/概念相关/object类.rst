=====================
object类
=====================

方法
=====================

- new_
- init_
- getattribute_
- getattr_
- setattr_
- delattr_
- enter_
- exit_
- str_
- class_
- iter_
- getitem_
- setitem_

.. _new:

__new__
---------------------

.. function:: __new__()

  code::

    def __new__(cls) -> Any: ...

  实例化对象的时候调用, 先执行 ``__new__()`` 返回对象实例, 再执行 ``__init__()`` 进行定义的初始化操作

  用处: 可以重写此方法实现单例, 相对于装饰器实现单例的好处是, 不会有装饰器实现单例的一些bug(暂且说是bug吧, 比如不能继承什么的)

.. _init:

__init__
---------------------

.. function:: __init__()

  code::

    def __init__(self) -> None: ...

  实例化对象时的初始化操作, 一般操作实例化时候传进来的值

  补充: 有一个名为 ``__init__.py`` 的文件, 在某目录根目录下新建此文件, 可以使该目录被识别为python模块

.. _getattribute:

__getattribute__
---------------------

.. function:: __getattribute__()

  code::

    def __getattribute__(self, name: str) -> Any: ...

  当访问实例属性时, 不管是方法还是成员变量, 都会默认调用这个(直接用类名调用不会触发),
  如果没找到 再去调用 ``__getattr__()``

  用处: 通过重写此方法实现代理

.. _getattr:

__getattr__
---------------------

.. function:: __getattr__()

  code::

    def __getattr__(self, name: str) -> None: ...

  当调用实例属性时, 没找到就调用, 默认再没有就报错, 可以通过重写此方法定义实例额外属性, 也可用作不冲突代理

  也可以直接 getattr(obj, name) 获取实例属性

  再次注意: **__getattr__ 方法是在访问 attribute 不存在的时候被调用**

.. _setattr:

__setattr__
---------------------

.. function:: __setattr__()

  code::

    def __setattr__(self, *args, **kwargs) -> None: ...

  与 getattr相对应, setattr是设置属性, getattr是获取属性

.. _delattr:

__delattr__
---------------------

.. function:: __delattr__()

  code::

    def __delattr__(self, name: str) -> None: ...

  删除实例属性

.. _enter:
.. _exit:

__enter__/__exit__
---------------------

.. function:: __enter__() 和 __exit__()

  实现自定义with语句需要重写的方法, with语句进入执行 __enter__(), 执行结束或异常 执行 __exit__(),

  注意,

  - enter的返回值是with实例化的值,
  - exit只有返回True时, 才不抛出异常
  - 其他相关使用不做赘述

.. _str:

__str__
---------------------

.. function:: __str__()

  code::

    def __str__(self, *args, **kwargs): ...

  设置直接打印实例时的值, 可以理解成将其转换为str类型的值

.. _class:

__class__
---------------------

.. function:: __class__()

  code::

    @property
    def __class__(self: _T) -> Type[_T]: ...
    # Ignore errors about type mismatch between property getter and setter
    @__class__.setter
    def __class__(self, __type: Type[object]) -> None: ...  # type: ignore # noqa: F811

  相当于java的get, set方法, 可以更方便的通过 @property 装饰器来访问成员变量

.. _iter:

__iter__
---------------------

使自身可迭代, 即可使用 for/next 循环.

.. _getitem:

__getitem__
---------------------

使自身可以用字典的形式 ``obj['x']`` 来取值.

.. _setitem:

__setitem__
---------------------

可与 getitem_ 一起使用, 不过这个是设置值的.

other 待后面补充::

    def __eq__(self, o: object) -> bool: ...
    def __ne__(self, o: object) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __sizeof__(self) -> int: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...
    def __reduce_ex__(self, protocol: int) -> Union[str, Tuple[Any, ...]]: ...
    def __dir__(self) -> Iterable[str]: ...
    def __init_subclass__(cls) -> None: ...

类属性
=====================

或者说成员变量

__slots__
---------------------

.. function:: __slots__: Union[str, Iterable[str]]

  默认情况下, python会使用字典保存实例相关的一些属性、 方法, 访问很方便但是会消耗额外内存,

  通过重定义此变量, 设置实例字典需要保存的属性, 节约空间

__dict__
---------------------

.. function:: __dict__: Dict[str, Any]

  实例对象会保存的一些属性, 如上所叙

__doc__
---------------------

.. function:: __doc__: Optional[str]

  类的使用说明文档定义

__module__
---------------------

.. function:: __module__: str

  待补充

__annotations__
---------------------

.. function:: __annotations__: Dict[str, Any]

  待补充



