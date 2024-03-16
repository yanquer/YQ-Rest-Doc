===================================
procfs 和 sysfs
===================================


.. post:: 2023-02-27 21:24:23
  :tags: linux, debian, debian手册
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


`procfs <https://zh.wikipedia.org/wiki/Procfs>`_ 和
`sysfs <https://zh.wikipedia.org/wiki/Sysfs>`_ 两个伪文件系统，
分别加载于 `/proc` 和 `/sys` 之上，
将内核中的数据结构暴露给用户空间。
或者说，这些条目是虚拟的，他们打开了深入了解操作系统运行的方便之门。

目录 `/proc` 为每个正在运行的进程提供了一个子目录，
目录的名字就是进程标识符（PID）。
需要读取进程信息的系统工具，如 `ps` ，可以从这个目录结构获得信息。

`/proc/sys` 之下的目录，
包含了可以更改某些内核运行参数的接口。
（你也可以使用专门的 `sysctl` () 命令修改，或者使用其预加载/配置文件 `/etc/sysctl.conf` ）

当人们看到这个特别大的文件 `/proc/kcore` 时，常常会惊慌失措。
这个文件于你的的电脑内存大小相差不多。
它被用来调试内核。它是一个虚拟文件，指向系统内存，所以不必担心它的大小。

`/sys` 以下的目录包含了内核输出的数据结构，它们的属性，以及它们之间的链接。
它同时也包含了改变某些内核运行时参数的接口。

参考::

  proc.txt(.gz)
  sysfs.txt(.gz)

  以及其他相关的Linux内核文档

  /usr/share/doc/linux-doc-*/Documentation/filesystems/*

  这些文件由 `linux-doc-*` 软件包提供。




