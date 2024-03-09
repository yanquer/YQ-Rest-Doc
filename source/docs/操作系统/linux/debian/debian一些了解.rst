============================
debian一些了解
============================

debian的服务基本上都可以在 ``/etc/init.d`` 下找到

使用apt安装deb本地包
============================

deb包可以通过dpkg安装::

  dpkg -i <package>

也可以通过apt安装::

  apt install ./<package>

.. note::

  apt 安装本地deb包时, 必须指定路径, 否则会去软件仓库找.

