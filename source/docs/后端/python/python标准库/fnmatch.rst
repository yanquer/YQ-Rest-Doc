===============
fnmatch模块
===============


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


介于普通字符串与 :doc:`/docs/后端/python/python标准库/re` 之间的字符串操作模块

fnmatch 模块提供了两个函数——fnmatch() 和 fnmatchcase() ，可以用来实现 这样的匹配。用法如下::

  if any(name.endswith(('.c', '.h')) for name in listdir(dirname)): ...
  >>> from fnmatch import fnmatch, fnmatchcase
  >>> fnmatch('foo.txt', '*.txt')
  True
  >>> fnmatch('foo.txt', '?oo.txt')
  True
  >>> fnmatch('Dat45.csv', 'Dat[0-9]*')
  True
  >>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
  >>> [name for name in names if fnmatch(name, 'Dat*.csv')] ['Dat1.csv', 'Dat2.csv']
  >>>

fnmatch() 函数使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来 匹配模式。比如::

  >>> # On OS X (Mac)
  >>> fnmatch('foo.txt', '*.TXT') False
  >>> # On Windows
  >>> fnmatch('foo.txt', '*.TXT') True
  >>>

可以使用 fnmatchcase() 来代替。它完全使用你的模 式大小写匹配。比如::

  >>> fnmatchcase('foo.txt', '*.TXT') False
  >>>

fnmatch
===============

使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来 匹配模式::

  >>> # On OS X (Mac)
  >>> fnmatch('foo.txt', '*.TXT') False
  >>> # On Windows
  >>> fnmatch('foo.txt', '*.TXT') True
  >>>

fnmatchcase
===============


