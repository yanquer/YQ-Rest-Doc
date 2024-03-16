==========================
mount
==========================


.. post:: 2023-02-23 23:14:15
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


mount命令

功能：文件挂载

格式::

  mount [-参数] [设备名称] [挂载点]

常用选项：

-a
  安装在/etc/fstab文件中类出的所有文件系统。
-f
  伪装mount，作出检查设备和目录的样子，但并不真正挂载文件系统。
-n
  不把安装记录在/etc/mtab 文件中。
-r
  将文件系统安装为只读。
-v
  详细显示安装信息。
-w
  将文件系统安装为可写，为命令默认情况。
-t <文件系统类型>
  指定设备的文件系统类型，常见的有：
   ext2 是linux目前常用的文件系统
   msdos MS-DOS的fat，就是fat16
   vfat windows98常用的fat32
   nfs 网络文件系统
   iso9660 CD-ROM光盘标准文件系统
   ntfs windows NT/2000/XP的文件系统
   auto 自动检测文件系统
-o <选项>
  指定挂载文件系统时的选项，有些也可写到在 /etc/fstab 中。常用的有：
   defaults 使用所有选项的默认值（auto、nouser、rw、suid）
   auto/noauto 允许/不允许以 –a选项进行安装
   dev/nodev 对/不对文件系统上的特殊设备进行解释
   exec/noexec 允许/不允许执行二进制代码
   suid/nosuid 确认/不确认suid和sgid位
   user/nouser 允许/不允许一般用户挂载
   codepage=XXX 代码页
   iocharset=XXX 字符集
   ro 以只读方式挂载
   rw 以读写方式挂载
   remount 重新安装已经安装了的文件系统
   loop 挂载“回旋设备”以及“ISO镜像文件”
--bind <dir1 dir2>
  命令来将两个目录连接起来，

  mount --bind 命令是将前一个目录挂载到后一个目录上，
  **所有对后一个目录的访问其实都是对前一个目录的访问**

关于 --bind
==========================

`mount --bind test1 test2` 为例，
当 mount --bind 命令执行后，Linux将会把被挂载目录的目录项（也就是该目录文件的block，记录了下级目录的信息）屏蔽，
即test2的下级路径被隐藏起来了（注意，只是隐藏不是删除，数据都没有改变，只是访问不到了）。
同时，内核将挂载目录 `test1` 的目录项记录在内存里的一个s_root对象里，
在mount命令执行时，VFS会创建一个vfsmount对象，这个对象里包含了整个文件系统所有的mount信息，
其中也会包括本次mount中的信息，这个对象是一个HASH值对应表（HASH值通过对路径字符串的计算得来），
表里就有 /test1 到 /test2 两个目录的HASH值对应关系。

命令执行完后，当访问 /test2下的文件时， 系统会告知 /test2 的目录项被屏蔽掉了，
自动转到内存里找VFS，通过 vfsmount 了解到 /test2 和 /test1 的对应关系，
从而读取到 /test1 的inode，这样在 /test2 下读到的全是 /test1 目录下的文件。

- mount --bind连接的两个目录的inode号码并不一样，
  只是被挂载目录的block被屏蔽掉，inode被重定向到挂载目录的inode（被挂载目录的inode和block依然没变）。
- 两个目录的对应关系存在于内存里，一旦重启挂载关系就不存在了。

在固件开发过程中常常遇到这样的情况：为测试某个新功能，必需修改某个系统文件。
而这个文件在只读文件系统上（总不能为一个小小的测试就重刷固件吧），
或者是虽然文件可写，但是自己对这个改动没有把握，不愿意直接修改。这时候 mount --bind 就是你的好帮手。

假设我们要改的文件是/etc/hosts，可按下面的步骤操作:

1. 把新的hosts文件放在/tmp下。 当然也可放在硬盘或U盘上。
2. ``mount --bind /tmp/hosts /etc/hosts``,
    此时的/etc目录是可写的，所做修改不会应用到原来的/etc目录，
    可以放心测试。测试完成了执行 ``umount /etc/hosts`` 断开绑定(可参考: :doc:`umount`)

例如::

   ## test1 test2为两个不同的目录
   linux-UMLhEm:/home/test/linux # ls test1
   11.test  1.test
   linux-UMLhEm:/home/test/linux # ls test2
   22.test  2.test
   linux-UMLhEm:/home/test/linux # ls -lid test1
   1441802 drwx------ 2 root root 4096 Feb 13 09:50 test1
   linux-UMLhEm:/home/test/linux # ls -lid test2
   1441803 drwx------ 2 root root 4096 Feb 13 09:51 test2

   ## 执行mount --bind 将test1挂载到test2上，inode号都变为test1的inode
   linux-UMLhEm:/home/test/linux # mount --bind test1 test2
   linux-UMLhEm:/home/test/linux # ls -lid test1
   1441802 drwx------ 2 root root 4096 Feb 13 09:50 test1
   linux-UMLhEm:/home/test/linux # ls -lid test2
   1441802 drwx------ 2 root root 4096 Feb 13 09:50 test2
   linux-UMLhEm:/home/test/linux # ls test2
   11.test  1.test

参考: `mount --bind使用方法 <https://www.cnblogs.com/xingmuxin/p/8446115.html>`_

.. _Disk-Partition-mount:

扩展可用存储空间
==========================

方案1: 使用 --bind
--------------------------

如果你在另一个分区里有一个带有可用空间的空目录（例如 `/path/to/emp-dir` ），
你可以通过带有 “ `--bind` ” 选项的 mount ，
将它挂载到一个你需要更多空间的目录（例如 `work-dir` ）::

  $ sudo mount --bind /path/to/emp-dir work-dir

.. note::

  这个只是相当于用 `/path/to/emp-dir` 暂时将 `work-dir` 屏蔽,
  信息保存与内存中, **只建议测试使用**

方案2: 使用 -t overlay
--------------------------

通过 overlay 挂载（overlay-mounting）另一个目录来扩展可用存储空间

如果你在另一个分区表中有可用的空间（例如， `/path/to/empty` 和  `/path/to/work` ），
你可以在其中建立一个目录并堆栈到你需要空间的那个旧的目录（例如， `/path/to/old` ），
要这样做，你需要用于 Linux 3.18 版内核或更新版本（对应 Debian Stetch 9.0 或更新版本）
的 `OverlayFS <https://en.wikipedia.org/wiki/OverlayFS>`_ ::

  $ sudo mount -t overlay overlay \
    -olowerdir=/path/to/old-dir,upperdir=/path/to/empty,workdir=/path/to/work

`/path/to/empty` 和 `/path/to/work` 应该位于可读写的分区，从而能够写入 `/path/to/old`



