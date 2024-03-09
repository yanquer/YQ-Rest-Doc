=======================
binlog
=======================

binlog是Mysql sever层维护的一种二进制日志，
与innodb引擎中的redo/undo log是完全不同的日志；

其主要是用来记录对mysql数据更新或潜在发生更新的SQL语句，并以"事务"的形式保存在磁盘中；

作用主要有：

- 复制：MySQL Replication在Master端开启binlog，
  Master把它的二进制日志传递给slaves并回放来达到master-slave数据一致的目的
- 数据恢复：通过mysqlbinlog工具恢复数据
- 增量备份

Binlog 包括两类文件：

- 二进制日志索引文件(.index)：记录所有的二进制文件。
- 二进制日志文件(.00000*)：记录所有 DDL 和 DML 语句事件。

**redo log**
  保证一致性（将修改后的数据记录，当前语句）
**undo log**
  保证原子性（将修改前的数据记录，与当前语句相反的语句）

binlog的清除/不记录
=======================

不记录
  在 配置文件的 mysqld 下写入 skip-log-bin
清除
  **手动清理**,
  查看主从库使用的是哪个binlog文件::

    show master status;
    show slave status;

  删除之前可以先做个备份

  清除指定日期的备份::

    purge master logs before '2016-09-01 17:20:00'; //删除指定日期以前的日志索引中binlog日志文件

  或者::

    purge master logs to'mysql-bin.000022'; //删除指定日志文件的日志索引中binlog日志文件

  .. note::

    使用该语法，会将对应的文件和mysql-bin.index中对应路径删除

    时间和文件名一定不可以写错，尤其是时间中的年和文件名中的序号，
    以防不小心将正在使用的binlog删除！！！切勿删除正在使用的binlog

  - reset master:将删除日志索引文件中记录的所有binlog文件，创建一个新的日志文件，起始值从000001开始。不要轻易使用该命令，这个命令通常仅仅用于第一次用于搭建主从关系的时的主库。
  - reset slave:清除master.info文件、relay-log.info文件，以及所有的relay log文件,并重新启用一个新的relaylog文件
自动清理
  设置binlog过期时间，使系统自动删除binlog文件

  **在mysql中修改**,
  查看binlog过期时间，这个值默认是0天，也就是说不自动清理，可以根据生产情况修改，本例修改为7天::

    mysql> show variables like 'expire_logs_days';
    +------------------------+-------+
    | Variable_name  | Value |
    +------------------------+-------+
    | expire_logs_days |   0  |
    +------------------------+-------+
    mysql> set global expire_logs_days = 7;    #设置binlog多少天过期

  设置之后不会立即清除，触发条件是以下之一：

  - binlog大小超过max_binlog_size，max_binlog_size默认为1G
  - 手动执行flush logs

  如果binlog非常多，不要轻易设置该参数，有可能导致IO争用，这个时候可以使用purge命令予以清除：

  将bin.000055之前的binlog清掉::

    mysql>purge binary logs to 'bin.000055';

  将指定时间之前的binlog清掉::

    mysql>purge binary logs before '2017-05-01 13:09:51';
配置文件中修改
  mysqld在每个二进制日志名后面添加一个数字扩展名。
  每次你启动服务器或刷新日志时该数字则增加。
  如果当前日志大小达到max_binlog_size,还会自动创建新的二进制日志。
  如果你正使用大的事务，二进制日志还会超过max_binlog_size:事务全写入一个二进制日志中，绝对不要写入不同的二进制日志中。

  expire_logs_days
    定义了mysql清除过期日志的时间。默认值为0,表示“没有自动删除”。
  max_binlog_size
    二进制日志最大大小，如果二进制日志写入的内容超出给定值，日志就会发生滚动。
    你不能将该变量设置为大于1GB或小于4096字节。 默认值是1GB。

  在my.cnf中添加配置,设置过期时间为30天::

    expire_logs_days = 30

  max_binlog_size使用默认值即可

  .. note::

    过期时间设置的要适当，对于主从复制，要看从库的延迟决定过期时间，
    避免主库binlog还未传到从库便因过期而删除，导致主从不一致！！！


