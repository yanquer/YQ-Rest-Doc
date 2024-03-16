===================================
mysql 备份方案
===================================


.. post:: 2023-02-20 22:06:49
  :tags: mysql
  :category: 数据库
  :author: YanQue
  :location: CD
  :language: zh-cn


全量备份
===================================

方案一： sql实现
-----------------------------------

sql 语句实现::

  mysqldump --lock-all-tables --flush-logs --master-data=2 -u $username -p $password $database_name > $bak_file

参数解释

--lock-all-tables
  对于InnoDB将替换为 --single-transaction。
  该选项在导出数据之前提交一个 BEGIN SQL语句，
  BEGIN 不会阻塞任何应用程序且能保证导出时数据库的一致性状态。
  它只适用于事务表，例如 InnoDB 和 BDB。
  本选项和 --lock-tables 选项是互斥的，因为 LOCK TABLES 会使任何挂起的事务隐含提交。
  要想导出大表的话，应结合使用 --quick 选项。
--flush-logs
  结束当前日志，生成并使用新日志文件
--master-data
  ``--master-data=2``.
  该选项将会在输出SQL中记录下完全备份后新日志文件的名称，用于日后恢复时参考，
  例如输出的备份SQL文件中含有::

    CHANGE MASTER TO MASTER_LOG_FILE='MySQL-bin.000002', MASTER_LOG_POS=106;
--all-databases
  备份所有数据库，备份单个库直接跟库名
--databases
  指定多个数据库
--quick, -q
  该选项在导出大表时很有用，
  它强制 MySQLdump 从服务器查询取得记录直接输出而不是取得所有记录后将它们缓存到内存中。
--ignore-table
  忽略某个数据表，如 --ignore-table test.user 忽略数据库test里的user表

.. note::

    对于mysqldump备份的数据, 可以直接进数据库执行::

      source bak.sql

    恢复

    命令大小写不敏感, 库名大小写敏感

方案二： django角度实现
-----------------------------------

备份::

  python manage.py dumpdata $app >$bak_file

恢复::

  python manage.py loaddata $bak_file

方案三： oracle商业软件mysqlbackup实现（可能需付费下载）
----------------------------------------------------------------------

完整备份::

  mysqlbackup --defaults-file=$mysqld_cnf_file --socket=$socket_file --with-timestamp --user=$user --password=$password --backup-dir=$backup_dir backup-and-apply-log

--defaults-file
  mysql配置文件目录
--socket
  socket目录 （默认不用输入，一般会找默认的）
--with-timestamp
  以时间来生成文件名
--user
  用户
--password
  密码
--backup-dir
  备份文件目录

backup-and-apply-log
  备份并检查日志文件

完整备份恢复::

  # copy-back 把back-dir复制到datadir中
  mysqlbackup --defaults-file=$mysqld_cnf_file --datadir=$sys_mysql_data_dir --backup-dir=$backup_dir copy-back

--datadir
  当前数据库相应的数据文件所在位置
--backup-dir
  当前备份文件所在目录

copy-back
  把back-dir复制到datadir中

.. note::

  在恢复时报错未找到innodb配置，两种方法解决，

  - 第一种在mysqld.cnf添加innodb的配置文件，具体配置在备份文件backup-my.cnf中，
  - 第二种方法直接将 --defaults-file指定到备份文件的backup-my.cnf目录

  在还原后，修改mysql这个目录和mysql里面的文件内容都把权限修改成mysql,否mysql无法启动

增量备份
===================================

方案一： bin-log 增量备份
-----------------------------------

备份大概顺序
  - 确认数据库开启 log_bin
  - 链接数据库刷新日志，执行 flush-logs
  - 备份旧的 bin-log 文件

恢复备份大概顺序
  - 还原旧的 bin-log 文件
  - 执行mysqlbinlog 恢复，
    如::

      mysqlbinlog --no-defaults $log_bin_file

.. note::

  若需定时操作，linux可加crontab定时器

方案二：mysqlbackup实现
-----------------------------------

说明，mysqlbackup是mysql企业版功能，oracle商业软件，需要付费使用

下载地址: `<https://www.mysql.com/downloads/>`_

备份
  多文件备份流程（推荐使用多文件的，就是恢复需要整理成单文件，此处就不写单文件流程了，基本一致）

  第一次增量备份::

    mysqlbackup --defaults-file=$socket_file --user=$user --password --with-timestamp  --incremental --incremental-base=dir:$base_bak_dir --incremental-backup-dir=$true_bak_dir backup

    --incremental 表示增量备份
    --incremental-base 基于哪个备份的备份
    --incremental-backup-dir 增量备份的备份存放目录

  第二次增量备份

      mysqlbackup --defaults-file=$socket_file --with-timestamp --user=$user --password --incremental --incremental-base=dir:$base_bak_dir --incremental-backup-dir=$true_bak_dir backup

  .. note::

    第二次 incremental-base 的位置是第一次增量备份的位置
