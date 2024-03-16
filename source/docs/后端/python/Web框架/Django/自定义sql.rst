============================
自定义sql
============================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


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








