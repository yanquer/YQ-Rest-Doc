==========================
bind9
==========================


.. post:: 2023-02-20 22:06:49
  :tags: linux, package
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


:参考::
    `ISC BIND9 - 最详细、最认真的从零开始的 BIND 9 - DNS服务搭建及其原理讲解 <https://www.cnblogs.com/doherasyang/p/14464999.html>`_

前置
==========================

DNS
--------------------------

DNS ( Domain Name Service) : 域名解析服务, 将字符串域名解析为数字IP

DNS ZONE
--------------------------

DNS域，被用来划分DNS主域。

传统的DNS域类似一个树状的结构，被分成不同的区域，这些区域可区分一个DNS服务器中命名空间中不同的区域。

DNS区域是构成DNS命名空间的一部分，由特定组织或管理员加以管理，其可以对权威性域名服务器等DNS组件更加精细的控制。

域名空间是一个分层数，其中DNS的根域位于顶部，DNS区域始于该树中的一个域，并且可以扩展到下边的子域。

资源记录类型
--------------------------

.. csv-table:: 资源记录类型
    :header: 字符串, 含义

    A       , Address地址， IPv4
    AAAA    , Address地址 IPv6
    NS      , Name Server域名服务器
    SOA     , Start of Authority 起始授权机构
    MX      , Mail Exchanger 邮件交换
    CNAME   , Canonical Name规范名. CNAME-records ( Canonical name for an alias )是域名的别名。
    PTR     , Pointer 指针，即反向DNS系统，用于查询IP地址时给出相关的域名，即查询IP地址的PTR记录给出该IP指向的域名，在 Zone 文件中被设置；
    TXT     , Text，网络名称系统的记录，可讲文字信息提供给网络意外的来源，其中有一个非常重要的功能就是当外部查询需要显示BIND的相关版本号时，可以指定 TXT查询，这个配置是默认的；谷歌会使用 TXT 记录来验证网站的拥有权以及确保电子邮件的安全；
    SRV     , Service 记录，域名中用于指定服务器并提供服务的位置：主机、端口号；一般在 Zone File 中被定义；

FQDN
--------------------------

FQDN(Fully Qualified Domain Name) 完全合格域名/全程域名，即域名可以通过DNS进行解析，其公式 FQDN = HostName + Domain。

解决多服务问题, 比如域名为 ``yanquer.con`` , ftp 用 ``ftp.yanquer.com`` , ssh 用 ``ssh.yanquer.com``

介绍
==========================

bind9 是目前市面是最主流的开源DNS软件

安装::

    apt install bind9

配置文件位置::

    /etc/bind/named.conf

查看其内容::

    root@6c378cbe42dd:/# cat /etc/bind
    bind/                   bindresvport.blacklist
    root@6c378cbe42dd:/# cat /etc/bind/named.conf
    // This is the primary configuration file for the BIND DNS server named.
    //
    // Please read /usr/share/doc/bind9/README.Debian.gz for information on the
    // structure of BIND configuration files in Debian, *BEFORE* you customize
    // this configuration file.
    //
    // If you are just adding zones, please do that in /etc/bind/named.conf.local

    include "/etc/bind/named.conf.options";
    include "/etc/bind/named.conf.local";
    include "/etc/bind/named.conf.default-zones";

可以看到其引用了三个文件:

- `/etc/bind/named.conf.options` : named.conf.options_
- `/etc/bind/named.conf.local` : named.conf.local_
- `/etc/bind/named.conf.default-zones` : named.conf.default-zones_

配置文件说明
==========================

- 以下文件都在 ``/etc/bind/`` 目录下
- 注意不要更改文件权限

named.conf.options
--------------------------

option 配置

named.conf.local
--------------------------

Zone 的引导配置文件

定义了 BIND9 中的 ZONE（区域）文件在named.conf.local文件中的定义，用于定义存储解析的域名的数据库文件，即域名与IP地址的映射关系以及DNS发送的解析域名数据包的相关参数设置，其定义的格式如下::

    zone "<YOUR DNS Domain Name >" {
        <Configurations>
    }

