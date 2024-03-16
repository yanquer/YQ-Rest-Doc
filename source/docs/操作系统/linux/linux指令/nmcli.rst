=======================
nmcli
=======================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


配置网络管理器

如, 要将名为 eth0 的有线网络接口配置为自动连接::

  sudo nmcli connection modify eth0 connection.autoconnect yes

