====================
安装kivy
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库, kivy
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网安装介绍: https://kivy.org/doc/stable/gettingstarted/installation.html

一般都是用的桌面系统开发, 所以直接使用 pip安装即可::

  pip install "kivy[full]" kivy_examples

可惜我用我的老Mac安装失败了, base Python3.11::

  ...

        Updated /private/var/folders/4x/bpwwvvpn6d38ckdfw01fdggc0000gn/T/pip-install-nkzgam0u/kivy_f50690eb2e4f4577bf77f4119d23842a/kivy/include/config.pxi
        Updated build/lib.macosx-13-x86_64-cpython-311/kivy/setupconfig.py
        Updated /private/var/folders/4x/bpwwvvpn6d38ckdfw01fdggc0000gn/T/pip-install-nkzgam0u/kivy_f50690eb2e4f4577bf77f4119d23842a/kivy/setupconfig.py
        Detected compiler is unix
        error: command '/usr/bin/clang' failed with exit code 1
        [end of output]

    note: This error originates from a subprocess, and is likely not a problem with pip.
    ERROR: Failed building wheel for kivy
  Failed to build kivy
  ERROR: Could not build wheels for kivy, which is required to install pyproject.toml-based projects

查询说需要安装python-dev, 但是Mac又没有这玩意儿,
然后去github `Kivy won't install on Python 3.11.0 <https://github.com/kivy/kivy/issues/8042>`_
上看了一下, 直接安装master的解决::

  pip install "kivy[full] @ https://github.com/kivy/kivy/archive/master.zip"






