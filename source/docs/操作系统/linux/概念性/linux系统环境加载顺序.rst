==============================
linux系统环境加载顺序
==============================

登陆shell(login shell)
==============================

取得 bash 时需要完整的登陆流程的，就称为 login shell.
比如通过ssh方式连接，或者由tty1 ~ tty6 登陆，
需要输入用户的账号与密码，此时取得的 bash 就称为login shell

当我们在终端上运行 `bash`、`zsh` 等命令登录系统时,启动的shell就是登录shell。
它的环境变量加载顺序是:

- /etc/profile 此文件为系统的每个用户设置环境信息，当用户第一次登录时，该文件被执行。 并从/etc/profile.d目录的配置文件中搜集shell的设置。
- /etc/bashrc 为每一个运行bash shell的用户执行此文件。当bash shell被打开时，该文件被读取。
- ~/.bash_profile 每个用户都可使用该文件输入专用于自己使用的shell信息，当用户登录时，该文件仅仅执行一次！默认情况下，他设置一些环境变量，执行用户的。bashrc文件。
- ~/.bash_login
- ~/.profile
- ~/.bashrc 该文件包含专用于你的bash shell的bash信息，当登录时以及每次打开新的shell时，该该文件被读取。
- ~/.bash_logout 当每次退出系统（退出bash shell）时，执行该文件。
  另外，/etc/profile中设定的变量（全局）的可以作用于任何用户，而~/.bashrc等中设定的变量（局部）只 能继承/etc/profile中的变量，他们是"父子"关系。
- ~/.bash_profile 是交互式、login 方式进入 bash 运行的
  ~/.bashrc 是交互式 non-login 方式进入 bash 运行的通常二者设置大致相同，所以通常前者会调用后者。

非登陆shell(non-login shell)
==============================

取得 bash 接口的方法不需要重复登陆的举动.
比如你以 X window 登陆 Linux 后， 再以 X 的图形化接口启动终端机，
此时该终端接口无需输入账号与密码，则为non-login shell;
又比如你在原本的 bash 环境下再次下达 bash 这个命令，
同样的也没有输入账号密码， 那第二个 bash (子程序) 也是 non-login shell.

当我们在终端上运行 `bash -c 'command'` 或在GUI程序中启动shell时,启动的shell就是非登录shell。
它的环境变量加载顺序是:

- /etc/bash.bashrc
- ~/.bashrc

.. note::

  可以通过 echo $0 查看属于那种Shell

演示
==============================

演示环境::

  [root@system1 ~]# more /etc/redhat-release
  Red Hat Enterprise Linux Server release 7.0 (Maipo)

当前从ssh登陆到服务器::

  [root@system1 ~]# tty
  /dev/pts/1

输入 echo $0， 显示结果为 -bash ，即为登陆shell::

  [root@system1 ~]# echo $0
  -bash
  [root@system1 ~]# ps
    PID TTY          TIME CMD
  77122 pts/1    00:00:00 bash
  77157 pts/1    00:00:00 ps

下面在X windows打开一个终端，如下，显示为/bin/bash，即非登陆shell::

  [root@system1 Desktop]# echo $0
  /bin/bash

  [root@system1 ~]# ps -ef|grep pts|grep bash
  root      73245  73241  0 11:49 pts/0    00:00:00 /bin/bash
  root      76511  73245  0 16:19 pts/0    00:00:00 bash
  root      77122  77118  0 17:02 pts/1    00:00:00 -bash
  root      77158  77118  0 17:03 pts/2    00:00:00 -bash
  root      77210  73241  0 17:04 pts/3    00:00:00 /bin/bash
  root      77283  77279  0 17:06 pts/4    00:00:00 -bash
  root      77332  77122  0 17:06 pts/1    00:00:00 grep --color=auto bash

在上传的结果中73245，77210为非登陆shell，77122，77158，77283为登陆shell


交互式shell(interactive shell)
============================================================

交互式模式就是在终端上执行，shell等待你的输入，并且立即执行你提交的命令。
这种模式被称作交互式是因为shell与用户进行交互。
这种模式也是大多数用户非常熟悉的：登录、执行一些命令、退出。当你退出后，shell也终止了。

无论是登录shell还是非登录shell,只要它 attach 到当前终端并接受用户的输入,
那它就是一个交互式shell。
交互式shell的环境变量加载顺序包括:

- 登录shell或非登录shell加载的所有文件
- ~/.inputrc

非交互式shell(non-interactive shell)
============================================================

shell也可以运行在另外一种模式：非交互式模式，以shell script(非交互)方式执行。
在这种模式 下，shell不与你进行交互，而是读取存放在文件中的命令,并且执行它们。
当它读到文件的结尾EOF，shell也就终止了。

如果一个shell在后台执行,不接受任何用户输入,那么它就是非交互式shell。非交互式shell仅加载:

- 登录shell加载的文件(/etc/profile和~/.bash_profile)
- 非登录shell加载的文件(/etc/bash.bashrc)

如下，执行 echo $-，查看其中的“i”选项（表示interactive shell）::

  [root@system1 ~]# echo $-
  himBH

如下，为非交互shell::

  [root@system1 ~]# echo 'echo $-' | bash
  hB

环境变量的调用顺序
==============================

对于登陆shell，读取~/.bash_profile配置文件时，会做出读取顺序判读，如下::

  ~/.bash_profile —> ~/.bash_login  —> ~/.profile

但 bash 的 login shell 配置只会读取上面三个文件的其中一个， 而读取的顺序则是依照上面的顺序。
也就是说，如果 ~/.bash_profile 存在，那么其他两个文件不论有无存在，都不会被读取。
如果 ~/.bash_profile 不存在才会去读取 ~/.bash_login，而前两者都不存在才会读取 ~/.profile 的意思。

在shell登出时会读取 ~/.bash_logout

**属于非登录shell：不需要输入密码的登录及远程 SSH 连接——>  ~/.bashrc（用户文件U2）——>/etc/bashrc（全局文件G2）**

如果用户的Shell 不是登录时启动的（比如手动敲下 bash 时启动或者其他不需要输入密码的登录及远程 SSH 连接情况）
那么这种非登录 Shell 只会加载 `~/.bashrc`（用户环境变量文件），并会去找 `/etc/bashrc`（全局环境变量文件），
因此如果希望在非登录 Shell 下也可读到设置的环境变量等内容，
就需要将变量设定写入 `~/.bashrc` 或者 `/etc/bashrc`，而不是 `~/.bash_profile` 或 `/etc/profile`

环境变量相关文件
==============================

- /etc/profile：系统配置文件，用户登录时读取一次
- /etc/profile.d: 系统配置文件夹, 一般下面的 `.sh` 文件会在/etc/profile加载之后进行加载
- /etc/bash.bashrc：（Ubuntu）系统配置文件，用户登录时读取一次，每次打开一个新终端会话时读取一次。
- /etc/bashrc： （Centos）系统配置文件，用户登录时读取一次，每次打开一个新终端会话时读取一次。
- ~/.profile（~/.bash_profile、~/.bash_login）：用户配置文件，用户登录时读取一次
- ~/.bashrc：用户配置文件，用户登录时读取一次，每次打开一个新终端会话时读取一次

对于 ~/.bash_profile、~/.bash_login、~/.profile，如果终端绑定的是 bash，
则按照顺序进行读取（如果存在，就不继续读取）

- 系统配置文件作用于全局，而用户配置文件仅针对当前登录的用户
- 先读取系统配置文件，再读取用户配置文件，用户配置文件的变量和表达式等都继承自系统配置文件


