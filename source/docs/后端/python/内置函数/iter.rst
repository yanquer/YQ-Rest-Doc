===================
iter
===================

创建一个迭代器

iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记 (结 尾) 值作为输入参数。
当以这种方式使用的时候，它会创建一个迭代器，这个迭代器会 不断调用 callable 对象直到返回值和标记值相等为止。

例::

  >>> import sys
  >>> f = open('/etc/passwd')
  >>> for chunk in iter(lambda: f.read(10), ''):
  ...   n = sys.stdout.write(chunk)
  ...
  nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false root:*:0:0:System Administrator:/var/root:/bin/sh
  daemon:*:1:1:System Services:/var/root:/usr/bin/false
  _uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico ...
  >>>

