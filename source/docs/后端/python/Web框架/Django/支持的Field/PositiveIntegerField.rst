========================
PositiveIntegerField
========================


就像 IntegerField 一样，但必须是正值或零（ 0 ）。
从 0 到 2147483647 的值在 Django 支持的所有数据库中都是安全的。出于向后兼容的原因，接受 0 的值::

  class PositiveIntegerField(**options)



