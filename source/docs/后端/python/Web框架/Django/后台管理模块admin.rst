==============================
后台管理模块admin
==============================

这里其实对应的就是 应用中的 admin.py

常用字段
==============================

例子::

  from django.contrib import admin

  from .models import Question


  class QuestionAdmin(admin.ModelAdmin):
      fieldsets = [
          (None,               {'fields': ['question_text']}),
          ('Date information', {'fields': ['pub_date']}),
      ]

  admin.site.register(Question, QuestionAdmin)

可以自行设置自定义的后台表单如例所示，自定义的类需要 register 在基类之后的类中字段定义方法

fields
  如::

    fields = ['pub_date', 'question_text']

  表示前台直接展示的字段以及顺序

  主要用于新增

fieldsets
  如::

    fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
        ]

  表示将这些字段分成几个字段集

  其中每个元组中第一个元素表示这个集的标题

  主要用于新增
list_display
  如::

    list_display = ('question_text', 'pub_date')

  表示在前台展示一个可视化的字段列表

  主要用于表格化的展示
list_filter
  如::

    list_filter = ['pub_date']

  表示允许在前端使用此字段的过滤选项（在侧边栏显示过滤选项）
search_fields
  如::

    search_fields = ['question_text']

  表示前端新增此字段的搜索框（后端将使用like查询）

自定义后台界面风格
==============================

通过 Django 的模板系统来修改

Django 的后台由自己驱动，且它的交互接口采用 Django 自己的模板系统。

- 在包含 manage.py 的工程目录内创建一个 templates 目录，放模板资源吧
- 在 settings.py 配置 DIRS选项

大致如下::

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]

TEMPLATES 作用
  包含所有 Django 模板引擎的配置的列表。列表中的每一项都是一个字典，包含了各个引擎的选项。

`DIRS <https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TEMPLATES-DIRS>`_
是一个包含多个系统目录的文件列表，用于在载入 Django 模板时使用，是一个待搜索路径。

:参考::
  - `自定义后台表单 <https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial07/>`_