恢复增量备份
  使用apply-log将完整备份做成最终备份::

    mysqlbackup --backup-dir=$res_bak_file apply-log

  将第一次增量备份备份完整备份中::

    mysqlbackup --incremental-backup-dir=$first_bak_dir --backup-dir=$res_bak_file apply-incremental-backup

  将第二次增量备份备份到完整备份中::

    mysqlbackup --incremental-backup-dir=$second_bak_dir --backup-dir=$res_bak_file apply-incremental-backup

  物理还原::

    mysqlbackup --defaults-file=/etc/mysql/mysql.cond.d/mysqld.cnf --backup-dir=$res_bak_file copy-back

.. note::

  apply-incremental-backup 每一个增量备份刷新日志

方案三：开源工具 xtraback 实现增量备份
----------------------------------------------------------------------

xtraback优点

- 备份速度快，物理备份可靠
- 备份过程不会打断正在执行的事务（无需锁表）
- 能够基于压缩等功能节约磁盘空间和流量
- 自动备份校验
- 还原速度快
- 可以流传将备份传输到另外一台机器上
- 在不增加服务器负载的情况备份数据

下载地址: `<https://www.percona.com/downloads/XtraBackup/LATEST/>`_

说明
  Xtrabackup中主要包含两个工具：

  - xtrabackup：是用于热备innodb，xtradb表中数据的工具，不能备份其他类型的表，也不能备份数据表结构；
  - innobackupex：是将xtrabackup进行封装的perl脚本，提供了备份myisam表的能力。

常用选项::

  --host     指定主机
  --user     指定用户名
  --password    指定密码
  --port     指定端口
  --databases     指定数据库
  --incremental    创建增量备份
  --incremental-basedir   指定包含完全备份的目录
  --incremental-dir      指定包含增量备份的目录
  --apply-log        对备份进行预处理操作
                      一般情况下，在备份完成后，数据尚且不能用于恢复操作，因为备份的数据中可能会包含尚未提交的事务或已经提交但尚未同步至数据文件中的事务。因此，此时数据文件仍处理不一致状态。“准备”的主要作用正是通过回滚未提交的事务及同步已经提交的事务至数据文件也使得数据文件处于一致性状态。
  --redo-only      不回滚未提交事务
  --copy-back     恢复备份目录

增量备份,
基于全量备份的增量备份与恢复

做一次增量备份（基于当前最新的全量备份）::

  innobackupex --user=$user --password=$password --defaults-file=$mysqld_cnf_file --incremental /backups/ --incremental-basedir=$whole_bak_dir

准备基于全量::

  innobackupex --user=$user --password=$password --defaults-file=$mysqld_cnf_file --apply-log --redo-only $whole_bak_dir

准备基于增量::

  innobackupex --user=$user --password=$password --defaults-file=$mysqld_cnf_file --apply-log --redo-only $whole_bak_dir --incremental-dir=$increase_dir

增量备份恢复::

  innobackupex --copy-back --defaults-file=$mysqld_cnf_file $bak_dir

解释::

  $whole_bak_dir
    指的是完全备份所在的目录。
  $increase_dir
    指定是第一次基于 $whole_bak_dir 增量备份的目录，
    其他类似以此类推，即如果有多次增量备份。每一次都要执行如上操作。

.. note::

  增量备份仅能应用于InnoDB或XtraDB表，对于MyISAM表而言，执行增量备份时其实进行的是完全备份。

此节参考: `xtrabackup的配置使用 <https://www.cnblogs.com/linuxk/p/9372990.html>`_


其他工具-MyDumper
===================================

相对于 `MySQL <https://cloud.tencent.com/product/cdb?from=10680>`_
官方提供的逻辑备份工具 mysqldump,
mydumper 最突出的特性就是可采用多线程并行备份，极大提高了数据导出的速度。

使用::

  mydumper -h $host -u $user -p $password --database $db --tables-lists $tables --compress --threads 4 --outputdir $path

  # 少一个  --tables-lists $tables 就是全库备份
  mydumper -h $host --database $db --compress --threads 4 --outputdir $path --defaults-file=$passfile

-c, --compress		    压缩输出文件
-m, --no-schemas	    不导出表结构
-t, --threads		      使用的线程数量
-F, --chunk-filesize	将表数据分割成这个输出大小的块，单位默认是MB






