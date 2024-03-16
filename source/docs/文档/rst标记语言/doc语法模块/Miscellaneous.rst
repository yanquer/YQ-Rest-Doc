====================================
Miscellaneous
====================================


.. post:: 2023-02-27 21:24:23
  :tags: rst标记语言, doc语法模块
  :category: 文档
  :author: YanQue
  :location: CD
  :language: zh-cn


include
====================================

嵌入文件内容, 不建议使用. 见 `including-an-external-document-fragment <https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment>`_

.. warning::

  “include”指令代表一个潜在的安全漏洞。可以通过“file_insertion_enabled”运行时设置禁用它。

raw
====================================

raw也存在安全问题, 故不建议使用.

支持的命令选项:

file: string (newlines removed)
  本地文件路径
url: string (whitespace removed)
  文件网络路径
encoding: string
  文件读取格式, 默认输入文件格式

raw可以将内容转换对应的格式, 如html, 例:

源码::

  .. raw:: html

    <hr width=500 size=10 color=red>


**效果**

.. raw:: html

  <hr width=500 size=10 color=red>


