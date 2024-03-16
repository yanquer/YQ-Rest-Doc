===============
Jinja2
===============


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


一个仿照 Django 的模版引擎, 安装::

  pip install Jinja2

加载模版::

  >>> from jinja2 import Template as T
  >>> t = T('ti is a test msg, say {{ msg }}')
  >>> t.render(msg='you say say you')
  'ti is a test msg, say you say say you'
  >>>

部分语法:

代码块::

  {% 代码块 %}

变量::

  {{ 变量 }}

注释::

  {# 注释 #}

行语句, 行内语句为 Python 代码::

  # 行语句

过滤器, 使用管道符号, 支持链式::

  {{ 变量 | 函数1 | 函数2 }}

一些预定义函数

字符串操作:

- safe, 禁用转义
- capitalize, 把变量值的首字母转成大写，其余字母转小写
- lower, 把值转成小写
- upper, 把值转成大写
- title, 把值中的每个单词的首字母都转成大写
- reverse, 字符串反转
- format, 格式化输出
- striptags, 渲染之前把值中所有的HTML标签都删掉
- truncate: 字符串截断

列表操作:

- first, 取第一个元素
- last, 取最后一个元素
- length, 获取列表长度
- sum, 列表求和
- sort, 列表排序

常用逻辑:

判断::

  {% if 条件 %}
    此处可以是html 代码
  {% endif %}

注意等价于::

  # if 条件
    此处可以是html 代码
  # endif

循环::

  {% for x in 列表 %}
    此处可以是html 代码
  {% endfor %}








