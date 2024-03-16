==================
halt
==================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


halt 命令通知硬件来停止所有的 CPU 功能，但是仍然保持通电。
你可以用它使系统处于低层维护状态。注意在有些情况会它会完全关闭系统。

停止机器::

  halt

关闭机器、关闭电源::

  halt -p

重启机器::

  halt --reboot



