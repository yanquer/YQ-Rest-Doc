================================
F Q
================================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


F
================================

F支持表内部字段的比较
--------------------------------

单下划线

例如，为了查找comments数目多于pingbacks数目的Entry，
可以构造一个F()对象来引用pingback数目，并在查询中使用该F()对象：

Entry有两个字段 number_of_comments，number_of_pingbacks::

  > from django.db.models import F
  > Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
  >

ps： 也支持加减乘除
如：查询rating比pingback和comment数目总和要小的Entry，可以这么写::

  > Entry.objects.filter(rating__lt=F('number_of_comments') + F('number_of_pingbacks'))

F支持跨表查询
--------------------------------

双下划线

在F()中使用双下划线来进行跨表查询。例如，查询author的名字与blog名字相同的Entry::

  > Entry.objects.filter(authors__name=F('blog__name'))

F，更新时用于获取原来的值
--------------------------------

如::

  from django.db.models import F,Q
  models.UserInfo.objects.all().update(age=F("age")+1)

Q，用于构造复杂查询条件
================================

应用一::

  models.UserInfo.objects.filter(Q(id__gt=1))
  models.UserInfo.objects.filter(Q(id=8) | Q(id=2))
  models.UserInfo.objects.filter(Q(id=8) & Q(id=2))

应用二::

  q1 = Q()
  q1.connector = 'OR'
  q1.children.append(('id__gt', 1))
  q1.children.append(('id', 10))
  q1.children.append(('id', 9))

  q2 = Q()
  q2.connector = 'OR'
  q2.children.append(('c1', 1))
  q2.children.append(('c1', 10))
  q2.children.append(('c1', 9))

  q3 = Q()
  q3.connector = 'AND'
  q3.children.append(('id', 1))
  q3.children.append(('id', 2))
  q2.add(q3,'OR')

  con = Q()
  con.add(q1, 'AND')
  con.add(q2, 'AND')

  models.UserInfo.objects.filter(con)










