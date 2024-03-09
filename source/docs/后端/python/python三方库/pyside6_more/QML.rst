====================
QML
====================

Qt设计的一种类似 CSS, JSON 的语言, 同时允许 JavaScript , 用于创建 UI 应用

可被其他组件集成, 可被 C++ 代码使用.


相对于传统 Python 代码中编写方式而言, 使用声明式 QML 更自然, 便捷, 开发 UI 部分更快速.

在官网教程中, 标题为 ``Your First QtQuick/QML Application`` ,
私以为 **QtQuick** 就是 QML. (待考证)

:官网地址:: `Your First QtQuick/QML Application <https://doc.qt.io/qtforpython/tutorials/basictutorial/qml.html>`_

可用模块

- QtQml
- QtQuick

结构
====================

一个 QML 至少由两个文件组成.

- QML UI 描述文件
- 加载 QML 的 Python 代码文件

例, 一个简单的 QML 文件 view.qml ::

  import QtQuick

  Rectangle {
      id: main
      width: 200
      height: 200
      color: "green"

      Text {
          text: "Hello World"
          anchors.centerIn: main
      }
  }

QtQuick 是一个 QML 模块.

Python 加载代码 main.py ::

  import sys
  from PySide6.QtWidgets import QApplication
  from PySide6.QtQuick import QQuickView

  if __name__ == "__main__":
      app = QApplication()
      view = QQuickView()

      view.setSource("view.qml")
      view.show()
      sys.exit(app.exec())

运行桌面应用时, 应该在 show 之前加入更新大小的代码::

  view.setResizeMode(QQuickView.SizeRootObjectToView)
  view.show()

整合QML到Python
====================

官网地址: `Python-QML integration <https://doc.qt.io/qtforpython/tutorials/qmlintegration/qmlintegration.html>`_

其实与上面的例子基本一致. 就是多了事件的部分.

加载 QML 文件::

  if __name__ == '__main__':
      app = QGuiApplication(sys.argv)
      QQuickStyle.setStyle("Material")
      engine = QQmlApplicationEngine()

      # Get the path of the current directory, and then add the name
      # of the QML file, to load it.
      qml_file = Path(__file__).parent / 'view.qml'
      engine.load(qml_file)

      if not engine.rootObjects():
          sys.exit(-1)

只需要 **QQmlApplicationEngine** 来加载 QML 文件.

使用 **@QmlElement** 定义 QML 定义的控件相应的事件::

  # To be used on the @QmlElement decorator
  # (QML_IMPORT_MINOR_VERSION is optional)
  QML_IMPORT_NAME = "io.qt.textproperties"
  QML_IMPORT_MAJOR_VERSION = 1

  @QmlElement
  class Bridge(QObject):

      @Slot(str, result=str)
      def getColor(self, s):
          if s.lower() == "red":
              return "#ef9a9a"
          elif s.lower() == "green":
              return "#a5d6a7"
          elif s.lower() == "blue":
              return "#90caf9"
          else:
              return "white"

      @Slot(float, result=int)
      def getSize(self, s):
          size = int(s * 34)
          if size <= 0:
              return 1
          else:
              return size

      @Slot(str, result=bool)
      def getItalic(self, s):
          if s.lower() == "italic":
              return True
          else:
              return False

      @Slot(str, result=bool)
      def getBold(self, s):
          if s.lower() == "bold":
              return True
          else:
              return False

在 QML 中定义相关部分(信号与槽)::

  Bridge {
    id: bridge
  }

比如, 点击按钮相关部分::

              RadioButton {
                  id: italic
                  Layout.alignment: Qt.AlignLeft
                  text: "Italic"
                  onToggled: {
                      leftlabel.font.italic = bridge.getItalic(italic.text)
                      leftlabel.font.bold = bridge.getBold(italic.text)
                      leftlabel.font.underline = bridge.getUnderline(italic.text)

                  }
              }

以下配置使用 style 触发::

  python main.py --style material

还可以加入 ``.conf`` 文件 ``qtquickcontrols2.conf`` ::

  [Controls]
  Style=Material

  [Universal]
  Theme=System
  Accent=Red

  [Material]
  Theme=Dark
  Accent=Red

加到 ``.qrc`` 文件::

  <!DOCTYPE RCC><RCC version="1.0">
  <qresource prefix="/">
      <file>qtquickcontrols2.conf</file>
  </qresource>
  </RCC>

生成 Python 代码::

  pyside6-rcc style.qrc > style_rc.py

导入到 main.py ::

  import sys
  from pathlib import Path

  from PySide6.QtCore import QObject, Slot
  from PySide6.QtGui import QGuiApplication
  from PySide6.QtQml import QQmlApplicationEngine, QmlElement
  from PySide6.QtQuickControls2 import QQuickStyle

  import style_rc

源码下载

- view.qml: :download:`../../../../../resources/code/pyside6/qml_example/view.qml`
- main.py: :download:`../../../../../resources/code/pyside6/qml_example/main.py`

**预览** :

**view.qml**

.. literalinclude:: ../../../../../resources/code/pyside6/qml_example/view.qml

**main.py**

.. literalinclude:: ../../../../../resources/code/pyside6/qml_example/main.py


使用 QtCreator
====================

下载: `<https://download.qt.io/snapshots/qtcreator/>`

注意安装的时候需要使用账户, 去 `官网 <https://login.qt.io/>`_ 注册一个账户即可.

官网使用教程: `QML Application Tutorial <https://doc.qt.io/qtforpython/tutorials/qmlapp/qmlapplication.html>`_

与数据库(SQL)结合
====================

官网: `QML, SQL and PySide Integration Tutorial <https://doc.qt.io/qtforpython/tutorials/qmlsqlintegration/qmlsqlintegration.html#sqldialog-py>`_

有时间按照教程试试

.. todo: 有时间按照教程试试




