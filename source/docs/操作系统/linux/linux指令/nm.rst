===========================
nm
===========================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


linux下自带的特定文件分析工具，
一般用来检查分析二进制文件、库文件、可执行文件中的符号表，返回二进制文件中各段的信息。

目标文件、库文件、可执行文件
======================================================

首先，提到这三种文件，我们不得不提的就是gcc的编译流程：预编译，编译，汇编，链接。

目标文件
  常说的目标文件是我们的程序文件(.c/.cpp,.h)经过
  预编译，编译，汇编过程生成的二进制文件,不经过链接过程，编译生成指令为::

    gcc(g++) -c file.c(file.cpp)

  将生成对应的file.o文件,file.o即为二进制文件
库文件
  分为静态库和动态库，这里不做过多介绍，库文件是由多个二进制文件打包而成，生成的.a文件，
  示例::

    ar -rsc liba.a test1.o test2.o test3.o

  将test1.o test2.o test3.o三个文件打包成liba.a库文件
可执行文件
  可执行文件是由多个二进制文件或者库文件(由上所得，库文件其实是二进制文件的集合)
  经过链接过程生成的一个可执行文件，对应windows下的.exe文件，
  可执行文件中有且仅有一个main()函数(用户程序入口，一般由bootloader指定，当然也可以改)，
  一般情况下，二进制文件和库文件中是不包含main()函数的，
  但是在linux下用户有绝对的自由，做一个包含main函数的库文件也是可以使用的,
  但这不属于常规操作，不作讨论。

上述三种文件的格式都是二进制文件。

为什么要用到nm
===========================

在上述提到的三种文件中，用编辑器是无法查看其内容的(乱码)，
所以当我们有这个需求(例如debug，查看内存分布的时候)
去查看一个二进制文件里包含了哪些内容时，这时候就将用到一些特殊工具，
linux下的nm命令就可以完全胜任(同时还有objdump和readelf工具，这里暂不作讨论)。

nm的常用命令参数
===========================

-A, -o, --print-file-name
  打印出每个符号属于的文件
-a, --debug-syms
  打印出所有符号，包括debug符号
-B
  BSD码显示

-C, --demangle[=style]
  对低级符号名称进行解码，
  C++文件需要添加(不然看C++编译好的内容就是编码的)

--no-demangle
  不对低级符号名称进行解码，默认参数
-D, --dynamic
  显示动态符号而不显示普通符号，一般用于动态库
-f format, --format=format
  显示的形式，默认为bsd，可选为sysv和posix
-g, --extern-only
  仅显示外部符号
-h, --help
  国际惯例，显示命令的帮助信息
-n, -v, --numeric-sort
  显示的符号以地址排序，而不是名称排序
-p, --no-sort
  不对显示内容进行排序
-P, --portability
  使用POSIX.2标准
-V, --version
  国际管理，查看版本
--defined-only
  仅显示定义的符号(Display only defined symbols for each object file)

对-C解码C++的说明
===========================

比如源码定义了add函数::

  int add(int a, int b){return a+b;}

编译为动态库文件(Mac下不知道为什么像是个假的动态库, 因为没有动态库符号表)::

  g++ -std=c++11 -dynamiclib -o libtest2.dylib test2.cpp

然后
nm不带C查看::

  $ nm -n  libtest2.dylib
  0000000000003d80 T __Z3addii

nm带C查看::

  $ nm -n -C libtest2.dylib
  0000000000003d80 T add(int, int)

关于输出数据的说明
===========================

以上为例::

  0000000000003d80 T add(int, int)

- 第一列: 偏移地址
- 第二列: 当前条目所对应的内存所在部分
- 第三列: 符号内容

字符所对应的含义::

  A     ：符号的值是绝对值，不会被更改
  B或b  ：未被初始化的全局数据，放在.bss段
  D或d  ：已经初始化的全局数据
  G或g  ：指被初始化的数据，特指small objects
  I     ：另一个符号的间接参考
  N     ：debugging 符号
  p     ：位于堆栈展开部分
  R或r  ：属于只读存储区
  S或s  ：指为初始化的全局数据，特指small objects
  T或t  ：代码段的数据，.test段
  U     ：符号未定义
  W或w  ：符号为弱符号，当系统有定义符号时，使用定义符号，当系统未定义符号且定义了弱符号时，使用弱符号。
  ？    ：unknown符号

参考: `linux下强大的文件分析工具 -- nm <https://www.cnblogs.com/downey-blog/p/10477835.html>`_

关于符号表说明
===========================

主要是针对C++文件的编译

以下面数据为例

源码为::

  int add(int a, int b){
    int tmp = a + 3;
    return tmp + b;
  }

  extern "C"{
    int add2(int a, int b){ return a+b+10;}
  }

``extern "C"`` 表示使用C标准导出函数, 意思是不会对函数名称进行修饰

编译指令::

  g++ -std=c++11 -dynamiclib -g -o libtest2.dylib test2.cpp

使用nm查看信息::

  $ nm -n -U libtest2.dylib
  0000000000003d60 T __Z3addii
  0000000000003d80 T _add2

对其进行解码::

  $ nm -n -CU libtest2.dylib
  0000000000003d60 T add(int, int)
  0000000000003d80 T _add2

如果要在其他地方进行提取, 如::

  // 定义原始函数指针类型
  typedef int (*OrigAddFunc)(int a, int b);

  // 定义全局变量存储原始函数指针
  OrigAddFunc origAdd = NULL;

  void* handle = dlopen("./libtest2.dylib", RTLD_LAZY);
  if (handle == NULL) {
      printf("无法打开当前可执行文件\n, info: %s\n", dlerror());
      return 1;
  }

  origAdd = (OrigAddFunc)dlsym(handle, "_Z3addii");
  if (origAdd == NULL) {
      printf("无法获取原始函数地址\n, info: %s\n", dlerror());
      dlclose(handle);
      return 1;
  }

主要是 ``(OrigAddFunc)dlsym(handle, "_Z3addii");``,
dlsym是针对库文件的函数名进行寻找,
C++默认会进行函数名修士, 所以如果要找 add 函数,
得先用 nm 找出修饰后的名称 ``_Z3addii`` (输出去掉下划线), 使用解析后的是不行的

如果是 add2, 源码已经用 ``extern "C"`` 指定使用C标准导出, 就可直接 ``dlsym(handle, "add2")``

