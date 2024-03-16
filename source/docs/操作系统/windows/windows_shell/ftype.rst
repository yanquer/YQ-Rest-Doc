================
ftype
================


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


显示或修改用在文件扩展名关联中的文件类型::

  FTYPE [fileType[=[openCommandString]]]

  fileType  指定要检查或改变的文件类型
  openCommandString 指定调用这类文件时要使用的开放式命令。

键入 FTYPE 而不带参数来显示当前有定义的开放式命令字符串的文件类型。
FTYPE 仅用一个文件类型启用时，它显示那个文件类型目前的开放式命令字符串。
如果不为开放式命令字符串指定，FTYPE 命令将删除那个文件类型的开放式命令字符串。
在一个开放式命令字符串之内，命令字符串 %0 或 %1 被通过关联调用的文件名所代替。
%* 得到所有的参数，
%2 得到第一个参数，
%3 得到第二个，等等。
%~n 得到其余所有以 nth 参数打头的参数；
n 可以是从 2 到 9 的数字。例如::

    ASSOC .pl=PerlScript
    FTYPE PerlScript=perl.exe %1 %*

允许你启用以下 Perl 脚本::

    script.pl 1 2 3

如果不想键入扩展名，则键入以下字符串::

    set PATHEXT=.pl;%PATHEXT%

被启动的脚本如下::

    script 1 2 3

.. note::

  ftype 设置 设置文件类型关联, 关联到'执行程序和参数'

  与 :doc:`/docs/操作系统/windows/windows_shell/assoc` 文件扩展名关联, 关联到'文件类型' 类似

说明:

当你双击一个.txt文件时，windows并不是根据.txt直接判断用 notepad.exe 打开
而是先判断.txt属于 txtfile '文件类型'
再调用 txtfile 关联的命令行 txtfile=%SystemRoot%\system32\NOTEPAD.EXE %1

可以在"文件夹选项"→"文件类型"里修改这2种关联::

  assoc           #显示所有'文件扩展名'关联
  assoc .txt      #显示.txt代表的'文件类型'，结果显示 .txt=txtfile
  assoc .doc      #显示.doc代表的'文件类型'，结果显示 .doc=Word.Document.8
  assoc .exe      #显示.exe代表的'文件类型'，结果显示 .exe=exefile
  ftype           #显示所有'文件类型'关联
  ftype exefile   #显示exefile类型关联的命令行，结果显示 exefile="%1" %*
  assoc .txt=Word.Document.8

设置.txt为word类型的文档，可以看到.txt文件的图标都变了::

  assoc .txt=txtfile

恢复.txt的正确关联::

  ftype exefile="%1" %*

恢复 exefile 的正确关联

如果该关联已经被破坏，可以运行 command.com ，再输入这条命令


