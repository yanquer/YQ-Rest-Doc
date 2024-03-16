=======================
pystack
=======================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


pypi: https://pypi.org/project/pystack/
github: https://github.com/bloomberg/pystack

查看其他python进程堆栈信息

安装, 此软件依赖与底层c库, 所以对于linux, mac等, 需要提前安装依赖库,
即使没有从源码构建.

mac这个库安装的时候一直找不到 elf.h, 放弃::

  In file included from src/pystack/_pystack.cpp:817:
  src/pystack/_pystack/elf_common.h:12:10: fatal error: 'elf.h' file not found
  #include <elf.h>
            ^~~~~~~


