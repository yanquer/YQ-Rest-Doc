================================
script
================================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


创建终端会话的 `text/x-script`, 记录终端会话并生成可重播的脚本

用法::

  script [option] [file]

支持的选项:

-a, --append
  增加到输出. 在现有输出录制的文件的内容上追加新的内容
-c, --command <command>
  直接执行给定的command指令而不是启动一个交互式终端.
-r
  子进程中返回退出代码
-e, --return
  return exit code of the child process
-f, --flush
  run flush after each write

  如果需要在输出到日志文件的同时，也可以查看日志文件的内容
  ，可以使用 -f 参数

  PS:可以用于教学,两个命令行接-f可以实时演示

--force
  use output file even when it is a link
-q, --quiet
  be quiet. 使script命令以静默模式运行
-V, --version
  output version information and exit.
  输出script的版本信息，然后退出
-h, --help
  display this help and exit
  输出script的帮助信息，然后退出.

-t, --timing[=<file>]
  output timing data to stderr (or to FILE).
  指明输出录制的时间数据


如, 记录终端的输出到文件::

  script -c "pv some_file.txt" /tmp/out.cast

结合用例说明
================================

script 指令可以用来记录终端会话并生成可重播的脚本。
使用script时,它会创建一个类型为text/x-script的文件,这个文件中包含了你在终端中所有操作的记录,包括输入和输出。

例如::

  script demo.script

这将启动 script,并将你的终端记录写入 demo.script 文件。
在这个会话结束后,demo.script 就包含了一个可以重播你所有操作的脚本。

可以用如下命令回放这个会话脚本::

  scriptreplay demo.script

它将逐步重现你之前在终端中的所有操作。

