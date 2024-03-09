=====================
linux 系统信号
=====================

Linux系统有两大类信号

- POSIX标准的规则信号(regular signal 1-31编号)
- 实时信号(real-time signal 32-63)

系统信号
=====================

一些常见的的 linux 系统信号。

.. csv-table::
  :header: 信号, 值, 描述

  1   ,  SIGHUP  ,  挂起进程
  2   ,  SIGINT  ,  终止进程(ctrl+c)
  3   ,  SIGQUIT ,  停止进程
  9   ,  SIGKILL ,  无条件终止进程, 强制杀死进程, 这个信号进程无法忽视, 直接在系统层面把进程杀掉. 所以在Python中他的不能监听的
  15  ,  SIGTERM ,  尽可能终止进程
  17  ,  SIGSTOP ,  无条件停止进程，但不是终止进程
  18  ,  SIGTSTP ,  停止或暂停进程，但不终止进程(ctrl+z)
  19  ,  SIGCONT ,  继续运行停止的进程

:参考::
  `<https://blog.csdn.net/qq_55723966/article/details/122304011>`_

规则信号(包括了上面的常用信号)

.. csv-table::
  :header: 信号编号, 名称, 默认动作, 说明

  1 , SIGHUP  , 终止  ,  终止控制终端或进程. 终端挂起或者控制进程终止
  2 , SIGINT  , 终止  ,  由键盘引起的中断(Ctrl-c)
  3 , SIGQUIT , dump  , 控制终端发送给进程的信号, 键盘产生的退出(Ctrl-\),
  4 , GIGILL  , dusmp , 非法指令引起
  5 , SIGTRAP , dump  , debug中断
  6 , SIGABRT/SIGIOT ,  dump  , 异常中止. 由abort(3)发出的退出指令
  7 , SIGBUS/SIGEMT  ,  dump  , 总线异常/EMT指令
  8 , SIGFPE  , dump  , 浮点运算溢出
  9 , SIGKILL , 终止  , 强制杀死进程(大招. 进程不可捕获). 这个信号进程无法忽视, 直接在系统层面把进程杀掉. 所以在Python中他的不能监听的
  10, SIGUSR1 , 终止  , 用户信号. 进程可自定义用途
  11, SIGSEGV , dump  , 非法内存地址. 无效的内存引用
  12, SIGUSR2 , 终止  , 用户信号. 进程可自定义用途
  13, SIGPIPE , 终止  , 向某个没有读取的管道中写入数据. 管道破裂: 写一个没有读端口的管道
  14, SIGALRM , 终止  , 时钟中断(闹钟). 由alarm(2)发出的信号
  15, SIGTERM , 终止  , 进程终止(进程可捕获)
  16, SIGSTKFLT , 终止, 协处理器栈错误
  17, SIGCHLD ,忽略   , 子进程退出或中断
  18, SIGCONT ,继续   , 如进程停止状态则开始运行
  19, SIGSTOP ,停止   , 停止进程运行
  20, SIGSTP  ,停止   , 键盘产生的停止
  21, SIGTTIN ,停止   , 后台进程请求输入
  22, SIGTTOU ,停止   , 后台进程请求输出
  23, SIGURG  ,忽略   , socket发送紧急情况
  24, SIGXCPU ,dump   , CPU时间限制被打破
  25, SIGXFSZ ,dump   , 文件大小限制被打破
  26, SIGVTALRM ,终止 , 虚拟定时时钟
  27, SIGPROF   ,终止 , profile timer clock
  28, SIGWINCH ,忽略  , 窗口尺寸调整
  29, SIGIO/SIGPOLL ,终止 , I/O可用
  30, SIGPWR  ,终止   , 电源异常
  31, SIGSYS/SYSUNUSED  ,dump , 系统调用异常

.. note::

  由于不同系统中同一个数值对应的信号类型不一样, 所以最好使用信号名称.

  信号的数值越小, 优先级越高.

信号量说明(参考)
=====================

.. .. csv-table:\:
..   :header: 编号, 名称, 默认动作, 说明

