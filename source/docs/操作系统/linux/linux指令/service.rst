=======================
service
=======================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


service 命令与传统的 SysVinit 和 Upstart 初始化系统相关。
较早期的 Linux 发行版（如早期的 Ubuntu、Red Hat 等）使用了这些初始化系统。
虽然许多现代 Linux 发行版已经转向使用 systemd，但它们通常仍然提供 service 命令作为向后兼容支持。

service命令可以启动、停止、重新启动和关闭系统服务，还可以显示所有系统服务的当前状态。

service命令的作用是去/etc/init.d目录下寻找相应的服务，进行开启和关闭等操作

要查看 service 命令是否被映射到 systemctl，可以通过检查 service 命令的实际文件类型和链接来实现::

  ls -l $(which service)

如果 service 命令被映射到 systemctl，输出结果可能类似于::

  lrwxrwxrwx 1 root root 21 Oct 13 10:10 /usr/sbin/service -> /usr/bin/systemctl

示例
=======================

开启关闭一个httpd服务::

  service httpd start/stop

查看系统服务的状态::

  service --status-all