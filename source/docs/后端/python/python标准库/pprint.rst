===================
pprint
===================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


pprint --- 数据美化输出

官网: https://docs.python.org/zh-cn/3/library/pprint.html

针对 json 格式数据的美化打印工具

pprint 模块提供了“美化打印”任意 Python 数据结构的功能，这种美化形式可用作对解释器的输入。
如果经格式化的结构包含非基本 Python 类型的对象，则其美化形式可能无法被加载。
包含文件、套接字或类对象，以及许多其他不能用 Python 字面值来表示的对象都有可能导致这样的结果。

PrettyPrinter
===================

.. function:: class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

  构造一个 PrettyPrinter 实例。 这个构造器支持一些关键字形参。

  stream:
    默认使用 sys.stdout, 类文件对象, 后面会调用其 write() 方法.
    如果 stream and sys.stdout 都为空, 则没有输出.
  indent = 1
    指定缩进
  depth:
    打印多少层, 默认无限制
  width =  80
    指定输出中每行所允许的最大字符数。
    如果一个数据结构无法在宽度限制之内被格式化，将显示尽可能多的内容。
  compact:
    影响长序列（列表、元组、集合等等）的格式化方式。

    - 如果 compact 为假值（默认）则序列的每一项将格式化为单独的行。
    - 如果 compact 为真值，则每个输出行格式化时将在 width 的限制之内尽可能地容纳多个条目。
  sort_dicts = True
    字典在格式化时将基于键进行排序，否则它们将按插入顺序显示。
  underscore_numbers = True
    整数在格式化时将使用 _ 字符作为千位分隔符，否则不显示下划线（默认）。

  在 3.4 版更改: 增加了 compact 形参。

  在 3.8 版更改: 增加了 sort_dicts 形参。

  在 3.10 版更改: 添加了 underscore_numbers 形参。

  在 3.11 版更改: No longer attempts to write to sys.stdout if it is None.

.. function:: pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

  打印格式化的对象/流描述信息. 若 stream=None, 使用 sys.stdout.

  可以使用 print = pprint.pprint 来替换默认行为.

  实际就是构造 PrettyPrinter_

  例::

    import pprint
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    stuff.insert(0, stuff)
    pprint.pprint(stuff)

    [<Recursion on list with id=...>,
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']
