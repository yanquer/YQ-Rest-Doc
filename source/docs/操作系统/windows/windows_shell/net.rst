================================
net
================================


.. post:: 2024-03-04 22:04:43
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


查看已经挂载/打开的网络地址 (指磁盘, ftp服务器啥的)::

  net use

删除上面列举出所有挂载的磁盘/服务器::

  net use /delete *

删除 z 盘映射::

  net use z: /delete

挂载samba共享为z盘::

  net use z:\\192.168.1.1\USB_discl /user:usernane passwd




