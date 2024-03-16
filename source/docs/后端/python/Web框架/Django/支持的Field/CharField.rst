=============================
CharField
=============================


.. post:: 2023-02-20 22:18:59
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


一个字符串字段，适用于小到大的字符串。

对于大量的文本，使用 :doc:`/docs/后端/python/Web框架/Django/支持的Field/TextField`

该字段的默认表单部件是一个 TextInput。

CharField 有两个额外的参数：

CharField.max_length
  必须的。该字段的最大长度（以字符为单位）。
  max_length 在数据库层面强制执行，在 Django 的验证中使用 MaxLengthValidator。

