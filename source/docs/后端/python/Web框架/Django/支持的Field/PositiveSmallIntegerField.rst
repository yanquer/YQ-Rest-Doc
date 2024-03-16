============================
PositiveSmallIntegerField
============================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


就像一个 PositiveIntegerField，但只允许在某一特定（数据库依赖的）点下取值。0 到 32767 的值在 Django 支持的所有数据库中都是安全的::

  class PositiveSmallIntegerField(**options)

