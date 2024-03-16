=============================
chpasswd
=============================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


读取未加密的密码，然后将加密后的密码写入 /etc/shadow::

  echo 'qwe123' | chpasswd

