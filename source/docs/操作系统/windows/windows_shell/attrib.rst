=================
attrib
=================


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


显示或更改文件属性::

  ATTRIB [+R | -R] [+A | -A] [+S | -S] [+H | -H] [+O | -O] [+I | -I] [+X | -X] [+P | -P] [+U | -U]
        [drive:][path][filename] [/S [/D]] [/L]

选项/参数说明::

  +   设置属性。
  -   清除属性。
  R   只读文件属性。
  A   存档文件属性。
  S   系统文件属性。
  H   隐藏文件属性。
  O   脱机属性。
  I   无内容索引文件属性。
  X   无清理文件属性。
  V   完整性属性。
  P   固定属性。
  U   非固定属性。
  [drive:][path][filename]
      指定属性要处理的文件。
  /S  处理当前文件夹及其所有子文件夹中
      的匹配文件。
  /D  也处理文件夹。
  /L  处理符号链接和
      符号链接目标的属性

例::

  md autorun
  attrib +a +s +h autorun

上面的命令将建立文件夹autorun，然后将其设为存档、系统、隐藏属性

