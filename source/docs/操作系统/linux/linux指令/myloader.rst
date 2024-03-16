==============================
myloader
==============================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


数据恢复

-d, --directory                   备份文件的文件夹
-q, --queries-per-transaction     每次事物执行的查询数量，默认是1000
-o, --overwrite-tables            如果要恢复的表存在，则先drop掉该表，使用该参数，需要备份时候要备份表结构
-B, --database                    需要还原的数据库
-e, --enable-binlog               启用还原数据的二进制日志
-h, --host                        主机
-u, --user                        还原的用户
-p, --password                    密码
-P, --port                        端口
-S, --socket                      socket文件
-t, --threads                     还原所使用的线程数，默认是4
-C, --compress-protocol           压缩协议
-V, --version                     显示版本
-v, --verbose                     输出模式, 0 = silent, 1 = errors, 2 = warnings, 3 = info, 默认为2


相关指令 :doc:`mydumper`, 用于数据备份
