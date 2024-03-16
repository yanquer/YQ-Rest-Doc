======================
pkexec
======================


.. post:: 2023-02-27 21:24:23
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


linux桌面系统下申请提权指令, 是一个用于Linux的通用工具，
它并不限于特定的桌面环境. 可在多个桌面系统中使用，包括但不限于:

- GNOME
- KDE Plasma
- Xfce
- LXQt
- Cinnamon
- MATE

用法::

  pkexec [--user username] <需要提权的指令/程序> [参数列表]

特别说明, pkexec执行脚本时, 虽然可能会一开始有 `DISPLAY` ,
但是使用bash执行脚本时, 不会自动将 `DISPLAY` 这个环境变量给读进去,
如::

  pkexec bash xxx.sh

`xxx.sh` 脚本内获取的 `DISPLAY` 为空, 详见 :doc:`/docs/操作系统/linux/Linux环境变量/DISPLAY`
