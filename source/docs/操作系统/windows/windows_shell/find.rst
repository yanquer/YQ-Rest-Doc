===============
find
===============


在文件中搜索字符串::

  FIND [/V] [/C] [/N] [/I] [/OFF[LINE]] "string" [[drive:][path]filename[ ...]]

选项::

  /V         显示所有未包含指定字符串的行。
  /C         仅显示包含字符串的行数。
  /N         显示行号。
  /I         搜索字符串时忽略大小写。
  /OFF[LINE] 不要跳过具有脱机属性集的文件。
  "string" 指定要搜索的文本字符串。
  [drive:][path]filename
             指定要搜索的文件。

如果没有指定路径，FIND 将搜索在提示符处键入
的文本或者由另一命令产生的文本。

但是实际使用, 感觉 ``dir | find /c /v`` 更像是打印所有行

统计行数, 比如查找的python进程的个数::

  tasklist | findstr /I "python" | find /c /v ""

