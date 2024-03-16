=====================
readelf
=====================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


参考:

- elf文件说明及介绍: https://zhuanlan.zhihu.com/p/112754720
- https://www.jianshu.com/p/0599d846e1df
- https://zhuanlan.zhihu.com/p/30516267

用于显示 elf 格式文件的信息。

语法::

  readelf elf-file(s)

readelf 用来显示一个或者多个 elf 格式的目标文件的信息，
可以通过它的选项来控制显示哪些信息。这里的 elf-file(s) 就表示那些被检查的文件。
可以支持32位，64位的 elf 格式文件，也支持包含 elf 文件的文档
（这里一般指的是使用 ar 命令将一些 elf 文件打包之后生成的例如 lib*.a 之类的“静态库”文件）。

与 :doc:`/docs/操作系统/linux/linux指令/objdump` 有点类似

选项(常用):

-a    显示so文件所以信息
-h    ELF文件头
-l program-headers
      静态加载分析时需要的信息
-S section-headers
      静态加载分析时需要的信息
-e    头信息，elf header，section header，program header
-s    显示符号表
-d    显示动态节



