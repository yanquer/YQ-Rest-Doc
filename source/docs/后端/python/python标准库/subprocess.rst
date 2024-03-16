=====================
subprocess
=====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


call
=====================

.. function:: subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

  父进程直接创建子进程执行程序(执行命令), 然后等待子进程完成

  返回值:
    返回子进程的 **退出状态** 即 child.returncode 属性 (返回状态码, 命令正常执行返回0, 报错则返回1))

  .. code-block::

    ret1=subprocess.call("ifconfig")
    ret2=subprocess.call("ipconfig")    # python3.5不是这样, 依然会抛出异常导致无法对ret2赋值
    print(ret1)     # 0
    print(ret2)     # 1

    ret = subprocess.call(["ls", "-l"], shell=False)    # shell为False的时候命令必须分开写
    ret = subprocess.call("ls -l", shell=True)

check_call
=====================

.. function:: subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

  父进程直接创建子进程执行程序, 然后等待子进程完成, 具体可以使用的参数, 参考上文 Popen 类的介绍。

  返回值:
    无论子进程是否成功, 该函数都返回 0.
    但是如果子进程的退出状态不是0, check_call() 抛出异常 CalledProcessError,
    异常对象中包含了 child.returncode 对应的返回码。

例, check_call()正常执行命令::

  >>> import subprocess
  >>> p = subprocess.check_call(['ping', '-c', '2', 'www.baidu.com'])
  PING www.baidu.com (39.156.66.14): 56 data bytes
  64 bytes from 39.156.66.14: icmp_seq=0 ttl=52 time=40.865 ms
  64 bytes from 39.156.66.14: icmp_seq=1 ttl=52 time=48.753 ms

  --- www.baidu.com ping statistics ---
  2 packets transmitted, 2 packets received, 0.0% packet loss
  round-trip min/avg/max/stddev = 40.865/44.809/48.753/3.944 ms
  >>> p
  0

例, check_call()错误执行命令::

  >>> p = subprocess.check_call(['ping', '-c', '2', 'www.xxxxxdu.com'])
  ping: cannot resolve www.xxxxxdu.com: Unknown host
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/usr/local/Cellar/python@3.9/3.9.10/Frameworks/Python.framework/Versions/3.9/lib/python3.9/subprocess.py", line 373, in check_call
      raise CalledProcessError(retcode, cmd)
  subprocess.CalledProcessError: Command '['ping', '-c', '2', 'www.xxxxxdu.com']' returned non-zero exit status 68.
  >>> p
  0

check_output
=====================

.. function:: subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

  执行命令, 如果执行成功则返回执行结果(以 **字符串** 的形式返回子进程的输出), 否则抛异常::

    subprocess.check_output(["echo", "Hello World!"])
    subprocess.check_output("exit 1", shell=True)

  返回值:
    字符串形式的子进程的输出结果,
    但是如果子进程的 **退出状态** 不是0, 那么抛出异常 CalledProcessError, 异常对象中包含了 child.returncode 对应的返回码。

  注意: check_output() 的函数签名中没有参数 ``stdout`` , 调用该方法时, 子进程的输出默认就返回给父进程。

