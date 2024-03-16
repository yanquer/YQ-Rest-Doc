===================================
settings常用字段
===================================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


TEMPLATES
  默认： `[]` （空列表）

  一个包含所有 Django 模板引擎的配置的列表。列表中的每一项都是一个字典，包含了各个引擎的选项。

  下面是一个配置，告诉 Django 模板引擎从每个安装好的应用程序中的 `templates` 子目录中加载模板::


    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
        },
    ]


  以下选项适用于所有后端。
BACKEND
  默认：未定义

  要使用的模板后端。内置的模板后端有：

  - `'django.template.backends.django.DjangoTemplates'`
  - `'django.template.backends.jinja2.Jinja2'`

  你可以通过将 `BACKEND` 设置为一个完全限定的路径（例如 `'mypackage.whatever.Backend'`）来使用一个不在 Django 中的模板后端。
NAME
  默认：见下方

  这个特定模板引擎的别称。它是一个标识符，允许选择一个引擎进行渲染。所有配置的模板引擎的别名必须是唯一的。

  它默认为定义引擎类的模块名称，即 `BACKEND` 的下一个到最后一个，如果没有提供的话。例如，如果后端是 `'mypackage.whatever.Backend'`，那么它的默认名称是 `'whatever'`。
DIRS
  默认： `[]` （空列表）

  按照搜索顺序，引擎应该查找模板源文件的目录。
APP_DIRS
  默认：`False`

  引擎是否应该在已安装的应用程序中查找模板源文件。

  .. note::

    默认的 `settings.py` 文件由 `django-admin startproject` 创建，设置 `'APP_DIRS': True`。
OPTIONS
  默认值： `{}` （空字典）

  要传递给模板后台的额外参数。根据模板后端的不同，可用的参数也不同。
  参见 `DjangoTemplates <https://docs.djangoproject.com/zh-hans/3.2/topics/templates/#django.template.backends.django.DjangoTemplates>`_
  和
  `Jinja2 <https://docs.djangoproject.com/zh-hans/3.2/topics/templates/#django.template.backends.jinja2.Jinja2>`_
  了解内置后端的选项



参考: `setting配置 <https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TEMPLATES>`_







