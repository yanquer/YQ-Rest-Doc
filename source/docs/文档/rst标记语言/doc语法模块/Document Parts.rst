=====================================
Document Parts
=====================================


.. post:: 2023-02-27 21:24:23
  :tags: rst标记语言, doc语法模块
  :category: 文档
  :author: YanQue
  :location: CD
  :language: zh-cn


contents
=====================================

生成当前文档目录

支持命令选项

depth: integer
  目录深度, 默认不限制
local: flag (empty)
  生成本地目录。条目将仅包括提供小节(flag)的子节。如果没有给出显式标题，目录将不会有标题。
backlinks: "entry" or "top" or "none"
  从部分标题生成链接回到目录条目、目录本身，或不生成反向链接
class: text
  设置类属性

用例, 源码::

  .. contents:: Here's a very long Table of
    Contents AAAAAA

**效果**

.. contents:: Here's a very long Table of
   Contents AAAAAA



header / footer
=====================================

“标题”和“页脚”指令创建文档装饰，可用于页面导航、注释、时间/测试等。

例如::

  .. header:: This space for rent BBBBBBBB.

这将向文档标题添加一个段落，该段落将显示在生成的网页顶部或每个打印页面的顶部。

这些指令可以累计多次使用。目前只支持一个页眉和页脚。

.. warning::

  实际测试不适用于rst生成的文档, 无任何效果, 弃之.






