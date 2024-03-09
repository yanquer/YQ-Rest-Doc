==================================
关键字-truncate
==================================

truncate
==================================

truncate使用语法

truncate的作用是清空表或者说是截断表，只能作用于表。
truncate的语法很简单，后面直接跟表名即可，例如::

	truncate table tbl_name 或者 truncate tbl_name 。

执行truncate语句需要拥有表的drop权限，从逻辑上讲，
truncate table类似于delete删除所有行的语句
或 drop table 然后再 create table 语句的组合。

为了实现高性能，它绕过了删除数据的DML方法，因此，它不能回滚。
尽管truncate table与delete相似，但它被分类为DDL语句而不是DML语句。

truncate与drop,delete的对比
==================================

上面说过truncate与delete，drop很相似，其实这三者还是与很大的不同的，下面简单对比下三者的异同。

- truncate与drop是DDL语句，执行后无法回滚；
	delete是DML语句，可回滚。
- truncate只能作用于表；delete，drop可作用于表、视图等。
- truncate会清空表中的所有行，但表结构及其约束、索引等保持不变；
	drop会删除表的结构及其所依赖的约束、索引等。
- truncate会重置表的自增值；delete不会。
- truncate不会激活与表有关的删除触发器；delete可以。
- truncate后会使表和索引所占用的空间会恢复到初始大小；
	delete操作不会减少表或索引所占用的空间，drop语句将表所占用的空间全释放掉。

truncate使用场景及注意事项
==================================

通过前面介绍，我们很容易得出truncate语句的使用场景，即该表数据完全不需要时可以用truncate。

- 如果想删除部分数据用delete，注意带上where子句；
- 如果想删除表，当然用drop；
- 如果想保留表而将所有数据删除且和事务无关，用truncate即可；
- 如果和事务有关，或者想触发trigger，还是用delete；
- 如果是整理表内部的碎片，可以用truncate然后再重新插入数据。

无论怎样，truncate表都是高危操作，特别是在生产环境要更加小心，下面列出几点注意事项，希望大家使用时可以做下参考。

- truncate无法通过binlog回滚。
- truncate会清空所有数据且执行速度很快。
- truncate不能对有外键约束引用的表使用。
- 执行truncate需要drop权限，不建议给账号drop权限。
- 执行truncate前一定要再三检查确认，最好提前备份下表数据。

