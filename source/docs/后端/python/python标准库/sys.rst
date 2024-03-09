================
sys
================

官网: `sys --- 系统相关的参数和函数 <https://docs.python.org/zh-cn/3/library/sys.html>`_

该模块提供了一些变量和函数。
这些变量可能被解释器使用，也可能由解释器提供。
这些函数会影响解释器。
本模块总是可用的。

仅记录常用的

属性
================

sys.argv
  一个列表，其中包含了被传递给 Python 脚本的命令行参数。
  argv[0] 为脚本的名称（是否是完整的路径名取决于操作系统）。
  如果是通过 Python 解释器的命令行参数 -c 来执行的， argv[0] 会被设置成字符串 '-c' 。
  如果没有脚本名被传递给 Python 解释器， argv[0] 为空字符串。

  为了遍历标准输入，或者通过命令行传递的文件列表，参照 fileinput 模块

  另请参阅 sys.orig_argv。

  .. note::

    在 Unix 上，系统传递的命令行参数是字节类型的。Python 使用文件系统编码和 "surrogateescape" 错误处理方案对它们进行解码。当需要原始字节时，可以通过 [os.fsencode(arg) for arg in sys.argv] 来获取。
sys.base_exec_prefix
  官网说的有点复杂. 实际就是虚拟环境目录
sys.base_prefix
  一般与上一个一致.
sys.byteorder
  本地字节顺序的指示符。

  在大端序（最高有效位优先）操作系统上值为 'big' ，
  在小端序（最低有效位优先）操作系统上为 'little'
sys.executable: str
  提供 Python 解释器的可执行二进制文件的绝对路径，仅在部分系统中此值有意义。
  如果 Python 无法获取其可执行文件的真实路径，则 sys.executable 将为空字符串或 None。
sys.modules
  这是一个字典，它将模块名称映射到已经被加载的模块。
  这可以被操纵来强制重新加载模块和其他技巧。
  然而，替换这个字典不一定会像预期的那样工作，从字典中删除重要的项目可能会导致 Python 出错。
  如果你想对这个全局字典进行迭代，一定要使用 sys.modules.copy() 或 tuple(sys.modules) 来避免异常，
  因为它的大小在迭代过程中可能会因为其他线程中的代码或活动的副作用而改变。
sys.orig_argv
  传给 Python 可执行文件的原始命令行参数列表。
sys.path
  一个由字符串组成的列表，用于指定模块的搜索路径。
  初始化自环境变量 PYTHONPATH，再加上一条与安装有关的默认路径。
sys.platform
  本字符串是一个平台标识符.

  对于 Unix 系统（除 Linux 和 AIX 外），该字符串是 Python 构建时的 uname -s 返回的小写操作系统名称，
  并附加了 uname -r 返回的系统版本的第一部分，如 'sunos5' 或 'freebsd8'

  对于其他系统:

  .. csv-table::
    :header: 系统, 平台值

    AIX,          'aix'
    Emscripten,   'emscripten'
    Linux,        'linux'
    WASI,         'wasi'
    Windows,      'win32'
    Windows/Cygwin, 'cygwin'
    macOS,        'darwin'
sys.platlibdir
  平台专用库目录。用于构建标准库的路径和已安装扩展模块的路径。

  在大多数平台上，它等同于 "lib"
sys.stdin;sys.stdout;sys.stderr
  解释器用于标准输入、标准输出和标准错误的 文件对象
sys.version
  一个包含 Python 解释器版本号加编译版本号以及所用编译器等额外信息的字符串。

  请不要从中提取版本信息，而应当使用 version_info 以及 platform 模块所提供的函数。
sys.api_version
  这个解释器的 C API 版本。当你在调试 Python及期扩展模板的版本冲突这个功能非常有用。
sys.version_info
  一个包含版本号五部分的元组: major, minor, micro, releaselevel 和 serial。
  除 releaselevel 外的所有值均为整数；发布级别值则为 'alpha', 'beta', 'candidate' 或 'final'。
  对应于 Python 版本 2.0 的 version_info 值为 (2, 0, 0, 'final', 0)。
  这些部分也可按名称访问，因此 sys.version_info[0] 就等价于 sys.version_info.major，依此类推。

  在 3.1 版更改: 增加了以名称表示的各部分属性。
sys.maxsize
  一个整数，表示 Py_ssize_t 类型的变量可以取到的最大值。

  在 32 位平台上通常为 2**31 - 1，在 64 位平台上通常为 2**63 - 1。
sys.maxunicode
  一个整数，表示最大的 Unicode 码点值，如 1114111 （十六进制为 0x10FFFF ）。

  在 3.3 版更改: 在 PEP 393 之前，sys.maxunicode 曾是 0xFFFF 或 0x10FFFF，
  具体取决于配置选项，该选项指定将 Unicode 字符存储为 UCS-2 还是 UCS-4。

