====================================
Python的编码
====================================


.. post:: 2024-02-21 21:55:17
  :tags: python, 概念相关
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


字符编码
====================================

- 为了处理英文字符，产生了ASCII码。
- 为了处理中文字符，产生了GB2312。
- 为了处理各国字符，产生了Unicode。
- 为了提高Unicode存储和传输性能，产生了UTF-8，它是Unicode的一种实现形式。

encode和decode
====================================

讲解编码和解码之前，先来讲讲Unicode和utf-8的关系，
推荐 `<http://flyer103.diandian.com/post/2014-03-09/40061199665>`_

可以这样来理解:
字符串是由字符构成，字符在计算机硬件中通过二进制形式存储，
这种二进制形式就是编码。
如果直接使用::

  字符串↔️字符↔️二进制表示（编码）

会增加不同类型编码之间转换的复杂性。所以引入了一个抽象层::

  字符串↔️字符↔️与存储无关的表示↔️二进制表示（编码）

这样，可以用一种与存储无关的形式表示字符，
不同的编码之间转换时可以先转换到这个抽象层，然后再转换为其他编码形式。
在这里，unicode 就是 “与存储无关的表示”，utf—8 就是 “二进制表示”。

python2中字符串有两种表示形式，str和unicode。
str可以理解为上面这段话中的二进制编码格式，unicode可以理解为抽象层。
encode是编码，即从unicode格式到二进制的编码格式如utf-8、gb2312等。decode是解码，
即从二进制编码格式到unicode编码格式。

原文: `<https://www.cnblogs.com/jinhaolin/p/5128973.html>`_

Python的字符编码
====================================

- Python2中默认的字符编码是ASCII码。
- Python2中字符串有str和unicode两种类型。str有各种编码的区别，unicode是没有编码的标准形式。
- Python2中可以直接查看到unicode的字节串。
- python3默认使用unicode编码，unicode字节串将被直接处理为中文显示出来。

decode()与encode()方法
====================================

- decode()方法将其他编码字符转化为Unicode编码字符。
- encode()方法将Unicode编码字符转化为其他编码字符。

python3一个新特性就是对文本和二进制做了更清晰的划分，文本是str，二进制是byte(\x01\x06...)

编码::

  encode：str --> byte

解码::

  decode：byte --> str

实际遇到的问题
====================================

win10下python2.7读取一个txt文本出现了乱码

最终解决方案有两个：

方案一: 使用decode方法::

  #text.txt是读取的文件内容，编码ANSI，实际应该是gb2312吧
  with open("text.txt","r") as f:
      lines = f.readlines()			#将内容转换为数组
      for line in lines:
          print line.decode('gb2312')	#直接print line会报错，参数为原本的编码

decode函数的参数是本身的编码，表示以此编码解析为unicode

方案二: 导入codecs模块::

  #text.txt是读取的文件内容，编码ANSI，实际应该是gb2312吧
  #codesc.open的encoding参数可以指定原文件的编码，读取写入就会自动转换
  with codecs.open("text.txt","r",encoding="gb2312") as f:
      lines = f.readlines()			#将内容转换为数组
      for line in lines:
          print line

其他
====================================

读文件时候asacll一直无法转换成功，使用json.dumps解决::

  >>> a='\xe6\x81\xb6\xe6\x84\x8f\xe8\xbd\xaf\xe4\xbb\xb6'
  >>> bb=json.dumps(a, encoding="UTF-8", ensure_ascii=False)
  >>> print(bb)








