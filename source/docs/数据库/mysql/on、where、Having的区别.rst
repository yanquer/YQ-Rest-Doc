
===========================
on、where、Having的区别
===========================

.. note::

  连接查询参考: :doc:`/docs/数据库/mysql/表内外连接`

WHERE与HAVING
===========================

- WHERE子句在GROUP BY分组和聚合函数之前对数据行进行过滤；
- HAVING子句对GROUP BY分组和聚合函数之后的数据行进行过滤。

因此，WHERE子句中不能使用聚合函数。例如，以下语句将会返回错误::

  -- 查找人数大于 5 的部门
  select dept_id, count(*)
  from employee
  where count(*) > 5
  group by dept_id;

因为在执行WHERE子句时，还没有计算count

另一方面，HAVING子句中不能使用除了分组字段和聚合函数之外的其他字段。例如，以下语句将会返回错误::

  -- 统计每个部门月薪大于等于 30000 的员工人数
  select dept_id, count(*)
  from employee
  group by dept_id
  having salary >= 30000;

因为经过GROUP BY分组和聚合函数之后，不再存在 salary 字段，HAVING子句中只能使用分组字段或者聚合函数

从性能的角度来说，HAVING子句中如果使用了 **分组字段** 作为过滤条件，应该替换成WHERE子句；
因为WHERE可以在执行分组操作和计算聚合函数之前过滤掉不需要的数据，性能会更好。
下面示例中的语句 1 应该替换成语句 2::

  -- 语句 1
  select dept_id, count(*)
  from employee
  group by dept_id
  having dept_id = 1;

  -- 语句 2
  select dept_id, count(*)
  from employee
  where dept_id = 1
  group by dept_id;

当然，WHERE和HAVING可以组合在一起使用。例如::

  select dept_id, count(*)
  from employee
  where salary > 10000
  group by dept_id
  having count(*) > 1;

  dept_id|count(*)|
  -------|--------|
        1|       3|

该语句返回了月薪大于 10000 的员工人数大于 1 的部门；
WHERE用于过滤月薪大于 10000 的员工；HAVING用于过滤员工数量大于 1 的部门。

WHERE 与 ON
===========================

当查询涉及多个表的关联时，我们既可以使用WHERE子句也可以使用ON子句指定连接条件和过滤条件。这两者之间的主要区别在于：

- 对于内连接（inner join）查询，WHERE和ON中的过滤条件等效；
- 对于外连接（outer join）查询，ON中的过滤条件在连接操作之前执行，
  WHERE中的过滤条件（逻辑上）在连接操作之后执行。

条件查询内连接
---------------------------

对于内连接查询而言，以下三个语句的结果相同::

  -- 语句 1
  select d.dept_name, e.emp_name, e.sex, e.salary
  from employee e, department d
  where e.dept_id = d.dept_id
  and e.emp_id = 10;

  dept_name|emp_name|sex|salary |
  ---------|--------|---|-------|
  研发部   |廖化    |男  |6500.00|

  -- 语句 2
  select d.dept_name, e.emp_name, e.sex, e.salary
  from employee e
  join department d on (e.dept_id = d.dept_id and e.emp_id = 10);

  dept_name|emp_name|sex|salary |
  ---------|--------|---|-------|
  研发部   |廖化    |男  |6500.00|

  -- 语句 3
  select d.dept_name, e.emp_name, e.sex, e.salary
  from employee e
  join department d on (e.dept_id = d.dept_id)
  where e.emp_id = 10;

  dept_name|emp_name|sex|salary |
  ---------|--------|---|-------|
  研发部   |廖化    |男  |6500.00|

语句 1 在WHERE中指定连接条件和过滤条件；语句 2 在ON中指定连接条件和过滤条件；
语句 3 在ON中指定连接条件，在WHERE中指定其他过滤条件。
上面语句不但结果相同，数据库的执行计划也相同。以 MySQL 为例，以上语句的执行计划如下::

  id|select_type|table|partitions|type |possible_keys       |key    |key_len|ref  |rows|filtered|Extra|
  --|-----------|-----|----------|-----|--------------------|-------|-------|-----|----|--------|-----|
  1|SIMPLE     |e    |          |const|PRIMARY,idx_emp_dept|PRIMARY|4      |const|   1|     100|     |
  1|SIMPLE     |d    |          |const|PRIMARY             |PRIMARY|4      |const|   1|     100|     |

尽管如此，仍然建议将两个表的连接条件放在ON子句中，将其他过滤条件放在WHERE子句中；
这样语义更加明确，更容易阅读和理解。对于上面的示例而言，推荐使用语句 3 的写法。

条件查询外连接
---------------------------

