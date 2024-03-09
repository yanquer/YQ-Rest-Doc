=============================
tasklist
=============================

查看所有进程, 想找类似与linux下 ps 时找到的::

  PS C:\Users\yanque> tasklist

  映像名称                       PID 会话名              会话#       内存使用
  ========================= ======== ================ =========== ============
  System Idle Process              0 Services                   0          8 K
  System                           4 Services                   0      3,568 K
  Registry                       268 Services                   0     55,028 K
  smss.exe                       936 Services                   0      1,032 K
  csrss.exe                     1212 Services                   0      6,520 K
  wininit.exe                   1312 Services                   0      6,996 K
  services.exe                  1384 Services                   0     10,852 K
  lsass.exe                     1408 Services                   0     28,764 K
  svchost.exe                   1528 Services                   0     31,748 K
  fontdrvhost.exe               1556 Services                   0      2,976 K

查看帮助::

  C:\Users\烟雀>tasklist /?

语法::

  TASKLIST [/S system [/U username [/P [password]]]]
           [/M [module] | /SVC | /V] [/FI filter] [/FO format] [/NH]

描述::

    该工具显示在本地或远程机器上当前运行的进程列表。


参数列表:
   /S     system           指定连接到的远程系统。

   /U     [domain\]user    指定应该在哪个用户上下文执行这个命令。

   /P     [password]       为提供的用户上下文指定密码。如果省略，则
                           提示输入。

   /M     [module]         列出当前使用所给 exe/dll 名称的所有任务。
                           如果没有指定模块名称，显示所有加载的模块。

   /SVC                    显示每个进程中主持的服务。

   /APPS 显示 Microsoft Store 应用及其关联的进程。

   /V                      显示详细任务信息。

   /FI    filter           显示一系列符合筛选器
                           指定条件的任务。

   /FO    format           指定输出格式。
                           有效值: "TABLE"、"LIST"、"CSV"。

   /NH                     指定列标题不应该
                           在输出中显示。
                           只对 "TABLE" 和 "CSV" 格式有效。

   /?                      显示此帮助消息。

筛选器::

    筛选器名称        有效运算符                  有效值
    -----------     ---------------           --------------------------
    STATUS          eq, ne                    RUNNING | SUSPENDED
                                              NOT RESPONDING | UNKNOWN
    IMAGENAME       eq, ne                    映像名称
    PID             eq, ne, gt, lt, ge, le    PID 值
    SESSION         eq, ne, gt, lt, ge, le    会话编号
    SESSIONNAME     eq, ne                    会话名称
    CPUTIME         eq, ne, gt, lt, ge, le    CPU 时间，格式为
                                              hh:mm:ss。
                                              hh - 小时，
                                              mm - 分钟，ss - 秒
    MEMUSAGE        eq, ne, gt, lt, ge, le    内存使用(以 KB 为单位)
    USERNAME        eq, ne                    用户名，格式为
                                              [域\]用户
    SERVICES        eq, ne                    服务名称
    WINDOWTITLE     eq, ne                    窗口标题
    模块         eq, ne                    DLL 名称

注意: 当查询远程计算机时，不支持 "WINDOWTITLE" 和 "STATUS"
      筛选器。

Examples::

    TASKLIST
    TASKLIST /M
    TASKLIST /V /FO CSV
    TASKLIST /SVC /FO LIST
    TASKLIST /APPS /FI "STATUS eq RUNNING"
    TASKLIST /M wbem*
    TASKLIST /S system /FO LIST
    TASKLIST /S system /U 域\用户名 /FO CSV /NH
    TASKLIST /S system /U username /P password /FO TABLE /NH
    TASKLIST /FI "USERNAME ne NT AUTHORITY\SYSTEM" /FI "STATUS eq running"



