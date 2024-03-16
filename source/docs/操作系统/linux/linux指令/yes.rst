===============
yes
===============


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


一直输出y换行,
对于有些交互式的指令且需要输入y来确认时可以使用, 比如::

  yes | apt install ssh

效果等价于::

  apt install ssh -y


yes命令用于重复输出字符串（output a string repeatedly until killed）。
这个命令可以帮你自动回答命令行提示，
例如，进入一个含有多个文件的目录，执行::

  yes | rm -i *

所有的::

  rm: remove regular empty file `xxx'?

提示都会被自动回答 y。这在编写脚本程序的时候会很用处。
yes命令还有另外一个用途，可以用来生成大的文本文件。（-i交互式）

参数

i
  会交互式询问

yes 后面直接跟单词或者字符表示一直输出这个





