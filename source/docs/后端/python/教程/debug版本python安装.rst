===============================
debug版本python安装
===============================

参考: https://docs.python.org/zh-cn/3.11/using/unix.html

找了一下资料, debug版本只有windows可以通过安装包安装,
其他如linux、mac等都得手动编译安装.

Mac下的安装
===============================

基本指令::

  wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
  tar -xzf Python-3.9.10.tgz
  cd Python-3.9.10
  ./configure --enable-optimizations --with-pydebug --prefix=/usr/local/python/python3.9.10  --with-openssl=/usr/local/opt/openssl@1.1 --with-lto
  make -j8 && sudo make altinstall

- --with-pydebug参数会编译带有debug符号的二进制文件,方便后期使用gdb进行调试
- --enable-optimizations 用 PROFILE_TASK 启用以配置文件主导的优化（PGO）（默认为禁用）.
  C 编译器 Clang 需要用到 llvm-profdata 程序进行 PGO。在 macOS 上，GCC 也需要用到它：在 macOS 上 GCC 只是 Clang 的别名而已。
  如果使用 --enable-shared 和 GCC ，还可以禁用 libpython 中的语义插值：在编译器和链接器的标志中加入 -fno-semantic-interposition 。
- --prefix指定安装路径
- --with-openssl指定openssl的路径, 否则ssl模块无法使用
- --with-lto: 启用链接时优化（Link Time Optimization，简称LTO）。
  链接时优化是一种编译器优化技术，通过在链接阶段对代码进行全局分析和优化，可以提高程序的性能。
  在启用LTO时，编译器将生成中间表示形式（IR）并将其保存到目标文件中。
  然后，在链接阶段，通过对所有目标文件中的IR进行深度优化和分析，以及整体代码重排和消除冗余等操作，生成最终可执行文件或库。

configure支持的参数可查看: https://docs.python.org/zh-cn/3.11/using/configure.html

make相关:

- make ：用标准库构建Python, -j8表示8个任务并行安装
- make clean ：移除构建的文件
- make distclean ：与 make clean 相同，但也删除由配置脚本创建的文件

.. warning::

  make install 可以覆盖或伪装 python3 二进制文件(系统默认的python3)。
  因此，建议使用 make altinstall 而不是 make install ，
  因为后者只安装了 exec_prefix/bin/pythonversion 。

后续遇到的问题
===============================

使用nuitka编译时, 有时候源码能跑过的, 构建出来跑不了,
所以研究了一下对于构建好的应用, 能否在Python的层面进行调试,
结果似乎不能,
虽然意外发现有nuitka一个 ``--python-debug`` 选项, 也只能实现编译后
的文件保留了原有的行号变量等信息, 最终还是得gdb(mac下lldb)出手.
可参考: :doc:`/docs/后端/python/python三方库/nuitka` .
不过需要安装支持debug的python版本, 也就是编译安装python
时需要添加 ``--with-pydebug`` 选项...

最开始使用上述流程安装好python时候, python使用没问题,
使用nuitka构建的时候出现报错::

  Undefined symbols for architecture x86_64:
    "_libintl_bindtextdomain", referenced from:
        fish_bindtextdomain(char const*, char const*) in libfishlib.a(fallback.cpp.o)
    "_libintl_gettext", referenced from:
        fish_gettext(char const*) in libfishlib.a(fallback.cpp.o)
    "_libintl_textdomain", referenced from:
        fish_textdomain(char const*) in libfishlib.a(fallback.cpp.o)
  ld: symbol(s) not found for architecture x86_64
  clang: error: linker command failed with exit code 1 (use -v to see invocation)

类似这样, 最开始查了一下以为是gettext库不对(在这之前已经安装了gettext),
以为出现找不到 _libintl, 是没设置好环境变量, 就设置了一下并重新编译安装::

  export LDFLAGS="-L/usr/local/opt/gettext/lib"
  export CPPFLAGS="-I/usr/local/opt/gettext/include"

.. sidebar::

  libintl 是 gettext 的一部分。gettext 是一个用于国际化和本地化的工具集，
  它提供了一种方式来在应用程序中从源代码中提取文本，并将其翻译成不同的语言。
  libintl 是 gettext 提供的一个库，用于处理多语言文本的运行时支持，
  包括翻译、格式化和字符编码等功能。通过使用 libintl，开发人员可以轻松地实现多语言支持的应用程序。

结果还是发现有问题, 后面试过给nuitka加参数, 指定 LD_LIBRARY_PATH 等, 都失败了.

