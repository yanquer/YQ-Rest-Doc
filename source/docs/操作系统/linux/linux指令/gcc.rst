========================
gcc
========================

详见 :doc:`/docs/后端/c/gcc(++)编译器`

**选项**

-I<dir> 	指定头文件所在目录, 会优先找此处指定的目录
-l<dir> 	指定库路径. 指定需要链接的库名，用于告诉链接器需要链接哪些库文件
-L<dir> 	指定库文件所在目录
-fno-lto  禁用链接时优化（LTO）
					当使用该选项编译源代码时，编译器将不会进行链接时优化，
					这可能会导致一些性能上的损失，但也可以避免某些链接错误。

.. note::

	`-fno-lto` 主要用于使用的链接文件是由其他版本LTO的gcc编译时导致无法继续编译时候吧

