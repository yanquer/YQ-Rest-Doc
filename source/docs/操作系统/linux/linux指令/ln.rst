===============
ln
===============


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


功能
===============

用来为文件创建链接，链接类型分为硬链接和符号链接两种，默认的链接类型是硬链接。如果要创建符号链接必须使用"-s"选项。

注意：符号链接文件不是一个独立的文件，它的许多属性依赖于源文件，所以给符号链接文件设置存取权限是没有意义的。

选项参数
===============


.. csv-table:: ln选项参数
	:header: 选项, 说明
	:delim: :

	--backup[=CONTROL]			:	为每个已存在的目标文件创建备份文件
	-b							:	类似--backup，但不接受任何参数
	-d, -F, --directory			:	创建指向目录的硬链接(只适用于超级用户)
	-f, --force					:	强行删除任何已存在的目标文件
	-i, --interactive			:	覆盖既有文件之前先询问用户；
	-L, --logical				:	取消引用作为符号链接的目标
	-n, --no-dereference		:	把符号链接的目的目录视为一般文件；
	-P, --physical				:	直接将硬链接到符号链接
	-r, --relative				:	创建相对于链接位置的符号链接
	-s, --symbolic				:	对源文件建立符号链接，而非硬链接；
	-S, --suffix=SUFFIX			:	用"-b"参数备份目标文件后，备份文件的字尾会被加上一个备份字符串，预设的备份字符串是符号“~”，用户可通过“-S”参数来改变它；
	-t, --target-directory=DIRECTORY	:	指定要在其中创建链接的DIRECTORY
	-T, --no-target-directory	:	将“LINK_NAME”视为常规文件
	-v, --verbose				:	打印每个链接文件的名称
	--help						:	显示此帮助信息并退出
	--version					:	显示版本信息并退出

.. note::

	常用: ``ln -snf $src $dist``

