===========================
contextvars
===========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网文档: https://docs.python.org/zh-cn/3/library/contextvars.html

上下文变量

本模块提供了相关API用于管理、存储和访问上下文相关的状态。
ContextVar 类用于声明 上下文变量 并与其一起使用。
函数 copy_context()  和类 Context 用于管理当前上下文和异步框架中。

在多并发环境中，有状态上下文管理器应该使用上下文变量，
而不是 threading.local() 来防止他们的状态意外泄露到其他代码

.. note::

  在异步/多并发环境中(多进程/多线程都属于多并发), `ContextVar(xxx).get()` 获取的值是实时同步的最新的

  ContextVar通过共享内存的方式提供了一种更轻量和Pythonic的不同任务间共享状态的机制.
  但不适合不同进程间通信;

  如果需要跨进程,还是更建议使用 `from multiprocessing import Manager`

常用有ContextVar

.. function:: class contextvars.ContextVar(name[, *, default])

  此类用于声明一个新的上下文变量，如::

    var: ContextVar[int] = ContextVar('var', default=42)

  name:
    上下文变量的名称，只读属性; 用于内省和调试，必需.

    调用 ContextVar.get() 时，如果上下文中没有找到此变量的值，则返回可选的仅命名参数 default 。

  .. important::

    上下文变量应该在顶级模块中创建，且永远不要在闭包中创建。
    Context 对象拥有对上下文变量的强引用，这可以让上下文变量被垃圾收集器正确回收。

  3.7.1 新版功能.

  get([default])
    返回当前上下文中此上下文变量的值。

    如果当前上下文中此变量没有值，则此方法会:

    - 如果提供了 default，返回其值；或者
      返回上下文变量本身的默认值，
    - 如果创建此上下文变量时提供了默认值；或者
      抛出 LookupError 异常。
  set(value)
    调用此方法设置上下文变量在当前上下文中的值。

    必选参数 value 是上下文变量的新值。

    返回一个 Token  对象，可通过 ContextVar.reset() 方法将上下文变量还原为之前某个状态。
  reset(token)
    将上下文变量重置为调用 ContextVar.set() 之前、创建 token 时候的状态。

    例如::

      var = ContextVar('var')

      token = var.set('new value')
      # code that uses 'var'; var.get() returns 'new value'.
      var.reset(token)

      # After the reset call the var has no value again, so
      # var.get() would raise a LookupError.

ContextVar-用例
===========================

code::

  CONTEXT_EXAMPLE = ContextVar('context-example', default=list())

