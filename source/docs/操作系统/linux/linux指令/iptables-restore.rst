=============================
iptables-restore
=============================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


批量导入Linux防火墙规则

例如将/tmp/iptables.txt规则写入iptables::

  iptables-restore < /tmp/iptables.txt

.. note::

  备份恢复时，
  :doc:`/docs/操作系统/linux/linux指令/iptables-save` 、
  iptables-restore
  两个都需要搭配重定向符使用



