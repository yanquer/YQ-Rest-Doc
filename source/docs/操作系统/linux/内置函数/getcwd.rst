===================================
getcwd
===================================


.. post:: 2023-02-23 23:14:15
  :tags: linux, 内置函数
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


获取当前目录

getcwd() failed
===================================

报错::

  sh: 0: getcwd() failed: No such file or directory

在一个不存在的目录上执行命令，会报上述错误， 这个目录是曾经存在，
后来给删除了，但某些管理工具的命令还存在于这个目录下执行。会报上述错误

方法是 换目录



