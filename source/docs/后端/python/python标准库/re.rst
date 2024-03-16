=================================
re
=================================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


通过正则表达式对字符串进⾏匹配

r
  在带有 `'r'` 前缀的字符串字面值中，反斜杠不必做任何特殊处理。
  因此 `r"\n"` 表示包含 `'\'` 和 `'n'` 两个字符的字符串，
  而 `"\n"` 则表示只包含一个换行符的字符串。

re.match函数
=================================

.. function:: re.match(pattern, string, flags=0)

  .. data:: pattern

    匹配的正则表达式

  .. data:: string

    要匹配的字符串

  .. data:: flags

    标志位，用于控制正则表达式的匹配方式，
    如：是否区分大小写，多行匹配等等。

    re.I 忽略大小写

    re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境

    re.M 多行模式

    re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）

    re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库

    re.X 为了增加可读性，忽略空格和 # 后面的注释


re.compile 函数
=================================

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用::

  prog = re.compile(pattern)
  result = prog.match(string)

等价于::

  result = re.match(pattern, string)

不过对于匹配使用的较多情况下, 可以使用全局的compile来节省时间.


举例::

  >>>import re
  >>> pattern = re.compile(r'\d+')
  m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
  >>> print m                                         # 返回一个 Match 对象
  <_sre.SRE_Match object at 0x10a42aac0>
  >>> m.group(0)   # 可省略 0
  '12'
  >>> m.start(0)   # 可省略 0
  3
  >>> m.end(0)     # 可省略 0
  5
  >>> m.span(0)    # 可省略 0
  (3, 5)

在上面，当匹配成功时返回一个 Match 对象，其中：

- group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
- start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
- end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
- span([group]) 方法返回 (start(group), end(group))

re.search函数
=================================

re.search 扫描整个字符串并返回第一个成功的匹配，如果没有匹配，就返回一个 None。

re.match与re.search的区别:

- re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
- re.search匹配整个字符串，直到找到一个匹配

举例::

  import re
  ret = re.search(r"\d+", "阅读次数为9999")
  print(ret.group())
  #结果：9999

re.findall函数
=================================

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 findall 匹配所有。

举例::

  import re
  ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
  print(ret)
  #结果：['9999', '7890', '12345']

举例2::

  import re
  alist = ['a','b','c']
  if re.findall('.$','dfghc')[0] in alist:
    print 'yes1'
  if re.findall('.$','dfgh')[0] in alist:
    print 'yes2'
  print 'over'
  #输出：
  #yes1
  #over

  #re.findall('.$','dfghc')其实是返回一个列表
  #但是匹配是找出结尾的字符所以只有一个，使用[0]获取
  #然后判断是否存在于alist

re.finditer函数
=================================

和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回::

  import re
  it = re.finditer(r"\d+", "12a32bc43jf3")
  for match in it:
    print(match.group())

  #结果：
  #12
  #32
  #43
  #3

re.sub函数
=================================

sub是substitute的所写，表示替换，将匹配到的数据进⾏替换。

.. function:: re.sub(pattern, repl, string, count=0, flags=0)

  pattern

    必选，表示正则中的模式字符串

  repl

    必选，就是replacement，要替换的字符串，也可为一个函数

  string

    必选，被替换的那个string字符串

  count

    可选参数，count 是要替换的最大次数，必须是非负整数。如果省略这个参数或设为 0，所有的匹配都会被替换

  flag

    可选参数，标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

举例：将匹配到的阅读次数加1

方法一::

  import re
  ret = re.sub(r"\d+", '998', "python = 997")
  print(ret)

结果：python = 998

方法二::

  import re
  def add(temp):
    #int（）参数必须是字符串，类似字节的对象或数字，而不是“re.Match”
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)
  ret = re.sub(r"\d+", add, "python = 997")
  print(ret)
  ret = re.sub(r"\d+", add, "python = 99")
  print(ret)

  #这里不懂是怎么把后面的参数传递过去的，
  #好像python就是这样传递参数的？但是有尝试将temp打印，出来是一个地址好像，并不是预期的字符串
  #理解是正常情况下传递的应该是整个字符串，但是这里使用了正则表达式匹配数字，所以只传递了数字，然后使用group函数来获取
  #根据这个思路尝试了一下
  #将匹配规则更改为"r".+",输出temp.group的值正常，temp为地址，re会将参数传递更改为地址传递

结果::

  python = 998
  python = 100

re.subn函数
=================================

行为与sub()相同，但是返回一个元组 (字符串, 替换次数)::

  re.subn(pattern, repl, string[, count])

返回::

  (sub(repl, string[, count]), 替换次数)

例如::

  import re
  pattern = re.compile(r'(\w+) (\w+)')
  s = 'i say, hello world!'
  print(re.subn(pattern, r'\2 \1', s))
  def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
  print(re.subn(pattern, func, s))
  ### output ###
  # ('say i, world hello!', 2)
  # ('I Say, Hello World!', 2)

re.split函数
=================================

根据匹配进⾏切割字符串，并返回⼀个列表。

