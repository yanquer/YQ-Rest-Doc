===========================
mydumper
===========================

数据库备份指令

-B, --database              要备份的数据库，不指定则备份所有库
-T, --tables-list           需要备份的表，名字用逗号隔开
-o, --outputdir             备份文件输出的目录
-s, --statement-size        生成的insert语句的字节数，默认1000000
-r, --rows                  将表按行分块时，指定的块行数，指定这个选项会关闭 --chunk-filesize
-F, --chunk-filesize        将表按大小分块时，指定的块大小，单位是 MB
-c, --compress              压缩输出文件
-e, --build-empty-files     如果表数据是空，还是产生一个空文件（默认无数据则只有表结构文件）
-x, --regex                 是同正则表达式匹配 'db.table'
-i, --ignore-engines        忽略的存储引擎，用都厚分割
-m, --no-schemas            不备份表结构
-k, --no-locks              不使用临时共享只读锁，使用这个选项会造成数据不一致
--less-locking              减少对InnoDB表的锁施加时间（这种模式的机制下文详解）
-l, --long-query-guard      设定阻塞备份的长查询超时时间，单位是秒，默认是60秒（超时后默认mydumper将会退出）
--kill-long-queries         杀掉长查询 (不退出)
-b, --binlogs               导出binlog
-D, --daemon                启用守护进程模式，守护进程模式以某个间隔不间断对数据库进行备份
-I, --snapshot-interval     dump快照间隔时间，默认60s，需要在daemon模式下
-L, --logfile               使用的日志文件名(mydumper所产生的日志), 默认使用标准输出
--tz-utc                    跨时区是使用的选项，不解释了
--skip-tz-utc               同上
--use-savepoints            使用savepoints来减少采集metadata所造成的锁时间，需要 SUPER 权限
--success-on-1146           Not increment error count and Warning instead of Critical in case of table doesn't exist
-h, --host                  连接的主机名
-u, --user                  备份所使用的用户
-p, --password              密码
-P, --port                  端口
-S, --socket                使用socket通信时的socket文件
-t, --threads               开启的备份线程数，默认是4
-C, --compress-protocol     压缩与mysql通信的数据
-V, --version               显示版本号
-v, --verbose               输出信息模式, 0 = silent, 1 = errors, 2 = warnings, 3 = info, 默认为 2

相关指令 :doc:`myloader`, 用于数据恢复
