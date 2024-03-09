==============
tskill
==============

类似 linux 的 kill, 低配版的 :doc:`/docs/操作系统/windows/windows_shell/taskkill`

结束进程::

  TSKILL processid | processname [/SERVER:servername] [/ID:sessionid | /A] [/V]

    processid           要结束的进程的 Process ID。
    processname         要结束的进程名称。
    /SERVER:servername  含有 processID 的服务器(默认值是当前值)。
                          使用进程名和 /SERVER 时，必须指定 /ID
                          或 /A
    /ID:sessionid       结束在指定会话下运行的进程。
    /A                  结束在所有会话下运行的进程。
    /V                  显示正在执行的操作的信息。