.. function:: re.split(pattern, string, maxsplit=0, flags=0)

  pattern

    匹配的正则表达式

  string

    要匹配的字符串

  maxsplit

    分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数

举例::

  import re
  ret = re.split(r":| ","info:xiaoZhang 33 shandong")
  print(ret)

结果：['info', 'xiaoZhang', '33', 'shandong']

python贪婪和⾮贪婪
=================================

Python⾥数量词默认是贪婪的（在少数语⾔⾥也可能是默认⾮贪婪），总是尝试匹配尽可能多的字符；⾮贪婪则相反，总是尝试匹配尽可能少的字符。

例如：正则表达式”ab*”如果用于查找”abbbc”，将找到”abbb”。而如果使用非贪婪的数量词”ab*?”，将找到”a”。

注：我们一般使用非贪婪模式来提取。

在"*","?","+","{m,n}"后⾯加上？，使贪婪变成⾮贪婪。

举例1::

  import re

  s="This is a number 234-235-22-423"

  #正则表达式模式中使⽤到通配字，那它在从左到右的顺序求值时，会尽量“抓取”满⾜匹配最⻓字符串，在我们上⾯的例⼦⾥⾯，“.+”会从字符串的启始处抓取满⾜模式的最⻓字符，其中包括我们想得到的第⼀个整型字段的中的⼤部分，“\d+”只需⼀位字符就可以匹配，所以它匹配了数字“4”，⽽“.+”则匹配了从字符串起始到这个第⼀位数字4之前的所有字符

  r=re.match(".+(\d+-\d+-\d+-\d+)",s)
  print(r.group(1))

  #⾮贪婪操作符“？”，这个操作符可以⽤在"*","+","?"的后⾯，要求正则匹配的越少越好
  r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
  print(r.group(1))

结果::

  4-235-22-423
  234-235-22-423

举例2::

  >>> re.match(r"aa(\d+)","aa2343ddd").group(1)
  '2343'
  >>> re.match(r"aa(\d+?)","aa2343ddd").group(1)
  '2'
  >>> re.match(r"aa(\d+)ddd","aa2343ddd").group(1)
  '2343'
  >>> re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
  '2343'

举例3：提取图片地址::

  import re
  test_str="<img data-original=https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973.jpg>"
  ret = re.search(r"https://.*?.jpg", test_str)
  print(ret.group())

r的作⽤
=================================

r：在带有 `'r'` 前缀的字符串字面值中，反斜杠不必做任何特殊处理。 因此 `r"\n"` 表示包含 `'\'` 和 `'n'` 两个字符的字符串，而 `"\n"` 则表示只包含一个换行符的字符串。

与大多数编程语言相同，正则表达式里使用”\”作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符”\”，那么使用编程语言表示的正则表达式里将需要4个反斜杠”\\\\”：前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。Python里的原生字符串很好地解决了这个问题，Python中字符串前⾯加上 r 表示原⽣字符串。

（前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。）

例::

  import re
  mm = "c:\\a\\b\\c"
  print(mm)#c:\a\b\c
  ret = re.match("c:\\\\",mm).group()
  print(ret)#c:\
  ret = re.match("c:\\\\a",mm).group()
  print(ret)#c:\a
  ret = re.match(r"c:\\a",mm).group()
  print(ret)#c:\a
  ret = re.match(r"c:\a",mm).group()
  print(ret)#AttributeError: 'NoneType' object has no attribute 'group'


正则匹配规则(基本适用所有语言)
=================================

匹配单个字符

.. table::

  =====  =================================          ====================
   字符   功能                                        位置
  =====  =================================          ====================
   .     匹配任意1个字符（除了\n）
   [ ]   匹配[ ]中列举的字符
   \d    匹配数字，即0-9                              可以写在字符集[...]中
   \D    匹配⾮数字，即不是数字                       可以写在字符集[...]中
   \s    匹配空⽩，即空格，tab键                      可以写在字符集[...]中
   \S    匹配⾮空⽩字符                               可以写在字符集[...]中
   \w    匹配单词字符，即a-z、A-Z、0-9、_             可以写在字符集[...]中
   \W    匹配⾮单词字符                               可以写在字符集[...]中
  =====  =================================          ====================

使用括号匹配的内容, 可以用 ``\1`` , ``\2`` 表示, 如::

  In [17]: re.sub(r'([a-z]+)([A-Z)]+)', r'\1_\2', 'distributeType').lower()
  Out[17]: 'distribute_type'

  # 这里不懂为什么加不加 + 一样
  # todo: +
  In [18]: re.sub(r'([a-z])([A-Z)])', r'\1_\2', 'distributeType').lower()
  Out[18]: 'distribute_type'

- ``\s``：表示匹配空白字符，包括空格、制表符、换行符等。它与[\r\n\t\f\v ]等效。
- ``\b``：表示匹配单词边界。一个单词被定义为由字母或数字组成的字符序列。\b匹配位于单词开头或结尾的位置，而不匹配任何实际字符。

