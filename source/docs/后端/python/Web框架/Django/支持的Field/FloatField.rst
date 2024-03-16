===========================
FloatField
===========================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


在 Python 中用一个 float 实例表示的浮点数::

  class FloatField(**options)

当 localize 为 False 时是 NumberInput 否则，该字段的默认表单部件是 TextInput。

FloatField vs. DecimalField
  FloatField 类有时会与 DecimalField 类混淆。
  虽然它们都表示实数，但它们表示的方式不同。
  FloatField 内部使用 Python 的 float 类型，
  而 DecimalField 则使用 Python 的 Decimal 类型。关于两者之间的区别，请参见 Python 的 decimal 模块的文档。




