=======================
自建局域网dns服务器
=======================


.. post:: 2024-03-09 18:21:01
  :tags: config_dns
  :category: 计算机网络
  :author: YanQue
  :location: CD
  :language: zh-cn


完全限定域名(FQDN) = 主机名 + 域名.

例: www.baidu.com = www(主机) + baidu.com(域名)

本机解析寻找顺序: 本机host文件 -> dns服务器

DNS解析方式::

    正向解析  FQDN -> IP
    反向解析  IP   -> FQDN


环境搭建
=======================

准备一个主机服务器, 设置静态ip, 注意保证使用的机器与此机器在同一个网段

打开windows功能管理, 安装 `DNS服务器`

打开: 服务器管理 -〉工具 -> DNS服务器

ubuntu配置dns服务器
=======================

:doc:`/docs/杂乱无章/计算机网络/config_dns/ubuntu配置dns`

其他部署方式
=======================

- Docker部署bind: :doc:`/docs/杂乱无章/计算机网络/config_dns/docker使用bind部署dns服务`
- Linux使用bind: :doc:`/docs/杂乱无章/计算机网络/config_dns/ubuntu配置dns` (debian也可)

综合
=======================

.. toctree::
  :maxdepth: 1

  docker-bind部署dns-管理面板
  docker使用bind部署dns服务
  ubuntu配置dns


