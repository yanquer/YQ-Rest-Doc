=======================================
/etc/resolv.conf
=======================================

配置本机使用dns服务器, 以nameserver开头, 可多行.

如果 `resolvconf` 软件包没有安装，
`/etc/resolv.conf` 是一个静态文件。
如果安装了，它是一个符号链接。
此外，它包含有解析策略的初始化信息。如 DNS 是 IP= `192.168.11.1` ,则包含如下::

  nameserver 192.168.11.1

`resolvconf` 软件包使这个 `/etc/resolv.conf` 文件成为一个符号链接，并通过钩子脚本自动管理其内容。

.. note::

  见: :doc:`/docs/操作系统/linux/linux指令/resolvconf`



