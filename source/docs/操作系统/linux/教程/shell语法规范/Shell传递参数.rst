==================================
Shell传递参数
==================================


.. post:: 2023-02-23 23:14:15
  :tags: linux, 教程, shell语法规范
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


主要是Shell传递命令行参数

特殊的 shell 参数经常在 shell 脚本里面被用到::

  shell 参数	值
  $0			shell 或 shell 脚本的名称
  $1			第一个 shell 参数
  $9			第 9 个 shell 参数
  $###			位置参数数量
  "$*"		"$1 $2 $3 $4 … "
  "$@"		"$1" "$2" "$3" "$4" …
  $?			最近一次命令的退出状态码
  $$			这个 shell 脚本的 PID
  $!			最近开始的后台任务 PID

Shell参数展开列表
==================================

参数表达式形式		如果 var 变量已设置那么值为	如果 var 变量没有被设置那么值为::

  ${var:-string}	"$var"						"string"
  ${var:+string}	"string"					"null"
  ${var:=string}	"$var"						"string" (并运行 "var=string")
  ${var:?string}	"$var"						在 stderr 中显示 "string" (出错退出)

详见: :doc:`shell的变量替换`

重要的Shell参数替换列表
==================================

参数替换形式与结果::

  ${var%suffix}     删除位于 var 结尾的 suffix 最小匹配模式
  ${var%%suffix}    删除位于 var 结尾的 suffix 最大匹配模式
  ${var###prefix}   删除位于 var 开头的 prefix 最小匹配模式
  ${var####prefix}  删除位于 var 开头的 prefix 最大匹配模式

详见: :doc:`shell的变量替换`


