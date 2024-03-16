=========================
awk
=========================


.. post:: 2023-02-27 21:24:23
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


文本和数据进行处理的编程语言

选项参数:

-F<fs>
  fs指定分割符
-v<var=value>
  赋值一个用户变量，将外部变量传递给awk
-f<script>
  从脚本文件中读取awk命令
-m<[fr] val>
  对val值设置内在限制，-mf选项限制分配给val的最大块数目；-mr选项限制记录的最大数目。这两个功能时Bell实验室awk拓展的功能，在标准awk不适用。

其他::

  $n 	当前记录的第n个字段，$开头都表示字段

**模式**

- /正则表达式/：使用通配符的拓展集
- 关系表达式：使用运算符进行操作，可以是字符串或数字的比较测试
- 模式匹配表达式：用运算符 ~ （匹配）和 !~ （不匹配）
- BEGIB语句块、pattern语句块、END语句块：参见awk的工作原理

.. note::

  语句块的书写, 最外层一定是单引号包裹, 如::

    $ echo "mysql                    <none>             57da161f45ac   12 months ago   517MB" | awk '{print $3}'
    57da161f45ac

  因为其内部是脚本内容, 用双引号, 会就地解析, 比如这里就是 ``$3`` 解析成当前的参数

awk内置变量（预定义变量）
=========================

**常用**

NF
  字段个数，（读取的列数） 每一行 $0 拥有的字段总数
NR
  记录数（行号），从1开始，新的文件延续上面的计数，新文件不从1开始. 目前awk所处理的第几行的数据
FNR
  读取文件的记录数（行号），从1开始，新的文件重新从1开始计数
FS(Field Separator)
  输入字段分隔符，默认是空格
OFS(Out of Field Separator)
  输出字段分隔符 默认也是空格
RS(Record Separator)
  输入行分隔符，默认为换行符
ORS(Output Record Separate)
  输出行分隔符，默认为换行符

.. note::

  RS、ORS、FS、OFS的英文解释绝不是这样的，这里只是解释清楚。建议去阅读awk的英文读物，其中解释了缩写的含义

  其他参考 关于Field与Record_

**所有**

说明：ANPG表示第一个支持变量的工具，[A]=awk、[N]=nawk、[P]=POSIXawk、[G]=gawk::

  $n  当前记录的第n个字段，比如n为1表示第一个字段，n为2表示第二个字段。
  $0  这个变量包含执行过程中当前行的文本内容。
  [N]  ARGC  命令行参数的数目。
  [G]  ARGIND  命令行中当前文件的位置（从0开始算）。
  [N]  ARGV  包含命令行参数的数组。
  [G]  CONVFMT  数字转换格式（默认值为%.6g）。
  [P]  ENVIRON  环境变量关联数组。
  [N]  ERRNO  最后一个系统错误的描述。
  [G]  FIELDWIDTHS  字段宽度列表（用空格键分隔）。
  [A]  FILENAME  当前输入文件的名。
  [P]  FNR  同NR，但相对于当前文件。
  [A]  FS  字段分隔符（默认是任何空格）。
  [G]  IGNORECASE  如果为真，则进行忽略大小写的匹配。
  [A]  NF  表示字段数，在执行过程中对应于当前的字段数。
  [A]  NR  表示记录数，在执行过程中对应于当前的行号。
  [A]  OFMT  数字的输出格式（默认值是%.6g）。
  [A]  OFS  输出字段分隔符（默认值是一个空格）。
  [A]  ORS  输出记录分隔符（默认值是一个换行符）。
  [A]  RS  记录分隔符（默认是一个换行符）。
  [N]  RSTART  由match函数所匹配的字符串的第一个位置。
  [N]  RLENGTH  由match函数所匹配的字符串的长度。
  [N]  SUBSEP  数组下标分隔符（默认值是34）。


BEGIN末尾的非0数字表示输出

这里非0数字可以理解为true::

  echo -e "111\n222" | awk -v a=3 -v val=god 'BEGIN{FS=OFS=","}{$a=val}1'

  111,,god
  222,,god

