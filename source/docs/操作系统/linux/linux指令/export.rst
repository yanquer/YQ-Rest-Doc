============================
export
============================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


export用于设置或显示环境变量,
显示当前导出成用户变量的shell变量(可以在当前shell以及子shell中使用的变量):

-p
  列出所有shell赋予程序的环境变量
-n
  删除指定的环境变量。实际并未删除，只是不会输出到后续指令的执行环境中
-f
  代表[变量名称]中为函数名称

还有一个特殊的作用是, 使用export导出后, 修改后的环境变量才对子进程可见, 如更新
PATH环境变量, 若只设置::

  PATH=“/usr/local/new_path:$PATH”

则生效范围只有当前shell, 使用::

  export PATH=$PATH

后才能对子进程可见

更规范的说法: 将一个shell私有变量使用export导出, 使其提升为用户变量.

