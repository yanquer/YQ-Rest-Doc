===================================
/etc/hosts
===================================


.. post:: 2023-02-23 23:14:15
  :tags: linux, 配置文件
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


查看本地域名与地址映射, 内容为 地址与域名的映射,

例如,  `/etc/hosts` 看起来如下::

  127.0.0.1 localhost
  127.0.1.1 host_name

  ### The following lines are desirable for IPv6 capable hosts
  ::1     localhost ip6-localhost ip6-loopback
  ff02::1 ip6-allnodes
  ff02::2 ip6-allrouters

每一行由 `IP 地址 <https://zh.wikipedia.org/wiki/IP_address>`_
开始，接下来是相关联的 `主机名 <https://zh.wikipedia.org/wiki/Hostname>`_.

host_name
  匹配在 `/etc/hostname` 里定义的主机名。

对于有永久 IP 地址的系统，这个永久 IP 地址应当代替这里的 `127.0.1.1`。

对于有永久 IP 地址和有
`域名系统 Domain Name System (DNS) <https://zh.wikipedia.org/wiki/Domain_Name_System>`_
提供
`完全资格域名 fully qualified domain name (FQDN) <https://zh.wikipedia.org/wiki/FQDN>`_
的系统，规范名 *host_name.domain_name* 应当被用来代替 *host_name*.



