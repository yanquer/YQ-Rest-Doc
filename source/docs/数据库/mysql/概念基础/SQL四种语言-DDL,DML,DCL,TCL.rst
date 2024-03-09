============================================
SQL四种语言: DDL,DML,DCL,TCL
============================================

参考: `SQL四种语言：DDL,DML,DCL,TCL <https://www.cnblogs.com/henryhappier/archive/2010/07/05/1771295.html>`_

DDL(Data Definition Language)
  数据库定义语言(statements are used to define the database structure or schema.)

  DDL是 **SQL** 语言的四大功能之一。

  用于定义数据库的三级结构，
  包括外模式、概念模式、内模式及其相互之间的映像，定义数据的完整性、安全控制等约束

  .. DDL不需要commit:

  适用范围：对数据库中的某些对象(例如，database,table)进行管理，如::

    CREATE
    ALTER
    DROP
    TRUNCATE
    COMMENT
    RENAME

  举例,
  创建数据库::

    create database IF NOT EXISTS hncu CHARACTER SET utf8;

  创建表格::

    use hncu;
    create table IF NOT EXISTS stud(
    id int,
    name varchar(30),
    age int
    );

  更改表结构(设置约束)::

    desc stud; //查看表结构
    alter table stud drop column age;
    alter table stud add column age int;

  删除表、删除数据库::

    drop table stud;
    drop database hncu;

DML(Data Manipulation Language)
  数据操纵语言 (statements are used for managing data within schema objects.)

  由DBMS提供，用于让用户或程序员使用，实现对数据库中数据的操作。

  DML分成交互型DML和嵌入型DML两类。
  依据语言的级别，DML又可分成过程性DML和非过程性DML两种。

  .. DML需要commit

  适用范围：对数据库中的数据进行一些简单操作，如::

    SELECT
    INSERT
    UPDATE
    DELETE
    MERGE
    CALL
    EXPLAIN PLAN
    LOCK TABLE

  主要指数据的增删查改: Select/delete/update/insert/call ::

    select * from stud;
    select name,age from stud; //查询指定的列
    select name as 姓名, age as 年龄 from stud;


DCL(Data Control Language)
  数据库控制语言授权，角色控制等

  - GRANT 授权
  - REVOKE 取消授权

TCL(Transaction Control Language)
  事务控制语言

  - SAVEPOINT 设置保存点
  - ROLLBACK 回滚
  - SET TRANSACTION

SQL主要分成四部分
  - 数据定义。（SQL DDL）用于定义SQL模式、基本表、视图和索引的创建和撤消操作。
  - 数据操纵。（SQL DML）数据操纵分成数据查询和数据更新两类。数据更新又分成插入、删除、和修改三种操作。
  - 数据控制。包括对基本表和视图的授权，完整性规则的描述，事务控制等内容。
  - 嵌入式SQL的使用规定。涉及到SQL语句嵌入在宿主语言程序中使用的规则。







