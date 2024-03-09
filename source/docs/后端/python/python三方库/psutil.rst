===============
psutil
===============

便捷的系统监控工具.

安装::

  pip install psutil

获取cpu信息
===============

获取cpu信息::

  psutil.cpu_times()

获取内存信息
===============

使用psutil获取物理内存和交换内存信息，分别使用::

  psutil.virtual_memory()
  psutil.swap_memory()

获取磁盘信息
===============

可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息::

  psutil.disk_partitions() # 磁盘分区信息
  psutil.disk_usage('/') # 磁盘使用情况
  psutil.disk_io_counters() # 磁盘IO

获取网络信息
===============

psutil可以获取网络接口和网络连接信息::

  psutil.net_io_counters() # 获取网络读写字节／包的个数
  psutil.net_if_addrs() # 获取网络接口信息
  psutil.net_if_stats() # 获取网络接口状态

要获取当前网络连接信息，使用net_connections()::

  psutil.net_connections()

若权限不足需要获取权限, 如 ``sudo`` 启动 (因为会调用系统的接口)

获取进程信息
===============

通过psutil可以获取到所有进程的详细信息::

  >>> psutil.pids() # 所有进程ID
  [3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]
  >>> p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
  >>> p.name() # 进程名称
  'python3.6'
  >>> p.exe() # 进程exe路径
  '/Users/michael/anaconda3/bin/python3.6'
  >>> p.cwd() # 进程工作目录
  '/Users/michael'
  >>> p.cmdline() # 进程启动的命令行
  ['python3']
  >>> p.ppid() # 父进程ID
  3765
  >>> p.parent() # 父进程
  <psutil.Process(pid=3765, name='bash') at 4503144040>
  >>> p.children() # 子进程列表
  []
  >>> p.status() # 进程状态
  'running'
  >>> p.username() # 进程用户名
  'michael'
  >>> p.create_time() # 进程创建时间
  1511052731.120333
  >>> p.terminal() # 进程终端
  '/dev/ttys002'
  >>> p.cpu_times() # 进程使用的CPU时间
  pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
  >>> p.memory_info() # 进程使用的内存
  pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
  >>> p.open_files() # 进程打开的文件
  []
  >>> p.connections() # 进程相关网络连接
  []
  >>> p.num_threads() # 进程的线程数量
  1
  >>> p.threads() # 所有线程信息
  [pthread(id=1, user_time=0.090318, system_time=0.062736)]
  >>> p.environ() # 进程环境变量
  {'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
  >>> p.terminate() # 结束进程
  Terminated: 15 <-- 自己把自己结束了

和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。

psutil还提供了一个test()函数，可以模拟出ps命令的效果::

  >>> import psutil
  >>> psutil.test()
  USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
  root           0 24.0 74270628 2016380 ?             Nov18   40:51  kernel_task
  root           1  0.1 2494140    9484 ?             Nov18   01:39  launchd
  root          44  0.4 2519872   36404 ?             Nov18   02:02  UserEventAgent
  root          45    ? 2474032    1516 ?             Nov18   00:14  syslogd
  root          47  0.1 2504768    8912 ?             Nov18   00:03  kextd
  root          48  0.1 2505544    4720 ?             Nov18   00:19  fseventsd
  _appleeven    52  0.1 2499748    5024 ?             Nov18   00:00  appleeventsd
  root          53  0.1 2500592    6132 ?             Nov18   00:02  configd
  ...

使用技巧
===============

例如用来回收自己残留的子进程::

  _pid = os.getpid()

  pro = psutil.Process(_pid)
  pro.terminate()



