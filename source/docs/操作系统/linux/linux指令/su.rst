=========================
su
=========================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


用户切换

用法::

  su [options] [-] [<user> [<argument>...]]

-l
  或者直接 ``-`` , 表示使用登录shell, 可以完全加载指定用户的环境


.. note::

  这里简单提一下与 :doc:`/docs/操作系统/linux/linux指令/sudo` 相关的,

  ``sudo -i`` 也可以切换到root用户, 不过切换过去后只是加载root到环境变量,
  并不是完全加载环境. 且执行的命令默认会有日志记录在 `/var/log/sudo/`,
  便于审计, 更安全.



