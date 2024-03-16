============================
Linux下DISPLAY作用
============================


.. post:: 2024-02-21 21:55:17
  :tags: linux, Linux环境变量
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


DISPLAY用来设置将图形显示到何处, 或者说设置或显示当前的显示环境
(指定X服务器的现实设备)

格式::

  hostname:display.number.screen.number

- hostname表示运行X服务器的主机名或IP地址
- display.number表示X服务器的编号
- screen.number表示屏幕的编号

默认值:
  当你在终端中启动X服务器时，系统会自动设置DISPLAY环境变量的值。
  通常情况下，默认值为:0.0，表示使用本地主机上的第一个X服务器和第一个屏幕。

显示当前的显示环境::

  echo $DISPLAY

一些常见使用
============================

设置显示环境
----------------------------

设置显示环境为本地显示器::

  export DISPLAY=:0

设置显示环境为第二个本地显示器::

  export DISPLAY=:1

设置显示环境为ip地址的第一显示器::

  export DISPLAY=ip:0

控制X11程序在哪个显示器上启动
--------------------------------------------------------

当设置了display变量后,启动的X11程序默认会在该显示环境打开。

例如, 在第二个显示器上启动xterm::

  export DISPLAY=:1
  xterm

运行远程程序
----------------------------

在本地显示远程linux服务器上的图形界面程序::

  ssh -X remote_server
  export DISPLAY=localhost:0.0    # 设置远程显示环境为本地显示器
  xterm                           # 远程服务器上的xterm将显示在本地显示器上

特殊情况, 提权后的变化
============================

主要针对使用 sudo, su, pkexec 这类指令.

- 设定当前登录普通用户为 `bob`
- 测试机器, ubuntu20

场景1: 使用 ``sudo su`` 切换root
--------------------------------------------------------

效果是切到到了root, 仅保留了最初用户(切换时使用的用户bob)的环境变量.

这个时候, DISPLAY的值没有变化

场景2: 使用 ``sudo su -`` 切换root
--------------------------------------------------------

效果是切到到了root, 同时加载root环境变量.

这个时候, DISPLAY的值是空字符串(root环境变量没有指定时)

场景3: 使用 ``pkexec <cmd>`` 切换root
--------------------------------------------------------

效果是只能以root身份执行当次cmd, 会保留用户bob的 DISPLAY 值,
但是, 使用的这个DISPLAY界面是受限制的,
pkexec启动的图形程序会在一个纯净和受限的X session下运行

实际场景: pkexec + sudo
--------------------------------------------------------

实际的应用场景就是 `pkexec` 的 `cmd` 做了一些操作后, 启动图形界面
时(比如存在SDL依赖), 需要以bob的身份启动::

  pkexec bash -c "xxx; sudo -u bob start_app"

这个时候就报错::

  failed to initialize SDL: No available video device

虽然pkexec会保留, 但是效果貌似还是行, 需要在pkexec之前手动重置::

  pkexec bash -c "export DISPLAY=$DISPLAY; sudo -u bob start_app"
  # pkexec bash -c "env DISPLAY=$DISPLAY sudo -u bob start_app"

脚本中使用 `export DISPLAY` 或 `env DISPLAY` , 一直会出现export这一步卡住的问题,
暂时没有找到原因. 不排除是 pkexec 使用了一些安全机制来隔离和限制启动进程的权限,
如对环境变量的修改, 导致 export 这一步会永远等待 ,看起来就像卡住了一样.

但是直接在命令行执行又不会卡, 就很懵.
且不export或者不env时候, 打印出的 DISPLAY 值是正确的,
必须得显示设置一下, 才能正常启动(我这里是启动的SDL).
而同事的 `ubuntu18` 又没有这个问题...

又尝试了一下, 发现直接::

  pkexec bash xxx.sh

而 `xxx.sh` 内部是读不到 `DISPLAY` 的值的.
卡的原因也找到了, 脚本加了::

  set -eu

因为没有定义 `DISPLAY` , 所以使用的时候直接退出了(-u)

.. note::

  这里没搞懂是根据什么来判断受限的, 试过不重置, 子进程也能正常获取到DISPLAY.

  为什么export能清除掉受限状态.






