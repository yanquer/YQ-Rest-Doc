======================
tempfile
======================

tempfile --- 生成临时文件和目录

官网: https://docs.python.org/zh-cn/3/library/tempfile.html

该模块用于创建临时文件和目录，它可以跨平台使用。

- TemporaryFile、NamedTemporaryFile、TemporaryDirectory 和 SpooledTemporaryFile
  是带有自动清理功能的高级接口，可用作上下文管理器。
- mkstemp() 和 mkdtemp() 是低级函数，使用完毕需手动清理。

.. function:: tempfile.TemporaryFile(mode='w+b', buffering=- 1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

  返回一个 file-like object （文件类对象）作为临时存储区域。
  创建该文件使用了与 mkstemp() 相同的安全规则。
  它将在关闭后立即销毁（包括垃圾回收机制关闭该对象时）。
  在 Unix 下，该文件在目录中的条目根本不创建，或者创建文件后立即就被删除了，其他平台不支持此功能。
  您的代码不应依赖使用此功能创建的临时文件名称，因为它在文件系统中的名称可能是可见的，也可能是不可见的。

  mode = 'w+b'
    创建的文件不用关闭，就可以读取或写入。
    因为用的是二进制模式，所以无论存的是什么数据，它在所有平台上都表现一致。

  在 POSIX 平台上，它返回的对象是真实的文件对象。
  在其他平台上，它是一个文件类对象 (file-like object)，它的 file 属性是底层的真实文件对象。

  如果可用，则使用 os.O_TMPFILE 标志（仅限于 Linux，需要 3.11 及更高版本的内核）。

  在 Posix 或 Cygwin 以外的平台上，TemporaryFile 是 NamedTemporaryFile 的别名。

.. function:: tempfile.NamedTemporaryFile(mode='w+b', buffering=- 1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None)

  与上一个基本一致, 不过多了参数 delete 控制结束时是否删除文件

  可以通过返回对象的name属性获取文件名.

.. function:: class tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None, ignore_cleanup_errors=False)

  创建临时目录, 返回对象的 name 属性中找到临时目录的名称

  这个类会使用与 mkdtemp() 相同的规则安全地创建一个临时目录。
  在完成上下文或销毁临时目录对象时，新创建的临时目录及其所有内容会从文件系统中被移除。

  此目录可通过调用 cleanup() 方法来显式地清理。
  如果 ignore_cleanup_errors 为真值，
  则在显式或隐式清理（例如在 Windows 上 PermissionError 移除打开的文件）期间出现的未处理异常将被忽略，
  并且剩余的可移除条目会被“尽可能”地删除。
  在其他情况下，错误将在任何上下文清理发生时被引发 (cleanup() 调用、退出上下文管理器、对象被作为垃圾回收或解释器关闭等)。

.. function:: tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)

  以最安全的方式创建一个临时文件。
  假设所在平台正确实现了 os.open() 的 os.O_EXCL 标志，则创建文件时不会有竞争的情况。
  该文件只能由创建者读写，如果所在平台用权限位来标记文件是否可执行，那么没有人有执行权。文件描述符不会过继给子进程。

  与 TemporaryFile() 不同，mkstemp() 用户用完临时文件后需要自行将其删除。

  suffix:
    不是 None 则文件名将以该后缀结尾，是 None 则没有后缀。
    mkstemp() 不会在文件名和后缀之间加点，如果需要加一个点号，请将其放在 suffix 的开头。
  prefix:
    不是 None，则文件名将以该前缀开头，是 None 则使用默认前缀。
    默认前缀是 gettempprefix() 或 gettempprefixb() 函数的返回值（自动调用合适的函数）。
  dir:
    不为 None，则在指定的目录创建文件，是 None 则使用默认目录。
    默认目录是从一个列表中选择出来的，这个列表不同平台不一样，但是用户可以设置 TMPDIR、TEMP 或 TMP 环境变量来设置目录的位置。
    因此，不能保证生成的临时文件路径很规范，比如，通过 os.popen() 将路径传递给外部命令时仍需要加引号。

  如果 suffix、prefix 和 dir 中的任何一个不是 None，就要保证它们是同一数据类型。
  如果它们是 bytes，则返回的名称的类型就是 bytes 而不是 str。
  如果确实要用默认参数，但又想要返回值是 bytes 类型，请传入 suffix=b''。

  text:
    为真值，文件会以文本模式打开。 否则，文件（默认）会以二进制模式打开。

  mkstemp() 返回一个元组，
  元组中第一个元素是句柄，它是一个系统级句柄，指向一个打开的文件（等同于 os.open() 的返回值），
  第二元素是该文件的绝对路径。

  在 3.5 版更改: 现在，suffix、prefix 和 dir 可以以 bytes 类型按顺序提供，以获得 bytes 类型的返回值。
  之前只允许使用 str。suffix 和 prefix 现在可以接受 None，并且默认为 None 以使用合适的默认值。

  在 3.6 版更改: dir 参数现在可接受一个路径类对象 (path-like object)。

