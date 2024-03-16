=============================
PositiveBigIntegerField
=============================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


New in Django 3.1.

就像一个 PositiveIntegerField，但只允许在某一特定点下的值（依赖于数据库）。
0 到 9223372036854775807 的值在 Django 支持的所有数据库中都是安全的::

  class PositiveBigIntegerField(**options)


