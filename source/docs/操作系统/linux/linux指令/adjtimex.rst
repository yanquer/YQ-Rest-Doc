===================================
adjtimex
===================================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


linux系统有两个时钟：

- 一个是由主板电池驱动的“Real Time Clock”也叫做RTC或者叫CMOS时钟，硬件时钟。
  当操作系统关机的时候，用这个来记录时间，但是对于运行的系统是不用这个时间的。
- 另一个时间是 “System clock”也叫内核时钟或者软件时钟，
  是由软件根据时间中断来进行计数的，内核时钟在系统关机的情况下是不存在的，
  所以，当操作系统启动的时候，内核时钟是要读取RTC时间来进行时间同步
  （有些情况下，内核时钟也可以通过ntp服务器来读取时间） 这两个时钟通常会有一些误差，
  所以长时间可以导致这两个时钟偏离的比较多，
  最简单的保持两个时间同步的方法是用软件测出他们之间的误差率，然后用软件进行修正。

adjtimex选项

-p, –print
  输出内核时间变量的值
-t, –tick val
  设置内核时钟计数间隔（微秒）
-f, –frequency newfreq
  设置系统时钟偏移量
-c, –compare[=count]
  比较系统时钟和CMOS时钟
-i, –interval tim
  设置时钟比较间隔时间 (sec)
-l, –log[=file]
  将当前时间记录到文件中
–host timeserver
  查询时间服务器
-u, –utc
  将CMOS时钟设置成UTC


每次重启NTP服务器之后大约要3－5分钟客户端才能与server建立正常的通讯连接





