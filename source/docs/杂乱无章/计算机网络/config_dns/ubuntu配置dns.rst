=======================
ubuntu配置dns服务器
=======================


.. post:: 2024-03-09 18:21:01
  :tags: config_dns
  :category: 计算机网络
  :author: YanQue
  :location: CD
  :language: zh-cn


配置dns服务器
=======================

为了方便直接使用docker部署, 先配置一个dns机器(后续以 myubuntu_dns_server 代称)::

    # 默认latest版本是 20版本的 focal
    docker pull ubuntu
    docker run --name myubuntu_dns_server -itd ubuntu

然后就部署好一个ubuntu服务器了, 进入::

    docker exec -it myubuntu_dns_server /bin/bash

配置apt源::

    # 安装证书验证模块才可以配置源
    apt update && apt install ca-certificates

    mv /etc/apt/sources.list /etc/apt/sources.list.bak

    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    " > /etc/apt/sources.list

    apt update && apt install vim

    # 安装查看ip工具
    apt install iproute2

查看ip为 172.17.0.5 ::

    ip a | grep inet

配置普通机器(可选)
=======================

再按照上述方式安装一个测试机器(后续以 myubuntu_g1 代称), 验证dns配置是否正确::

    docker run --name myubuntu_g1 -itd ubuntu

    # 参考上面
    ...

    # 查看ip为 172.17.0.4
    ip a | grep inet

    # 安装 bind9-utils 以使用host
    apt install bind9-utils host

dns-server继续配置
=======================

实际还应该固定此服务器ip为静态ip, 此处docker部署忽略.

dns服务器(myubuntu_dns_server)安装bind9(目前市面是最主流的开源DNS软件) ::

    apt install bind9

bind9默认会有一些配置文件, 参见 :doc:`/docs/操作系统/linux/package/bind9软件包`

配置option
=======================

配置option::

    // 允许进行普通查询的 IP 地址列表，默认允许所有；
    sed -ie "3a \ \ \ \ \ \ \ \ listen-on port 53 { ${ip}; }; allow-query { any; };
    "  /etc/bind/named.conf.options

其实就是加上::

    listen-on port 53 { ${ip}; };
    allow-query { any; };

其中 listen-on 必须配置, 让named知道监听的端口与地址.

allow-query 是默认 any 可以忽略

配置正向解析
=======================

.. sidebar:: 若配置type为slave

    若需要配置从服务器, 格式参考下面配置::

        zone "aaa.com" IN {
            type slave;                 // 从模式
            masters { 172.17.0.5; };    // 主服务器的IP
            file "slaves/aaa.localhost";
            allow-update { none; };
        };

在 `/etc/bind/named.conf.local` 添加以下内容::

    zone "study.edu" IN {
        type master;
        file "/var/cache/bind/named.study.com";
    };

表示配置一个 `study.edu` 域名, 作为master, 配置文件在 `/var/cache/bind/named.study.com`

.. tip::

    可直接::

        cp /etc/bind/db.local /var/cache/bind/named.study.com

    然后修改

现在配置 `/var/cache/bind/named.study.com` ::

    ;
    ; BIND data file for study.com
    ;
    $TTL	604800
    @	IN	SOA	study.com. root.study.com. (
                    2		; Serial
                604800		; Refresh
                86400		; Retry
                2419200		; Expire
                604800 )	; Negative Cache TTL
    ;
    @	IN	NS	localhost.
    @	IN	A	172.17.0.4
    @	IN	AAAA	::1

    ; A 表示ipv4地址 AAAA表示ipv6地址 NS表示使用的dns服务器
    ; www 会自动加到 study.com. 实际为 www.study.com
    www	IN	A	172.17.0.4
    ; qq 会自动加到 study.com. 实际为 qq.study.com
    qq	IN	A	172.17.0.6

