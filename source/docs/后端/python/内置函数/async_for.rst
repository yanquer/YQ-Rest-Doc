====================
async for
====================

异步迭代器.

普通对象的for循环只需要实现 ``__iter__`` 即可

对于 async for而言, 若需要支持, 需要实现 ``__aiter__`` 返回一个异步迭代器（asynchronous iterator）对象;
若需要对象本身就是一个迭代器. 还需要实现 ``__anext__`` , 返回一个awaitable类型的值(异步迭代器对象);

例::

  class AsyncIteratorWrapper:
      def __init__(self, obj):
          self._it = iter(obj)

      def __aiter__(self):
          return self

      async def __anext__(self):
          try:
              value = next(self._it)
          except StopIteration:
              raise StopAsyncIteration
          return value

  async for letter in AsyncIteratorWrapper("abc"):
      print(letter)




