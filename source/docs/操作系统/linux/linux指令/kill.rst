=======================
kill
=======================

类似的指令:

- :doc:`/docs/操作系统/linux/linux指令/killall`
- :doc:`/docs/操作系统/linux/linux指令/pkill`

.. 杀死进程

发送信号

Linux kill 命令用于删除执行中的程序或工作。
kill 可将指定的信息送至程序。
预设的信息为 SIGTERM(15)，可将指定程序终止。
若仍无法终止该程序，可使用 SIGKILL(9) 信息尝试强制删除程序。

程序或工作的编号可利用 ps 指令或 jobs 指令查看。

语法::

  kill [-s <信息名称或编号>][程序]  或  kill [-l <信息编号>]

参数说明::

  -l <信息编号>  若不加<信息编号>选项，则 -l 参数会列出全部的信息名称。
  -s <信息名称或编号>  指定要送出的信息。
  [程序]  [程序]可以是程序的PID或是PGID，也可以是工作编号。

使用 `kill -l` 命令列出所有可用信号

最常用的信号是::

  1 (HUP)：重新加载进程。
  9 (KILL)：杀死一个进程。
  15 (TERM)：正常停止一个进程。

发送SIGHUP信号，可以使用一下信号::

  kill -HUP pid

彻底杀死进程::

  kill -9 123456

  # 或者  kill -KILL 123456

杀死指定用户所有进程::

  kill -9 $(ps -ef | grep hnlinux) //方法一 过滤出hnlinux用户进程
  kill -u hnlinux //方法二

