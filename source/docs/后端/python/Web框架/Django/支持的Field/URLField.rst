======================
URLField
======================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


URL 的 CharField，由 URLValidator 验证::

  class URLField(max_length=200, **options)

该字段的默认表单部件是一个 URLInput。

像所有的 CharField 子类一样， URLField 接受可选的 max_length 参数。如果你没有指定 max_length 参数，则使用默认的 200。




