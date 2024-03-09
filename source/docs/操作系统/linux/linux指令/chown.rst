===================
chown
===================

Linux chown（change owner）用于变更文件或目录的拥有者或所属群组

语法::

  chown [-cfhvR] [--help] [--version] user[:group] file...

选项参数
===================

-c  显示更改的部分的信息
-f  忽略错误信息
-h  修复符号链接
-v  显示详细的处理信息
-R  处理指定目录以及其子目录下的所有文件
--help                  显示辅助说明
--version               显示版本
-f, --quite, --silent   不显示错误信息
--reference=<file>      使用 file 文件的所有者和组, 而不是指定的 user:group

其他::

  user : 新的文件拥有者的使用者 ID
  group : 新的文件拥有者的使用者组(group)


说明::

  #user:group   指定所有者和所属工作group。当省略“:group”，仅改变文件所有者
  #文件: 指定要改变所有者和工作group的文件列表。支持多个文件和目标，支持shell通配符。
  chown -R user:group  file

