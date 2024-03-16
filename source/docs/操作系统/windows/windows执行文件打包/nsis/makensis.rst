======================
makensis指令
======================


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows执行文件打包, nsis
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


使用nsis脚本命令行打包
======================

前置, 设置好环境变量::

  NSISDIR       NISI 安装目录, 与可在脚本定义的 ${NSISDIR} 一致
  NSISCONFDIR   NISI 配置文件目录
  APPDATA(windows) / HOME(not windows)  加载用户配置文件

语法::

  makensis [ option | script.nsi | - ] [...]

选项说明::

  /LICENSE    显示license信息
  /V=<[0-4]>  相关信息输出. 只能是 0-4
              0 不输出
              1 仅error信息
              2 warnings and errors
              3 info, warnings, and errors
              4 所有级别信息

  /P=<[0-5]>  设置安装优先级. 只能是 0-5
              0 空闲(idle)时安装
              1 below normal
              2 normal (default)
              3 above normal
              4 high
              5 realtime. 实时安装?

  /O=<filename>
              将输出写入到 filename (不输出到屏幕).

  /LAUNCH     executes the generated installer.
              执行生成的安装程序

  /PAUSE      makes makensis pause before quitting, which is useful when executing directly from Windows.
              在退出之前暂停

  /NOCONFIG   disables inclusion of nsisconf.nsh. Without this parameter, installer defaults are set from nsisconf.nsh.

  /CMDHELP    prints basic usage information for command (if specified), or all commands (if command is not specified).

  /HDRINFO    prints information about which options were used to compile makensis.

  /NOCD       disables the current directory change to that of the .nsi file

  /INPUTCHARSET   allows you to specify a specific codepage for files without a BOM. (ACP|OEM|CP#|UTF8|UTF16<LE|BE>)

  /OUTPUTCHARSET  allows you to specify the codepage used by stdout when the output is redirected. (ACP|OEM|CP#|UTF8[SIG]|UTF16<LE|BE>[BOM])

  /PPO, /SAFEPPO  will only run the preprocessor and print the result to stdout. The safe version will not execute instructions like !appendfile or !system. !packhdr and !finalize are never executed.

  /WX         treats warnings as errors

  /D          switch one or more times will add to symbols to the globally defined list (See !define).

  /X          switch one or more times will execute the code you specify following it. Example: "/XAutoCloseWindow false"

  Specifying a dash (-) for the script name will tell makensis to use the standard input as a source.


.. note::

  注意参数顺序

  官网: `usage <https://nsis.sourceforge.io/Docs/Chapter3.html#usage>`_





