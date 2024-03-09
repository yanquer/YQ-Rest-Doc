=============================
DecimalField
=============================

一个固定精度的十进制数，在 Python 中用一个 Decimal 实例来表示。它使用 DecimalValidator 验证输入::

  class DecimalField(max_digits=None, decimal_places=None, **options)

有两个 必要的 参数：

DecimalField.max_digits
  数字中允许的最大位数。请注意，这个数字必须大于或等于 decimal_places。
DecimalField.decimal_places
  与数字一起存储的小数位数。

例如，如果要存储精度为小数点后两位的 999 的数字，你可以使用::

  models.DecimalField(..., max_digits=5, decimal_places=2)

并以 10 位小数的精度来存储最多约 10 亿的数字::

  models.DecimalField(..., max_digits=19, decimal_places=10)

当 localize 为 False 时是 NumberInput 否则，该字段的默认表单部件是 TextInput。

.. note::

  关于 FloatField 和 DecimalField 类之间差异的更多信息，请参见 FloatField vs. DecimalField。你还应该注意小数字段的 SQLite 限制。