awk中$NF是什么意思? ::

  #pwd
  /usr/local/etc
  ~# echo $PWD | awk -F/ '{print $NF}'
  etc
  #NF代表：浏览记录的域的个数
  #$NF代表  ：最后一个Field(列)


:原文链接::
  - `<https://blog.csdn.net/qq_41673534/article/details/80252016>`_
  - `linux：awk之RS、ORS与FS、OFS <https://www.cnblogs.com/fhefh/archive/2011/11/16/2251656.html>`_


**把ORS理解成RS反过程，这样更容易记忆和理解**，看下面的例子::

  [zhangy@localhost test]$ awk 'BEGIN{ORS="\n"}{print $0}' test1  //awk '{print $0}' test1二者是一样的
  111 222
  333 444
  555 666
  [zhangy@localhost test]$ awk 'BEGIN{ORS="|"}{print $0}' test1
  111 222|333 444|555 666|

FS为空的时候::

  [zhangy@localhost test]$ echo "111|222|333"|awk 'BEGIN{FS=""}{NF++;print $0}'
  1 1 1 | 2 2 2 | 3 3 3


**当FS为空的时候，awk会把一行中的每个字符，当成一列来处理**。

关于Field与Record
=========================

什么是field（字段），什么是record（记录行）？

示例::

  1.txt

  1. i am a student.
  2. i like to swim
  3. hello moto

1代表第一个记录行，2代表第二个记录行，3代表第三个记录行。
通过观察我们可以知道总共有3个记录行（record）。

看看第一行：“i am a student”，这一行的每个单词都是一个字段（field）。
“i”是一个字段，“am”是一个字段，“a”是一个字段，“student”是一个字段，
该行总共有4个字段。

RS
=========================

记录行分隔符, 示例::

  1.txt

  1. a\n
  2. b\n
  3. c\n
  4. d\n
  5. e\n

该文本总共有5行，每一行都有一个换行符“\n”。
所以每行记录都是以“\n”为一个（换行的）标志。

可以用以下方法来理解：

找到某某标志，让每个某某后的内容重新变成一行

示例::

  1.txt

  a|b|c

代码::

  awk 'BEGIN{ RS="|"; } { print $0 }'

  a
  b
  b

ORS
=========================

可以看成RS的逆向过程, 示例::

  1.txt

  a
  b
  c

可以这样理解：

观察每一行的“换行符号”，然后将“换行符号”替换成你想要的符号::

  awk 'BEGIN{ ORS="----" }{ print $0 }' 1.txt

  a----b----c----

FS
=========================

字段分隔符

FS默认值为“ （空格）”,如“hello moto”.

在“hello moto”中有一个空格，空格就是hello与moto的分隔符（separator），而hello与moto就为字段（files）。awk以空格来区分。

在看看“i----love----you”,如果我们用命令“awk “{ print $1 }””会看到结果为::

  i----love----you

如果想打印出三个字母，通过观察可发现“----”为分隔符::

  awk 'BEGIN{ FS="----";}{ print $1,$2,$3 }' filename

  i love you

OFS
=========================

输出的字段分隔符。

这么解释吧，如上例中“i----love----you”，“----”为分隔符(FS)，如果我们想改为用其他符号显示可以这样::

  awk 'BEGIN{ FS="----";OFS="*****" }{ print $1,$2,$3 }' filename

  i*****love*****you

其实OFS还有一个例子::

  echo "abc" | awk '{ OFS="." } { NF=NF; print NF,$0}'

结果::

  1.abc

PS
=========================

RS与ORS可以说成是一个互逆的过程（↔）也可以看成一个替换的过程，
但是看成互逆的过程比较好理解；FS与OFS就是一个替换的过程。

RS,ORS,FS,OFS区别和联系
=========================

平常用的::

  print $0

等价于::

  printf $0 ORS

RS与ORS
-------------------------

RS是记录分隔符，默认的分隔符是 ``\n``，具体用法看下::

  [root@krlcgcms01 mytest]# cat test1     //测试文件
  111 222
  333 444
  555 666

