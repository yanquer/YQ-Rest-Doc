===========================
内部类Meta
===========================

可用的选项

abstract
  abstract = True，表示这是一个 :doc:`/docs/后端/python/Web框架/Django/抽象基类`
app_label
  如果在 INSTALLED_APPS 中定义了一个应用程序之外的模型，它必须声明它属于哪个应用程序::

    app_label = 'myapp'

  如果你想用 app_label.object_name 或 app_label.model_name 来表示一个模型，你可以分别使用::

    model._meta.label 或 model._meta.label_lower
db_table
  用于模型的数据库表的名称
base_manager_name
  管理器的属性名

  管理器的属性名，例如，'objects'，用于模型的 _base_manager。

  说实话 没懂
db_tablespace
  数据库表空间名称

  `表空间（Tablespaces） | Django 文档 | Django (djangoproject.com) <https://docs.djangoproject.com/zh-hans/3.2/topics/db/tablespaces/>`_
default_manager_name
  模型的管理器名称

  模型的 `_default_manager <https://docs.djangoproject.com/zh-hans/3.2/topics/db/managers/#django.db.models.Model._default_manager>`_ 管理器名称。
default_related_name
  从相关对象到这个对象的关系默认使用的名称。默认为 `_set`。

  这个选项还可以设置 `related_query_name <https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name>`_

  由于字段的反向名称应该是唯一的，所以如果你打算对你的模型进行子类化，就要小心了。
  为了避免名称冲突，名称的一部分应该包含 `'%(app_label)s'` 和 `'%(model_name)s'`，
  它们分别被模型所在的应用程序的名称和模型的名称所取代，都是小写的。
  见 `抽象模型的相关名称 <https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#abstract-related-name>`_ 段落。
get_latest_by
  模型中的字段名或字段名列表

  我的理解是 以这个字段集进行排序
managed
  默认为True，表示Django 管理 数据库表的生命周期。

  如果 False，将不对该模型进行数据库表的创建、修改或删除操作。
  如果该模型代表一个现有的表或一个通过其他方式创建的数据库视图，这一点很有用。
  这是在 managed=False 时 唯一 的区别。模型处理的所有其他方面都与正常情况完全相同。
order_with_respect_to
  使该对象可以根据给定字段（通常是 ForeignKey ）进行排序。
ordering
  对象的默认排序
permissions
  表的额外权限

  创建此对象时要输入权限表的额外权限。为每个模型自动创建添加、更改、删除和查看权限。
  这个例子指定了一个额外的权限，can_deliver_pizzas ::

    permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]

  这是一个由二元元组组成的列表或元组，格式为 (permission_code, human_readable_permission_name)。
default_permissions
  默认值为 ('add', 'change', 'delete', 'view') 。

  你可以自定义这个列表，例如，如果你的应用不需要任何默认的权限，可以将其设置为空列表。
  它必须在模型创建之前通过 migrate 在模型上指定，以防止任何遗漏的权限被创建。
proxy
  如果 `proxy = True`，作为另一个模型子类的模型将被视为 `代理模型 <https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#proxy-models>`_
required_db_features
  当前连接应具备的数据库特征列表，以便在迁移阶段考虑模型。
  例如，如果你将此列表设置为 ['gis_enabled']，则模型将只在支持 GIS 的数据库上同步。
  在使用多个数据库后端进行测试时，跳过一些模型也很有用。避免模型之间的关系，
  这些模型可能会被创建，也可能不会被创建，因为 ORM 不会处理这个问题。
required_db_vendor
  本模型所特有的支持的数据库厂商名称。目前的内置厂商名称是： `sqlite`，`postgresql`，`mysql` 和 `oracle`。
  如果该属性不为空，且当前连接厂商与之不匹配，则该模型将不会同步。
select_on_save
  确定 Django 是否会使用 1.6 之前的
  `django.db.models.Model.save() <https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#django.db.models.Model.save>`_ 算法.
  旧的算法使用 `SELECT` 来确定是否有一条现有的记录需要更新。
  新算法直接尝试 `UPDATE`。在一些罕见的情况下，Django 看不到现有行的 `UPDATE`。
  例如 PostgreSQL 的 `ON UPDATE` 触发器会返回 `NULL`。
  在这种情况下，即使数据库中存在一条记录，新算法最终也会进行 `INSERT`。

  通常不需要设置这个属性。默认值是 `False`。

  关于新旧保存算法，请参见 `django.db.models.Model.save() <https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#django.db.models.Model.save>`_
indexes
  定义索引列表

  如::

    from django.db import models

    class Customer(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)

        class Meta:
            indexes = [
                models.Index(fields=['last_name', 'first_name']),
                models.Index(fields=['first_name'], name='first_name_idx'),
            ]

unique_together
  一组字段名，组合起来必须是唯一的
index_together
  可以理解为联合索引
constraints
  表约束
verbose_name
  对象的注释 单数
verbose_name_plural
  对象的复数，默认是上一个加s
label
  对象的表示，返回 app_label.object_name，例如 'polls.Question'。
label_lower
  模型的表示，返回 app_label.model_name，例如 'polls.question'。




