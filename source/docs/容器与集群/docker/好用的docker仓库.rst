===================
好用的docker仓库
===================


.. post:: 2024-03-09 18:21:01
  :tags: docker
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


- ⭐️ webmin_ , 控制面板
- ⭐️ jellyfin_, 媒体服务器
- aliyun-webdav, 阿里云盘webdva
- ⭐️ ariang：下载机
- emqx ：Mqtt服务中心，工作环境偶尔用
- kms：服务器 激活自己和朋友的windows+office
- nastools ：管理界面（不好用，废弃掉）
- onthing ：网心云，带宽赚钱（废弃掉，不缺这每天2块钱）
- ⭐️ photoprism ：照片管理工具，可以上传照片，但没必要
- ftp ：开启ftp服务器（不常用）
- nginx ：部署项目，代理一些本地文件
- ⭐️ autoBangumi ：自动追番
- arsenal（武器库）： 提供一个webhook，调用即可发送邮件，用自己的域名发送，接入阿里云DDNS功能

webmin
===================

控制面板,

拉取::

  docker pull johanp/webmin

默认配置::

  Username: root

  Password: password

hubdocker地址: `johanp/webmin <https://hub.docker.com/r/johanp/webmin>`_

还有samba管理, bind ( :doc:`/docs/杂乱无章/计算机网络/config_dns/docker-bind部署dns-管理面板` ) 等相关的

jellyfin
===================

媒体服务器

拉取::

  docker pull linuxserver/jellyfin



地址: `linuxserver/jellyfin <https://hub.docker.com/r/linuxserver/jellyfin>`_
