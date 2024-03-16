=====================
配置docker-debian
=====================


.. post:: 2023-03-03 23:21:11
  :tags: linux, debian
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


拉取debian镜像::

  docker pull debian

运行::

  docker run --name mydebian -dit debian

进入::

  docker exec -it mydebian /bin/bash


安装验证工具(HTTPS)::

  sudo apt install apt-transport-https ca-certificates

换源::

  mv /etc/apt/sources.list /etc/apt/sources.list.bak

  echo "# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
  deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free

  deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free

  deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free

  # deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free
  # # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free

  deb https://security.debian.org/debian-security bullseye-security main contrib non-free
  # deb-src https://security.debian.org/debian-security bullseye-security main contrib non-free
  " > /etc/apt/sources.list

  apt update

清华源地址debian配置帮助: `debian <https://mirrors.tuna.tsinghua.edu.cn/help/debian/>`_

.. note::

  如果报错 ``Certificate verification failed: The certificate is NOT trusted.``
  有两种解决方式

  1. 将 https 改成 http
  2. 先安装  apt-transport-https ca-certificates


