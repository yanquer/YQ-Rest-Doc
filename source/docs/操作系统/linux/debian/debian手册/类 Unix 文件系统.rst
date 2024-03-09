======================================
类 Unix 文件系统
======================================

在GNU/Linux和其他 `类Unix <https://zh.wikipedia.org/wiki/Unix-like>`_ 操作系统中，
`文件 <https://zh.wikipedia.org/wiki/Computer_file>`_ 被组织到
`目录 <https://zh.wikipedia.org/wiki/Directory_(file_systems)>`_ 中。
所有的文件和目录排放在以 “`/`” 为根的巨大的树里。
叫它树是因为如果你画出文件系统，它看起来就像一棵树，但是它是颠倒过来的。

这些文件和目录可以分散在多个设备中。
:doc:`/docs/操作系统/linux/linux指令/mount` 用于把某个设备上找到的文件系统附着到巨大的文件树上。
相反的， `umount` 把它再次分离。
在最近的 Linux 内核里， `mount`
带某些参数时可以把文件树的一部分绑定到另外的地方，
或者可以把文件系统挂载为共享的、私有的、从设备、或不可绑定的。
对每个文件系统支持的挂载选项可以在 `/usr/share/doc/linux-doc-*/Documentation/filesystems/` 找到。

Unix系统上叫做 **目录** ，
某些其他系统上叫做 **文件夹** 。
请同样留意，在任何Unix系统上，没有的 **驱动器** 的概念，
例如 “`A:`” 。 这只有一个文件系统，并且所有东西都包含在内。
这相对于 Windows 来说是一个巨大的优点。




