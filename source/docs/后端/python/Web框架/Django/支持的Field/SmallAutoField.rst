=============================
SmallAutoField
=============================

就像一个 AutoField，但只允许值在一定（依赖于数据库）的限制下。1 到 32767 的值在 Django 支持的所有数据库中都是安全的::

  class SmallAutoField(**options)



