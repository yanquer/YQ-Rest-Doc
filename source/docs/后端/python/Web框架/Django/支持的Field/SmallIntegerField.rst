===========================
SmallIntegerField
===========================

就像一个 IntegerField，但只允许在某一特定（依赖于数据库的）点下取值。从 -32768 到 32767 的值在 Django 支持的所有数据库中都是安全的::

  class SmallIntegerField(**options)





