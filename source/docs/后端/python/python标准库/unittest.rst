===============
unittest
===============


.. post:: 2023-02-20 22:18:59
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


mock
===============

:官网文档::
  `unittest.mock-上手指南 <https://docs.python.org/zh-cn/3/library/unittest.mock-examples.html>`_

模拟方法调用, 比如测试的时候, 只想测试某一个类, 但是类有相关联的其他类, 那么可以使用 ``Mock()`` 来代替其他类.


记录一些坑
---------------

Can't pickle <class 'mock.Mock'>
+++++++++++++++++++++++++++++++++++

报错::

  pickle.PicklingError: Can't pickle <class 'mock.Mock'>: it's not the same object as mock.Mock

类似这种 pickle 序列化报错, 大部分是在 :doc:`/docs/后端/python/概念相关/多进程` 下进行测试而出现的序列化问题

但是这里是 Mock 本身的问题, 使用以下方式解决::

  class PickableMock(Mock):
    def __reduce__(self):
        return (Mock, ())

:可参考解决地址::
  `Can't pickle MagicMock or Mock #139 <https://github.com/testing-cabal/mock/issues/139>`_