也可以定义反向解析域名通过以下的格式进行定义::

    zone "<YOUR IP ADDRESS>-addr.arpa" {
        <Configurations>
    }

`Configurations` 常用参数配置如下:

- file: 用于指出域名与IP地址解析的数据库配置文件；
- allow-transfer: 这个地方的配置是用来给出 Failover 或者是 递归查询DNS服务器的IP地址，如果之前在 options 里配置的allow-transfer 如果设置成了参数 yes， 那么需要在这里指出递归查询服务器的IP地址；
- type: 用于指定当前DNS解析服务器的位置，是主服务器 master 还是从服务器 slaver

named.conf.default-zones
--------------------------

机器默认域名配置::

    # vim /etc/default/bind9
    OPTIONS="-u bind -4"

Zone File
--------------------------

保存 RR (Record Resource) 信息的文件

DNS Record Types 分为很多种

- 地址解析 ( Address Records)
- 别名记录（Alias Records）
- 邮件交换记录（Email Exchange Records）
- 域名服务器记录（Name Server Records）；

确定你的需求，再编写你的Zone File；

配置含义说明
++++++++++++++++++++++++++++++++++++++++++

在 zone file 中，注释的符号是：``;`` (分号)

``@`` ( at - sign ) 是代表当前的区域，即 每一个 域名就是一个区域(region)，
一般在 ``$ORIGIN [REGION NAME]`` 设定了当前作用的区域，作用区域是代表当前的解析域名区域；

例::

    ;
    ; BIND data file for local loopback interface
    ;
    ; Import ZSK / KSK
    ;
    ;
    $ORIGIN domain.com.
    ; 我们已经定义了一个区域，那么在定义 SOA 的时候可以进行两种定义方式
    @ IN SOA ns.domain.com. admin.domain.com. (
                    3        ; Serial
                604800       ; Refresh
                86400        ; Retry
                2419200      ; Expire
                604800 )     ; Negative Cache TTL
    ; 或者我们不需要 at-sign - @ 符号，直接引用ORIGIN的名字
    ；在这里这两条配置代表的含义是一样的
    domain.com. ns.domain.com. admin.domain.com. (
                    3        ; Serial
                604800       ; Refresh
                86400        ; Retry
                2419200      ; Expire
                604800 )     ; Negative Cache TTL

上边的配置中

- ``@`` 代表了当前的区域 ``domain.com.``
- ``domain.com.`` 就是当前的区域

Zone File - TTL
++++++++++++++++++++++++++++++++++++++++++

TTL 规定了Resource Record 的失效时间，即当前资源记录能够被缓存的时间长短，默认的单位为秒，能够设定的最大时间长度是 32 bit 的整形变量 ( 0 到 4294967295 )，单位是秒；RR都会被保存在DNS的解析服务器的cache上，有一个失效的时间，TTL就是控制这个失效时间的一个参数；

这个参数可以单独进行设定，也可以在 SOA 设定中进行配置：

- 单独设定： ``$TTL [TIME]``
- 在 SOA 中进行设定： ``SOA - Negative Cache TTL``

  例::

    $TTL 6048000

Zone File - SOA
++++++++++++++++++++++++++++++++++++++++++

SOA - Start of Authority， 起始授权部分，是每一个 Zone File 必须包含的部分，也是包含域名的关键信息。

如果有多台DNS来管理同一个域名，就需要在 zone file 中规定如何规定两个域名解析服务器了 - Name Server；
即需要在定义 Zone Fie 的时候，需要特别明确 SOA 的定义，SOA 定义了域名解析服务器的对于区域 (Location) 的数据信息来源，即规定了解析区域的IP相关地址；

每一个域名区域都需要一个 SOA 记录；

