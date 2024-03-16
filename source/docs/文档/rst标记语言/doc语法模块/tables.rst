=================================
tables
=================================


.. post:: 2023-03-01 00:19:35
  :tags: rst标记语言, doc语法模块
  :category: 文档
  :author: YanQue
  :location: CD
  :language: zh-cn


参考: `<https://docutils.sourceforge.io/docs/ref/rst/directives.html#tables>`_

table
=================================

表格

支持命令选项:

align: "left", "center", or "right"
  水平对齐方式
width: length or percentage
  将表的宽度设置为指定长度或行宽度的百分比。如果省略，渲染器将根据其内容或列宽度来确定表的宽度。
widths: "auto", "grid", or a list of integers
  明确设置列宽度。如果与宽度选项一起使用，则指定相对宽度。覆盖table_style设置或类值“colwidths-auto”。默认值取决于table_style配置设置。

  “auto”将列宽度的确定委托给后端（LaTeX，HTML浏览器，...）。默认Html5

  “grid”根据输入列的宽度（以字符为单位）确定列宽度。这个没怎么懂.

源码::

  .. table:: Truth table for "not"
    :width: 30%

    =====  =====
      A    not A
    =====  =====
    False  True
    True   False
    =====  =====

**效果**

.. table:: Truth table for "not"
   :width: 30%

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

csv-table
=================================

以csv（逗号分隔值）数据的形式写表格.

- 支持单元格内的块标记和内联标记。线端在单元格中被识别。

- 不支持检查每行中的列数是否相同。该指令会自动在短行末尾添加空条目。

支持命令选项:

align: "left", "center", or "right"
  水平布局方式
delim: char , "tab" , "space"
  表格列分隔符, 默认逗号, 可自定义为冒号等
encoding: string
  若使用url或者csv文件的数据, 用什么编码解析, 默认使用文件输出编码
escape: char
  将使用的分隔符转义为普通符号, 默认是双引号
  如:

    - 一列(这里双双引号最终是一对双引号)
      "He said, ""Hi!"""
    - 两列(双引号不会被输出)
      -M, "move/rename a branch, even if target exists"

file: string (newlines removed)
  引用本地csv文件的路径
header: CSV data
  表格头定义, 需要在 header-rows 之前
header-rows:  integer
  除了header定义的表头, 数据主体还有几行是表头, 默认0.
keepspace: flag (empty)
  将分隔符后面的空格视为显著的(将空格输出)。默认情况下是忽略此类空格。
quote: char
  一个字符字符串，用于引用包含分隔符或以引号字符开头的元素。默认为“（引用）。可以指定为Unicode代码点；有关语法详细信息，请参阅unicode指令。
stub-columns: integer
  用作存根的表列数量（左侧的行标题）。默认为0。
url: string (whitespace removed)
  一个CSV数据表格的链接.
widths: integer [integer...] or "auto"
  相对列宽度列表。默认值为等宽度列（100%/#columns）。

  “auto”将列宽度的确定委托给后端（LaTeX，HTML浏览器，...）。

width: length or percentage
  将表的宽度设置为指定长度或行宽度的百分比。如果省略，渲染器将根据其内容或列宽度来确定表的宽度。

.. warning::

  “Csv-table”指令的“:file:”和“:url:”选项代表了潜在的安全漏洞。它们可以通过“file_insertion_enabled”运行时设置禁用。

源码::

  .. csv-table:: Frozen Delights!
    :header:
      "Treat", "Quantity", "Description"
      "Treat2", "Quantity2", "Description2"
    :widths: 15, 10, 30
    :header-rows: 1

    "Albatross", 2.99, "On a stick!"
    "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
    crunchy, now would it?"
    "Gannet Ripple", 1.99, "On a stick!"

**效果**

.. csv-table:: Frozen Delights!
  :header:
    "Treat", "Quantity", "Description"
    "Treat2", "Quantity2", "Description2"
  :widths: 15, 10, 30
  :header-rows: 1

  "Albatross", 2.99, "On a stick!"
  "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
  crunchy, now would it?"
  "Gannet Ripple", 1.99, "On a stick!"

list-table
=================================

以列表的形式创建表格, 注意保持元素列一致

支持的命令选项:

align: "left", "center", or "right"
  水平对其方式
header-rows: integer
  表头行数
stub-columns: integer
  用作存根的表列数量（左侧的行标题）。默认为0。
width: length or percentage
  将表的宽度设置为指定长度或行宽度的百分比。如果省略，渲染器将根据其内容或列宽度来确定表的宽度。
widths: integer [integer...] or "auto"
  相对列宽度列表。默认值为等宽度列（100%/#columns）。

  “auto”将列宽度的确定委托给后端（LaTeX，HTML浏览器，...）。

源码::

  .. list-table:: Frozen Delights!
    :widths: 15 10 30
    :header-rows: 1
    :stub-columns: 1

    * - Treat
      - Quantity
      - Description
    * - Albatross
      - 2.99
      - On a stick!
    * - Crunchy Frog
      - 1.49
      - If we took the bones out, it wouldn't be
      crunchy, now would it?
    * - Gannet Ripple
      - 1.99
      - On a stick!

**效果**

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1
   :stub-columns: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

