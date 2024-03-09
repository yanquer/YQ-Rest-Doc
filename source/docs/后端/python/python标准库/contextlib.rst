=========================
contextlib
=========================

contextlib --- 为 with语句上下文提供的工具

官网: https://docs.python.org/zh-cn/3/library/contextlib.html

此模块为涉及 with 语句的常见任务提供了实用的工具。

常用的两个装饰器:

- @contextlib.contextmanager
- @contextlib.asynccontextmanager

.. function:: @contextlib.contextmanager

  这个函数是一个 decorator ，它可以定义一个支持 with 语句上下文管理器的工厂函数，
  而不需要创建一个类或区 ``__enter__()`` 与 ``__exit__()`` 方法。

  尽管许多对象原生支持使用 with 语句，但有些需要被管理的资源并不是上下文管理器，
  并且没有实现 close() 方法而不能使用 contextlib.closing 。

  示例，展示如何确保正确的资源管理::

    from contextlib import contextmanager

    @contextmanager
    def managed_resource(*args, **kwds):
        # Code to acquire resource, e.g.:
        resource = acquire_resource(*args, **kwds)
        try:
            yield resource
        finally:
            # Code to release resource, e.g.:
            release_resource(resource)

    with managed_resource(timeout=3600) as resource:
        # Resource is released at the end of this block,
        # even if code in the block raises an exception

  被装饰的函数在被调用时，必须返回一个 generator 迭代器。
  这个迭代器必须只 yield 一个值出来，这个值会被用在 with 语句中，绑定到 as 后面的变量，如果给定了的话。

  当生成器发生 yield 时，嵌套在 with 语句中的语句体会被执行。
  语句体执行完毕离开之后，该生成器将被恢复执行。
  如果在该语句体中发生了未处理的异常，则该异常会在生成器发生 yield 时重新被引发。
  因此，你可以使用 try...except...finally 语句来捕获该异常（如果有的话），或确保进行了一些清理。
  如果仅出于记录日志或执行某些操作（而非完全抑制异常）的目的捕获了异常，生成器必须重新引发该异常。
  否则生成器的上下文管理器将向 with 语句指示该异常已经被处理，程序将立即在 with 语句之后恢复并继续执行。

  contextmanager() 使用 ContextDecorator 因此它创建的上下文管理器不仅可以用在 with 语句中，还可以用作一个装饰器。
  当它用作一个装饰器时，每一次函数调用时都会隐式创建一个新的生成器实例
  （这使得 contextmanager() 创建的上下文管理器满足了支持多次调用以用作装饰器的需求，而非“一次性”的上下文管理器）。

.. function:: @contextlib.asynccontextmanager

  与 contextmanager() 类似，但创建的是 asynchronous context manager 异步的上下文管理器 。

  这个函数是一个 decorator ，它可以定义一个支持 async with 语句的异步上下文管理器的工厂函数，
  而不需要创建一个类或区分 ``__aenter__()`` 与 ``__aexit__()`` 方法。它必须被作用在一个 asynchronous generator 函数上

  一个简单的示例::

    from contextlib import asynccontextmanager

    @asynccontextmanager
    async def get_connection():
        conn = await acquire_db_connection()
        try:
            yield conn
        finally:
            await release_db_connection(conn)

    async def get_all_users():
        async with get_connection() as conn:
            return conn.query('SELECT ...')

  3.7 新版功能.

  使用 asynccontextmanager() 定义的 **上下文管理器可以用作装饰器**::

    import time
    from contextlib import asynccontextmanager

    @asynccontextmanager
    async def timeit():
        now = time.monotonic()
        try:
            yield
        finally:
            print(f'it took {time.monotonic() - now}s to run')

    @timeit()
    async def main():
        # ... async code ...

  用作装饰器时，每次函数调用都会隐式创建一个新的生成器实例。
  这使得由 asynccontextmanager() 创建的 “一次性” 上下文管理器能够满足作为装饰器所需要的支持多次调用的要求。

  在 3.10 版更改: 使用 asynccontextmanager() 创建的异步上下文管理器可以用作装饰器。

.. function:: contextlib.closing(thing)

  返回一个在语句块执行完成时关闭 things 的上下文管理器。这基本上等价于::

    from contextlib import contextmanager

    @contextmanager
    def closing(thing):
        try:
            yield thing
        finally:
            thing.close()

  并允许你编写这样的代码::

    from contextlib import closing
    from urllib.request import urlopen

    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)

  而无需显式地关闭 page 。 即使发生错误，在退出 with 语句块时， page.close() 也同样会被调用。

.. function:: contextlib.aclosing(thing)

  返回一个在语句块执行完成时调用 aclose() 方法来关闭 things 的异步上下文管理器。这基本上等价于::

    from contextlib import asynccontextmanager

    @asynccontextmanager
    async def aclosing(thing):
        try:
            yield thing
        finally:
            await thing.aclose()

  重要的是，aclosing() 支持在异步生成器因遭遇 break 或异常而提前退出时对其执行确定性的清理。 例如::

    from contextlib import aclosing

    async with aclosing(my_generator()) as values:
        async for value in values:
            if value == 42:
                break

  此模块将确保生成器的异步退出代码在与其迭代相同的上下文中执行
  （这样异常和上下文变量将能按预期工作，并且退出代码不会在其所依赖的某些任务的生命期结束后继续运行）。

  3.10 新版功能.






