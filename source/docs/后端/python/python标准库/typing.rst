=================
typing
=================

类型注解模块

Union
=================

Union 是当有多种可能的数据类型时使用，比如函数有可能根据不同情况有时返回str或返回list，那么就可以写成::

  Union[list, str]

Optional
=================

Optional 是Union的一个简化， 当 数据类型中有可能是None时，比如有可能是str也有可能是None，
则::

  Optional[str]

相当于::

  Union[str, None]

注意 和 函数有默认参数None有区别，有区别，有区别，不可省略默认参数，如下示例::

  # 原始
  def func(args = None):

  # 错
  def func(args:Optional[str]) -> None:

  # 对
  def func(args:Optional[str] = None) -> None:

Type
=================

表示值为所指定类或其子类:

  arg1: Type[ClassObj]

.. _CR_Callable:

Callable
=================

表示可调用对象, 支持指定参数与返回值.

eg, 异步函数的类型注解::

  Callable[..., Awaitable]

表示是async函数, 且参数任意, 相当于此函数::

  async def fun(...) -> Awaitable:

.. _an_is_typing:

判断注解是否引入了typing
==================================

Python 中没有强定义类型, 不过可以使用类型注解, 如::

  @dataclass
  class Person(object):
    name: str
    pet: List[Cat] = field(default_factory=list)
    pet2: Cat = field(default_factory=Cat)

类型注解除了使用基础的数据类型, 还可以使用 typing 模块下的定义, 判断是否是typing下的注解::

  from typing import _GenericAlias

  for f in fields(Person):
    print('type', f.type)
    if isinstance(f.type, _GenericAlias):
      print(f'{f.name} is isinstance of _GenericAlias')

获取typing注解的详细信息
==================================

获取注解参数列表, 使用::

  typing.get_args()

获取注解的详细类型, 如::

  In [31]: import typing

  In [32]: typing.get_args(typing.Dict[str, tuple])
  Out[32]: (<class 'str'>, <class 'tuple'>)

返回结果是一个元组

获取相关基础类型
==================================

获取注解原始类型, 使用 typing.get_origin ::

  In [33]: typing.get_origin(typing.Dict[str, tuple])
  Out[33]: <class 'dict'>





