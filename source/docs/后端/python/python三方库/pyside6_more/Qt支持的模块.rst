================
Qt支持的模块
================

:官网地址::
  `modules <https://doc.qt.io/qtforpython/modules.html>`_

一些附加说明:

.. toctree::
  :maxdepth: 1

  ./modules/index

其实主要是 pyside6 下面的一些模块:

- QtBluetooth, 提供与设备蓝牙接口的访问
- QtCharts, 提供一系列便捷使用的图表组件
- QtConcurrent, 提供多线程编程的高级接口, 不需要关心如何维护底层的锁等.
- 🪐 QtCore, 核心非 GUI 方法
- 🪐 QtGui, 核心 GUI 方法
- QtDataVisualization, 3维可视化数据展示(条形图, 散点图, 表层图)
- QtDBus, 统一的, 基于linux的 IPC, RPC 协议
- QtDesigner, 继承 Qt Designer 的类
- QtHelp, 内置帮助文档(与在线文档内容一致)
- Qt Multimedia, 多媒体使用相关 API
- Qt Multimedia Widgets, 多媒体使用相关基础控件 API
- QtNetwork, 编码 TCP/IP 客户端/服务端相关
- Qt Network Authorization, 暴露用户密码, 提供 Qt 应用对 在线应用(如HTTP服务)的限制性访问
- QtNfc, 访问设备NFC接口
- QtOpenGL, 易于使用 OpenGL (GPU相关的GUI接口, 一系列操作图形/图片的函数API)
- QtOpenGL Widgets, OpenGL 相关的控件.
- Qt Positioning, 位置访问. 卫星信息和区域监测
- Qt PDF, 展示PDF文档相关
- Qt PDF Widgets, 支持的PDF视图控件
- QtPrintSupport, 跨平台打印支持
- QtQml, QML [1]_ API (引入类似Web XML技术).
- QtQuick, Qt 应用中嵌入 Qt Quick (引入类似Web XML技术), 其实就是嵌入 js 形式编码的东西
- QtQuickControls2, 从 C++ 设置控件
- QtQuickWidgets, QtQuick 相关控件的嵌入
- QtRemoteObjects, 基于Qt的 IPC 模块, 易于与计算机进程通信
- Qt Scxml, 从 SCXML 文件创建和使用状态机
- Qt Sensors, 访问硬件传感器
- Qt Serial Port, 与硬件及虚拟串口的交互
- Qt Spatial Audio, 在3D空间中建模声源及其周围环境
- QtSql, 提供与数据库的无缝衔接
- QtStateMachine, 创建和执行状态图 (没懂)
- QtSvg, svg图片的展示
- QtSvgWidgets, svg相关控件
- QtTest, Qt 的单元测试库
- QtUiTools, 处理 Qt Designer 设计的内容, 应该是 ``.ui`` 文件
- Qt WebChannel, 无缝衔接对 HTML/JavaScript 的访问, 主要是通过其 QObject 或 QML objects
- QtWebEngine Core C++ Classes, QtWebEngine 和 QtWebEngineWidgets 的公共 API 共享
- QtWebEngine Widgets C++ Classes, 提供Qt 应用内 C++ 类对 Web 部分内容的渲染
- QtWebEngine QML Types, Qt 应用内 QML 类型对 Web 部分内容的渲染
- Qt WebSockets, 与 WebSocket 的通信
- 🪐 QtWidgets, 使用 C++ 的方法, 对 Qt GUI 的拓展
- QtXml, 提供了 C++ 层面的 DOM 实现
- Qt3DAnimation, 基础的 3D 动画元素
- Qt3D Core, 近乎实时模拟系统的功能 方法
- Qt3D Extras, Qt 3D 开发的预构建元素
- Qt3D Input, Qt 3D 开发下, 处理用户输入
- Qt3D Logic, Qt 3D 开发下, 启用帧与Qt 3D后端的同步
- Qt3D Render, 支持使用Qt 3D进行2D和3D渲染的功能
- Qt CoAP, 实现由RFC 7252定义的CoAP客户端
- Qt OPC UA, 用于工业应用中的数据建模和数据交换的协议
- Qt MQTT, 提供MQTT协议规范的实现

.. [1] QML: 是 Qt 为 Qt Quick 打造的描述界面的新语言，然而就语法上，基本就是对 Javascript 做了扩展。
  几乎所有 Javascript 的语法都可以使用。


