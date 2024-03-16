===============================
es遇到的问题
===============================


.. post:: 2023-02-20 22:06:49
  :tags: elasticsearch
  :category: 数据库
  :author: YanQue
  :location: CD
  :language: zh-cn


防火墙
===============================

开放9200端口允许访问::

  iptables -I INPUT -p tcp --dport 9200 -j ACCEPT

查看已有的端口::

  iptables -L -n

es解决跨域问题
===============================

修改ElasticSearch配置文件，config下：ElasticSearch.yml在最后面加两行代码::

  http.cors.enabled: true
  http.cors.allow-origin: "*"

此步骤可以允许ElasticSearch跨域 ，注意“：”后有空格

日志乱码
===============================

在config的jvm.options添加::

  -Dfile.encoding=GBK

集群配置
===============================

.. 在config下的elasticsearch.yml下:\:

..   cluster.name: training_safe_2021	# 设置集群名字
..   node.name: safe_ll_0622				    # 设置当前节点名字

..   path.data: ../elastic_all/es_data
..   path.logs: ../elastic_all/es_logs

主节点
--------------------------------

elasticsearch.yml::

  # 集群名，节点名
  cluster.name: test-master
  node.name: test-node1

  node.master: true						#设置充当master节点，默认为true
  node.data: false						#设置不充当data节点，默认为true
  network.host: 192.168.1.1				#(内网ip)
  network.bind_host: 192.168.1.1			#(内网ip)

  http.port: 9393    						#对外访问
  transport.tcp.port: 9303    			#各节点通信

  --------------------------------- Discovery ----------------------------------

  #Pass an initial list of hosts to perform discovery when new node is started:
  #The default list of hosts is ["127.0.0.1", "[::1]"]
  discovery.zen.ping.unicast.hosts: ["192.168.1.1:9303","192.168.1.1:9304","192.168.1.1:9305"]    #分别为各节点通信端口

副节点之一
--------------------------------

elasticsearch.yml::

  cluster.name: test-master
  node.name: test-node2

  #设置充当master节点，默认为true
  node.master: false
  #设置不充当data节点，默认为true
  node.data: true
  network.host: 192.168.1.1(内网ip)
  network.bind_host: 192.168.1.1(内网ip)

  http.port: 9394    #对外访问
  transport.tcp.port: 9304    #各节点通信

  --------------------------------- Discovery ----------------------------------

  #Pass an initial list of hosts to perform discovery when new node is started:
  #The default list of hosts is ["127.0.0.1", "[::1]"]
  discovery.zen.ping.unicast.hosts: ["192.168.1.1:9303","192.168.1.1:9304","192.168.1.1:9305"]    #分别为各节点通信端口

副节点之二
--------------------------------

elasticsearch.yml::

  cluster.name: test-master
  node.name: test-node3

  # 设置充当master节点，默认为true
  node.master: false
  # 设置不充当data节点，默认为true
  node.data: true
  network.host: 192.168.1.1(内网ip)
  network.bind_host: 192.168.1.1(内网ip)

  http.port: 9395    #对外访问
  transport.tcp.port: 9305    #各节点通信

  # --------------------------------- Discovery ----------------------------------

  # Pass an initial list of hosts to perform discovery when new node is started:
  # The default list of hosts is ["127.0.0.1", "[::1]"]
  discovery.zen.ping.unicast.hosts: ["192.168.1.1:9303","192.168.1.1:9304","192.168.1.1:9305"]    #分别为各节点通信端口


报错 `[Cannot assign requested address: bind]`
==============================================================

配置中的集群配置 `discovery.zen.ping.unicast.hosts` 的ip
跟当前本机的 `network.host` 不一致，果断把自己给坑了(-_-)
（ `当然这是为了模拟集群而在一台机器上部署多个节点，
生产环境不推荐这么搞，为了数据安全以及性能提升，还是一机一节点的好` ）

单机部署还是绑定自己本地吧

报错master not discovered yet, this node has not previously joined a bootstrapped (v7+) cluster
============================================================================================================================

下午、晚上都在报这个错，

最开始的yml配置文件是这个样子，我建立了一个不存储数据的master节点，
三个数据处理的node节点（node节点没有成为master的机会）

