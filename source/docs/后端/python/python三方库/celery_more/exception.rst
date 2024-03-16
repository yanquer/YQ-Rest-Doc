=================
自定义异常
=================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库, celery_more
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


Python 的异常必须要符合一些简单规则，才能被 pickle 模块支持以及序列化。

使用 Pickle 作为序列化器时，引发不可拾取异常的任务将无法正常工作。

为确保异常是可被处理的，异常必须要在 .args 属性中提供初始化的参数。最简单的方法就是使用异常调用 ``Exception.__init__``

让我们来看一些有用的例子，还有一个不适用的例子::

  # OK:
  class HttpError(Exception):
      pass

  # BAD:
  class HttpError(Exception):

      def __init__(self, status_code):
          self.status_code = status_code

  # OK:
  class HttpError(Exception):

      def __init__(self, status_code):
          self.status_code = status_code
          Exception.__init__(self, status_code)  # <-- REQUIRED

所以规则是：对于任何支持自定义参数 ``*args`` 的异常，都必须使用 ``Exception.__init__(self, *args)``

关键字参数没有特殊支持，如果需要保存关键字参数，当异常被 unpickled 时，需要将它们作为普通的参数进行传递::

  class HttpError(Exception):

      def __init__(self, status_code, headers=None, body=None):
          self.status_code = status_code
          self.headers = headers
          self.body = body

          super(HttpError, self).__init__(status_code, headers, body)



