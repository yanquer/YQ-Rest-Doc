==========================
UUIDField
==========================

一个用于存储通用唯一标识符的字段。使用 Python 的 UUID 类。当在 PostgreSQL 上使用时，它存储在一个 uuid 的数据类型中，否则存储在一个 char(32) 中::

  class UUIDField(**options)

通用唯一标识符是 primary_key 的 AutoField 的一个很好的替代方案。数据库不会为你生成 UUID，所以建议使用 default ::

  import uuid
  from django.db import models

  class MyUUIDModel(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      # other fields

请注意，一个可调用对象（省略括号）被传递给 default，而不是 UUID 的实例。

在 PostgreSQL 上查找
  在 PostgreSQL 上使用 iexact、contains、icontains、startswith、istartswith、endswith 或 iendswith 在 PostgreSQL
  上查找没有连字符的值是行不通的，因为 PostgreSQL 将它们存储在一个连字符的 uuid 数据类型中。



