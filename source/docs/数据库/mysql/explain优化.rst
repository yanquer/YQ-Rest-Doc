==================================
explain 优化
==================================

explain 查询优化神器

EXPLAIN语句的基本语法如下::

  explain select select_option

select_options是SELECT语句的查询选项，包括FROM WHERE子句等

输出结果列选项含义:

id
  SELECT识别符.
  这是SELECT的查询序列号, 表示查询中执行select子句或操作表的顺序,
  id相同，执行顺序从上到下, id不同，id值越大执行优先级越高;
select_type
  表示SELECT语句的类型.

  它可以是以下几种取值：

  - SIMPLE:表示简单查询，其中不包括连接查询和子查询；
  - PRIMARY:表示主查询，或者是最外层的查询语句，最外层查询为PRIMARY，也就是最后加载的就是PRIMARY；
  - UNION:表示连接查询的第2个或后面的查询语句， 不依赖于外部查询的结果集
  - DEPENDENT UNION:连接查询中的第2个或后面的SELECT语句，依赖于外面的查询；
  - UNION RESULT:连接查询的结果；
  - SUBQUERY:子查询中的第1个SELECT语句；不依赖于外部查询的结果集
  - DEPENDENT SUBQUERY:子查询中的第1个SELECT，依赖于外面的查询；
  - DERIVED:导出表的SELECT（FROM子句的子查询）,MySQL会递归执行这些子查询，把结果放在临时表里。
  - DEPENDENT DERIVED:派生表依赖于另一个表
  - MATERIALIZED:物化子查询
  - UNCACHEABLE SUBQUERY:子查询，其结果无法缓存，必须针对外部查询的每一行重新进行评估
  - UNCACHEABLE UNION:UNION中的第二个或随后的 select 查询，属于不可缓存的子查询
table
  表示查询的表
partitions
  查询将从中匹配记录的分区。该值适用NULL于未分区的表
type
  表示表的连接类型

  - system: 该表是仅有一行的系统表。这是const连接类型的一个特例
  - const: 数据表最多只有一个匹配行，它将在查询开始时被读取，并在余下的查询优化中作为常量对待。
    const表查询速度很快，因为只读取一次,const用于使用常数值比较PRIMARY KEY或UNIQUE索引的所有部分的场合。
  - eq_ref:对于每个来自前面的表的行组合，从该表中读取一行,
    可以用于使用=运算符进行比较的索引列 .
    比较值可以是常量，也可以是使用在此表之前读取的表中列的表达式
  - ref:对于来自前面的表的任意行组合，将从该表中读取所有匹配的行，ref可以用于使用“＝”或“＜＝＞”操作符的带索引的列。
  - fulltext:使用FULLTEXT 索引执行联接
  - ref_or_null:这种连接类型类似于ref，但是除了MySQL还会额外搜索包含NULL值的行。此联接类型优化最常用于解析子查询
  - index_merge:此联接类型指示使用索引合并优化。在这种情况下，key输出行中的列包含使用的索引列表，并key_len包含使用的索引 的最长键部分的列表
  - unique_subquery:类型替换 以下形式的eq_ref某些 IN子查询,unique_subquery 只是一个索引查找函数，它完全替代了子查询以提高效率。
  - index_subquery:连接类型类似于 unique_subquery。它代替IN子查询,但只适合子查询中的非唯一索引
  - range:只检索给定范围的行，使用一个索引来选择行。key列显示使用了哪个索引。key_len包含所使用索引的最长关键元素。当使用＝、＜＞、＞、＞＝、＜、＜＝、IS NULL、＜＝＞、BETWEEN或者IN操作符用常量比较关键字列时，类型为range
  - index:该index联接类型是一样的 ALL，只是索引树被扫描。这发生两种方式：1、如果索引是查询的覆盖索引，并且可用于满足表中所需的所有数据，则仅扫描索引树。在这种情况下，Extra列显示为 Using index，2、使用对索引的读取执行全表扫描，以按索引顺序查找数据行。 Uses index没有出现在 Extra列中。
  - ALL:对于前面的表的任意行组合进行完整的表扫描
possible_keys
  指出MySQL能使用哪个索引在该表中找到行.
  若该列是NULL，则没有相关的索引.
  在这种情况下，可以通过检查WHERE子句看它是否引用某些列或适合索引的列来提高查询性能.
  如果是这样，可以创建适合的索引来提高查询的性能。
kye
  表示查询实际使用的索引，如果没有选择索引，该列的值是NULL.
  要想强制MySQL使用或忽视possible_keys列中的索引，在查询中使用FORCE INDEX、USE INDEX或者IGNORE INDEX
key_len
  表示MySQL选择的索引字段按字节计算的长度，若键是NULL，则长度为NULL.
  注意，通过key_len值可以确定MySQL将实际使用一个多列索引中的几个字段
ref
  表示使用哪个列或常数与索引一起来查询记录。
rows
  显示MySQL在表中进行查询时必须检查的行数。
Extra
  表示MySQL在处理查询时的详细信息

参考: `MySQL索引原理及慢查询优化 <https://tech.meituan.com/2014/06/30/mysql-index.html>`_



