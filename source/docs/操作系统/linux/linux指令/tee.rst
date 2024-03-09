=====================
tee
=====================

| 读取标准输入的数据，并将其内容输出成文件(同时输出到终端与文件)。

语法::

	tee [-ai][--help][--version][文件...]

参数
=====================

-a,--append 			附加到既有文件的后面，而非覆盖它．
-i,--ignore-interrupts 	忽略中断信号。
--help 					在线帮助。
--version 				显示版本信息。

实例
=====================

将 ls 的结果同时输出到屏幕与文件::

	┌──(yanque㉿3675b5ebb8ce)-[~/test]
	└─$ ls -lh
	total 8.0K
	-rw-r--r-- 1 yanque yanque 8 Feb 25 06:42 file1
	-rw-r--r-- 1 yanque yanque 8 Feb 25 06:42 file2

	┌──(yanque㉿3675b5ebb8ce)-[~/test]
	└─$ ls -lh | tee t.log
	total 8.0K
	-rw-r--r-- 1 yanque yanque 8 Feb 25 06:42 file1
	-rw-r--r-- 1 yanque yanque 8 Feb 25 06:42 file2
	-rw-r--r-- 1 yanque yanque 0 Feb 25 06:43 t.log

	┌──(yanque㉿3675b5ebb8ce)-[~/test]
	└─$ cat t.log
	total 8.0K
	-rw-r--r-- 1 yanque yanque 8 Feb 25 06:42 file1
	-rw-r--r-- 1 yanque yanque 8 Feb 25 06:42 file2
	-rw-r--r-- 1 yanque yanque 0 Feb 25 06:43 t.log

.. note::

	如果只是使用 tee, 会打开一个交互窗口, 在里面输入需要写入的内容,

	退出直接 ctrl + c 即可