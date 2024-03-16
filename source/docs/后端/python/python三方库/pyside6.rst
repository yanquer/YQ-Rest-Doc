============================
Python Qt官方框架 pyside6
============================


.. post:: 2024-03-09 18:21:01
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


:官网文档::
  `Qt for Python <https://doc.qt.io/qtforpython/>`_

相关资源官网下载地址: `<https://download.qt.io/snapshots/>`_

安装::

  pip install pyside6


主要组件:

- PySide6:    使用QT6的API
- ShiBoken6:  提供了些与 C++ 交互的方式 (把C++项目拓展到python), 及一些工具方法(工具模块)

其实安装的还有额外的包::

  (dev_venv) yanque@mbp14 project % pip list | grep -iE 'pyside|shi'
  PySide6                       6.4.1
  PySide6-Addons                6.4.1
  PySide6-Essentials            6.4.1
  shiboken6                     6.4.1

- PySide6-Essentials, 是必要包
- PySide6-Addons, 附加(additional)包

PySide6.QtWidgets下常用控件
============================

布局相关

- QHBoxLayout, 水平布局(从左到右)
- QVBoxLayout, 垂直布局(从上到下)
- QGridLayout, 格子布局
- QFormLayout, 只有两列的格子布局

控件

- QPushButton, 点击按钮
- QLineEdit, 单行文本框
- QPlainTextEdit, 多行纯文本框
- QTextBrowser, 文本浏览器(只读)
- QLabel, 普通标签

详情
============================

.. toctree::
  :maxdepth: 1

  ./pyside6_more/index


