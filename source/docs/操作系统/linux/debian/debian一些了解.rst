============================
debian一些了解
============================


.. post:: 2024-02-21 21:55:17
  :tags: linux, debian
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


debian的服务基本上都可以在 ``/etc/init.d`` 下找到

使用apt安装deb本地包
============================

deb包可以通过dpkg安装::

  dpkg -i <package>

也可以通过apt安装::

  apt install ./<package>

.. note::

  apt 安装本地deb包时, 必须指定路径, 否则会去软件仓库找.

