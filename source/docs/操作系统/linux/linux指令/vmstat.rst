=============================
vmstat
=============================

vmstat是Virtual Meomory Statistics（虚拟内存统计）的缩写，
可对操作系统的虚拟内存、进程、CPU活动进行监控。
它是对系统的整体情况进行统计，
不足之处是无法对某个进程进行深入分析。

vmstat工具提供了一种低开销的系统性能观察方式。
因为vmstat本身就是低开销工具，
在非常高负荷的服务器上，
你需要查看并监控系统的健康情况，在控制窗口还是能够使用vmstat输出结果。

语法::

  vmstat [-a] [-n] [-S unit] [delay [ count]]
  vmstat [-s] [-n] [-S unit]
  vmstat [-m] [-n] [delay [ count]]
  vmstat [-d] [-n] [delay [ count]]
  vmstat [-p disk partition] [-n] [delay [ count]]
  vmstat [-f]
  vmstat [-V]

选项
  -a
    显示活跃和非活跃内存
  -f
    显示从系统启动至今的fork数量 。
  -m
    显示slabinfo
  -n
    只在开始时显示一次各字段名称。
  -s
    显示内存相关统计信息及多种系统活动数量。
  -d
    显示磁盘相关统计信息
  -p
    显示指定磁盘分区统计信息
  -S
    使用指定单位显示。参数有 k 、K 、m 、M，
    分别代表1000、1024、1000000、1048576字节（byte）。默认单位为K（1024 bytes）
  -V
    显示vmstat版本信息。

  delay
    刷新时间间隔。如果不指定，只显示一条结果。
  count
    刷新次数。如果不指定刷新次数，但指定了刷新时间间隔，这时刷新次数为无穷。

输出含义
=============================

如直接执行::

  # vmstat
  procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
  r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
  2  0      0 6300920 268396 937448    0    0  1944   289  532  779  1  2 97  1  0

procs
  - r 列表示运行和等待cpu时间片的进程数，如果长期大于1，说明cpu不足，需要增加cpu;
  - b 列表示在等待资源的进程数，比如正在等待I/O、或者内存交换等
memory
  - swpd 切换到内存交换区的内存数量(k表示),
    如果swpd的值不为0，或者比较大，比如超过了100m，只要si、so的值长期为0，系统性能还是正常
  - free 当前的空闲页面列表中内存数量(k表示)
  - buff 作为buffer cache的内存数量，一般对块设备的读写才需要缓冲。
  - cache: 作为page cache的内存数量，一般作为文件系统的cache，
    如果cache较大，说明用到cache的文件较多，如果此时IO中bi比较小，说明文件系统效率比较好。
swap
  - si 由磁盘进入内存交换区数量
  - so 由内存交换区进入磁盘数量
IO
  - bi 从块设备读入数据的总量（读磁盘）（每秒kb）
  - bo 块设备写入数据的总量（写磁盘）（每秒kb）

  这里我们设置的bi+bo参考值为1000，如果超过1000，
  而且wa值较大应该考虑均衡磁盘负载，可以结合iostat输出来分析。
system
  显示采集间隔内发生的中断数

  - in 列表示在某一时间间隔中观测到的每秒设备中断数
  - cs列表示每秒产生的上下文切换次数，如当 cs 比磁盘 I/O 和网络信息包速率高得多，都应进行进一步调查。
cpu
  表示cpu的使用状态

  - us 列显示了用户方式下所花费 CPU 时间的百分比。
    us的值比较高时，说明用户进程消耗的cpu时间多，但是如果长期大于50%，需要考虑优化用户的程序。
  - sy 列显示了内核进程所花费的cpu时间的百分比。这里us + sy的参考值为80%，如果us+sy 大于 80%说明可能存在CPU不足。
  - id 列显示了cpu处在空闲状态的时间百分比
  - wa 列显示了IO等待所占用的CPU时间的百分比。
    如果wa超过30%，说明IO等待严重，
    这可能是磁盘大量随机访问造成的，也可能磁盘或者磁盘访问控制器的带宽瓶颈造成的(主要是块操作)。

参考: `<https://zhuanlan.zhihu.com/p/162711990>`_