定义的方式是::

    [LOCATION NAME] IN SOA [PRIMARY_DNS_SERVER_NAME] [EMAIL_ADDRESS_NAME] (
            1           ; Serial
            3h          ; Refresh after 3 hours
            1h          ; Retry after 1 hour
            1w          ; Expire After 1 Week
            1h          ; Negative caching TTL of 1 day
    )

配置举例::

    domain.com. ns.domain.com. admin.domain.com. (
                    3        ; Serial
                604800       ; Refresh
                86400        ; Retry
                2419200      ; Expire
                604800 )     ; Negative Cache TTL

解释一下上边的相关参数：

- ``Location Name`` 从前边 ``$ORIGIN`` 我们已经知道是一个区域的名称，或者用 @ 进行代替；
- ``PRIMARY_DNS_SERVER_NAME`` 用于规定解析当前域名的主服务器，这个服务器的IP地址以及详细资源需要在后边被规定；
- ``EMAIL_ADDRESS_NAME`` 指定了管理员的 Email 地址，以上边为例： ``admin.domain.com. == admin@domain.com.``
- ``Serial`` 序号，代表着当前数据库文件的新旧， 该值越大表示当前数据库的配置越新，一般来说这个值设定的值遵循 YYYYMMMMDDDD 的格式； 这个数值必须小于 4294967296；在这里涉及到一个 从服务器 ( Slave )的 配置问题，如果你需要 从服务器 何时从主服务器拉取最新的配置，就需要保持从服务器这个数值低于主服务器的数值；
- ``Refresh``  更新的频率，设置 Slave DNS 服务器 去向 主服务器 进行配置更新的周期；
- ``Retry`` 失败重新尝尝试时间，如果 Slave 服务器无法对 Master 进行链接，则需要设置这个值规定多长时间进行一次重试连接；
- ``Expire`` 是失效时间，如果一直失败连接，那么这个配置规定了重试连接的最大时间；
- ``Negative Cache TTL`` 缓存时间，在整个 zone file 都没有规定 TTL 时间的情况下，那么就以 SOA 中规定的 TTL 为主；

对于各个参数的限制::

    Refresh >= Retry × 2
    Refresh + Retry < Expire
    Expire >= Retry × 10
    Expire >= 7 Days

.. note::

    在所有的配置中，``ns.domain.com != ns.domain.com.`` ，必须注意在 zone file 中的配置文件的最后 ``.`` 必须不能省略；

    如果不写最后一个的 ``.`` 那么该域名就是一个 相对名 ，结果就是在解析的过程中，这条资源就被当成 ``ns.domain.com.domain.com``


zone file - Name Server Records
++++++++++++++++++++++++++++++++++++++++++

Name Server Records 定义了在当前 DNS服务器 中的 NS 的 IP地址，在每一个 zone file 中必须指定 主/从 域名解析器的IP地址， 使用 A 记录，这个IP地址必须与你搭建的DNS服务器保持一致；

举例::

    ; 记录 NS 记录
    @                IN            NS            ns.domain.com.
    ; 记录 NS 记录对应的 IP 地址信息
    ns.domain.com.   IN            A            192.168.1.1

zone file - Address Records
++++++++++++++++++++++++++++++++++++++++++

Address Records 记录了 域名 与 IP 地址的对应关系::

    ns.domain.com.                IN            A            192.168.1.1

zone file - Canonical Name Records
++++++++++++++++++++++++++++++++++++++++++

CName 将 单个昵称或者别名映射到一个可能存在在区域外的真实的区域.
在一个域名下存在多个子域名，如果需要更改映射之前的子域名，那么只需要更改映射的域名地址就可以了::

    ;
    $TTL 2d
    $ORIGIN domain.com.
    ...
    server1        IN        A        192.168.1.1
    www            IN        CNAME    Server1

配置项说明
==========================

acl
--------------------------

