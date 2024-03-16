===========================
g++
===========================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


一般用于编译C++

选项:

-I<dir> 	    指定头文件所在目录, 会优先找此处指定的目录
-l<dir> 	    指定需要链接的库名，用于告诉链接器需要链接哪些库文件
              即指定动态库的名称(去掉lib前缀和.so后缀)
-L<dir> 	    指定动态库搜索路径
-fno-lto      禁用链接时优化（LTO）
					    当使用该选项编译源代码时，编译器将不会进行链接时优化，
					    这可能会导致一些性能上的损失，但也可以避免某些链接错误。
-shared       生成动态库(.so文件),而不是静态库(.a文件)
-fPIC         生成位置无关代码(position-independent code),
              使得代码可以在不同的内存地址执行,这对于动态库是必需的
-g            在编译过程中生成调试信息(debugging information),
              并将其嵌入到最终的可执行文件或目标文件中。
              带有调试信息的可执行文件可以用调试器(debugger)来调试和跟踪代码
-c            仅编译,不链接。只生成目标文件(.o文件),不生成可执行文件。


对于 `-c` 选项的说明
===========================

通常g++的使用流程是:

- 编译源文件(.c或.cpp)生成目标文件(.o文件),使用-c选项
- 链接多个目标文件和库文件,生成可执行文件,使用-o选项指定输出文件

所以-c选项使得编译和链接成两个步骤进行。比如::

  g++ -c hello.c  # 仅编译,生成hello.o
  g++ -c main.c   # 仅编译,生成main.o
  g++ hello.o main.o -o hello # 链接目标文件生成可执行文件

如果不使用-c选项,g++会自动执行编译和链接两个步骤,例如::

  g++ hello.c main.c -o hello  # 会编译hello.c和main.c,然后链接生成可执行文件hello

例-生成静态库文件和共享库文件
================================

编译myfile.cpp::

  g++ -c myfile.cpp

.. note::

  静态库文件和共享库文件都是由.o目标文件生成

生成共享库文件libmy.so::

  g++ -shared -fPCI -o libmy.so myfile.o

打包成静态库文件libmy.a::

  ar -r libmy.a myfile.o
  # ar: creating libmy.a




