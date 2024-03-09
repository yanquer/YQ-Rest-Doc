============================
自定义sql
============================

使用::

  Manager.raw(raw_query,params=(),translations=None)

如::

  >>> Person.objects.raw('''SELECT first AS first_name,
  ...                              last AS last_name,
  ...                              bd AS birth_date,
  ...                              pk AS id,
  ...                       FROM some_other_table''')

带参::

  >>> lname = 'Doe'
  >>> Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])

参考: `执行原生 SQL 查询 | Django 文档 | Django (djangoproject.com) <https://docs.djangoproject.com/zh-hans/3.2/topics/db/sql/>`_