..   SIGHUP, 	终止进程, 		终端线路挂断
..   SIGINT, 	终止进程, 		中断进程
..   SIGQUIT, 	建立CORE文件, 	终止进程，并且生成core文件
..   SIGILL, 	建立CORE文件,	非法指令
..   SIGTRAP, 	建立CORE文件,	跟踪自陷
..   SIGBUS, 	建立CORE文件, 	总线错误
..   SIGSEGV, 	建立CORE文件, 	段非法错误
..   SIGFPE, 	建立CORE文件, 	浮点异常
..   SIGIOT, 	建立CORE文件, 	执行I/O自陷
..   SIGKILL, 	终止进程, 		杀死进程
..   SIGPIPE, 	终止进程, 		向一个没有读进程的管道写数据
..   SIGALarm, 	终止进程, 		计时器到时
..   SIGTERM, 	终止进程, 		软件终止信号
..   SIGSTOP, 	停止进程, 		非终端来的停止信号
..   SIGTSTP, 	停止进程, 		终端来的停止信号
..   SIGCONT, 	忽略信号, 		继续执行一个停止的进程
..   SIGURG, 	忽略信号, 		I/O紧急信号
..   SIGIO, 		忽略信号, 		描述符上可以进行I/O
..   SIGCHLD, 	忽略信号, 		当子进程停止或退出时通知父进程
..   SIGTTOU, 	停止进程, 		后台进程写终端
..   SIGTTIN, 	停止进程, 		后台进程读终端
..   SIGXGPU, 	终止进程, 		CPU时限超时
..   SIGXFSZ, 	终止进程, 		文件长度过长
..   SIGWINCH, 	忽略信号, 		窗口大小发生变化
..   SIGPROF, 	终止进程, 		统计分布图用计时器到时
..   SIGUSR1, 	终止进程, 		用户定义信号1
..   SIGUSR2, 	终止进程, 		用户定义信号2
..   SIGVTALRM, 	终止进程, 		虚拟计时器到时

- SIGHUP 本信号在用户终端连接(正常或非正常)结束时发出, 通常是在终端的控制进程结束时, 通知同一session内的各个作业, 这时它们与控制终端不再关联.
- SIGINT 程序终止(interrupt)信号, 在用户键入INTR字符(通常是Ctrl-C)时发出
- SIGQUIT 和SIGINT类似, 但由QUIT字符(通常是Ctrl-)来控制. 进程在因收到SIGQUIT退出时会产生core文件, 在这个意义上类似于一个程序错误信号.
- SIGILL 执行了非法指令. 通常是因为可执行文件本身出现错误, 或者试图执行数据段. 堆栈溢出时也有可能产生这个信号.
- SIGTRAP 由断点指令或其它trap指令产生. 由debugger使用.
- SIGABRT 程序自己发现错误并调用abort时产生.
- SIGIOT 在PDP-11上由iot指令产生, 在其它机器上和SIGABRT一样.
- SIGBUS 非法地址, 包括内存地址对齐(alignment)出错. eg: 访问一个四个字长的整数, 但其地址不是4的倍数.
- SIGFPE 在发生致命的算术运算错误时发出. 不仅包括浮点运算错误, 还包括溢出及除数为0等其它所有的算术的错误.
- SIGKILL 用来立即结束程序的运行. 本信号不能被阻塞, 处理和忽略.
- SIGUSR1 留给用户使用
- SIGSEGV 试图访问未分配给自己的内存, 或试图往没有写权限的内存地址写数据.
- SIGUSR2 留给用户使用
- SIGPIPE Broken pipe
- SIGALRM 时钟定时信号, 计算的是实际的时间或时钟时间. alarm函数使用该信号.
- SIGTERM 程序结束(terminate)信号, 与SIGKILL不同的是该信号可以被阻塞和处理. 通常用来要求程序自己正常退出. shell命令kill缺省产生这个信号.
- SIGCHLD 子进程结束时, 父进程会收到这个信号.
- SIGCONT 让一个停止(stopped)的进程继续执行. 本信号不能被阻塞. 可以用一个handler来让程序在由stopped状态变为继续执行时完成特定的工作. 例如, 重新显示提示符.

:参考::
  https://www.jianshu.com/p/1a9ea7f4d46e



