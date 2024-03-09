===========================
模型模块module
===========================

总览::

  module.objects.all() 获取该实例的所有信息
  module.objects.add() 添加
  module.objects.create() 创建
  module.objects.get()
  module.objects.filter(**kargs) 过滤器 返回包含指定参数的QuerySet
  module.objects.exclude(**kargs) 返回不包含指定参数的QuerySet
  module.objects.annotate()
  module.objects.order_by() 排序
  module.objects.annotate()
  module.objects.alias()

.. 关于filter/other

.. 过滤后的QuerySet都是唯一的

.. 前缀为变量或者说字段名

.. 后缀如下：

.. - `__gt` : 大于
.. - `__gte` : 大于等于
.. - `__lt` : 小于
.. - `__lte` : 小于等于
.. - `__in` : 其中之一
.. - `__range` : 范围
.. - `__year` : 日期-年

.. - `__exact`：“精确”匹配（区分大小写）

.. - `__iexact`：是不区分大小写的匹配项

.. - `__contains`：区分大小写的模糊查询

.. - `__icontains`：不区分大小写的模糊查询，与`contains`相对应。
.. - `__startswith`：以什么开头的模糊查询（**区分大小写**）
.. - `__istartswith`：以什么开头的模糊查询（**不区分大小写**）
.. - `__endswith`：以什么结尾的模糊查询（**区分大小写**）
.. - `__iendswith`：以什么结尾的模糊查询（**不区分大小写**）
.. - `__isnull` : 是空的
.. - `__regex` : 区分大小写的正则匹配
.. - `__iregex` : 不区分大小写的正则匹配

模型类
===========================

模型定义
---------------------------

每个模型都是python的一个类，且需继承 django.db.models.Model
类下每个属性都相当于一个数据库字段

每当新建一个模型的时候，都需要在 setting.py下的  INSTALL_APPS 配置，如
新建 app::

  python manage.py start myapp

配置app::

  INSTALL_APPS = [
    'myapp'
  ]

将变更好的内容写入数据库::

  # 查找所有可用的模型 为任意一个在数据库中不存在对应数据表的模型创建迁移脚本文件
  python manage.py makemigrations

  # 将变更写入数据库
  python manage.py migrate

模型中的字段类型
---------------------------

`<https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#model-field-types>`_

模型中的字段选项, 关于类中的字段,
每个字段都应该是 Field 类的实例

.. toctree::
  :glob:

  支持的Field/*

参考: `Django模型字段 <https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#model-field-types>`_



字段选项，部分解释
---------------------------

max_length
  指定该字段长度
db_index
  True表示将为此字段建索引
default
  该字段的默认值 。可以是可调用对象，但是默认不可变
primary_key
  为True时，表示将该字段设置为主键。同时表示 null=False 和 unique=True ,

  如果该模型中一个主键都没有设置，那么将会自动添加一个字段来设置主键。
  主键字段是只读的。如果改变了现有对象的主键值，然后将其保存，则会在旧对象旁边创建一个新对象。
verbose_name
  该字段的含义, 字段备注名（相当于给他一个注释）
unique
  设置为True，表示字段必须在整个表中保持值唯一。属于数据库级别和模型验证中强制执行。
unique_for_date
  将其设置为 DateField 或 DateTimeField 的名称，要求该字段的日期字段值是唯一的。
unique_for_month
  与上一个一致，区别为要求月份唯一
unique_for_year
  要求年份唯一
null
  如果设置为True，表示当该字段为空时，Django会将数据库中该字段设置为NULL。默认False
blank
  默认False。True表示该字段允许为空。

  与null的区别是，null仅表示数据库层面的空，而 blank涉及表单验证，为Flase表示表单该字段必填
db_column
  字段使用的数据库列名，未指定时使用数据库名
db_tablespace
  如果这个字段有索引，那么要为这个字段的索引使用的 数据库表空间 的名称。

  默认是项目的 DEFAULT_INDEX_TABLESPACE （如果有设置）,或者是模型的 db_tablespace （如果有）。
  如果后端不支持索引的表空间，则忽略此选项。

  这里其实没搞懂为啥索引也有表空间，搜了一下暂时没得到答案 `mysql的表空间使用 <https://blog.csdn.net/finalkof1983/article/details/83829341>`_

editable
  默认为True。 False表示该字段不会在管理或者任何其他地方中显示
error_messages
  覆盖该字段引发的默认消息。传入一个与你想覆盖的错误信息相匹配的键值的字典。

  这里也没懂啥意思 -_- ，可参考 `error_messages <https://docs.djangoproject.com/zh-hans/3.2/topics/forms/modelforms/#considerations-regarding-model-errormessages>`_

help_text
  额外的帮助文档，随表单控件一起显示。即便字段未用与表单，对于生成文档也可用。

  这个也没懂 ^_^
validators
  要为该字段运行的验证器列表。更多信息请参见 `验证器文档 <https://docs.djangoproject.com/zh-hans/3.2/ref/validators/>`_

  这个有点深，表示自定义验证机制
choices
  一系列二元数组，在表单上表示为选择框

  如，一个选项列表::

    from django.db import models

    class Person(models.Model):
        # 一个选项列表
        SHIRT_SIZES = (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
        )
        name = models.CharField(max_length=60)
        shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

  注意，当choices的顺序变动时，将创建新的迁移

  当代码包含此字段时，可以使用 ``get_定义值_dispaly`` 来获取响应的结果，如::

    >>> p = Person(name="Fred Flintstone", shirt_size="L")
    >>> p.save()
    >>> p.shirt_size
    'L'
    >>> p.get_shirt_size_display()
    'Large'
through
  仅用于多对多字段中, 指定使用哪个模型







