===========================
doc可用于rst文本元素
===========================

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
