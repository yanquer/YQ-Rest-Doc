==================
Shiboken
==================

安装 pyside6 自带的模块

- 可使用其访问一些内部信息, 一般用于 debug
- 使用 Shiboken 创建的对象都是 Python 对象

.. note::

  **其实就是将 C++ 对象转换为可调用的 Python 对象**

一些工具方法:

- def isValid_ (obj)
- def wrapInstance_ (address, type)
- def getCppPointer_ (obj)
- def delete_ (obj)
- def isOwnedByPython_ (obj)
- def wasCreatedByPython_ (obj)
- def dump_ (obj)
- def disassembleFrame_ (marker)

isValid
==================

.. function:: def isValid (obj)

  判断 obj 的方法是否可以正常使用而不抛出异常

  当所指向的 C++ 对象已销毁或者不可达时, 装饰器无效.

  obj:
    Python 对象

wrapInstance
==================

.. function:: def wrapInstance (address, type)

  对 C++ 对象, 使用指定的 内存地址 address 创建一个 Python 装饰器, 返回值即所给类 type 的对象

  address:
    内存地址. 若地址不可用, 或者没指向指定 type 的 C++ 对象, 将会 undefined ?
  type:
    使用来实例对象的类, 必须是 Shiboken 类型, 当返回对象在 Python 内部的引用计数不为0时, 相关联底层 C++ 对象不会被销毁


getCppPointer
==================

.. function:: def getCppPointer (obj)

  返回 被给定 obj 装饰的, 包含了 C++ 对象地址的长元组.

delete
==================

.. function:: def delete (obj)

  删除被 obj 装饰的 C++ 对象

isOwnedByPython
==================

.. function:: def isOwnedByPython (obj) -> bool

  obj:
    Python 对象, 如果不是 Shiboken 下的类型, 将会抛出 TypeError

  @retuen: bool
    True:  Python 可正确删除底层的 C++ 对象, 即 C++ 对象完全被 obj 所 `代理`
    False:

wasCreatedByPython
====================================

.. function:: def wasCreatedByPython (obj) -> bool

  是否给定的对象是被 Python 创建

  @return: bool
    True:  给定的对象是被 Python 创建
    False:

dump
==================

.. function:: def dump (obj) -> str

  只应在 debug 时使用.

  如果 obj 不是 Shiboken 下的类型, 将会打印信息

  @return: str
    返回对象的 str 信息, 还可能包含自己实现的相关信息

disassembleFrame
==================

.. function:: def disassembleFrame (marker)

  只应用于 debug

  打印当前 Python 执行的堆栈信息并刷新, 打印的信息将会被 marker 所包裹.

  如果想在此位置打断点(基于C++的断点), 可使用纯函数名. marker 在 C++ 下是一个 string.

  如果是基于 Python 的断点, 在需要断点的位置使用此装饰器. marker 在 Python 下可以是任意对象, 将会调用对象内部的 ``str`` 方法

  marker:
    用于包裹打印出的堆栈信息