然后突然想起看一下动态库的链接是啥(linux下是ldd, mac默认没有, 有个相似的otool),
编译安装的debug版本如下::

  $ otool -L  /usr/local/python/python3.9.10/bin/python3.9
  /usr/local/python/python3.9.10/bin/python3.9:
    /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 1971.0.0)
    /usr/local/opt/gettext/lib/libintl.8.dylib (compatibility version 12.0.0, current version 12.0.0)
    /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1319.100.3)

又去找了一个正常的看::

  $ readlink -f  `which python3`
  /usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/bin/python3.11

  $ otool -L /usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/bin/python3.11
  /usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/bin/python3.11:
    /usr/local/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/Python (compatibility version 3.11.0, current version 3.11.0)
    /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1319.100.3)

一对比, 编译安装的多了个 `/usr/local/opt/gettext/lib/libintl.8.dylib`, ls查看了一下位置,
路径没问题啊, 为什么会这样?
百度无果, 开墙, 谷歌, 终于在github发现了类似的一个问题,
不过是由 **CMAKE** 引起, 参见: https://github.com/fish-shell/fish-shell/issues/5244,
**CMAKE** 也有说明有其他地方已经提出: https://gitlab.kitware.com/cmake/cmake/-/issues/18921, 现在这问题四年了还没关.

有位大佬在19年已经说明好问题了::

  I can reproduce this - looks like I've got the Mono libintl, and if I add the brew gettext tools to my path, I get the same problem.

  I have spent some time reviewing the current state:

  - libintl is not shipped in macOS, but can be picked up by FindPackage(Intl)
  - the gettext binaries (msgfmt etc) are not shipped in macOS, but can be picked up by FindPackage(gettext)
  - if both libintl and the gettext binaries are detected, the include directories get added to the global include directories
  - regardless of the gettext state, the libintl libraries are added to the list of library dependencies of the fishlib target (this is inconsistent with the previous item and probably needs fixing, perhaps through an add_library target)

  If you have Mono installed, libintl's headers are picked up by CMake from /Library/Frameworks/Mono.framework, but the libraries are not found in the same prefix (Intl_LIBRARY:FILEPATH=Intl_LIBRARY-NOTFOUND). Unfortunately, this cannot be used as a signal that libintl is not available, because this is exactly the state that glibc is in with libintl compiled into the main library.

  This is only exposed as a problem when gettext is in the path, because of the requirement for both gettext and libintl for the include_directory call (as above).

  pkg-config would not help here, because it does not ship on macOS.

  I think this is a bug in CMake's FindIntl module, which I'll report to them. Someone has a similar problem in EOSIO/eos#1539.

  For now, you can work around this either by turning off the use of translation (cmake -DWITH_GETTEXT=0), or enable it by adding an additional library search path (cmake -DCMAKE_LIBRARY_PATH=/Library/Frameworks/Mono.framework/Libraries).

简而言之就是, 因为brew手动安装了gettext, 同时系统也安装了Mono(一个.Net的什么框架), 然而Mono下
已存在libintl库, 这个时候系统内就有两个地方存在这个库了.
然后编译安装Python时, 会自动探测包位置, brew包管理器发现了有gettext这个包, 所以就使用了,
但是, 用的这个又多了一些东西(暂且这么说, 实际编译时不需要这些), 就导致了使用nuitka时的报错
(他这里虽然是CMAKE, 但是原因是一致的).
而且后面fish-shell处理了这问题: https://github.com/fish-shell/fish-shell/commit/970a963896162617af3e18fb2df953dbeac0a4fc

.. note::

  我就很诧异, 没其他人遇到这个问题吗...

看了一下我的 ``/Library/Frameworks/Mono.framework`` 下面, 果然已经有一个 ``libintl.8.dylib``,
所以自己brew安装的gettext就是个多余的, 导致编译安装好的python多了个自安装的libintl动态库链接,
尝试过手动指定路径没找到方法, 最后 ``brew uninstall gettext`` 后再重新编译安装后解决::

  sudo make clean
  sudo make distclean
  sudo rm -rf /usr/local/python/python3.9.10
  ./configure --enable-optimizations --with-pydebug --prefix=/usr/local/python/python3.9.10  --with-openssl=/usr/local/opt/openssl@1.1
  sudo make -j8 && sudo make altinstall

查看链接位置::

  $ otool -L  /usr/local/python/python3.9.10/bin/python3.9
  /usr/local/python/python3.9.10/bin/python3.9:
    /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 1971.0.0)
    /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1319.100.3)

正常了


