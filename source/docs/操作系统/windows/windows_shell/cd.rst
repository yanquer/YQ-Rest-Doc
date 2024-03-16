========================
cd
========================


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


显示当前目录名或改变当前目录::

  CHDIR [/D] [drive:][path]
  CHDIR [..]
  CD [/D] [drive:][path]
  CD [..]

    ..   指定要改成父目录。

键入 CD drive: 显示指定驱动器中的当前目录。
不带参数只键入 CD，则显示当前驱动器和目录。

使用 /D 开关，除了改变驱动器的当前目录之外，还可改变当前驱动器。

如果命令扩展被启用，CHDIR 会如下改变:

当前的目录字符串会被转换成使用磁盘名上的大小写。
所以，如果磁盘上的大小写如此，``CD C:\TEMP`` 会将当前目录设为 ``C:\Temp``

CHDIR 命令不把空格当作分隔符，因此有可能将目录名改为一个
带有空格但不带有引号的子目录名。例如::

     cd \winnt\profiles\username\programs\start menu

与下列相同::

     cd "\winnt\profiles\username\programs\start menu"

在扩展停用的情况下，你必须键入以上命令。


特别说明-更新驱动器
========================

一般而言, 直接使用 cd 命令时, 不能更改驱动器,

只有加 /d 选项时, 才支持更改驱动器. 如::

  ; 无效
  C:\Users>cd "D:\Program Files"

  ; 有效
  C:\Users>cd /d  "D:\Program Files"

  D:\Program Files>