例, check_output() 调用的子进程正常与错误退出::

  >>> subprocess.check_output(["echo", "Hello World!"])
  b'Hello World!\n'

  >>> subprocess.check_output("exit 1", shell=True)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/usr/local/Cellar/python@3.9/3.9.10/Frameworks/Python.framework/Versions/3.9/lib/python3.9/subprocess.py", line 424, in check_output
      return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
    File "/usr/local/Cellar/python@3.9/3.9.10/Frameworks/Python.framework/Versions/3.9/lib/python3.9/subprocess.py", line 528, in run
      raise CalledProcessError(retcode, process.args,
  subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1.
  >>>

.. note::

  使用上面提到的三个方法: ``call(), check_call(), check_output()`` 时,
  尽量不要将参数 ``stderr`` 和 ``stdout`` 设置为 ``subprocess.PIPE`` ,
  这几个函数默认都会等待子进程完成, 子进程产生大量的输出数据如果造成管道堵塞, 父进程再等待子进程完成可能造成死锁。

Popen
=====================

.. function:: subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)

  执行复杂的系统命令. **创建并返回一个子进程** , 并在这个进程中执行指定的程序。

  实例化 Popen 可以通过许多参数详细定制子进程的环境, 但是只有一个参数是必须的, 即位置参数 **args**

  args
    shell命令, 可以是字符串或者序列类型（如：list, 元组）

    要执行的命令或可执行文件的路径。

    一个由字符串组成的序列（通常是列表）,
    列表的第一个元素是可执行程序的路径,
    剩下的是传给这个程序的参数.

    如果没有要传给这个程序的参数, args 参数可以仅仅是一个字符串。
  bufsize: int = 0
    指定缓冲

    控制 ``stdin`` , ``stdout`` , ``stderr`` 等参数指定的文件的缓冲, 和打开文件的 内建函数 ``open()`` 中的参数 ``bufsize`` 含义相同。

    0 无缓冲,1 行缓冲,其他正数表示近似的缓冲区字节数, 负值表示使用系统默认值. 默认是0.
  executable=None
    如果这个参数不是 None, 将替代参数 args 作为可执行程序
  stdin=None
    表示指定子程序的标准输入
  stdout=None
    表示指定子程序的标准输出
  stderr=None
    表示指定子程序的标准错误

    对于 ``stdin, stdout`` 和 ``stderr`` 而言, 如果他们是 None（默认情况）, 那么子进程使用和父进程相同的标准流文件。

    父进程如果想要和子进程通过 communicate() 方法通信, 对应的参数必须是 subprocess.PIPE

    当然 ``stdin, stdout`` 和 ``stderr`` 也可以是已经打开的 file 对象, 前提是以合理的方式打开, 比如 ``stdin`` 对应的文件必须要可读等。
  preexec_fn=None
    只在Unix平台下有效, 用于指定一个可执行对象（callable object）, 它将在子进程运行之前被调用

    默认是None, 否则必须是一个函数或者可调用对象, 在子进程中首先执行这个函数, 然后再去执行为子进程指定的程序或Shell。
  close_sfs: bool = False
    在windows平台下, 如果close_fds被设置为True,
    则新创建的子进程将不会继承父进程的输入、输出、错误管道.
    所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。

    布尔型变量, 为 True 时, 在子进程执行前强制关闭所有除 stdin, stdout和stderr外的文件
  shell: bool = False
    布尔型变量, 明确要求使用shell运行程序, 与参数 executable 一同指定子进程运行在什么 Shell 中

    如果executable=None 而 shell=True, 则使用 /bin/sh 来执行 args 指定的程序
    也就是说, Python首先起一个shell, 再用这个shell来解释指定运行的命令.
    注意这个时候有个特殊情况,
    如果参数args是字符串, 那么一般不会有啥问题,
    如果参数是列表, 那么列表会当错/bin/sh的参数传递, 有可能导致无法正常识别指令.
    比如::

      subprocess.Popen(['tar', '-zxf', 'xxx.tar.gz'], shell=True)

    实际触发的是::

      /bin/sh -c tar -zxf xxx.tar.gz

    会报错tar没有给选项(因为被当错了sh的参数), 所以这时候还是老老实实的shell=False吧.

    注意 windows 下, 普通权限执行文件不需要设置此选项, 但是, 当执行文件需要申请权限时, 必须设置为 true, 才可以触发权限申请的框.
  cwd=None
    用于设置子进程的当前目录

    代表路径的字符串, 指定子进程运行的工作目录, 要求这个目录必须存在；
  env: dict = None
    用于指定子进程的环境变量。如果env = None, 子进程的环境变量将从父进程中继承。
  universal_newlines: bool = False
    不同系统的换行符不同, True 表示 ``stdout`` 和 ``stderr``  使用 ``\n`` 通用换行（universal newline）模式
  startupinfo=None
    只在windows下有效, 将被传递给底层的 ``CreateProcess()`` 函数, 用于设置子进程的一些属性, 如：主窗口的外观, 进程的优先级等等
  createionflags: int = 0
    同上

  同 Linux 中创建子进程类似, 父进程创建完子进程后, 并不会自动等待子进程执行,
  父进程在子进程之前推出将导致子进程成为孤儿进程, 孤儿进程统一由 init 进程接管, 负责其终止后的回收工作。

  如果父进程在子进程之后终止, 但子进程终止时父进程没有进行最后的回收工作,
  子进程残留的数据结构称为僵尸进程。大量僵尸进程将耗费系统资源,
  因此父进程及时等待和回收子进程是必要的, 除非能够确认自己比子进程先终止, 从而将回收工作过渡给 init 进程。

  这个等待和回收子进程的操作就是wait()函数

