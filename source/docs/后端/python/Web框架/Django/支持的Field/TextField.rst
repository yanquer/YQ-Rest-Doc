=====================
TextField
=====================

一个大的文本字段。该字段的默认表单部件是一个 Textarea::

  class TextField(**options)

如果你指定了 max_length 属性，它将反映在自动生成的表单字段的 Textarea 部件中。
但是，它并没有在模型或数据库层面被强制执行。使用一个 CharField 来实现。

TextField.db_collation
  New in Django 3.2.

  该字段的数据库字符序名称。

.. note::

  字符序名称是不标准化的。因此，这将无法在多个数据库后端之间进行移植。

  Oracle
    Oracle 不支持 TextField 的字符序。



