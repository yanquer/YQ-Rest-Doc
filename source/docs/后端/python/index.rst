================================
Python
================================

.. toctree::
  :glob:

  Web框架/index
  cookbook/*
  相关技术实现/index
  python三方库/*
  python标准库/*
  概念相关/*
  性能分析/index
  包管理器
  问题总结/index
  教程/index

python 中 := 的作用
================================

部分语言中 := 是一个赋值语句

python正常来说是没有这种这种语法的

不过有一种特殊情况是用于生成式的赋值操作

    [x for x in range(10)]
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [y for x in range(10) if (y:=(x*2))]
    # [2, 4, 6, 8, 10, 12, 14, 16, 18]

(暂时只见过这种情况)

python的单双引号
================================

基本没有差别，混合使用可以减少转义::

  >#包含单引号字符串
  >my_str = 'I\'m a student'
  >my_str = "I'm a student"
  >
  >#双引号
  >my_str = "Jason said \"I like you\""
  >my_str = 'Jason said "I like you"'

文件读写模式
================================

python 文件处理的打开方式有很多种::

  os.mknod("test.txt")      # 创建空文件
  fp = open("test.txt",w)   # 直接打开一个文件，如果文件不存在则创建文件

这里主要介绍open 模式,
要了解文件读写模式，需要了解几种模式的区别，以及对应指针

r
  读取文件，若文件不存在则会报错
w
  写入文件，若文件不存在则会先创建再写入，会覆盖原文件
a
  写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾
rb,wb,ab
  分别于r,w,a类似，但是用于读写二进制文件
r+
  可读、可写，文件不存在也会报错，写操作时会覆盖;
  即可以读取文件内容，保存原有内容，追加写内容，写动作则是追加的新内容。其作用和a+基本相同。
w+
  可读，可写，文件不存在先创建，会覆盖;
  即w+是打开后，清空原有内容，成为一个新的空文件，对这个空文件具有读写权限。
a+
  可读、可写，文件不存在先创建，不会覆盖，追加在末尾
rb+
  以二进制读写模式打开 (参见 r+ )
wb+
  以二进制读写模式打开 (参见 w+ )
ab+
  以二进制读写模式打开 (参见 a+ )

参考: `<https://blog.csdn.net/longshenlmj/article/details/9921665>`_


在linux使用py遇到的一些问题
================================

``pkg_resources.DistributionNotFound: pip==0.8.1``

具体报错如下::

  $ sudo pip install gevent-websocket

  Traceback (most recent call last):
  File "/usr/local/bin/pip", line 5, in <module>
  from pkg_resources import load_entry_point
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 2675, in <module>
  parse_requirements(__requires__), Environment()
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 552, in resolve
  raise DistributionNotFound(req)
  pkg_resources.DistributionNotFound: pip==0.8.1


可以使用which pip查看一下命令的位置，然后vim查看一下，
会发现文件里是定死了版本号的，想办法改一下
可能是安装了多个pip版本或者pip管理包工具引起的
最终的解决方案::

  which pip
  # /usr/local/bin/pip

  python -m pip install --upgrade --force pip==9		#这里我需要的是9版本的pip
  cat /usr/local/bin/pip2.7 >/usr/local/bin/pip		#这里是which位置

  which pip
  # /usr/bin/local	这里因为我自己设置的原因有一个
  ln -s /usr/local/bin/pip2.7 /usr/bin/local

  ##
  #	源文件/usr/bin/local和/usr/local/bin/pip都限制死了pip版本，把正确的写进去
  ##

关于python的字典
================================

python3.6之前的dict都是无序的

当版本 >= 3.6 时，字典为有序的

py3.6 之前的无序字典::

  > 是以八行三列的数据结构存储
  >
  > 每一行有三列，每一列占用8byte的内存空间，所以每一行会占用24byte的内存空间
  >
  > 第一列：哈希值对8取余 hash(sKey)
  >
  > 第二列：sKey
  >
  > 第三列：sValue

当字典的键值对数量超过当前数组长度的2/3时，数组会进行扩容，
8行变成16行，16行变成32行。
长度变了以后，原来的余数位置也会发生变化，此时就需要移动原来位置的数据，导致插入效率变低。

py3.6之后::

  > 换成了两个一维列表组成

my_dict = {}

此时的内存示意图 （indices 指数 entries 条目）::

  indices = [None, None, None, None, None, None, None, None]

  entries = []

这里先通过对 sKey 取余为 x ，然后 在 entries 插入一个列表 [ "hash值", sKey, sValue]
再在 indices 保存插入列表的下标，indices[x] = 下标

Python自带的这个 `hash` 函数，和我们传统上认为的Hash函数是不一样的。
Python自带的这个 `hash` 函数计算出来的值，只能保证在每一个运行时的时候不变，
但是当你关闭Python再重新打开，那么它的值就可能会改变，

关于负数取余
================================

带余除法，

对于任意一个整数n ，都可以表示为 n=k*q + r ，其中 0 <= r < q
这里的 r 就是 n 除以 q 的余数，通常记做 n≡r(mod q)

例如-9=(-2)*5+1，则-9除以5的余数为1。

注：java 中 % 优先级高于 -

项目管理工具
================================

才发现python居然没有项目管理工具比如maven

.. 有时候摸索一下maven是怎么弄得

只有个pip :doc:`/docs/后端/python/包管理器`

python的按位与、或
================================

同为 2的n次方 的数

按位或的值等于各个数相加

并且用其中的一个值和最终的数与会得到他本身，反之为0::

  if __name__ == '__main__':
      a, b, c = 2, 4, 8
      d = a | b | c

      print(d)
      print(a & d)
      print(d & c)
      print(32 & d)
      print(32 & c)

      # 14
      # 2
      # 8
      # 0
      # 0

一些斜杠转义
================================

**转义字符**, 顾名思义，也就是在我们编码时会使用到的特殊字符::

  | 转义字符          | 描述       |
  | ----------------- | ---------- |
  | \（处于行尾位置） | 续行符     |
  | \\                | 反斜杠     |
  | ’                 | 单引号     |
  | \"                | 双引号     |
  | \b                | 退格       |
  | \n                | 换行       |
  | \v                | 纵向制表符 |
  | \t                | 横向制表符 |
  | \r                | 回车       |
  | \f                | 换页       |

python执行linux命令
================================

code::

  import subprocess
  import os

  def subprocess_():
      """
      subprocess模块执行linux命令
      :return:
      """
      subprocess.call("ls") # 执行ls命令

  def system_():
      """
      system模块执行linux命令
      :return:
      """
      # 使用system模块执行linux命令时，如果执行的命令没有返回值res的值是256
      # 如果执行的命令有返回值且成功执行，返回值是0
      res = os.system("ls")

  def popen_():
      """
      popen模块执行linux命令。返回值是类文件对象，获取结果要采用read()或者readlines()
      :return:
      """
      val = os.popen('ls').read() # 执行结果包含在val中

  def main():
      subprocess_() # 方法1
      system_() # 方法2
      popen_() # 方法3


if __name__ == '__main__':
    main()

赋值
================================

快速赋值::

  a=b=c=[]

  # 因为[]是可变的, a b c 共享内存

设计模式
================================

`<https://refactoringguru.cn/design-patterns/catalog>`_

关于多线程队列实现
================================

:doc:`/docs/后端/python/python标准库/threading`
  队列是基于双向队列 dedque 实现
:doc:`/docs/后端/python/python标准库/multiprocessing`
  队列是基于 管道 pipe 实现

  有最大限制，win10是1408，linux是6570

关于可重入锁
================================

为什么要有可重入锁？

当存在继承或者递归调用的时候，可能会出现重复加锁的情况，

如果不能重复加锁，就会自己把自己给锁死

\*args, \*\*kwargs
================================

单个 * 表示元组列表
** 表示转换为字典	这个时候首层的字典的键必须为字符串

python三种基础序列类型
================================

- list		可变序列，存放同类项目的集合
- tuple		不可变序列，存放固定长度的不同种类的对象集合
- range		不可变的数字序列，通常在for循环中循环指定的次数

一些优化建议
================================

- 创建列表时，建议有初始值就写初始值，不要创建空列表再填充。因为创建空列表一定会扩容
- 列表的合并，使用 extend或者 += 较好于直接 +

pyhton的选项
================================

执行时不生成pyc文件::

  python -B

获取对象/文件大小
================================

对象
  使用 ``sys.getsizeof()``
  获取程序中声明的一个整数，存储在变量中的大小

  相似场景：文件复制案例中需要获取文件大小，尝试使用 sys.getsizeof()方法
  确认：sys.getsizeof()方法用于获取变量中存储数据的大小

  详细可参考: :doc:`/docs/后端/python/python标准库/sys`
文件
  使用::

    os.path.getsize(path)

  获取指定路径 path 下的文件的大小，以字节为单位
  参考: :doc:`/docs/后端/python/python标准库/os`

