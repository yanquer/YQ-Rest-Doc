====================
os
====================

官网: `os --- 多种操作系统接口 <https://docs.python.org/zh-cn/3/library/os.html>`_

属性
====================

os.environ

  一个 mapping 对象，其中键值是代表进程环境的字符串。
  例如，environ['HOME'] 是你的主目录（在某些平台上）的路径名，相当于 C 中的 getenv("HOME")。

函数
====================


.. function:: os.ctermid()

  返回与进程控制终端对应的文件名。

.. function:: os.get_terminal_size(fd=STDOUT_FILENO, /)

  返回终端窗口的尺寸，格式为 (columns, lines)，它是类型为 terminal_size 的元组。

  可选参数 fd （默认为 STDOUT_FILENO 或标准输出）指定应查询的文件描述符。

  如果文件描述符未连接到终端，则抛出 OSError 异常。

  shutil.get_terminal_size() 是供常规使用的高阶函数，os.get_terminal_size 是其底层的实现。

  可用性: Unix, Windows。

.. function:: os.walk(top, topdown=True, onerror=None, followlinks=False)

  生成目录树中的文件名，方式是按上->下或下->上顺序浏览目录树。
  对于以 top 为根的目录树中的每个目录（包括 top 本身），
  它都会生成一个三元组 (dirpath, dirnames, filenames)。

.. function:: os.path.getsize(path)

  获取指定路径 path 下的文件的大小，以字节为单位
  计算机中的单位换算::

    字节→1024-K→1024-M→1024-G→1024-T…

.. function:: os.popen(command[, mode[, bufsize]])

  用于从一个命令打开一个管道。
  在Unix，Windows中有效

  参数
    command
      使用的命令。
    mode
      模式权限可以是 ‘r’(默认) 或 ‘w’。
    bufsize
      指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；
      其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。
      负的bufsize意味着使用系统的默认值，
      一般来说，对于tty设备，它是行缓冲；
      对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。

  返回值
    返回一个文件描述符号为fd的打开的文件对象

  这种调用方式是通过管道的方式来实现，函数返回一个file对象，
  里面的内容是脚本输出的内容（可简单理解为echo输出的内容），使用os.popen调用test.sh的情况::

    >> import os
    >>> os.popen("./test.sh")
    <open file './test.sh', mode 'r' at 0x7f6cbbbee4b0>
    >>> f=os.popen("./test.sh")
    >>> f
    <open file './test.sh', mode 'r' at 0x7f6cbbbee540>
    >>> f.readlines()
    ['hello python!\n', 'hello world!\n']
    >>>

  .. note::

    os.popen不会等cmd命令执行完毕就继续下面的代码(非阻塞),
    可以调用 readlines() 强行读阻塞.

    python调用Shell脚本，有两种方法：os.system()和os.popen(),
    前者返回值是脚本的退出状态码，后者的返回值是脚本执行过程中的输出内容

.. function:: os.system(command)

  该方法在调用完shell脚本后，返回一个16位的二进制数，
  低位为杀死所调用脚本的信号号码，高位为脚本的退出状态码，
  即脚本中“exit 1”的代码执行后，os.system函数返回值的高位数则是1，
  如果低位数是0的情况下，则函数的返回值是0x0100,换算为十进制得到256。

  要获得os.system的正确返回值，可以使用位移运算（将返回值右移8位）还原返回值::

    >>> import os
    >>> os.system("./test.sh")
    hello python!
    hello world!
    256
    >>> n=os.system("./test.sh")
    hello python!
    hello world!
    >>> n
    256
    >>> n>>8
    1
    >>>






