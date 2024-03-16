================
mode
================


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


配置系统设备。

串行端口::

  MODE COMm[:] [BAUD=b] [PARITY=p] [DATA=d] [STOP=s]
                [to=on|off] [xon=on|off] [odsr=on|off]
                [octs=on|off] [dtr=on|off|hs]
                [rts=on|off|hs|tg] [idsr=on|off]

设备状态::

  MODE [device] [/STATUS]

打印重定向::

  MODE LPTn[:]=COMm[:]

选择代码页::

  MODE CON[:] CP SELECT=yyy

代码页状态::

  MODE CON[:] CP [/STATUS]

显示模式::

  MODE CON[:] [COLS=c] [LINES=n]

击键率::

  MODE CON[:] [RATE=r DELAY=d]

例::

  mode con cols=113 lines=15 & color 9f

此命令设置DOS窗口大小：15行，113列

