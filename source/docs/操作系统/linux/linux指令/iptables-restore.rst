=============================
iptables-restore
=============================

批量导入Linux防火墙规则

例如将/tmp/iptables.txt规则写入iptables::

  iptables-restore < /tmp/iptables.txt

.. note::

  备份恢复时，
  :doc:`/docs/操作系统/linux/linux指令/iptables-save` 、
  iptables-restore
  两个都需要搭配重定向符使用



