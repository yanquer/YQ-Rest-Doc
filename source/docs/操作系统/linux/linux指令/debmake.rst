=======================
debmake
=======================


.. post:: 2023-02-27 21:24:23
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


需要构建 `debian` 的软件包(deb包)时,
可通过此命令自动生成需要的deb目录结构.

deb包构建可参考: :doc:`/docs/操作系统/linux/教程/本地构建deb包`

一般与 :doc:`/docs/操作系统/linux/linux指令/debbuild` 一起使用, 如::

  $ tar -xzmf debhello-0.0.tar.gz
  $ cd debhello-0.0
  $ debmake
    ... manual customization
  $ debuild
    ...

