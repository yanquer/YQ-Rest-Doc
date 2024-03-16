===========================
setlocal
===========================


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


开始批处理文件中环境改动的本地化操作。在执行 SETLOCAL 之后所做的环境改动只限于批处理文件。
要还原原先的设置，必须执行 ENDLOCAL。
达到批处理文件结尾时，对于该批处理文件的每个尚未执行的 SETLOCAL 命令，都会有一个隐含的 ENDLOCAL 被执行。

SETLOCAL

如果启用命令扩展，则 SETLOCAL 更改如下:

SETLOCAL 批命令现在可以接受可选参数::

        ENABLEEXTENSIONS / DISABLEEXTENSIONS
            启用或禁用命令处理器扩展。这些
            参数比 CMD /E:ON 或 /E:OFF
            开关有优先权。请参阅 CMD /? 获取详细信息。
        ENABLEDELAYEDEXPANSION / DISABLEDELAYEDEXPANSION
            启用或禁用延缓环境变量
            扩展。这些参数比 CMD
            /V:ON 或 /V:OFF 开关有优先权。请参阅 CMD /? 获取详细信息。

无论在 SETLOCAL 命令之前的设置是什么，这些修改会一直
生效，直到出现相应的 ENDLOCAL 命令。

在给定参数的情况下，
SETLOCAL 命令将设置 ERRORLEVEL 值。如果给定两个有效参数中的一个，另一个未给定，
则该值为零。
通过以下方法，你可以在批脚本中
使用此项来确定扩展是否可用::

    VERIFY OTHER 2>nul
    SETLOCAL ENABLEEXTENSIONS
    IF ERRORLEVEL 1 echo Unable to enable extensions

此方法之所以有效，是因为在 CMD.EXE 的旧版本上，SETLOCAL
不设置 ERRORLEVEL 值。如果参数不正确，VERIFY 命令会将
ERRORLEVEL 值初始化为非零值。


