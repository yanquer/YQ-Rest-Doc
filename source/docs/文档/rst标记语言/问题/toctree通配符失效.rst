==================================
toctree通配符失效
==================================

toctree有一个glob属性, 需要指定才可以使用通配符::

  .. toctree::
    :glob:

    xxx/*

官文原文说明::

  You can use "globbing" in toctree directives, by giving the glob flag option.
  All entries are then matched against the list of available documents, and matches are inserted into the list alphabetically. Example:

  .. toctree::
    :glob:

    intro*
    recipe/*
    *

使用此属性, 将匹配, 按结果字母顺序列出.

