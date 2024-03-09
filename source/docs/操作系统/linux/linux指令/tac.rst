=========================
tac
=========================

跟 :doc:`cat` 相反

tac命令就是将文件反向输出(有缓冲)，刚好和cat输出相反。

语法格式::

  tac [参数] [文件]

常用参数

-b          在行前而非行尾添加分隔标志
-r          将分隔标志视作正则表达式来解析
-s          使用指定字符串代替换行作为分隔标志
--version   显示版本信息并退出
--help      显示此帮助信息并退出

**参考实例**

反向列出test.txt文件的内容::

  [root@linuxcool ~]# cat test.txt
  hello world
  hello linuxcool
  hello linuxprobe
  [root@linuxcool ~]# tac test.txt
  hello linuxprobe
  hello linuxcool
  hello world


