=====================
getfattr
=====================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


get extended attributes of filesystem objects

获取文件系统扩展属性信息(用 :doc:`/docs/操作系统/linux/linux指令/setfattr` 命令设置的属性)

语法格式::

  getfattr [参数] 文件名

常用参数：

-d
  显示所有扩展属性值
-e
  设置编码值类型
-h
  不引用符号链接
-m
  包括名称匹配正则表达式模式的属性
-n
  显示已命名的扩展属性值
-P
  跳过所有符号链接
-R
  递归处理所有子文件
--help
  显示帮助信息
--version
  显示版本信息




