===========================
doc可用于rst文本元素
===========================


.. post:: 2024-03-09 18:21:01
  :tags: rst标记语言, doc语法模块
  :category: 文档
  :author: YanQue
  :location: CD
  :language: zh-cn


这是按照指令分类

.. toctree::
  :maxdepth: 1

  Admonitions
  Images
  body-elements
  tables
  Document Parts
  Directives for Substitution Definitions
  Miscellaneous

Common Options
===========================

| 公共选项参数

- class		不知道有啥用
- name		设置方便引用

  如:

  .. code::

    .. image:: bild.png
      :name: my picture

    # 引用方式1
    .. _my picture:

    # 引用方式2
    .. image:: bild.png

参考: `docutils文档 <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_
