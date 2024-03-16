===========================
DateTimeField
===========================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


一个日期和时间，在 Python 中用一个 datetime.datetime 实例表示。与 DateField 一样，使用相同的额外参数::

  class DateTimeField(auto_now=False, auto_now_add=False, \*\*options)

该字段的默认表单部件是一个单独的 DateTimeInput。管理中使用两个单独的 TextInput 部件，并使用 JavaScript 快捷方式。

