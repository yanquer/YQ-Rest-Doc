=============================
PositiveBigIntegerField
=============================

New in Django 3.1.

就像一个 PositiveIntegerField，但只允许在某一特定点下的值（依赖于数据库）。
0 到 9223372036854775807 的值在 Django 支持的所有数据库中都是安全的::

  class PositiveBigIntegerField(**options)