最开始，在文件配置中最重要的cluster.initial_master_nodes没有配置，导致无法绑定master节点，所以一直报错，

后指定了initial_master_nodes为四个节点，也在报错，

是因为只将第一个不存储数据的节点设置了node.master:true，
其他几个都设置的false，所以其他几个节点没有成为master节点的机会，

修改为cluster.initial_master_nodes: ["127.0.0.1:9300"]，问题解决一半，

因为只有master节点跟node1节点是正确的，另外两个节点还是在报错，正在寻找原因中。。。。

更新，原因找到了，master主节点没有实时去发现从节点，先把三个从节点启动了，最后再启动主节点就可以了，
更稳妥的解决方案是，在主节点上想方法设置一下实时从节点的发现。这一点明天继续寻找是否可以实现。

附主节点配置::

  #集群名，节点名
  cluster.name: test-master
  node.name: test-node1

  node.master: true						#设置充当master节点，默认为true
  node.data: false						#设置不充当data节点，默认为true
  network.host: 192.168.1.1				#(内网ip)
  network.bind_host: 192.168.1.1			#(内网ip)

  http.port: 9393    						#对外访问
  transport.tcp.port: 9303    			#各节点通信

  --------------------------------- Discovery ----------------------------------

  #Pass an initial list of hosts to perform discovery when new node is started:
  #The default list of hosts is ["127.0.0.1", "[::1]"]
  discovery.seed_hosts: ["127.0.0.1:9300","127.0.0.1:9301","127.0.0.1:9302","127.0.0.1:9303"]    #分别为各节点通信端口
  cluster.initial_master_nodes: ["127.0.0.1:9300"]

上面的基本信息介绍
===============================

可以看到有两个地址，{127.0.0.1:9300}和{127.0.0.1:9200}，相应的有两个端口号：9300和9200，
9300是端口transport端口号，9200是http端口号，详见：和 Elasticsearch 交互
验证ES是否启动成功：访问127.0.0.1:9200，看是否能访问成功~::

  {
    "name" : "-WsJ6Vr",
    "cluster_name" : "elasticsearch",
    "cluster_uuid" : "QKps9rpJQCiBJ4zBsXwgpQ",
    "version" : {
      "number" : "5.4.0",
      "build_hash" : "780f8c4",
      "build_date" : "2017-04-28T17:43:27.229Z",
      "build_snapshot" : false,
      "lucene_version" : "6.5.0"
    },
    "tagline" : "You Know, for Search"
  }

一个运行中的 Elasticsearch 实例称为一个"节点"，
而"集群"是由一个或者多个拥有相同 cluster.name 配置的节点组成
所以这就启动了一个ES节点，其中：

- name：表示这个ElasticSearch实例的名字；
- cluster_name：表示该节点所在的集群的名字，集群名相同的节点都会自动加入该集群；
- version：表示版本号，number是当前ES的版本号，lucene_version是当前ES所基于的Lucence的版本号

数据data缓存
===============================

默认情况下es的data都是存在于path.data所指定的目录的，path.data默认为文件的data目录，

所以data存在着上一次或者上几次的运行配置

故有些时候需要清空data来重新运行

Python版本
===============================

哭了，NS用的是python2.7，es导的es7.13的模块，而模块es7.13调用了urllib3的方法，最后urllib3只支持python3

是为什么发现这个问题的呢？

因为外网机下载好es的python的模块之后安装到内网机，windows安装时报错缺少两个模块::

  certifi，urllib

然后去下载安装，成功，接着自己写了个测试使用，成功


然后接入数据库数据，
debian安装es7，比win上多安装一个模块，因为装urllib3的时候提示报错，
查询后是setuptools版本过低，遂去找了适合python2的最新模块包，

报错找不到RecursionError，
然后在http_urllib3.py里也确实没有发现RecursionError是在哪里定义的，
然后去搜了urllib3这个模块，发现只支持python3


所以如果现在要改的话
要么把服务器python2.7升级，但是这样要改很多包
要么就把es7的模块给换了，本地集群的服务的得重新来，合着白装了这几个。。。

现在尝试，就未定义RecursionError这个错来修复，尝试注释之类的

嗯，注释了这个except，没报这个错了，

新的错误：虚拟机连接不上宿主机









