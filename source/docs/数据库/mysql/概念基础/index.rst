===========================
mysql概念定义
===========================


关键字

.. toctree::
  :maxdepth: 1

  关键字
  关键字-truncate

数据类型

.. toctree::
  :maxdepth: 1

  数据类型VARCHAR和CHAR

基础

.. toctree::
  :maxdepth: 1

  函数API
  binlog
  SQL四种语言-DDL,DML,DCL,TCL
  存储过程
  触发器
  函数自定义


外键约束
===========================

外键约束（表2）对父表（表1）的含义:
  在父表上进行update/delete以更新或删除在子表中有一条或多条对应匹配行的候选键时，
  父表的行为取决于：在定义子表的外键时指定的on update/on delete子句。

含义

CASCADE
  删除包含与已删除键值有参照关系的所有记录
SET NULL
  修改包含与已删除键值有参照关系的所有记录，使用NULL值替换(只能用于已标记为NOT NULL的字段)
RESTRICT
  拒绝删除要求，直到使用删除键值的辅助表被手工删除，并且没有参照时(这是默认设置，也是最安全的设置)
NO ACTION
  啥也不做





