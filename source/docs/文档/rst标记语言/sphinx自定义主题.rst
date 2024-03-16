===============================
sphinx自定义主题
===============================


.. post:: 2023-02-20 22:06:49
  :tags: rst标记语言
  :category: 文档
  :author: YanQue
  :location: CD
  :language: zh-cn


:日期: 2023.02.24 周五
:参考: `主题开发 <https://www.sphinx-doc.org/zh_CN/master/development/theming.html>`_

主题目录大概结构::

    .
    ├── __init__.py
    ├── breadcrumbs.html
    ├── footer.html
    ├── layout.html
    ├── search.html
    ├── searchbox.html      以上几个html文件都是html模版
    ├── static              静态资源路径
    └── theme.conf          主题配置, ini配置形式

theme.conf 配置
===============================

:inherit:
    继承哪个主题, 主要用于查找缺失的模版
:stylesheet:
    main CSS name
:pygments_style:
    待补充
:sidebars:
    提供了用逗号分隔的侧边栏模板列表，用于构造提要栏。可以配置 ``html_sidebars`` 覆盖此值.


`[options]` 模块用于配置变量的值, 此处设置的值可以被 config.py 定义的 ``html_theme_options`` 覆盖.

如::

    [theme]
    inherit = base theme
    stylesheet = main CSS name
    pygments_style = stylename
    sidebars = localtoc.html, relations.html, sourcelink.html, searchbox.html

    [options]
    variable = default value


配置静态资源
===============================

默认情况下, static 目录下的文件会被复制到 _static

若需要使用其他目录下的文件, 可参考此方法::

    from os import path
    from sphinx.util.fileutil import copy_asset_file

    def copy_custom_files(app, exc):
        if app.builder.format == 'html' and not exc:
            staticdir = path.join(app.builder.outdir, '_static')
            copy_asset_file('path/to/myextension/_static/myjsfile.js', staticdir)

    def setup(app):
        app.connect('build-finished', copy_custom_files)


模版使用自定义函数
===============================

例, 定义函数::

    # 注册方法
    def setup_my_func(app, pagename, templatename, context, doctree):
        # 模版使用的方法
        def my_func(mystring):
            return "Your string is %s" % mystring
        # 注册到上下文
        context['my_func'] = my_func

    # 配置
    def setup(app):
        app.connect("html-page-context", setup_my_func)

在模版中使用::

    <div>
    {{ my_func("some string") }}
    </div>

基于配置的js脚本
===============================

方案一, 使用js_t模版
-------------------------------

在 static 目录下配置js模版(以 js_t 为后缀的文件), 此文件最后将会转换为 _static 目录下去掉 _t 后的js文件

如::

     project/static/test.js_t -> project/_buid/html/_static/test.js

.. note::

    本来就是js文件的会原样复制

方案二, 使用python函数配置
-------------------------------

使用 Sphinx.add_js_file() , 需要先在 config.py 配置变量

如, 在 config 配置了变量 my_javascript_variable, 使用以下方式注入 ::

    # 读取变量插入到js文件
    def add_js_variable(app):
        # This is a configuration that you've specified for users in `conf.py`
        js_variable = app.config['my_javascript_variable']
        js_text = "var my_variable = '%s';" % js_variable
        app.add_js_file(None, body=js_text)

    # builder初始化后 执行此方法
    def setup(app):
        # 注入配置变量
        app.add_config_value('my_javascript_variable', 0, 'html')
        # Run the function after the builder is initialized
        app.connect('builder-inited', add_js_variable)

.. function:: Sphinx.add_js_file(js_file, text)

    在文件js_file的头部插入 text, 一般为js代码

    如果 js_file 为 None, 将会插入到主页面的头部


.. note::

    如果自定义的js文件报错可能会使用基础模版的js

