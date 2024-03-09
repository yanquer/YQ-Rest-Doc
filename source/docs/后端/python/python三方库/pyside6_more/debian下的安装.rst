====================
debian下的安装
====================

使用docker配置, 见: :doc:`/docs/操作系统/linux/debian/配置debian容器`

安装 Python3 必要的包::

  apt install python3 python3-pip python3-venv vim

配置 pip 豆瓣源::

  cd ~
  mkdir .pip && cd .pip
  echo "[global]
  index-url = https://pypi.douban.com/simple/
  [install]
  trusted-host=pypi.douban.com
  " >pip.conf

官网要求安装的依赖包::

  apt install libgl-dev python3-dev python3-distutils python3-setuptools

配置虚拟环境::

  python3 -m venv dev_venv

  . dev_venv/bin/activate

拉去源码并构建::

  apt install git cmake

  mkdir project && cd project

  git clone https://code.qt.io/pyside/pyside-setup

  cd pyside-setup && git checkout 6.4 && pip install -r requirements.txt

  python setup.py build --qtpaths=/opt/Qt/6.4.0/gcc_64/bin/qtpaths --build-tests --ignore-git --parallel=8

  python setup.py install --qtpaths=/opt/Qt/6.4.0/gcc_64/bin/qtpaths --build-tests --ignore-git --parallel=8


整体源码:

.. literalinclude:: ../../../../../resources/code/docker_debian_install_pyside6.sh


