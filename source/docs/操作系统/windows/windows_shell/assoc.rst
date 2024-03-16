====================
assoc
====================


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


显示或修改文件扩展名关联::

  ASSOC [.ext[=[fileType]]]

  .ext      指定跟文件类型关联的文件扩展名
  fileType  指定跟文件扩展名关联的文件类型

键入 ASSOC 而不带参数，显示当前文件关联。
如果只用文件扩展名调用 ASSOC，则显示那个文件扩展名的当前文件关联。
如果不为文件类型指定任何参数，命令会删除文件扩展名的关联。


.. note::

  assoc 设置 文件扩展名关联, 关联到'文件类型'

  与 :doc:`/docs/操作系统/windows/windows_shell/ftype` 设置文件类型关联, 关联到'执行程序和参数' 类似



