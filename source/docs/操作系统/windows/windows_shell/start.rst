=============
start
=============

启动一个单独的窗口以运行指定的程序或命令::

  START ["title"] [/D path] [/I] [/MIN] [/MAX] [/SEPARATE | /SHARED]
        [/LOW | /NORMAL | /HIGH | /REALTIME | /ABOVENORMAL | /BELOWNORMAL]
        [/NODE <NUMA node>] [/AFFINITY <hex affinity mask>] [/WAIT] [/B]
        [command/program] [parameters]

选项/参数说明::

    "title"     在窗口标题栏中显示的标题。
    path        启动目录。
    B           启动应用程序，但不创建新窗口。
                应用程序已忽略 ^C 处理。除非应用程序
                启用 ^C 处理，否则 ^Break 是唯一可以中断
                该应用程序的方式。
    I           新的环境将是传递
                给 cmd.exe 的原始环境，而不是当前环境。
    MIN         以最小化方式启动窗口。
    MAX         以最大化方式启动窗口。
    SEPARATE    在单独的内存空间中启动 16 位 Windows 程序。
    SHARED      在共享内存空间中启动 16 位 Windows 程序。
    LOW         在 IDLE 优先级类中启动应用程序。
    NORMAL      在 NORMAL 优先级类中启动应用程序。
    HIGH        在 HIGH 优先级类中启动应用程序。
    REALTIME    在 REALTIME 优先级类中启动应用程序。
    ABOVENORMAL 在 ABOVENORMAL 优先级类中启动应用程序。
    BELOWNORMAL 在 BELOWNORMAL 优先级类中启动应用程序。
    NODE        将首选非一致性内存结构(NUMA)节点指定为
                十进制整数。
    AFFINITY    将处理器关联掩码指定为十六进制数字。
                进程被限制在这些处理器上运行。

                将 /AFFINITY 和 /NODE 结合使用时，会对关联掩码
                进行不同的解释。指定关联掩码，以便将零位作为起始位置(就如将 NUMA
                节点的处理器掩码向右移位一样)。
                进程被限制在指定关联掩码和 NUMA 节点之间的
                那些通用处理器上运行。
                如果没有通用处理器，则进程被限制在
                指定的 NUMA 节点上运行。
    WAIT        启动应用程序并等待它终止。
    command/program
                如果它是内部 cmd 命令或批文件，则
                该命令处理器是使用 cmd.exe 的 /K 开关运行的。
                这表示运行该命令之后，该窗口
                将仍然存在。

                如果它不是内部 cmd 命令或批文件，则
                它就是一个程序，并将作为一个窗口化应用程序或
                控制台应用程序运行。

    parameters  这些是传递给 command/program 的参数。

注意: 在 64 位平台上不支持 SEPARATE 和 SHARED 选项。

通过指定 /NODE，可按照利用 NUMA 系统中的内存区域的方式创建进程。
例如，可以创建两个完全通过共享内存互相通信的进程以共享相同的首选 NUMA 节点，从而最大限度地减少内存延迟。
只要有可能，它们就会分配来自相同 NUMA 节点的内存，并且会在指定节点之外的处理器上自由运行::

    start /NODE 1 application1.exe
    start /NODE 1 application2.exe

这两个进程可被进一步限制在相同 NUMA 节点内的指定处理器上运行。
在以下示例中，application1 在节点的两个低位处理器上运行，而 application2在该节点的其后两个处理器上运行。
该示例假定指定节点至少具有四个逻辑处理器。请注意，节点号可更改为该计算机的任何有效节点号，而无需更改关联掩码::

    start /NODE 1 /AFFINITY 0x3 application1.exe
    start /NODE 1 /AFFINITY 0xc application2.exe

如果命令扩展被启用，通过命令行或 START 命令的外部命令调用会如下改变:

将文件名作为命令键入，非可执行文件可以通过文件关联调用。
    (例如，WORD.DOC 会调用跟 .DOC 文件扩展名关联的应用程序)。
    关于如何从命令脚本内部创建这些关联，请参阅 ASSOC 和 FTYPE 命令。

执行的应用程序是 32 位 GUI 应用程序时，CMD.EXE 不等应用程序终止就返回命令提示符。
如果在命令脚本内执行，该新行为则不会发生。

如果执行的命令行的第一个符号是不带扩展名或路径修饰符的字符串 "CMD"，"CMD" 会被 COMSPEC 变量的数值所替换。
这防止从当前目录提取 CMD.EXE。

如果执行的命令行的第一个符号没有扩展名，CMD.EXE 会使用PATHEXT 环境变量的数值来决定要以什么顺序寻找哪些扩展名。
PATHEXT 变量的默认值是::

  .COM;.EXE;.BAT;.CMD

请注意，该语法跟 PATH 变量的一样，分号隔开不同的元素。

查找可执行文件时，如果没有相配的扩展名，看一看该名称是否与目录名相配。
如果确实如此，START 会在那个路径上调用Explorer。
如果从命令行执行，则等同于对那个路径作 CD /D。

批处理中调用外部程序的命令（该外部程序在新窗口中运行，批处理程序继续往下执行，不理会外部程序的运行状况），
如果直接运行外部程序则必须等外部程序完成后才继续执行剩下的指令

例::

  start explorer d:\

调用图形界面打开D盘

有一类似指令 call 与区别, 见 :doc:`/docs/操作系统/windows/windows_shell/call`

注意: 有时候使用 start 启动时候无效::

  start "C:\user xx\xx.bat"

是因为有个 title 参数, 这时候加个空标题即可::

  start "" "C:\user xx\xx.bat"

