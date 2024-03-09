======================
trap
======================

指定在接收到信号之后将要采取的动作

用法::

  trap "动作" "信号"

支持的信号见: :doc:`/docs/操作系统/linux/概念性/linux系统信号`

例如，收到0信号执行 ``exit 1`` ::

  trap "exit 1" 0

与set协作
======================

:doc:`/docs/操作系统/linux/linux指令/set` 支持在脚本执行错误时退出,
那如果要在退出时候打印一些消息或者清理应该如何做?

``set -e`` 在检查到命令异常返回时并没有信号的产生,
故trap指令就不能写信号了, 而是写bash内置定义的 ``ERR`` (不区分大小写)::

  #!/bin/bash

  error_exit() {
    echo "error, exit"
  }

  set -e
  trap error_exit ERR

  echo 1
  ss
  echo 2
  echo 3

.. note::

  dash中貌似没有内置对ERR的支持

对ERR的说明::

  在 Bash 中，ERR 并不是一个具体的信号。在错误检测机制中，ERR 是对发生错误退出的状态的引用.
  虽然 ERR 不是一个实际的信号，但它可以被 trap 命令捕获和处理.


