===================
高级Python
===================


.. post:: 2023-02-20 22:06:49
  :tags: python, 教程
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


主要对Python中支持的操作做一个归纳总结.

生成器效率高于推导式

字符串操作
===================

普通字符串, 直接使用内置的::

  split   转换为数组
  replace 替换字符
  find    查找字符位置

使用 :doc:`/docs/后端/python/python标准库/re` 模块::

  re.sub      使用正则替换
  re.match    从字符串开始匹配
  re.findall  查找所有匹配的字符串

注意:

- 使用正则时候的贪婪匹配与非贪婪匹配
- ``.`` 表示除换行外的任意字符
- ``()`` 表示分组
- ``?:``
- 大量匹配, 是用 ``re.compile`` 先预编译

元祖转换对象






