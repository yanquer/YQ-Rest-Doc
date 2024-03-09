==================
dis
==================

官网: `dis --- Python 字节码反汇编器 <https://docs.python.org/zh-cn/3/library/dis.html?highlight=dis#module-dis>`_

通过反汇编支持CPython的 bytecode 分析。
该模块作为输入的 CPython 字节码在文件 Include/opcode.h 中定义，并由编译器和解释器使用。


CPython 实现细节： 字节码是 CPython 解释器的实现细节。
不保证不会在Python版本之间添加、删除或更改字节码。不应考虑将此模块的跨 Python VM 或 Python 版本的使用。

示例：给出函数 myfunc()::

  def myfunc(alist):
      return len(alist)

the following command can be used to display the disassembly of myfunc()::

  >>>
  dis.dis(myfunc)
    2           0 RESUME                   0

    3           2 LOAD_GLOBAL              1 (NULL + len)
              14 LOAD_FAST                0 (alist)
              16 PRECALL                  1
              20 CALL                     1
              30 RETURN_VALUE



