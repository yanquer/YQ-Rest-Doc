========================================
tcping
========================================


.. post:: 2024-03-04 22:04:43
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


与 :doc:`/docs/操作系统/linux/linux指令/ping` 和 :doc:`/docs/操作系统/linux/linux指令/telnet` 都不同,
是一款跨平台的基于Go的, tcp链接检查工具.
使用传输层协议，可以检测IP端口状态和查看ping 值，
即使源地址禁 ping 也可以通过 tcping 来监控服务器网络状态。

Windows下载::

  https://elifulkerson.com/projects/tcping.php

MacOS安装::

  brew install tcping

.. note::

  看了下, 貌似最开始只有win版, 不知道啥写的, 然后是后面才有人用Go根据这个写的其他平台的版本,
  目前排名最高的两个::

    https://github.com/cloverstd/tcping

    # 这个更新勤点
    https://github.com/pouriyajamshidi/tcping

  MacOS下看了下, 用的是收藏量不高的::

    brew info tcping
    ==> tcping: stable 2.1.0 (bottled), HEAD
    TCP connect to the given IP/port combo
    https://github.com/mkirchner/tcping
    /usr/local/Cellar/tcping/2.1.0 (5 files, 39.4KB) *
      Poured from bottle using the formulae.brew.sh API on 2024-03-04 at 10:07:05
    From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/t/tcping.rb
    License: MIT

用法::

  tcping [-q] [-f <4|6>] [-t timeout_sec] [-u timeout_usec] <host> <port>



举例::

  ### 默认端口为80
  tcping google.com

  ### 带上80端口
  tcping google.com 80

  ### 带上443端口
  tcping google.com 443

  ### 多个端口
  tcping google.com 80 443

  ### 连续的端口
  tcping google.com 80-85

  ### 多个连续的端口
  tcping google.com 80-83 443-445

  ### IPV6 地址
  tcping [::1]