函数
================

.. function:: sys._clear_type_cache()

  清除内部的类型缓存。类型缓存是为了加速查找方法和属性的。在调试引用泄漏的时候调用这个函数 只会 清除不必要的引用。

  这个函数应该只在内部为了一些特定的目的使用。

.. function:: sys.exit([arg])

  引发一个 SystemExit 异常，表示打算退出解释器。

  arg 默认为 0. 表示正常退出;
  非0整型, 表示异常终止.

  大多数系统要求该值的范围是 0-127，否则会产生不确定的结果。
  某些系统为退出代码约定了特定的含义，但通常尚不完善；

  Unix 程序通常用 2 表示命令行语法错误，
  用 1 表示所有其他类型的错误。

  传入其他类型的对象:

  - 如果传入 None 等同于传入 0，
  - 如果传入其他对象则将其打印至 stderr，且退出代码为 1

  特别地，sys.exit("some error message") 可以在发生错误时快速退出程序。

  由于 exit() 最终 "只" 引发了一个异常，它只在从主线程调用时退出进程，而异常不会被拦截。
  try 语句的 finally 子句所指定的清理动作会被遵守，并且有可能在外层拦截退出的尝试。

  在 3.6 版更改: 在 Python 解释器捕获 SystemExit 后，如果在清理中发生错误（如清除标准流中的缓冲数据时出错），则退出状态码将变为 120。

.. function:: sys.getallocatedblocks()

  返回解释器当前已分配的内存块数，无论它们大小如何。本
  函数主要用于跟踪和调试内存泄漏。
  因为解释器有内部缓存，所以不同调用之间结果会变化。
  可能需要调用 _clear_type_cache() 和 gc.collect() 使结果更容易预测。

  如果当前 Python 构建或实现无法合理地计算此信息，允许 getallocatedblocks() 返回 0。

  3.4 新版功能.

.. function:: sys.getdefaultencoding()

  返回当前 Unicode 实现所使用的默认字符串编码名称。

.. function:: sys.getdlopenflags()

  返回当前 dlopen() 调用所使用的标志位的值。
  标志值对应的符号名称可以在 os 模块中找到（形如 RTLD_xxx 的常量，如 os.RTLD_LAZY ）。

  可用性: Unix。

.. function:: sys.getfilesystemencoding()
  获取 文件系统编码格式: 与 文件系统错误处理句柄 一起使用以便在 Unicode 文件名和字节文件名之间进行转换。
  文件系统错误处理句柄是由 getfilesystemencoding() 来返回的。

  为获得最佳兼容性，在任何时候都应使用 str 来表示文件名，尽管使用 bytes 来表示文件名也是受支持的。
  接受还返回文件名的函数应当支持 str 或 bytes 并在内部将其转换为系统首选的表示形式。

.. function:: sys.getrecursionlimit()

  返回当前的递归限制值，即 Python 解释器堆栈的最大深度。
  此限制可防止无限递归导致的 C 堆栈溢出和 Python 崩溃。

  该值可以通过 setrecursionlimit() 设置。

.. function:: sys.getsizeof(object[, default])

  返回对象的大小（以字节为单位）。
  该对象可以是任何类型。
  所有内建对象返回的结果都是正确的，但对于第三方扩展不一定正确，因为这与具体实现有关。

  只计算直接分配给对象的内存消耗，不计算它所引用的对象的内存消耗。

  对象不提供计算大小的方法时，如果传入过 default 则返回它，否则抛出 TypeError 异常。

  如果对象由垃圾回收器管理，则 getsizeof() 将调用对象的 __sizeof__ 方法，并在上层添加额外的垃圾回收器。

  可以参考 recursive sizeof recipe 中的示例，关于递归调用 getsizeof() 来得到各个容器及其所有内容物的大小。

.. function:: sys.gettrace()

  返回由 settrace() 设置的跟踪函数。

  CPython 实现细节： gettrace() 函数仅用于实现调试器，性能分析器，打包工具等。
  它的行为是实现平台的一部分，而不是语言定义的一部分，因此并非在所有 Python 实现中都可用。

.. function:: sys._getframe([depth])

  返回来自调用栈的一个帧对象。如果传入可选整数 depth，则返回从栈顶往下相应调用层数的帧对象。
  如果该数比调用栈更深，则抛出 ValueError。depth 的默认值是 0，返回调用栈顶部的帧。

  Raises an auditing event sys._getframe with argument frame.

  CPython 实现细节： 这个函数应该只在内部为了一些特定的目的使用。不保证它在所有 Python 实现中都存在。

  通过::

    sys._getframe([depth]).f_locals

  获取此栈局部变量








