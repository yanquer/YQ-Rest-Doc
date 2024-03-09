==============================
DurationField
==============================


一个用于存储时间段的字段——在 Python 中用 timedelta 建模。
当在 PostgreSQL 上使用时，使用的数据类型是 interval，
在 Oracle 上使用的数据类型是 INTERVAL DAY(9) TO SECOND(6)。否则使用微秒的 bigint::

  class DurationField(**options)

.. note::

  DurationField 的算术在大多数情况下是可行的。
  但在 PostgreSQL 以外的所有数据库中，将 DurationField 的值与 DateTimeField 实例上的算术进行比较，将无法达到预期的效果。


