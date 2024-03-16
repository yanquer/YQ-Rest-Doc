=========================
rename
=========================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


在Debian或者Ubuntu环境下使用的语法是::

  rename 's/stringx/stringy/' files

而在CentOS下或者RedHat下是::

  rename stringx stringy files

rename的参数分为三部分::

  #stringx ： 被替换字符串
  #stringy ：替换字符串
  #files ：匹配的文件列表

