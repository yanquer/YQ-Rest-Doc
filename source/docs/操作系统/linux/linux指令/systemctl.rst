===================
systemctl
===================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


一个systemd工具，主要负责控制systemd系统和服务管理器.
systemd 是许多现代 Linux 发行版（如 Ubuntu、Fedora、Debian 等）的默认初始化系统。
systemd 采用了并行启动方式，提供了更快的启动速度和更高的灵活性。

.. systemctl是RHEL 7 的服务管理工具中主要的工具，

systemctl 是 systemd 的主要命令行工具，用于控制和管理系统服务、挂载点、设备等.
它融合之前 service_ 和 chkconfig_ 的功能于一体。可以使用它永久性或只在当前会话中启用/禁用服务。

Systemd(system daemon)是一个系统管理守护进程、工具和库的集合，用于取代System V初始进程。
Systemd的功能是用于集中管理和配置类UNIX系统。

常见用法
===================

列出所有可用单元::

  systemctl list-unit-files
  systemctl list-units

列出所有失败单元::

  systemctl --failed

检查某个单元是否启动::

  systemctl is-enabled httpd.service

检查某个服务的运行状态::

  systemctl status httpd.service

列出所有服务::

  systemctl list-unit-files --type=service

查询服务是否激活::

  systemctl is-active httpd

服务查看是否配置开机自启动::

  systemctl is-enabled <service-name>

服务配置开机自启动(禁用+启用)::

  systemctl disable httpd
  systemctl enable httpd

使用systemctl命令杀死服务::

  systemctl kill httpd

列出系统的各项服务，挂载，设备等::

  systemctl list-unit-files --type

获得系统默认启动级别和设置默认启动级别::

  systemctl get-default
  systemctl set-default multi-user.target

启动运行等级::

  systemctl isolate multiuser.target

重启、停止，挂起、休眠系统等::

  systemctl reboot
  systemctl halt
  systemctl suspend
  systemctl hibernate
  systemctl hybrid-sleep

.. _service: :doc:`/docs/操作系统/linux/linux指令/service`
.. _chkconfig: :doc:`/docs/操作系统/linux/linux指令/chkconfig`