对于外连接而言，连接条件只能用ON子句表示，因为WHERE子句无法表示外连接的语义。例如::

  select d.dept_name, e.emp_name, e.sex, e.salary
  from department d
  left join employee e on (e.dept_id = d.dept_id)
  where d.dept_name = '保卫部';

  dept_name|emp_name|sex|salary|
  ---------|--------|---|------|
  保卫部   |        |   |      |

由于“保卫部”没有员工，我们需要使用外连接返回部门的信息；
WHERE条件用于过滤 dept_id = 6 的数据；此时，员工表中返回的都是 NULL。

.. note::

  Oracle 支持在WHERE子句的右/左侧使用 (+) 表示左/右外连接，但是无法表示全外连接。

对于以上语句，如果将WHERE子句中的过滤条件放到ON子句中，结果将会完全不同::

  select d.dept_name, e.emp_name, e.sex, e.salary
  from department d
  left join employee e on (e.dept_id = d.dept_id and d.dept_name = '保卫部');

  dept_name|emp_name|sex|salary|
  ---------|--------|---|------|
  行政管理部|        |   |      |
  人力资源部|        |   |      |
  财务部   |        |   |      |
  研发部   |        |   |      |
  销售部   |        |   |      |
  保卫部   |        |   |      |

左外连接返回了所有的部门信息，而且员工信息都为 NULL；
显然，这不是我们期望的结果。我们可以通过执行计划分析一下为什么会这样，
仍然以 MySQL 为例::

  explain analyze
  select d.dept_name, e.emp_name, e.sex, e.salary
  from department d
  left join employee e on (e.dept_id = d.dept_id and d.dept_name = '保卫部');

  -> Nested loop left join  (cost=7.60 rows=30) (actual time=0.098..0.278 rows=6 loops=1)
      -> Table scan on d  (cost=0.85 rows=6) (actual time=0.052..0.057 rows=6 loops=1)
      -> Filter: (d.dept_name = '保卫部')  (cost=0.71 rows=5) (actual time=0.035..0.035 rows=0 loops=6)
          -> Index lookup on e using idx_emp_dept (dept_id=d.dept_id)  (cost=0.71 rows=5) (actual time=0.020..0.032 rows=4 loops=6)

查询计划显示使用 Nested loop left join 方式执行连接操作；
对于 department 使用全表扫描的方式返回 6 行记录；
对于 employee 表采用索引（idx_emp_dept）查找，
同时使用“d.dept_name = '保卫部'”作为过滤条件，循环 6 次返回了 0 行记录；
最终返回了上面的结果。

作为对比，我们可以看看将过滤条件放到WHERE子句时的执行计划::

  explain analyze
  select d.dept_name, e.emp_name, e.sex, e.salary
  from department d
  left join employee e on (e.dept_id = d.dept_id)
  where d.dept_name = '保卫部';

  -> Nested loop left join  (cost=1.98 rows=5) (actual time=0.074..0.078 rows=1 loops=1)
      -> Filter: (d.dept_name = '保卫部')  (cost=0.85 rows=1) (actual time=0.049..0.053 rows=1 loops=1)
          -> Table scan on d  (cost=0.85 rows=6) (actual time=0.039..0.047 rows=6 loops=1)
      -> Index lookup on e using idx_emp_dept (dept_id=d.dept_id)  (cost=1.12 rows=5) (actual time=0.021..0.021 rows=0 loops=1)

查询计划显示使用 Nested loop left join 方式执行连接操作；
对于 department 通过扫描返回 1 行记录（d.dept_name = '保卫部'）；
对于 employee 表采用索引（idx_emp_dept）查找，
同时使用 dept_id=d.dept_id 作为过滤条件，循环 1 次返回了 0 行记录。

.. note::

  一般来说，对于左外连接查询，左表的过滤应该使用WHERE子句，
  右表的过滤应该使用ON子句；右外连接查询正好相反；全外连接的过滤条件使用ON子句。

在使用jion时，on和where条件的区别如下：

- on 条件是在生成临时表时使用的条件，返回on条件匹配的记录。
- where 条件是在临时表生成好后，再对临时表进行过滤的条件。
  这时已经没有left join的含义（必须返回左边表的记录）了，条件不为真的就全部过滤掉。

on、where、having这三个都可以加在条件的子句中，on是最先执行，where次之，having最后。
  对于内连接，inner join（inner join即join）和 = 等号结果一样，但实现原理完全不同，
  join是基于hashtable连接比较，
  而=直接就是取笛卡尔集再过滤，所以后者效率低，是O(N^2)，前者是O(LogN)。

  .. note::

    笛卡尔集, 就是一个表的所有行跟另一个表的所有行全连接  

参考: `【MySQL】连接查询 以及 on、where、Having的区别 <https://www.cnblogs.com/birdy-silhouette/p/14011817.html>`_