一般来说，ACL模块用来承担控制主机可以访问域名解析服务器的角色，其设置不会让控制文件的配置非常冗余和庞大。
采用这个配置可以有效防范DOS以及Spoofing攻击。
一般来说定义这部分的内容来规定IP是否能够被接入以及Blacklist来阻止某些特定的IP地址介入到域名解析服务器中。

ACL匹配客户端是否能够接入到域名服务器基于三个基本的特征:

- 客户端的IPv4或者IPv6地址
- 用于签署请求的 TSIG 和 SIG(0) 密钥
- 在DNS客户端子网选项中编码的前缀地址

匹配 acl 定义以及使用规则如下： string 是用来命名IP地址集的一个变量名，可以随意地被命名::

    acl <string> { <address_match_element>; ... };

举一个在 named.conf.options 文件中被定义的例子::

    acl bogusnets {
        0.0.0.0/8;  192.0.2.0/24; 224.0.0.0/3;
        10.0.0.0/8; 172.16.0.0/12; 192.168.0.0/16;
    }; // 这个部分
    // Set up an ACL called our-nets. Replace this with the
    // real IP numbers.
    acl our-nets { 172.16.2.11/24; 172.16.2.12/24; }; //子网的名称

logging
--------------------------

logging 部分的配置为DNS解析服务器提供了日志记录的功能，DNS服务器上的所有日志记录被存储到了指定的文件中。

其通用的配置文件为::

    logging {
        category <string> { <channel_name_string>; ... };
        channel <string> {
                buffered <boolean>;
                file <quoted_string> [ versions ( unlimited | <integer> ) ]
                    [ size <size> ] [ suffix ( increment | timestamp ) ];
                null;
                print-category <boolean>;
                print-severity <boolean>;
                print-time ( iso8601 | iso8601-utc | local | <boolean> );
                severity <log_severity>;
                stderr;
                syslog [ <syslog_facility> ];
        };
    };

从上边的通用配置格式可以看出来，logging 模块分为两个部分，category 和 channel.

channel的作用是指定输出的方式、日志格式的选项和事件的严重性，每一个channel 可以指定一个 category 来指定记录的事件类型。

category 用来区分不同的事件产生的类别或者场景，比如：客户端请求-client request、配置文件解析处理-Configuration file parsing and processing。

如果在 named.conf.options 文件中没有指定 logging 模块系统会给出一个默认的配置::

    logging {
        category default { default_syslog; default_debug; };
        category unmatched { null; };
    };

channel 的配置规则
+++++++++++++++++++++

所有的日志输出都需要 channel 来指定输出格式，BIND9 对于创建 channel 的数量没有限制。

每一个 channel 都需要为该通道的日志信息指定一个 destination clause - 目的句柄，目的句柄在 channel 阶段被配置，这个目的句柄用来区分：

- 输出到具体的文件的名字 - file
- 输出到具体的系统日志工具中（syslog/syslogd）- syslog
- 输出到终端显示- 标准错误流(standard error stream)
- 或者该错误消息直接被丢弃 - null。

其次，channel 的配置可以规定每一个错误日志消息的响应级别，默认的响应级别是info ，channel 可以规定接受错误消息的级别；
此外，channel 还可以控制输出错误日志消息的格式，可以包含：响应时间戳、category名字、严重等级等。

channel 的配置参数
+++++++++++++++++++++

