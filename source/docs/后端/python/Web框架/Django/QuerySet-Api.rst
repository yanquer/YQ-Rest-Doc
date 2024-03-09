===========================
QuerySet Api
===========================

包含两个公开属性：

- ordered：查询时候是否有序（True/False）
- db：查询时使用的数据库

模型.objects的一些方法
===========================

每次执行都是返回一个新的QuerySet()

总览::

  module.objects.all() 获取该实例的所有信息
  module.objects.add() 添加
  module.objects.create() 创建
  module.objects.get()
  module.objects.filter(*kargs)	过滤器 返回包含指定参数的QuerySet，底层通过AND连接多个参数
  module.objects.exclude(*kargs)	返回不包含指定参数的QuerySet，底层是用NOT()包裹的AND
  module.objects.annotate()	聚合查询，对QuerySet的每个对象进行注解
  module.objects.order_by() 排序
  module.objects.annotate()
  module.objects.alias()	对QuerySet的每个字段设置别名，相当于as（没搞懂）
  module.objects.select_related()	会获取外键对应的对象，在需要的时候就不用重新查询数据库了（主要用于一对多字段的查询）
  module.objects.prefetch_related()	多对多字段的查询（通过外键所对应实体找外键所在实体），底层使用的in
  module.objects.reverse()	反向查询
  module.objects.distinct( \*fields )	反向查询
  module.objects.values()	返查询字典而不是实例
  module.objects.defer()	单次加载时，指定不加载指定的字段，后续是需要时再加载
  module.objects.only()	单次加载时，指定加载指定的字段，未指定的需要再加载
  module.objects.extra()

所有查询操作参考: `<https://www.liujiangblog.com/course/django/129>`_

module.objects.all()
  获取该实例的所有信息

  注意::

    Entry.objects.filter(pub_date__year=2006)

  等价于::

    Entry.objects.all().filter(pub_date__year=2006)
module.objects.add()
  添加
module.objects.create()
  创建
module.objects.get()
  获取
module.objects.filter(\*kargs)
  过滤器 返回包含指定参数的QuerySet，底层通过AND连接多个参数

  如果是多个filter，那么这些filter的链之间是或的关系（or）
module.objects.exclude(\*kargs)
  返回不包含指定参数的QuerySet，底层是用NOT()包裹的AND
module.objects.annotate()
  聚合查询，对QuerySet的每个对象进行注解
module.objects.order_by()
  排序
module.objects.alias()
  对QuerySet的每个字段设置别名

  好像相当于as（没搞懂）
module.objects.select_related()
  会获取外键对应的对象，

  在需要的时候就不用重新查询数据库了（主要用于一对多字段的查询）
module.objects.prefetch_related()
  多对多字段的查询

  (通过外键所对应实体找外键所在实体)，底层使用的in
module.objects.reverse()
  反向查询
module.objects.distinct(\*fields )
  反向查询
module.objects.values()
  反查询字典而不是实例

  注意values与distinct使用会影响排序结果
module.objects.defer()
  返回对象实例，指定不加载字段

  单次加载时，指定不加载指定的字段，后续是需要时再加载
module.objects.only()
  返回对象实例，指定加载字段

  单次加载时，指定加载指定的字段，未指定的需要再加载

  多个链式的only，只会以最后一个为准::

    > 比如:ret=Book.object.all().only('name')
    >         id始终会查,结果是queryset对象,套book对象(里面只有id与name字段)
    >         问:如果取price,发生了什么?
    >         它会再次查询数据库,对数据库造成压力
extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
  有时候，Django 查询语法本身并不能很容易地表达一个复杂的 WHERE 子句。
  对于这些边缘情况，Django 提供了 extra() QuerySet 修饰符——用于将特定的子句注入到由 QuerySet 生成的 SQL 中。

  如果在 extra() 调用之后使用 values() 子句，
  则 extra() 中的 select 参数所定义的任何字段必须明确地包含在 values() 调用中。
  任何在 values() 调用之后进行的 extra() 调用将忽略其额外选择的字段。

  官网文档说计划 extra将在未来废弃

filter/other
===========================

过滤后的QuerySet都是唯一的

前缀为变量或者说字段名

后缀如下：

- `__gt` : 大于
- `__gte` : 大于等于
- `__lt` : 小于
- `__lte` : 小于等于
- `__in` : 其中之一
- `__range` : 范围
- `__year` : 日期-年

- `__exact`：“精确”匹配（区分大小写）

- `__iexact`：是不区分大小写的匹配项

- `__contains`：区分大小写的模糊查询

- `__icontains`：不区分大小写的模糊查询，与`contains`相对应。
- `__startswith`：以什么开头的模糊查询（**区分大小写**）
- `__istartswith`：以什么开头的模糊查询（**不区分大小写**）
- `__endswith`：以什么结尾的模糊查询（**区分大小写**）
- `__iendswith`：以什么结尾的模糊查询（**不区分大小写**）
- `__isnull` : 是空的
- `__regex` : 区分大小写的正则匹配
- `__iregex` : 不区分大小写的正则匹配