.. function:: tempfile.mkdtemp(suffix=None, prefix=None, dir=None)

  以最安全的方式创建一个临时目录，创建该目录时不会有竞争的情况。该目录只能由创建者读取、写入和搜索。

  mkdtemp() 用户用完临时目录后需要自行将其删除。

  返回新目录的绝对路径。

  在 3.5 版更改: 现在，suffix、prefix 和 dir 可以以 bytes 类型按顺序提供，以获得 bytes 类型的返回值。之前只允许使用 str。suffix 和 prefix 现在可以接受 None，并且默认为 None 以使用合适的默认值。

  在 3.6 版更改: dir 参数现在可接受一个路径类对象 (path-like object)。

.. function:: tempfile.gettempdir()

  返回放置临时文件的目录的名称。这个方法的返回值就是本模块所有函数的 dir 参数的默认值。

  Python 搜索标准目录列表，以找到调用者可以在其中创建文件的目录。这个列表是：

  - TMPDIR 环境变量指向的目录。
  - TEMP 环境变量指向的目录。
  - TMP 环境变量指向的目录。

  与平台相关的位置：

  - 在 Windows 上，依次为 C:\TEMP、C:\TMP、\TEMP 和 \TMP。
  - 在所有其他平台上，依次为 /tmp、/var/tmp 和 /usr/tmp。

  不得已时，使用当前工作目录。
  搜索的结果会缓存起来，参见下面 tempdir 的描述。

  在 3.10 版更改: 总是返回一个字符串。 在之前的版本中它会返回任意 tempdir 值而不考虑它的类型，只要它不为 None。

.. function:: tempfile.gettempdirb()

  与 gettempdir() 相同，但返回值为字节类型。

.. function:: tempfile.gettempprefix()

  返回用于创建临时文件的文件名前缀，它不包含目录部分。

.. function:: tempfile.gettempprefixb()

  与 gettempprefix() 相同，但返回值为字节类型。

本模块使用一个全局变量来存储由 gettempdir() 返回的临时文件使用的目录路径。
它可被直接设置以覆盖选择过程，但不建议这样做。
本模块中的所有函数都接受一个 dir 参数，它可被用于指定目录。
这是不会通过改变全局 API 行为对其他无准备代码造成影响的推荐做法。

用例::

  import tempfile

  # create a temporary file and write some data to it
  fp = tempfile.TemporaryFile()
  fp.write(b'Hello world!')
  # read data from file
  fp.seek(0)
  fp.read()
  b'Hello world!'
  # close the file, it will be removed
  fp.close()

  # create a temporary file using a context manager
  with tempfile.TemporaryFile() as fp:
      fp.write(b'Hello world!')
      fp.seek(0)
      fp.read()
  b'Hello world!'
  >>>
  # file is now closed and removed

  # create a temporary directory using the context manager
  with tempfile.TemporaryDirectory() as tmpdirname:
      print('created temporary directory', tmpdirname)
  >>>
  # directory and contents have been removed











