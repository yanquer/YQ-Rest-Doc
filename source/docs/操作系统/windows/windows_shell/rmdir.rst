================
rmdir
================

删除一个目录

语法::

  RMDIR [/S] [/Q] [drive:]path
  RD [/S] [/Q] [drive:]path

选项::

  /S  递归删除, 用于删除目录树. 类似于 linux rm 的 -r

  /D  安静模式. 类似于 linux rm 的 -f


.. note::

  大小写不敏感, 如::

    rmdir /s xx
