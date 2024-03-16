=====================
debian查看版本
=====================


.. post:: 2024-02-21 21:55:17
  :tags: linux, debian
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


在 Debian 或基于 Debian 的 Linux 发行版中，有多种方法可以查看当前系统的版本信息：

使用 lsb_release 命令::

  lsb_release -a

这个命令可以显示当前系统的发行版名称、版本号、Codename 和描述信息。

查看 /etc/issue 文件::


   cat /etc/issue


这个文件包含了当前系统的版本和发行版信息。

查看 /etc/os-release 文件::

  cat /etc/os-release

这个文件包含了当前系统的发行版名称、版本号、ID 和描述信息。

使用 uname 命令::

   uname -a

这个命令可以显示当前系统的内核版本、主机名和操作系统类型等信息。

其中，lsb_release 命令是最常用的方法之一，可以提供比较详细的系统版本信息。如果您只需要查看基本的版本信息，可以使用其他方法。

