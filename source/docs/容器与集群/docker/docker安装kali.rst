===========================
Docker安装Kali
===========================


.. post:: 2023-02-20 22:06:49
  :tags: docker
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


命令
===========================

.. code-block:: sh

  # 拉取镜像
  docker pull kalilinux/kali-rolling

  # 查看
  docker images

  # 运行
  # -t 让 docker 分配一个伪终端并绑定到容器的标准输入上
  # -p 映射端口,
  # -d 保持后台运行，
  # -c 执行一些命令
  # docker run -t -d -p 60000:22  -p 60001:5901 -p 60002:5902 fd54aef8e4ea  /bin/sh -c "while true; do echo hello world; sleep 1; done"
  docker run --rm -t -d -p 60000:5900 -p 60001:5901 -p 60002:5902 --name mykali kalilinux/kali-rolling
  docker run -t -d -p 60000:5900 -p 60001:5901 -p 60002:5902 --name mykali kalilinux/kali-rolling

  # 查看容器
  docker ps

  # 进入
  docker exec -it mykali /bin/bash

系统环境配置

.. code-block::

  # 修改 root 用户密码
  passwd root

国内修改镜像源

.. code-block::

  # 阿里云镜像源
  vi /etc/apt/sources.list

  #中科大

  deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

  deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

  #阿里云

  deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib

  deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
  #清华大学

  deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free

  deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
  #浙大

  deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free

  deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free

  #东软大学

  deb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib

  deb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
  #官方源

  deb http://http.kali.org/kali kali-rolling main non-free contrib

  deb-src http://http.kali.org/kali kali-rolling main non-free contrib

  #163
  deb http://mirrors.163.com/debian/ jessie main non-free contrib
  deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib
  deb http://mirrors.163.com/debian/ jessie-backports main non-free contrib
  deb-src http://mirrors.163.com/debian/ jessie main non-free contrib
  deb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib
  deb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib
  deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
  deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib

SSH服务

.. code-block::

  # 更新系统
  apt-get update && apt-get upgrade
  # 安装所需软件
  apt-get install vim net-tools openssh-server
  # 修改 vim 配置文件，允许 root 用户远程登录
  vim /etc/ssh/sshd_config

  #启动 ssh 服务
  service ssh start
  #允许开机自启动
  systemctl enable ssh

通过60000端口ssh连接

必要工具安装

.. code-block:: sh

  apt update
  apt install lsb-release vim git python3 net-tools kali-linux-everything

.. note::

  kali-linux-everything 太大了, 几个G了还没完

  官网建议这样装:

  .. code-block:: sh

    # apt update && apt -y install <package>
    apt update && apt -y install kali-linux-headless
    apt update && apt -y install kali-linux-large


