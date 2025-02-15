====================
Pyside6
====================

.. toctree::
  :maxdepth: 1

  QML
  Qt支持的模块
  debian下的安装
  教程
  使用docker安装
  项目介绍
  数据可视化工具

基本概念说明

Qt, QML, Widgets区别

:参考::
  `Qt, QML, Widgets…What Is The Difference? <https://doc.qt.io/qtforpython/tutorials/pretutorial/whatisqt.html>`_

Qt
====================

可以是使用 C++ 开发的 Qt 框架,

也可以是 使用此框架开发的 Qt 应用程序.

QML
====================

Qt设计的一种类似 CSS, JSON 的语言, 同时允许 JavaScript , 用于创建 UI 应用

可被其他组件集成, 可被 C++ 代码使用.

Widgets
====================

预定义的一些 Qt 控件, 控件原则是: 基本与系统原生窗口外观一致.

如果需要更新外观样式(可能会违背上面的原则), 参考... 没参考了, 官网文档都 404 了...

Python And C++
====================

使用 Python 开发时, 不需要了解 C++ 的实现.

不过可以混合使用.

- 在用户代码级别, Python 实现基本做到了全覆盖(C++ 的实现), 可以任意重写
- 若使用 C++ 自定义控件, 可以创建 Python 绑定以便于在 Python 使用
- 若有特殊的需求实现需要使用到自定义的 C++ 库, 也可以创建其绑定以便 Python 使用
- 对于一个 C++ 的 Qt 程序而言, 可以通过暴露单例的 Python 绑定 给 Python 解释器以便其使用 (就像一个 Python 插件系统)

不过这些实现(后面三个实现), 依赖于 Shiboken_ (绑定生成工具)


文件类型
====================

:官网::
  `File Types <https://doc.qt.io/qtforpython/tutorials/pretutorial/typesoffiles.html>`_

- ``.ui``  , 类似 XML 文件的形式来绘制 GUI 界面, 使用 ``pyside6-uic`` 将其转换为 Python 代码. 编写参考: `using-ui-files <https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html#using-ui-files>`_
- ``.qrc`` , 资源文件, 编写方式类似 XML, 使用 ``pyside6-rcc`` 将其转换为 Python 代码. 编写参考: `using-qrc-files <https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html#using-qrc-files>`_
- ``.qml`` , 语言文件, 绘制页面.
- ``.pyproject``, 新版本内容是基于 JSON 的格式. 可用于配置给 C++ 项目处理的一些文件.


一些命令行
====================

:参考::
  `Which IDEs Are Compatible? <https://doc.qt.io/qtforpython/tutorials/pretutorial/whichide.html>`_

打开 Qt Designer 工具以创建 ``.ui`` 文件::

  pyside6-designer

将 ``.ui`` 文件转换为 Python 代码::

  pyside6-uic -i form.ui -o ui_form.py

将 ``.qrc`` 文件转换为 Python 代码::

  pyside6-rcc -i resources.qrc -o rc_resources.py


可使用的开发工具(IDE)
========================================

.. todo: QtCreator 了解

- QtCreator, 有个好处是有一些模版可以使用, 下载: `QtCreator <https://www.qt.io/zh-cn/product/development-tools>`_ (这个还真没听说过, 有空了解一下)
- Visual Studio Code, 需要安装插件: ``ext install seanwu.vscode-qt-for-python``
- PyCharm, 需手动配置相关工具. 如 ``Qt Designer`` .
  配置位置: ``File > Settings > tools > PyCharm External Tools``

.. _Shiboken:

Shiboken - 绑定生成器(Python/C++)
========================================

下包含函数: :doc:`/docs/后端/python/python三方库/pyside6_more/modules/Shiboken`

pip 安装的时候, 默认会一起安装的模块::

  yanque@yanquedembp code % pip list | grep shiboken
  shiboken6                            6.4.0.1

包含了一些工具来保证 Pyside 可以正确运行 (主用于debug吧)

还有一个 ``Shiboken Generator`` 默认不会自动一起安装.

教程中提到的 ``Shiboken`` 大多指的是 ``Shiboken Generator`` ,
详见: :doc:`/docs/后端/python/python三方库/pyside6_more/modules/Shiboken Generator`

什么时候需要 ``Shiboken Generator`` ?

- 若仅运行一个 Python 级别的 Qt 应用, 则不需要
- 若需要于 C++ 层面的代码结合, 如继承或自定实现的 C++ 的绑定, 需要

项目部署
========================================

:官网::
  `distribution <https://doc.qt.io/qtforpython/tutorials/pretutorial/distribution.html>`_
  `deployment <https://doc.qt.io/qtforpython/deployment/index.html#deployment-guides>`_

尤其是跨平台时.

官方建议是构建冻结文件, 其实就是将代码打包成平台的相应包, 不同的模块可以打包成不同的包以适配大型应用, 因为这样可以分布式的更新仅需更新的文件.

个人比较熟悉的是: `deployment-nuitka <https://doc.qt.io/qtforpython/deployment/deployment-nuitka.html>`_


