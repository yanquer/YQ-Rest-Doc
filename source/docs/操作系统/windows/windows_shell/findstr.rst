=============================
findstr
=============================

搜索字符串, 想找类似与linux下 :doc:`/docs/操作系统/linux/linux指令/grep` 时找到的::

  PS C:\Users\yanque> tasklist | findstr dllhost
  dllhost.exe                   1416 Console                    9     27,020 K
  dllhost.exe                  19296 Console                    9     17,220 K

在文件中寻找字符串, 语法::

  FINDSTR [/B] [/E] [/L] [/R] [/S] [/I] [/X] [/V] [/N] [/M] [/O] [/P] [/F:file]
          [/C:string] [/G:file] [/D:dir list] [/A:color attributes] [/OFF[LINE]]
          strings [[drive:][path]filename[ ...]]

支持参数说明::

  /B         在一行的开始配对模式。
  /E         在一行的结尾配对模式。
  /L         按字使用搜索字符串。
  /R         将搜索字符串作为一般表达式使用。
  /S         在当前目录和所有子目录中搜索匹配文件。
  /I         指定搜索不分大小写。
  /X         打印完全匹配的行。
  /V         只打印不包含匹配的行。
  /N         在匹配的每行前打印行数。
  /M         如果文件含有匹配项，只打印其文件名。
  /O         在每个匹配行前打印字符偏移量。
  /P         忽略有不可打印字符的文件。
  /OFF[LINE] 不跳过带有脱机属性集的文件。
  /A:attr    指定有十六进位数字的颜色属性。请见 "color /?"
  /F:file    从指定文件读文件列表 (/ 代表控制台)。
  /C:string  使用指定字符串作为文字搜索字符串。
  /G:file    从指定的文件获得搜索字符串。 (/ 代表控制台)。
  /D:dir     查找以分号为分隔符的目录列表
  strings    要查找的文字。
  [drive:][path]filename
             指定要查找的文件。

除非参数有 /C 前缀，请使用空格隔开搜索字符串。
例如, 在文件 x.y 中寻找 "hello" 或 "there" ::

  FINDSTR "hello there" x.y

文件 x.y  寻找"hello there" ::

  FINDSTR /C:"hello there" x.y

一般表达式的快速参考::

  .        通配符: 任何字符
  *        重复: 以前字符或类出现零或零以上次数
  ^        行位置: 行的开始
  $        行位置: 行的终点
  [class]  字符类: 任何在字符集中的字符
  [^class] 补字符类: 任何不在字符集中的字符
  [x-y]    范围: 在指定范围内的任何字符
  /x       Escape: 元字符 x 的文字用法
  /<xyz    字位置: 字的开始
  xyz/>    字位置: 字的结束

多个搜索条件使用空格隔开, 如列出当前目录下, 非 ``.`` 开头, 不以 ``music`` 或者 ``video`` 开头的结果::

  dir /b | findstr /v /i "\. music video"

