============================
IntegerField
============================

一个整数。从 -2147483648 到 2147483647 的值在 Django 支持的所有数据库中都是安全的::

  class IntegerField(\*\*options)

它使用 MinValueValidator 和 MaxValueValidator 根据默认数据库支持的值来验证输入。

当 localize 为 False 时是 NumberInput 否则，该字段的默认表单部件是 TextInput。



