===========================
BooleanField
===========================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


一个 true／false 字段。

该字段的默认表单部件是 CheckboxInput，或者如果 null=True 则是 NullBooleanSelect。

当 Field.default 没有定义时，BooleanField 的默认值是 None。

