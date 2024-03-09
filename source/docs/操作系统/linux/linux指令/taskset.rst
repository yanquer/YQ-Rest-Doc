==============================
taskset
==============================

taskset命令用于设置进程（或 线程）的处理器亲和性（Processor Affinity），
可以将进程（或 线程）绑定到特定的一个 或 多个CPU上去执行，
而不允许将进程（或 线程）调度到其他的CPU上。

将进程绑定到指定的CPU上运行，这样可以避免大量的进程切换产生的无效时间。
通过 taskset 命令可将某个进程与某个CPU核心绑定，使得其仅在与之绑定的CPU核心上运行。

线程是最小的内核执行调度单元，因此，准确地说是将某个线程与某个CPU核心绑定，而非某个进程。

taskset命令是依据线程PID（TID）查询或设置线程的CPU亲和性（与哪个CPU核心绑定）。

常用参数

-a, --all-tasks   设置或检索所有任务（线程）的CPU相关性对于给定的PID
-c, --cpu-list    将掩码解释为处理器的数字列表
-p, --pid         在现有PID上操作，不要启动新任务
-V, --version     显示版本信息
-h, --help        显示帮助信息

例子::

  [root@localhost ~]# ps -eLf | grep qemu
  root       1389   1339   1389  0    3 14:48 pts/0    00:00:10 /usr/libexec/qemu-kvm -cpu SandyBridge -vnc 0.0.0.0:1 centos1708.img
  root       1389   1339   1393  2    3 14:48 pts/0    00:00:36 /usr/libexec/qemu-kvm -cpu SandyBridge -vnc 0.0.0.0:1 centos1708.img
  root       1389   1339   1395  0    3 14:48 pts/0    00:00:00 /usr/libexec/qemu-kvm -cpu SandyBridge -vnc 0.0.0.0:1 centos1708.img
  root       2638   1409   2638  0    1 15:10 pts/1    00:00:00 grep --color=auto qemu
  [root@localhost ~]# taskset -p 1393
  pid 1393's current affinity mask: ff
  [root@localhost ~]# taskset -p 1389
  pid 1389's current affinity mask: ff

输出结构处理器亲和性掩码是ff，表示进程（或 线程）可以在Host上让任何一个CPU运行。
查看进程（或 线程）允许允许CPU范围使用 -c 参数。
由于我的Host CPU是4核2线程，因此有8颗逻辑CPU::

  [root@localhost ~]# taskset -cp 1393
  pid 1393's current affinity list: 0-7
  [root@localhost ~]# taskset -cp 1389
  pid 1389's current affinity list: 0-7

更改具体某一进程（或 线程）CPU亲和性
============================================================

指令::

  taskset -p  hexadecimal mask PID/LWP

上面1393号线程可以在0~7号CPU之间允许，现在设置掩码0x11（二进制0001 0001），表示可以在0~4号CPU上允许::

  [root@localhost ~]# taskset -p 0x11  1393
  pid 1393's current affinity mask: ff
  pid 1393's new affinity mask: 11
  [root@localhost ~]# taskset -p   1393
  pid 1393's current affinity mask: 11
  [root@localhost ~]# taskset -cp   1393
  pid 1393's current affinity list: 0,4

为具体某一进程（或 线程）CPU亲和性指定一组范围
============================================================

使用-c参数::

  [root@localhost ~]# taskset -cp 0,3  1393
  pid 1393's current affinity list: 0,4
  pid 1393's new affinity list: 0,3
  [root@localhost ~]# taskset -cp   1393
  pid 1393's current affinity list: 0,3




