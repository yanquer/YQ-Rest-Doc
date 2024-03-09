=================
with
=================

with相当于 try catch finnally语句

自定义的with语句, 需要实现::

  # coding: utf-8

  class TW(object):

    # with包含初始化时执行, 返回值给到语句定义的as别名
    def __enter__(self):
      return 999

    # 出现异常或者正常结束时候执行
    # 返回值为True时, 不抛出异常, 否则正常抛出异常
    def __exit__(self, exc_type, exc_val, exc_tb):
      if exc_tb:
        print(exc_type, exc_val, exc_tb)
      return True

  with TW() as t:
    print(t)
    raise ValueError('error test')

async with语句
=====================

异步上下文管理器.

用于异步编程.

与 with 不同的是,
如果要实现异步的调用, 需要实现 ``__aenter__`` 与 ``__aexit__`` 方法::

  class AsyncContextManager:
      async def __aenter__(self):
          await log('entering context')

      async def __aexit__(self, exc_type, exc, tb):
          await log('exiting context')

这时就可以异步调用::

  async with AsyncContextManager():
    ...