- buffered: 用来规定是否刷新错误日志的文件，其参数值为<boolean>，在 BIND9 中 <boolean> 值的参数值为 yes / no，如果设置成为 yes 那么日志消息流(一般每一个错误日志消息都是一个 Log Entry)就不会刷新，而是被保存在缓冲区中了，不会刷新到文件中。
- file： 类似于Linux的通道概念，file 将日志输出流通过通道直接输出给文件，从上边的通用配置可以看出来可以为 file 指定文本文件的大小 - size ；指定 log 文件的版本号 - version；指定用于命名备份版本的格式 - suffix
- size 用来限制log文件的大小，如果log文件的大小设置超过了设定的阈值，那么系统会自动停止输出内容到文件中；
- versions： 用于指定新创建的 log文件数存储到本地的上限值，默认的参数值为unlimited，当指定的文件的大小超过设定的size值得时候，如果没有指定 versions，那么系统就不会继续写进log；如果制定了versions，那么就会继续写入；
- suffix ：设定用来命名log文件的方式；好像没啥用，我添加这个参数没有什么反应...；
- syslog：将通道定向到系统的日志文件流中； 常用的支持日志文件服务为：dameon、syslog、local6、local7；
- severity：用来承担定义日志严重级别的定义角色，相当于 syslog - priorities。比如说定义了日志的严重级别为 Debug，那么会输出日志事件 Debug 以上的错误到文件中。一般常用的严重等级： debug[level]、notice、warning、dynamic - 与当前服务器的日志保持一致；一般的 DNS服务器的日志等级调成 info即可；
- stderr：将通道指向服务器的标准错误流。这是为了在服务器作为前台进程运行时使用；
- print-time： yes / no / local / iso8601 / iso8061-utc 可以设定不同的输出到日志文件的时间格式；
- print-category：打印日志消息配置category 的信息到你设定的日志文件中；
- print-severity： 打印日志的严重等级

category词组配置规则
+++++++++++++++++++++

category词组配置规则::

    category <config_string> { <channel_name_string>; ... };

- client： 客户端请求；
- cname：由于是CNAME而不是a /AAAA记录 的域名服务器；
- config： 配置文件解析和处理过程；
- database：与名称服务器内部用于存储区域和缓存数据的数据库相关的消息；
- general： 没有被归类的 category 类别的其他种类的日志文件信息；
- lame-servers： 远程服务器中的错误配置，BIND 9在解析期间试图查询这些服务器时发现；
- network： 网络操作；
- notify： 通知协议；
- queries：记录所有查询 DNS服务器的 query；
- query-errors： 关于导致某些失败的查询的信息；
- xfer-in：区域传输服务器正在接收；
- xfer-out：区域传输服务器正在发送的信息；
- zoneload：加载区域和创建自动空区域；

怎么配置这个服务
+++++++++++++++++++++

配置的 logging 服务会创建指定的日志文件，该日志文件从服务挂起的时候被创建，用于记录DNS服务中的相关的配置信息以及交换信息。

在 Debian9 的默认存储目录为 /var/cache/bind/\*. 也可以为其指定你想要存储的位置.
我个人喜欢将 BIND 日志和系统日志保存在一起，即保存路径为：/var/log/bind。
这个路径不是在你安装 BIND 时候就已经创建了，需要你自己创建对应的文件目录；

如果你想要配置成一个自己的目录，首先你需要创建一个自定义的目录，比如说我指定了我想要存放日志的文件的目录： /var/log/bind，如果不为这个文件使用chown命令指定权限的话会出现 isc_stdio_open '/var/log/example.log' failed 的报错：

