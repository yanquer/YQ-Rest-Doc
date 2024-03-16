=============================
find
=============================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


在指定目录下查找文件。

任何位于参数之前的字符串都将被视为欲查找的目录名。

如果使用该命令时，不设置任何参数，则 find 命令将在当前目录下查找子目录与文件。并且将查找到的子目录和文件全部进行显示。

语法::

	find   path   -option   [   -print ]   [ -exec   -ok   command ]   {} \;

find 根据下列规则判断 path 和 expression，在命令列上第一个 - ( ) , ! 之前的部份为 path，之后的是 expression。如果 path 是空字串则使用目前路径，如果 expression 是空字串则使用 -print 为预设 expression。
expression 中可使用的选项有二三十个之多，在此只介绍最常用的部份。

.. csv-table:: 匹配方式
	:delim: :

	-mount, -xdev	: 只检查和指定目录在同一个文件系统下的文件，避免列出其它文件系统中的文件
	-amin n			: 在过去 n 分钟内被读取过
	-anewer file 	: 比文件 file 更晚被读取过的文件
	-atime n 		: 在过去 n 天内被读取过的文件
	-cmin n 		: 在过去 n 分钟内被修改过
	-cnewer file 	:比文件 file 更新的文件
	-ctime n 		: 在过去 n 天内创建的文件
	-mtime n 		: 在过去 n 天内修改过的文件. n为数字，表示n天之前的【一天之内】被改动过的文件
	-empty 			: 空的文件-gid n or -group name, gid 是 n 或是 group 名称是 name
	-ipath p, -path p 		: 路径名称符合 p 的文件，ipath 会忽略大小写
	-name name, -iname name : 文件名称符合 name 的文件。iname 会忽略大小写
	-size n 		: 文件大小 是 n 单位，b 代表 512 位元组的区块，c 表示字元数(字节)，k 表示 kilo bytes(kb)，w 是二个位元组, M(Mb), G(Gb), 可与 + - 搭配使用。
	-type c 		: 文件类型是 c 的文件. 支持参数, d 目录, c 字型装置文件, b 区块装置文件, p 具名贮列, f 一般文件, l 符号连结, s socket
	-pid n 			: process id 是 n 的文件
	-inum n 		: 指定 inodenum 为n
	-newer file 	: file作为一个存在的文件，列出比file更新的文件
	-user user 		: 文件属主为user
	-group group 	: 文件属组为group
	-perm			: 文件权限
	-maxdepth		: 递归查找层数
	-delete			: 对于所有检索到的项目进行删除操作
	-exec			: 执行指定命令
	-samefile : 查看有哪些相同的文件, 比如当你知道一个文件, 想知道它有被哪些链接了

你可以使用 ( ) 将运算式分隔，并使用下列运算::

	exp1 -and exp2
	! expr
	-not expr
	exp1 -or exp2
	exp1, exp2

	# -and 等价于 -a
	# -or  等价于 -o

如检索 /usr 下文件名以 python 开头且类型为目录的文件::

	find /usr -type d -name 'python*'

该命令等同于::

	find /usr -type d -a -name 'python*'

更复杂的组合形式如::

	find / '(' -mmin -5 -o -mtime +50 ')' -a -type f



选项详解
=============================

mtime
-----------------------------

文件修改时间::

	-mtime n 	: 在过去 n 天内修改过的文件. n为数字，表示n天之前的【一天之内】被改动过的文件
	-mtime +n 	: 列出n天之前被改动过的文件【不包含n天】
	-mtime -n 	: 列出n天之后被改动过的文件【包含n天】

type
-----------------------------

文件类型::

	-type d 目录
	-type c 字型装置文件
	-type b 区块装置文件
	-type p 具名贮列
	-type f 一般文件
	-type l 符号连结
	-type s socket

size
-----------------------------

文件大小(对于目录来说没有意义)::

	c 字节
	k kb
	M Mb
	G Gb

可与 +, - 搭配使用, 如检索文件大小高于 1 GB 的文件::

	find / -size +1G

perm
-----------------------------

文件权限

如搜索 /usr 目录下所有权限为 r-xr-xr-x（即系统中的所有用户都只有读写权限）的文件和目录，

可以使用以下命令::

	find /usr -perm a=rx

或者::

	find /usr -perm u=rx,g=rx,o=rx

亦可直接使用数字的形式::

	find /usr -perm 333

若仅需要匹配某一个字集::

	# /a=x 中的 / 表示仅匹配权限子集. 即只要有执行权限即可.
	find /usr -perm /a=x

maxdepth
-----------------------------

find默认是递归检索项目的, 可使用 ``-maxdepth`` 限制递归查找层数.

如搜索时向下递归的层数最大为 3::

	find / -maxdepth 3

exec
-----------------------------

执行自定义命令

如将 home 目录下所有的 py 文件复制到 bak 目录下::

	find ~ -type f -name '*.py' -exec cp {} bak ';'

其中的大括号（{}）作为检索到的文件的 占位符 ，而分号作为命令结束的标志。因为分号是 Shell 中有特殊含义的符号，所以需要使用单引号括起来, 或者用 ``\`` 也可。

+的作用
+++++++++++++++++++++++++++++

多文件打包::

	# + 表示多个文件都一起打包在此处, 否则最终压缩包内只有一个py文件
	find ~ -type f -name '*.py' -exec tar -czvf py_file.tar.gz {} +




