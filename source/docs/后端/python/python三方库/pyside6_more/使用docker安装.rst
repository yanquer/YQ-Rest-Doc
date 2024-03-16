====================
使用docker安装
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库, pyside6_more
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


使用 指定版本安装 Python 并进入::

  docker run --name python39 -itd -p 2222:22 python:3.9
  docker exec -it python39 /bin/bash

  # 就不换源了, 感觉三方源还不如官方源快
  apt update
  apt install vim ssh iproute2 rsync

  # vim  /etc/ssh/sshd_config 允许root登录

  # 更新密码
  passwd

  # 配置 pip 源
  cd ~
  mkdir .pip && cd .pip
  echo "[global]
  index-url = https://pypi.douban.com/simple/
  [install]
  trusted-host=pypi.douban.com
  " >pip.conf

  pip install pyside6





