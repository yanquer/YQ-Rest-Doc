===========================
launchctl
===========================


.. post:: 2023-02-20 22:06:49
  :tags: Mac, Mac指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


MacOS不像 Linux 有 ``/etc/init.d/rc.local``
以及 ``service`` 的方式可以设置程序随机启动，
而是使用 plist 文件管理.

你可以写一个plist文件放到 ``~/Library/Launch Agents/`` 下面，
文件里描述你的程序路径和启动参数，
那么这个用户登录时就会启动这个程序了，而且是杀不了的，被杀了之后会自动重新启动

plist文件分布在::

  /System/Library/LaunchDaemons/
      System-wide daemons provided by OS X
      其中 apache的httpd程序启动配置文件 org.apache.httpd.plist 就在这里。
  /System/Library/LaunchAgents/
      由Mac OS X为用户定义的任务项
  /Library/LaunchDaemons
      由管理员定义的守护进程任务项
  /Library/LaunchAgents
      由管理员为用户定义的任务项
      如果放到/Library/Launch Agents/下面的话，就是一开机就启动
  ~/Library/LaunchAgents
    由用户自己定义的任务

这些配置文件由程序 **launchctl** 设置是否加载

说明
  launchctl 管理 MacOS 的启动脚本，控制启动计算机时需要开启的服务.
  也可以设置定时执行特定任务的脚本，就像Linux :doc:`cron </docs/操作系统/linux/linux指令/crond>` 一样.

  launchctl需要root权限。

常用命令
===========================

显示当前的启动脚本::

  launchctl list

开机时自动启动Apache服务器::

  sudo launchctl load -w /System/Library/LaunchDaemons/org.apache.httpd.plist

设置开机启动并立即启动改服务::

  launchctl load -w   **.pist

设置开机启动但不立即启动服务::

  launchctl load **.pist

停止正在运行的启动脚本::

  sudo launchctl unload [path/to/script]

再加上-w选项即可去除开机启动::

  sudo launchctl unload -w [path/to/script]

执行定时脚本|设置开机启动步骤::

  1. 写执行脚本 （通过 brew 安装软件 brew 会为我们自动生成。）
  2. 去对应的目录下建立plist文件
  3. 加载服务
      > 1 cd 进入指定 plist 文件目录
      > 2 launchctl load *.plist #加载
          launchctl unload *.plist #取消
      > 3 launchctl list #查看服务

还可设置别名便于操作::

  1. vim ~/.bash_profile #编辑添加如下脚本
  2. 命名别名（以 nginx 为例）
      > 启动：alias nginx.start=’launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist’
      > 关闭：alias nginx.stop=’launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist’
      > 重启：alias nginx.restart=’nginx.stop && nginx.start’

.. note::

  - 在launchctl list 命令结果中出现的 plist 文件才会有效;
  - Agents文件夹下的plist是需要用户登录后，才会加载的，
    而Daemons文件夹下得plist是只要开机，可以不用登录就会被加载

参考: `MacOS launchctl 启动进程控制 <https://www.jianshu.com/p/baa23cc820d2>`_

用例-查找docker进程并关闭
===========================

list查找然后关闭和启动它::

  $ launchctl list | grep docker
  111117   0       com.docker.docker.2388
  $ launchctl stop com.docker.docker.2388 && launchctl start com.docker.docker.2388