.. sidebar:: 关于 `shell: bool = False` 参数

  有需求在linux下使用pkexec来申请权限, 如执行ls
  可以成功执行的两种调用:

    subprocess.Popen('pkexec ls', shell=True)
    subprocess.Popen(['sh', '-c', 'pkexec ls'], shell=False)

  不能生效的调用(弹出界面一闪而逝或者压根不显示)::

    subprocess.Popen(['pkexec', 'ls'], shell=False)

  后面发现这个貌似实际是::

    pkexec ls &

  与这个的区别::

    sh -c "pkexec ls"

.. note::

  对于的系统命令而言, 当存在关键词参数且参数的值有空格时, 不要使用::

    Popen(['cmd', '--update=t t t'])

  而是使用::

    Popen(['cmd', '--update', 't t t'])

  因为前者会把 ``'--update=t t t'`` 解析为带引号的字符串::

    "--update=t t t"

  从而导致识别不了关键字参数 ``--update``

例1::

  import subprocess
  ret1 = subprocess.Popen(["mkdir","t1"])
  ret2 = subprocess.Popen("mkdir t2", shell=True)

.. note::

  终端输入的命令分为两种：

  - 非交互式: 输入即可得到输出, 如 ifconfig
  - 交互式: 输入进行某环境, 依赖再输入, 如 python

例2::

  import subprocess

  obj = subprocess.Popen("mkdir t3", shell=True, cwd='/home/dev',)     #在cwd目录下执行命令
  import subprocess

  obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  obj.stdin.write("print(1)\n")
  obj.stdin.write("print(2)")
  obj.stdin.close()

  cmd_out = obj.stdout.read()
  obj.stdout.close()
  cmd_error = obj.stderr.read()
  obj.stderr.close()

  print(cmd_out)
  print(cmd_error)
  import subprocess

  obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  obj.stdin.write("print(1)\n")
  obj.stdin.write("print(2)")

  out_error_list = obj.communicate()
  print(out_error_list)
  import subprocess

  obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  out_error_list = obj.communicate('print("hello")')
  print(out_error_list)

例3:

创建一个子进程, 然后执行一个简单的命令::

  >>> import subprocess
  >>> p = subprocess.Popen('ls -l', shell=True)
  >>> total 164
  -rw-r--r--  1 root root   133 Jul  4 16:25 admin-openrc.sh
  -rw-r--r--  1 root root   268 Jul 10 15:55 admin-openrc-v3.sh
  ...
  >>> p.returncode
  >>> p.wait()
  0
  >>> p.returncode
  0

这里也可以使用 ``p = subprocess.Popen(['ls', '-cl'])`` 来创建子进程。

属性
---------------------

Popen创建的子进程有一些有用的属性, 假设 p 是 Popen 创建的子进程, p 的属性包括：

- p.pid : 子进程的PID。
- p.returncode : 该属性表示子进程的返回状态.
  returncode可能有多重情况::

    None  —— 子进程尚未结束；
    ==0   —— 子进程正常退出；
    > 0   —— 子进程异常退出, returncode 对应于出错码；
    < 0   —— 子进程被信号杀掉了。

- p.stdin, p.stdout, p.stderr : 子进程对应的一些初始文件,
  如果调用Popen()的时候对应的参数是subprocess.PIPE, 则这里对应的属性是一个包裹了这个管道的 file 对象,

