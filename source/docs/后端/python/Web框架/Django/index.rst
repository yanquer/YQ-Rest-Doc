===============================
Django
===============================


学习进度: `<https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/>`_
下的字段选项

`执行查询 | Django 文档 | Django (djangoproject.com) <https://docs.djangoproject.com/zh-hans/3.2/topics/db/queries/>`_


:参考::
  - `使用Django <https://docs.djangoproject.com/zh-hans/3.2/topics/>`_
  - `编写你的第一个 Django 应用，第 3 部分 <https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial03/>`_


.. toctree::
  :maxdepth: 1

  创建项目
  模型模块module
  自定义sql
  内部类Meta
  抽象基类
  后台管理模块admin
  settings常用字段
  应用打包
  测试
  QuerySet-Api
  FQ
  问题总结

模型类
===============================

方法

Model.save()
  `Model.save(force_insert=False, force_update=False, using=DEFAULT_DB_ALIAS, update_fields=None <https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#django.db.models.Model.save>`_

  For details on using the `force_insert` and `force_update` arguments,
  see `强制执行 INSERT 或 UPDATE <https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#ref-models-force-insert>`_ .
  Details about the `update_fields` argument can be found in the
  `指定要保存的字段 <https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#ref-models-update-fields>`_ section.

  如果你想自定义保存行为，你可以覆盖这个 `save()` 方法。
  更多细节请参见 `重写之前定义的模型方法 <https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#overriding-model-methods>`_


模型中的一些函数/方法

`__str__()`
  返回值表示这个对象的str
`get_absolute_url()`
  计算一个对象的url

  任何需要一个唯一url的都需要定义此方法


常用指令
===============================

常用指令::

  # 查看django位置
  python -c "import django; print(django.__path__)"

  # 打开django自带的命令行工具
  python manage.py shell

  # 启动 polls应用的自动化测试
  python manage.py test polls

  # 创建 django 项目
  $ django-admin startproject $pro

  # 安装模块app
  $ python manage.py startapp $app

  # 启动服务
  $ python manage.py runserver 0:8000

  # 查找所有可用的模型 为任意一个在数据库中不存在对应数据表的模型创建迁移脚本文件
  $ python manage.py makemigrations

  # 运行这些迁移来自动创建数据库表
  #  migrate 命令只会为在 INSTALLED_APPS 里声明了的应用进行数据库迁移。
  $ python manage.py migrate

  # 创建某个app的表结构
  $ python manage.py makemigrations $app
  $ python manage.py migrate

  # 含 django 的环境变量shell
  $ python manage.py shell

url path 四个参数::

  # view 可以是 使用 include() 使用其他的app下的url
  # name 别名
  path('route', view.fun, name='')

创建管理员用户::

  $ python manage.py createsuperuser
  Username: admin
  Email address: admin@example.com
  Password: **********
  Password (again): *********
  Superuser created successfully.

数据库的设置 setting.py::

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'mydatabase',
          'USER': 'mydatabaseuser',
          'PASSWORD': 'mypassword',
          'HOST': '127.0.0.1',
          'PORT': '5432',
      }
  }

默认的，Django 会在外键字段名后追加字符串 `"_id"` 。（同样，这也可以自定义。）


.. ### 附3：创建虚拟环境

.. 用于创建和管理虚拟环境的模块称为[venv](https://docs.python.org/3/library/venv.html#module-venv)。[ venv](https://docs.python.org/3/library/venv.html#module-venv)通常会安装您可用的最新版本的Python。如果您的系统上有多个版本的Python，则可以通过运行或所需的任何版本来选择特定的Python版本。`python3`

.. 要创建虚拟环境，请确定要放置它的目录，然后将[venv](https://docs.python.org/3/library/venv.html#module-venv)模块作为脚本运行


.. # 创建环境位置 常用 .开始，以区分环境变量
.. python3 -m venv $mydir

.. 启动

.. # 如果是windows
.. $mydir/scripts/activate.bat

.. # 如果是 linux
.. source $mydr/bin/activate

.. [使用虚拟工具安装包创建隔离的python环境](https://docs.python.org/3/tutorial/venv.html)


外键
===============================

pk就是primary key的缩写。通常情况下，一个模型的主键为“id”，所以下面三个语句的效果一样::

  > Blog.objects.get(id__exact=14) # Explicit form
  > Blog.objects.get(id=14) # __exact is implied
  > Blog.objects.get(pk=14) # pk implies id__exact

参考: `查询操作 <https://www.liujiangblog.com/course/django/129>`_

web的瓶颈
===============================

1. 单个请求里太多sql串行查询导致耗时长
2. 单个sql太过复杂导致耗时长

