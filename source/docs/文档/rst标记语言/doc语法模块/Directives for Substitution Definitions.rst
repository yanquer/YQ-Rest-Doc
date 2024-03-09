================================================
Directives for Substitution Definitions
================================================

replace
================================================

用于替换上下文文本.

源码::

  .. |奥斯| replace:: 奥斯特洛夫斯基

  |奥斯| 说过: 钢铁是我教你们练成的. 开个玩笑.


**效果**

.. |奥斯| replace:: 奥斯特洛夫斯基

|奥斯| 说过: 钢铁是我教你们练成的. 开个玩笑.

另外, 由于reStructuredText不支持嵌套内联标记，因此创建带有样式文本的引用的唯一方法是使用“替换”指令的替换.
例如:

I recommend you try |Python|_.

.. |Python| replace:: Python, *the* best language around
.. _Python: https://www.python.org/

对应源码::

  I recommend you try |Python|_.

  .. |Python| replace:: Python, *the* best language around
  .. _Python: https://www.python.org/

unicode
================================================

用于转换Unicode字符, 没什么应用场景, 见 `unicode-character-codes <https://docutils.sourceforge.io/docs/ref/rst/directives.html#unicode-character-codes>`_

date
================================================

用于嵌入当前日期, 格式等同于 time 模块的 `time.strftime() <https://docs.python.org/3/library/time.html#time.strftime>`_

默认格式为 `%Y-%m-%d`

例, 源码::

  .. |date| date::
  .. |time| date:: %H:%M

  今天是 |date|.

  文档被创建与 |date| at |time|.

**效果**

.. |date| date::
.. |time| date:: %H:%M

今天是 |date|.

文档被创建与 |date| at |time|.




