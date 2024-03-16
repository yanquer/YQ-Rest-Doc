===================
elf文件
===================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 概念性
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


参考:

- https://zhuanlan.zhihu.com/p/59590848
- https://zhuanlan.zhihu.com/p/112754720

Linux 上可执行程序遵循的是 ELF（Executable and Linking Format）格式,
是一个定义了目标文件内部信息如何组成和组织的文件格式。
内核会根据这些信息加载可执行文件，内核根据这些信息可以知道从文件哪里获取代码，
从哪里获取初始化数据，在哪里应该加载共享库，等信息。

分类

- .o目标文件
  由::

    gcc -c test.c

  得到的test.o就是目标文件，目标文件通过链接可生成可执行文件。
  静态库其实也算目标文件，静态库是通过ar命令将目标打包为.a文件。
  如::

    ar crv libtest.a test.o
- 可执行文件
  可由::

    gcc -o test test.c

  生成
- .so共享库
  可由生成::

    gcc test.c -fPIC -shared -o libtest.so

可以通过 :doc:`/docs/操作系统/linux/linux指令/readelf` 来区分上面三种类型的ELF文件