.. warning::

    这种解析配置文件需要注意空格问题, 切记

    否则可能会出现这种问题: ``Host 5.0.17.172.in-addr.arpa not found: 2(SERVFAIL)``

重启 bind9::

    /etc/init.d/named restart

测试::

    root@e376019130d3:/# host www.study.edu 172.17.0.5
    Using domain server:
    Name: 172.17.0.5
    Address: 172.17.0.5#53
    Aliases:

    www.study.edu has address 172.17.0.4
    root@e376019130d3:/#
    root@e376019130d3:/#
    root@e376019130d3:/# host qq.study.edu 172.17.0.5
    Using domain server:
    Name: 172.17.0.5
    Address: 172.17.0.5#53
    Aliases:

    qq.study.edu has address 172.17.0.6

配置反向解析
=======================

.. warning::

    多次配置不同的反向代理, 不用重复写 `/etc/bind/named.conf.local` 下的 `zone "0.17.172.in-addr.arpa"`

在 `/etc/bind/named.conf.local` 增加以下内容::

    zone "0.17.172.in-addr.arpa" {
        type master;
        file "/var/cache/bind/named.reverse.db.xxx";
    };

.. tip::

    可直接::

        cp /etc/bind/db.127 /var/cache/bind/named.reverse.db.xxx

    然后修改

现在配置 `/var/cache/bind/named.reverse.db.xxx` ::

    ;
    ; BIND reverse data file for 172.17.0
    ;
    $TTL	604800
    @	IN	SOA	study.com. admin.study.com. (
                    1		; Serial
                604800		; Refresh
                86400		; Retry
                2419200		; Expire
                604800 )	; Negative Cache TTL
    ;
    @	IN	NS	study.com.
    ; 表示 172.17.0.5 会被解析为 study.com. 注意这里都是倒着来
    5	IN	PTR	study.com.

重启::

    /etc/init.d/named restart

测试反向解析::

    root@e376019130d3:/#
    root@e376019130d3:/# host 172.17.0.5 172.17.0.5
    Using domain server:
    Name: 172.17.0.5
    Address: 172.17.0.5#53
    Aliases:

    5.0.17.172.in-addr.arpa domain name pointer study.com.
    root@e376019130d3:/#

.. tip::

    配置dns解析在 `/etc/resolv.conf` 文件, 作用等同于上面的 `172.17.0.5`, 若存在相应配置就, 上述命令可以不用写此IP

设置为DNS缓存服务器
=======================

在 `/etc/bind/named.conf.options` 增加以下内容::

    allow-query { any; };
    allow-query-cache { any; };     // 允许查询缓存的IP地址列表；
    recursion yes;                  // 允许递归查询；
    allow-recursion { any; };       // 允许递归查询的IP地址列表；
    forward only;                   // 允许转发；
    forwarders { 172.17.0.5; };     // 转发列表，172.17.0.5 为前面配置的授权服务器；
    dnssec-validation no;           // 关闭 dnssec；

重启bind9::

    /etc/init.d/named restart

验证::

    # 清除dns缓存
    rndc flush

    # +norecurse 不允许递归查询
    dig @172.17.0.4 www.study.com A +norecurse

    # 在授权服务器上抓包
    tcpdump -i eth1 port 53
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth1, link-type EN10MB (Ethernet), capture size 262144 bytes
    ^C
    0 packets captured
    0 packets received by filter
    0 packets dropped by kernel

然后再基于允许递归查询抓包, 可以看出 缓存服务器向授权服务器进行递归查询.

不允许递归查询时，DNS 缓存服务器会将缓存结果发送给客户端.

:此部分缓存参考::
    `Bind9：配置 DNS 授权服务器和 DNS 缓存服务器 <https://blog.csdn.net/xufuangchao/article/details/107558494>`_

附, 基础配置脚本, 功能: 配置本机为dns授权服务器

.. literalinclude:: ../../../../resources/code/config_dns.sh
    :language: shell