首先你必须手动创建自己的文件到指定目录下；
解决方法是::

    sudo chown bind:root /var/log/bind/* ；

现在我们已经基本上了解了 logging 的工作原理.
其工作机制简单地来说就是，首先你需要创建一个 channel 来规定输出日志流的格式还以及日志文件名、文件版本.
每一个 channel 可以被多个 category 调用使用，
每一个 category 相当于一个 BIND9 内嵌的服务模块，
服务模块去调用日志配置模最后输出格式化日志。

在这里我之前并没有给出对应的配置示例，现在给出示例::

    // named.conf.options 文件中给出logging的配置示例
    logging {
        // 在我自己使用BIND进行DNS解析的时候，出现了 TIME_OUT 的相关错误，这个错误是需要在 client 进行日志记录
        // 因此对于客户端的解析需要有相关的日志配置，才能发现在解析时的问题
        //
        //
        //
            category client { default_client; } // 指定 client 所有的错误
            channel default_client {
                file "/var/log/bind/err/client.log" version 1 size 20m
                print-category yes;
                print-time iso8061;
                severity debug 3;
            }
    }

options
--------------------------

options 的参数设置会影响整个 BIND9 DNS环境的配置，具体各部分常用到的配置参数如下

- listen-on： 用于配置监听的端口以及IPv4地址，默认的监听端口为：53；
- listen-on-v6：用于监听 IPv6 地址以及端口；
- directory: 用于指定读取DNS数据文件的文件夹，默认的文件夹的路径为：/var/cache/bind；
- dump-file：选项用来设置域名缓存数据库文件的位置，可以自己定义。默认的存储文件为：named_dump.db；
- statistics-file：选项用来设置状态统计文件的位置，可以自己定义。；
- memstatistics-file ：选项用来设置服务器输出的内存使用统计信息。默认保存在 /var/named/data 目录下，文件名为 named.memstats；
- allow-query：选项用来设置允许DNS查询的客户端地址，默认值为localhost, 可以设置为某个网段、任意地址、具体的某台主机三种情况。例如，要修改为任意地址，就在括号内的加入 any，也可以引用之前创建的 acl 内的所有地址；
- recursion：用于设置递归查询，一般客户机和服务器之间属于递归查询，即当客户机向DNS服务器发出查询请求后，若DNS服务器本身不能解析，则会向另外的DNS服务器发出查询请求，得到结果后转交给客户机。此选项有yes和no两个值。这个选项用于设置 Failover 非常有用；
- dnssec-enable： 选项用来设置是否启用DNSSEC支持，DNSSEC可以用来验证DNS数据的有效性，该选项有yes和no两个值，默认值为yes。
- dnssec-validation：选项用来设置是否启用DNSSEC确认，默认值为yes，可以选择 auto。
- bindkeys-file ： 用来设置内置信任的密钥文件，其默认值为 /etc/named/iscdlv.key；
- managed-keys-directory： 选项用于指定目录中的文件存储位置，跟踪管理 DNSSEC 密钥， 这部分的内容在后边会有介绍；
- forwarders：DNS转发器。用于设定该DNS解析服务器无法进行当前域名解析的情况下，进行转发解析的DNS地址，其中 8.8.8.8 和 8.8.4.4 是谷歌的免费DNS服务器的网络地址；233.5.5.5 和 233.6.6.6 是阿里云的免费DNS地址。当设置了 forwarder 的转发器之后，所有的非本域的和在缓存中无法查找到的域名查询都转发都设置的DNS转发器，由DNS转发器 完成转发操作。因此这台转发器的缓存中就记录了丰富的域名信息。因此如果遇到非本域的查询，转发器的缓存就可以做到查询，从而减少了向外部的查询流量。
- forward: 选择默认的IP地址即可；
- rrset-order：
  在 BIND 9 提供的负载均衡策略建立在一个名称（域名 - Name）使用多个资源记录 ( Records ) 的情况下，其实现的轮询机制并不是传统的负载均衡服务器实现的轮询机制 - 即追踪和记录每一次应答的资源顺序；
  BIND 9 实现了一个类似 List 的数据结构，将所有的资源记录填入到 一个顺序表中，这个填入的次序随机，或者根据设定的参数随机；

  格式::

    [class class_name] [type type_name] [name “domain_name”] order ordering

  如果参数没有被赋值，那么默认的赋值为::

    class: ANY type: ANY Name: *

  参数:

  - fixed ： 根据 zone 文件定义资源记录的顺序按照顺序逐个进行解析；
  - random： 根据 zone 文件资源记录随机返回解析记录；
  - cyclic： 创建一个循环，循环输出资源记录；
  - none： 完全随机的资源返回形式；

controls
--------------------------

controls语句声明了系统管理员用于管理名称服务器远程操作的控制通道。
rndc使用这些控制通道向名称服务器发送命令，并从名称服务器检索非dns结果。

