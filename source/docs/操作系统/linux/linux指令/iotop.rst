=========================
iotop
=========================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


iotop 一个用来监视磁盘I/O使用状况的top类工具。
iotop具有与top相似的UI，其中包括PID、用户、I/O、进程等相关信息。
Linux下的IO统计工具如iostat，nmon等大多数是只能统计到per设备的读写情况，
如果你想知道每个进程是如何使用IO的就比较麻烦，使用iotop命令可以很方便的查看。

iotop使用Python语言编写而成，要求Python2.5（及以上版本）和Linux kernel2.6.20（及以上版本）。
iotop提供有源代码及rpm包，可从其官方主页下载。

选项

-o
  只显示有io操作的进程
-b
  批量显示，无交互，主要用作记录到文件。
-n NUM
  显示NUM次，主要用于非交互式模式。
-d SEC
  间隔SEC秒显示一次。
-p PID
  监控的进程pid。
-u USER
  监控的进程用户。
-t, --time
  加上时间戳，非交互非模式

iotop常用快捷键::

  左右箭头：改变排序方式，默认是按IO排序。
  r：改变排序顺序。
  o：只显示有IO输出的进程。
  p：进程/线程的显示方式的切换。
  a：显示累积使用量。
  q：退出。

