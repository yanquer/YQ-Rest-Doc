=============================
exec
=============================


.. post:: 2023-02-26 21:30:12
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


用于调用并执行指令的命令。

exec命令通常用在shell脚本程序中，可以调用其他的命令。
如果在当前终端中使用命令，则当指定的命令执行完毕后会立即退出终端。

语法::

  exec(选项)(参数)

选项

-c    在空环境中执行指定的命令。

如::

  exec -c echo Linux C++          # 调用命令执行，执行完毕后退出


