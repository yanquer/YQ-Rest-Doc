===================
traceback
===================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


写几个常用的吧暂时.

.. function:: traceback.print_tb(tb, limit=None, file=None)

  如果 *limit* 是正整数，那么从 traceback 对象 "tb" 输出最高 limit 个（从调用函数开始的）栈的堆栈回溯条目；
  如果 limit 是负数就输出 abs(limit) 个回溯条目；
  又如果 limit 被省略或者为 None，那么就会输出所有回溯条目。

  如果 file 被省略或为 None 那么就会输出至标准输出 ``sys.stderr`` 否则它应该是一个打开的文件或者文件类对象来接收输出

  在 3.5 版更改: 添加了对负数值 limit 的支持

.. function:: traceback.print_exception(exc, /, [value, tb, ]limit=None, file=None, chain=True)

  打印回溯对象 tb 到 file 的异常信息和整个堆栈回溯。这和 print_tb() 比有以下方面不同：

  如果 tb 不为 None，它将打印头部 Traceback (most recent call last):
  它将在栈回溯之后打印异常类型和 value
  如果 type(value) 为 SyntaxError 且 value 具有适当的格式，它会打印发生语法错误的行并用一个圆点来指明错误的大致位置。
  从 Python 3.10 开始，可以不再传递 value 和 tb，而是传递一个异常对象作为第一个参数。 如果提供了 value 和 tb，则第一个参数会被忽略以便提供向下兼容性。

  可选的 limit 参数具有与 print_tb() 的相同含义。 如果 chain 为真值（默认），则链式异常（异常的 __cause__ 或 __context__ 属性）也将被打印出来，就像解释器本身在打印未处理的异常时一样。

  在 3.5 版更改: etype 参数会被忽略并根据 value 推断出来。

  在 3.10 版更改: etype 形参已被重命名为 exc 并且现在是仅限位置形参。

.. function:: ttraceback.extract_tb(tb, limit=None)

  返回一个 StackSummary 对象来代表从回溯对象 tb 提取的 "预处理" 栈回溯条目列表。
  它适用于栈回溯的替代格式化。
  可选的 limit 参数具有与 print_tb() 的相同含义。
  "预处理" 栈回溯条目是一个 FrameSummary 对象，其中包含代表通常为栈回溯打印的信息的 filename, lineno, name 和 line 等属性。
  line 是一个去除了前导和末尾空白符的字符串；如果源代码不可用则它将为 None。

.. function:: ttraceback.extract_stack(f=None, limit=None)

  从当前的栈帧提取原始回溯信息。
  返回值具有与 extract_tb() 的相同格式。
  可选的 f 和 limit 参数具有与 print_stack() 的相同含义。

.. function:: ttraceback.format_list(extracted_list)

  给定一个由元组或如 extract_tb() 或 extract_stack() 所返回的 FrameSummary 对象组成的列表，返回一个可打印的字符串列表。
  结果列表中的每个字符串都对应于参数列表中具有相同索引号的条目。
  每个字符串以一个换行符结束；对于那些源文本行不为 None 的条目，字符串也可能包含内部换行符。

.. function:: traceback.print_exc(limit=None, file=None, chain=True)

  This is a shorthand for print_exception(sys.exception(), limit, file, chain).

.. function:: traceback.format_exc(limit=None, chain=True)

  以字符串形式打印堆栈异常.

  类似于 print_exc(limit) 但会返回一个字符串而不是打印到一个文件。

.. function:: traceback.format_tb(tb, limit=None)

  是 format_list(extract_tb(tb, limit)) 的简写形式。

.. function:: traceback.format_stack(f=None, limit=None)

  以字符串的形式打印堆栈调用.

  是 format_list(extract_stack(f, limit)) 的简写形式。







