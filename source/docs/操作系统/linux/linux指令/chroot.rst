=========================
chroot
=========================

参考: `<https://www.cnblogs.com/sparkdev/p/8556075.html>`_

即 change root directory (更改 root 目录)。

在 linux 系统中，系统默认的目录结构都是以 /，即以根 (root) 开始的。
而在使用 chroot 之后，系统的目录结构将以指定的位置作为 / 位置。

可以用它来简单的实现文件系统的隔离。
但在一个容器技术繁荣的时代，用 chroot 来进行资源的隔离实在是 low 了点。
所以 chroot 的主要用途还是集中在系统救援、维护等一些特殊的场景中。

语法::

  chroot NEWROOT [COMMAND [ARG]...]

.. sidebar:: 为什么要使用 chroot 命令

  - 增加了系统的安全性，限制了用户的权力:
    在经过 chroot 之后，在新根下将访问不到旧系统的根目录结构和文件，这样就增强了系统的安全性。
    一般会在用户登录前应用 chroot，把用户的访问能力控制在一定的范围之内。
  - 建立一个与原系统隔离的系统目录结构，方便用户的开发:
    使用 chroot 后，系统读取的是新根下的目录和文件，这是一个与原系统根下文件不相关的目录结构。
    在这个新的环境中，可以用来测试软件的静态编译以及一些与系统不相关的独立开发。
  - 切换系统的根目录位置，引导 Linux 系统启动以及急救系统等:
    chroot 的作用就是切换系统的根位置，而这个作用最为明显的是在系统初始引导磁盘的处理过程中使用，
    从初始 RAM 磁盘 (initrd) 切换系统的根位置并执行真正的 init. 比如文末的用例.

参数选项
=========================

如果不给 chroot 指定执行的命令，默认它会执行 '${SHELL} -i'，而我的系统中 ${SHELL} 为 /bin/bash。

通过 chroot 运行 busybox 工具
==================================================

busybox 包含了丰富的工具，我们可以把这些工具放置在一个目录下，然后通过 chroot 构造出一个 mini 系统。

简单起见我们直接使用 docker 的 busybox 镜像打包的文件系统。先在当前目录下创建一个目录 rootfs::

  $ mkdir rootfs

然后把 busybox 镜像中的文件释放到这个目录中::

  $ (docker export $(docker create busybox) | tar -C rootfs -xvf -)

通过 ls 命令查看 rootfs 文件夹下的内容::

  $ ls rootfs

执行 chroot 后的 ls 命令::

  $ sudo chroot rootfs /bin/ls

虽然输出结果与刚才执行的 ls rootfs 命令形同，但是这次运行的命令却是 rootfs/bin/ls。

运行 chroot 后的 pwd 命令::

  $ sudo chroot rootfs /bin/pwd
  /

可以看出直接把rootfs当作根目录.

检查程序是否运行在 chroot 环境下
==================================================

通过 /proc 目录下的文件检查进程的中的根目录

如当打开一个sh会话::

  sudo chroot rootfs /bin/sh

检查/bin/sh根目录::

  pid=$(pidof -s sh)
  sudo ls -ld /proc/$pid/root

结果会打印实际的链接地址.

实例：通过 chroot 重新设置 root 密码
==================================================

systemd 的管理机制中，rescure 模式和 emeryency 模式是无法直接取得 root 权限的，
需要使用 root 密码才能进入 rescure 和 emeryency 环境。

可以为内核的启动指定 "rd.break" 参数，从而让系统在启动的早期停下来，
此时我们可以通过使用 root 权限并结合 chroot 命令完成设置 root 密码的操作。

- 在系统启动过程中进入开机菜单时按下字母键 e 进程开机菜单的编辑模式
- 找到以 "linux16 /vmlinuz-" 开头的行。如果默认没有看到该行，需要按向下键把它滚动出来。
  然后定位到该行结尾处，输入一个空格和字符串 " rd.break"
- 接着按下 ctrl + x 以该设置继续启动，启动过程中操作系统会停下来，这是系统启动过程中的一个非常早的时间点
  所以系统的根目录还挂载在 RAM disk 上(就是内存中的一个文件系统)，
  我们可以通过 mount 命令检查系统当前挂载的文件系统::

    mount

  该时间点的最大优势是我们具有 root 权限！开始设置新的 root 密码。
- 把 /sysroot 重新挂载为
  可读写的模式::

    mount -o remount,rw /sysroot

- chroot 命令把根目录切换到我们原来的
  环境中::

    chroot /sysroot

  此时可以理解为：我们以 root 权限登录了原来的系统，修改密码就很容易
- 为 root 用户设置新的
  密码::

    echo "new_root_pw" | passwd --stdin root

- 接下来还要处理 SELinux 相关的问题。由于当前的环境中 SELinux 并未启动，
  所以我们对文件的修改可能造成文件的 context 不正确。
  为了确保开机时重新设定 SELinux context，必須在根目录下添加隐藏文件 .autorelabel::

    touch /.autorelabel

- 从 chroot 中退出，
  并重启系统::

    exit
    reboot

  重新进入登陆界面时就可以使用刚才设置的密码以 root 登陆了


