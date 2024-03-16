=====================================
指令export、env、set三者的区别
=====================================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 概念性
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


export、env、set三者的区别

.. note::

  echo $PATH  #输出当前环境变量
  locale   #设置系统语言环境

- set 用来显示本地变量 :doc:`/docs/操作系统/linux/linux指令/set`
- env 用来显示环境变量 :doc:`/docs/操作系统/linux/linux指令/env`
- export 用来显示和设置环境变量 :doc:`/docs/操作系统/linux/linux指令/export`

shell变量
=====================================

shell变量包括两种变量

- 本shell私有的变量：通过赋值语句定义好的变量，可以通过如下方法定义shell变量::

    A1="1234"
    delcare A2="2345"

- 用户的环境变量：通过export语法导出的shell私有变量，可以通过如下方法导出用户环境变量::

    A1="1234"
    export A1  #先定义再导出
    export A3="34"

导出成的用户环境变量可以在所有的shell中看到

总结
=====================================

- set 显示当前shell的定义的私有变量，包括当前用户的环境变量，按变量名称排序；
- env 显示当前用户的变量
- export 显示当前导出成用户变量的shell变量，并显示变量的属性(是否只读)，按变量名称排序；
- declare 同set 一样，显示当前shell的定义的变量，包括用户的环境变量。

每个shell有自己特有的变量（set）显示的变量，这个和用户变量是不同的，
当前用户变量和你用什么shell无关，不管你用什么shell都在，
比如HOME,SHELL等这些变量，但shell自己的变量不同shell是不同的，比
如BASH_ARGC， BASH等，这些变量只有set才会显示，是bash特有的，
export不加参数的时候，显示哪些变量被导出成了用户变量，
因为一个shell自己的变量可以通过export “导出”变成一个用户变量。


