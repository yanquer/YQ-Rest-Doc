===========================
fileinput
===========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/fileinput.html

迭代来自多个输入流的行

此模块实现了一个辅助类和一些函数用来快速编写访问标准输入或文件列表的循环。
如果你只想要读写一个文件请参阅 open()。

典型用法为::

  import fileinput
  for line in fileinput.input(encoding="utf-8"):
      process(line)

此程序会迭代 sys.argv[1:] 中列出的所有文件内的行，如果列表为空则会使用 sys.stdin。
如果有一个文件名为 '-'，它也会被替换为 sys.stdin 并且可选参数 mode 和 openhook 会被忽略。
要指定替代文件列表，请将其作为第一个参数传给 input()。 也允许使用单个文件。

所有文件都默认以文本模式打开，但你可以通过在调用 input() 或 FileInput 时指定 mode 形参来重载此行为。
如果在打开或读取文件时发生了 I/O 错误，将会引发 OSError。

在 3.3 版更改: 原来会引发 IOError；现在它是 OSError 的别名。

如果 sys.stdin 被使用超过一次，则第二次之后的使用将不返回任何行，
除非是被交互式的使用，或都是被显式地重置 (例如使用 sys.stdin.seek(0))。

空文件打开后将立即被关闭；它们在文件列表中会被注意到的唯一情况只有当最后打开的文件为空的时候。

反回的行不会对换行符做任何处理，这意味着文件中的最后一行可能不带换行符。

你可以通过将 openhook 形参传给 fileinput.input() 或
FileInput() 来提供一个打开钩子以便控制文件的打开方式。
此钩子必须为一个函数，它接受两个参数 filename 和 mode，并返回一个以相应模式打开的文件类对象。
如果指定了 encoding 和/或 errors，它们将作为额外的关键字参数被传给这个钩子。
此模块提供了一个 hook_compressed() 来支持压缩文件。