RS默认分割符 ``\n``::

  [root@krlcgcms01 mytest]# awk '{print $0}' test1  //awk 'BEGIN{RS="\n"}{print $0}' test1 这二个是一样的
  111 222
  333 444
  555 666

其实你可以把上面test1文件里的内容理解为::

  111 222\n333 444\n555 6666

利用 ``\n`` 进行分割。看下一个例子

**自定义RS分割符**::

  [zhangy@localhost test]$ echo "111 222|333 444|555 666"|awk 'BEGIN{RS="|"}{print $0,RT}'
  111 222 |
  333 444 |
  555 666

结合上面一个例子，就很容易理解RS的用法了

**RS也可能是正则表达式**::

  [zhangy@localhost test]$ echo "111 222a333 444b555 666"|awk 'BEGIN{RS="[a-z]+"}{print $1,RS,RT}'
  111 [a-z]+ a
  333 [a-z]+ b
  555 [a-z]+

从例3和例4，我们可以发现一点， **当RT是利用RS匹配出来的内容。如果RS是某个固定的值时，RT就是RS的内容**。

**RS为空时**::

  [zhangy@localhost test]$ cat -n test2
  1  111 222
  2
  3  333 444
  4  333 444
  5
  6
  7  555 666
  [zhangy@localhost test]$ awk 'BEGIN{RS=""}{print $0}' test2
  111 222
  333 444
  333 444
  555 666
  [zhangy@localhost test]$ awk 'BEGIN{RS="";}{print "<",$0,">"}' test2  //这个例子看着比较明显
  < 111 222 >
  < 333 444     //这一行和下面一行，是一行
  333 444 >
  < 555 666 >

从这个例子， **可以看出当RS为空时，awk会自动以多行来做为分割符**。

**ORS记录输出分符符，默认值是 ``\n``**

**把ORS理解成RS反过程，这样更容易记忆和理解**，看下面的例子::

  [zhangy@localhost test]$ awk 'BEGIN{ORS="\n"}{print $0}' test1  //awk '{print $0}' test1二者是一样的
  111 222
  333 444
  555 666
  [zhangy@localhost test]$ awk 'BEGIN{ORS="|"}{print $0}' test1
  111 222|333 444|555 666|

FS与OFS
-------------------------

**FS指定列分割符**::

  [zhangy@localhost test]$ echo "111|222|333"|awk '{print $1}'
  111|222|333
  [zhangy@localhost test]$ echo "111|222|333"|awk 'BEGIN{FS="|"}{print $1}'
  111

**FS也可以用正则**::

  [zhangy@localhost test]$ echo "111||222|333"|awk 'BEGIN{FS="[|]+"}{print $1}'
  111

**FS为空的时候**::

  [zhangy@localhost test]$ echo "111|222|333"|awk 'BEGIN{FS=""}{NF++;print $0}'
  1 1 1 | 2 2 2 | 3 3 3

**当FS为空的时候，awk会把一行中的每个字符，当成一列来处理**。

**RS被设定成非 ``\n`` 时， ``\n`` 会成FS分割符中的一个** ::

  [zhangy@localhost test]$ cat test1
  111 222
  333 444
  555 666
  [zhangy@localhost test]$ awk 'BEGIN{RS="444";}{print $2,$3}' test1
  222 333
  666

**222和333之间是有一个 ``\n`` 的，当RS设定成444后，222和333被认定成同一行的二列了，其实按常规思想是二行的一列才对**。

**OFS列输出分隔符** ::

  [zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{print $1,$2}' test1
  111|222
  333|444
  555|666
  [zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{print $1 OFS $2}' test1
  111|222
  333|444
  555|666

**test1只有二列，如果100列，都写出来太麻烦了吧。** ::

  [zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{print $0}' test1
  111 222
  333 444
  555 666
  [zhangy@localhost test]$ awk 'BEGIN{OFS="|";}{NF=NF;print $0}' test1
  111|222
  333|444
  555|666

为什么第二种方法中的OFS生效呢？个人觉得， **awk觉查到列有所变化时，就会让OFS生效**，没变化直接输出了。





