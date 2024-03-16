================
chkconfig
================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


chkconfig是管理系统服务(service)的命令行工具。
所谓系统服务(service)，就是随系统启动而启动，随系统关闭而关闭的程序。

chkconfig可以更新(启动或停止)和查询系统服务(service)运行级信息。
更简单一点，chkconfig是一个用于维护/etc/rc[0-6].d目录的命令行工具。

常见用法
================

用法::

  chkconfig [--list] [--type <类型>] [名称]
          chkconfig --add <名称>
          chkconfig --del <名称>
          chkconfig --override <名称>
          chkconfig [--level <级别>] [--type <类型>] <名称> <on|off|reset|resetpriorities>

设置service开机是否启动::

  chkconfig name on/off/reset

on、off、reset用于改变service的启动信息.
on表示开启，off表示关闭，reset表示重置。
默认情况下，on和off开关只对运行级2，3，4，5有效，reset可以对所有运行级有效。

.. note::

  在Redhat7上，运行chkconfig命令，都会被转到systemcle命令上。

设置service运行级别::

  chkconfig --level levels

指定服务的运行级别，即指定运行级别2,3,4,5等(即 init_ 的运行级别):

- 0：- 关机
- 1：单用户模式
- 2：无网络连接的多用户命令行模式
- 3：有网络连接的多用户命令行模式
- 4：不可用
- 5：带图形界面的多用户模式
- 6：重新启动

列出service启动信息::

  chkconfig --list [name]

如果不指定name，会列出所有services的信息.

每个service每个运行级别都会有一个启动和停止脚本；
当切换运行级别时，init不会重启已经启动的service，也不会重新停止已经停止的service。

欲查看对特定 target 启用的服务请执行::

  systemctl list-dependencies [target]

.. _init: :doc:`/docs/操作系统/linux/linux指令/init`

