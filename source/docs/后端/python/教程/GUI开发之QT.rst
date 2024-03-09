=====================
GUI开发之QT
=====================

前言
=====================

Qt是由C++开发的跨平台GUI框架, 针对Python有提供相应的Api

题主系统: MacOs 13

QT的Python相关框架
=====================

- PyQt

  第三方公司产品,

  开源协议为GPL协议, 意味着使用此库, 所开发产品必须开源

- PySide

  QT的亲子,

  开源协议为LGPL协议, 使用此库, 开不开源皆自由

  PySide2对应QT5;

  PySide6对应Qt6

两者提供接口基本一致

此处主要介绍用 PySide6


PySide6
=====================

安装PySide6
+++++++++++++++++++++

``pip install pyside6``

设计界面
+++++++++++++++++++++

- QtWidget

  当前最常用

- QML

  较新型, QT正在推广

此处主要使用 QtWidget


使用QtWidget开发
=====================



designer 图形化开发
+++++++++++++++++++++

  命令行执行 ``pyside6-designer`` 启动

  .. figure:: ../../../../resources/images/2022-11-19-15-14-22.png
    :align: center
    :width: 480px

    在 Mac 下启动如下所示

  后续操作自己探索吧, 这界面没有 windows 版熟悉, 暂时不想研究

  界面设计完成后可以保存为UI后缀文件,
  使用 ``pyside6-uic $file.ui >ui.py`` 转换成py文件才可以使用

  .. note::

    生成的文件编码不是utf-8

手动编码
+++++++++++++++++++++

见 :doc:`/docs/后端/python/python三方库/pyside6`