方法
---------------------

.. function:: p.poll()

  检查子进程  p 是否已经终止, 返回 p.returncode 属性 (参考下文 Popen 对象的属性)；

.. function:: p.wait()

  等待子进程 p 终止, 返回 p.returncode 属性；

  注意: wait() 立即阻塞父进程, 直到子进程结束！

.. function:: p.communicate(input=None)

  和子进程 p 交流, 将参数 ``input`` （字符串）中的数据发送到子进程的 stdin, 同时从子进程的 stdout 和 stderr 读取数据, 直到EOF。

  返回值:
    二元组 (stdoutdata, stderrdata)

  分别表示从标准出和标准错误中读出的数据。

  父进程调用 p.communicate() 和子进程通信有以下限制:

  - 只能通过管道和子进程通信, 也就是说, 只有调用 Popen() 创建子进程的时候参数 stdin=subprocess.PIPE,
    才能通过 p.communicate(input) 向子进程的 stdin 发送数据；只有参数 stout 和 stderr 也都为 subprocess.PIPE , 才能通过p.communicate() 从子进程接收数据, 否则接收到的二元组中, 对应的位置是None。
  - 父进程从子进程读到的数据缓存在内存中, 因此commucate()不适合与子进程交换过大的数据。

  注意: communicate() 立即阻塞父进程, 直到子进程结束！

.. function:: p.send_signal(signal)

  向子进程发送信号 ``signal``

.. function:: p.terminate()

  终止子进程 p , 等于向子进程发送 SIGTERM 信号；

.. function:: p.kill()

  杀死子进程 p , 等于向子进程发送 SIGKILL 信号；


subprocess模块的其他属性
==========================================

- subprocess.PIPE : 调用本模块提供的若干函数时, 可作为 ``std`` 参数的值, 为标准流文件打开一个管道.
  例: 使用管道连接标准流文件::

    import subprocess
    child1  = subprocess.Popen([ 'ls' ,  '-l' ], stdout = subprocess.PIPE)
    child2  = subprocess.Popen([ 'wc' ,  '-l' ], stdin = child1.stdout, stdout = subprocess.PIPE)
    out  = child2.communicate()
    child1.wait()
    child2.wait()
    print (out)

  这里将子进程 child1 的标准输出作为子进程 child2 的标准输入, 父进程通过 communicate() 读取 child2 的标准输出后打印。

- subprocess.STDOUT : 调用本模块提供的若干函数时, 可作为 stderr 参数的值, 将子进程的标准错误输出打印到标准输出。

subprocess模块定义的异常
==========================================

.. function:: subprocess.CalledProcessError

  什么时候可能抛出该异常: 调用 check_call() 或 check_output() , 子进程的退出状态不为 0 时。

  该异常包含以下信息:

  - returncode: 子进程的退出状态；
  - cmd: 创建子进程时指定的命令；
  - output: 如果是调用 check_output() 时抛出的该异常, 这里包含子进程的输出, 否则该属性为None。

总结
==========================================

使用 Popen 可以在Python进程中创建子进程

- 如果只对子进程的执行退出状态感兴趣, 可以调用 subprocess.call() 函数
- 如果想通过异常处理机制解决子进程异常退出的情形,
  可以考虑使用 subprocess.check_call() 和 subprocess.check_output。
- 如果希望获得子进程的输出, 可以调用 subprocess.check_output(), 但 Popen() 无疑是功能最强大的。

subprocess模块的缺陷在于默认提供的父子进程间通信手段有限, 只有管道；同时创建的子进程专门用来执行外部的程序或命令。

Linux下进程间通信的手段很多, 子进程也完全可能从创建之后继续调用

:参考::
  `python - subprocess.Popen()多进程 <https://blog.csdn.net/liuyingying0418/article/details/100939697>`_
  `subprocess: 可以在当前程序中执行其他程序或命令 <http://www.cnblogs.com/Security-Darren/p/4733368.html>`_

