=============================
shell退出状态码
=============================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 教程, shell语法规范
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


.. csv-table:: Linux退出状态码
  :header: 状态码, 描述

  0,      命令成功结束
  1,      通用未知错误
  2,      误用shell命令
  126,    命令不可执行
  127,    没找到命令
  128,    无效退出参数
  128+x,  Linux信号x的严重错误
  130,    命令通过Ctrl+C终止
  255,    退出状态码越界

返回值
=============================

只能返回整数值::

  #!/bin/bash

  function getResultFun(){
      echo "这是我的第一个 shell 函数!"
      return `expr 1 + 1`
  }

  getResultFun
  echo $?

