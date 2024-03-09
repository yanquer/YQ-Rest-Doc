===================================
body-elements
===================================

| 可以理解为html的body

参考: `docutils文档 -> body-elements <https://docutils.sourceforge.io/docs/ref/rst/directives.html#body-elements>`_

topic
===================================

可以理解为自然小节, 能较好控制样式效果

源码::

  .. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

**效果**

.. topic:: Topic Title

  Subsequent indented lines comprise
  the body of the topic, and are
  interpreted as body elements.

sidebar
===================================

支持的选项

subtitle: text
  副标题, 可选


源码::

  .. sidebar:: sidebar title
    :subtitle: sidebar sub Title

    this is a sidebar ...

**效果**  (在右边, 屏幕侧边)

.. sidebar:: sidebar title
  :subtitle: sidebar sub Title

  this is a sidebar ...

line-block
===================================

一个保留原有缩进的段落, 不建议使用, 建议直接使用竖线

用例说明, 源码::

  .. line-block::

    早, 吃早饭
    中
      吃吃吃吃吃吃吃吃吃吃
    晚
      面条面条面条面条面条面条

**效果**

  .. line-block::
    :name: line_block

    早, 吃早饭
    中
      吃吃吃吃吃吃吃吃吃吃
    晚
      面条面条面条面条面条面条

code
===================================

支持的命令选项:

number-lines: [int]
  是否展示行号, 值为起始行号, 默认为1

math
===================================

显示数学公式, 前提需要格式支持

epigraph
===================================

名言警句, 引用诗歌等

用例, 源码::

  .. epigraph::

    No matter where you go, there you are.
    (译: 无论你去哪里，你都在那里)。

    -- Buckaroo Banzai

**效果**

.. epigraph::

  No matter where you go, there you are.
  (译: 无论你去哪里，你都在那里)。

  -- Buckaroo Banzai

compound
===================================

“复合”指令用于创建复合段落，它是包含多个物理正文元素(如简单段落、文字块、表格、列表等)的单个逻辑段落，而不是直接包含文本和内联元素。

例如, 源码::

  .. compound::

    如果要查看当前目录下所有文件, 可以使用ls命令::

      ls ./

    某些无权限的文件可能无法访问, 这时需要给予相应的权限

**效果**

.. compound::

  如果要查看当前目录下所有文件, 可以使用ls命令::

    ls ./

  某些无权限的文件可能无法访问, 这时需要给予相应的权限

container
===================================

注意紧跟着的相当于类属性(相当于HTML的CLASS属性), 具体的效果需要用户自定义, 具体怎么自定义暂时没从官方文档看到, 难不成是自定义CSS ?

比如以下的custom::

  .. container:: custom

    本段可以以自定义方式呈现。




