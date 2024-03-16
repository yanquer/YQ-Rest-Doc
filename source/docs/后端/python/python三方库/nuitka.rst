====================
nuitka
====================


.. post:: 2023-02-20 22:18:59
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


nuitka中文官网: https://nuitka.net/zh_CN/index.html

Nuitka 是一个将 Python 代码编译成 C 或 C++ 代码的工具.
可以享受到python级别的开发速度，c级别的运行速度

Mac 下安装::

  pip install nuitka

额外建议安装orderedset， 这个是使用的时候建议安装, 原因:
Nuitka:WARNING: Using very slow fallback for ordered sets,
please install 'orderedset' PyPI package
for best Python compile time performance::

  pip install orderedset

简单使用
====================

当前系统版本安装的是python3版本的，所以于之前直接用 nuitka运行不一致，现在是nuitka3.
最简单的编译一个python文件::

  nuitka3 xxx.py

Win使用的时候会提示安装 ccache来加速，根据提示输入安装就是了，
我的是在 'https://nuitka.net/ccache/v4.2.1/ccache-4.2.1.zip' 自动下载安装
执行成功后会在当前目录下生成相应的可执行文件和编译文件夹，xxx.bin（win下是exe文件）跟xxx.build，

命令选项
====================

如::

  nuitka --standalone --show-progress --show-memory --plugin-enable=tk-inter --include-data-dir=resource=resource  --onefile trigger-angle.py
  python -m nuitka --standalone --show-progress --show-memory --plugin-enable=pyqt5 --windows-icon-from-ico=res/icon.ico  --include-data-dir=jsons=jsons --include-data-dir=pyqt=pyqt --include-data-dir=res=res --windows-disable-console --onefile  .\main_pyqt.py

**常用**

--module=<file>       指定主文件(入口文件), 比如main.py
--standalone, -s      生成独立的可执行文件(包含所有依赖项, 使目标机器不需要自己安装Python即可运行)
--onefile             是否打包为一个单独的 exe 文件(像pyinstaller一样)， 默认生成位置是在项目根目录下
--output-dir=<dir>, -o<dir>
                      输出目录, 生成exe到 dir文件夹 下面去
--plugin-enable=<plugin>
                      手动指定需要编译的三方包模块,
                      比如一些GUI模块tkinter, numpy, pytorch
                      如: --plugin-enable=tk-inter
--include-files       指定文件包含到编译输出
--include-data-file=<source=target>
                      包含的文件夹, 会直接复制过去
                      source代表当前(编译前的源代码阶段)位置;
                      target代码编译后放置的位置,
                      注意 = 不能甚省略.

--show-memory         查看编译时内存占用
--show-progress       查看编译进度, 显示进度条
--remove-output, -x   删除编译后的文件.

--python-flag=<FLAG>, -k<FLAG>
                      使用指定 Python 解释器编译.
--show-scons          显示 Scons 命令及其参数，方便调试.
--recurse-all, -r     递归处理所有导入过的模块
--show-modules, -m    显示要编译的所有模块
--experimental-annotations, -ea
                      启用实验性的类型注释功能. 即是否将Python代码中已有的
                      类型注解转换为C(++)的强类型定义.
--no-pyi-file, -np    不生成.pyi文件
--lto=<[yes,no]>      是否启用链接时优化（Link Time Optimization，LTO）.
                      它的作用是在链接可执行文件时，对整个程序进行全局优化，以达到更好的性能。
                      会增加额外的编译时间消耗.
                      启用后(yes)，nuitka 会在编译过程中生成 LLVM bitcode 文件，然后使用 LLVM 工具链进行链接。
                      LLVM 提供了一种跨平台的链接时优化技术，可以对各个模块之间的函数调用关系和数据依赖关系进行分析，
                      从而进行更加有效的优化。
--debug               启用编译后的可执行文件的运行时调试支持(也就是调试相关的符号表, 没有的话没法gdb调试)
--python-debug        用于生成可以进行调试的编译后的二进制文件（或者.so/.dll库文件）。
                      它会保留源代码中的所有调试信息，包括行号、变量名称等
                      .. 可以在 Python 调试器中进行调试, 好像只能设置远程调试服务器, 待测试

**包含/导入模块/包**

--include-package=PACKAGE
                        显示指定需要包含的整个包. 默认为空.
                        复制比如numpy,PyQt5 这些带子文件夹的包
                        e.g. "some_package.sub_package". Python 将会寻找并包含到编译输出.
                        为了避免导入不需要的包, 可以使用, 如 "--nofollow-import-to=*.tests".
--include-module=MODULE
                        包括单个模块。以一个Python命名空间给出，
                        复制比如when.py 这种以.py结尾的模块.
                        例如“Some_Package.Some_Module”，然后Nuitka将
                        找到它并将其包含在二进制或扩展中
                        模块，并使其可通过以下方式导入
                        密码。默认为空。
--include-plugin-directory=<MODULE/PACKAGE>
                        另外包含指定路径的下的包/模块.
                        此处找到的将会覆盖原来有的. 可指定多次.
                        默认为空.
--include-plugin-files=PATTERN
                        包含文件内能匹配 PATTERN 的. 会覆盖原有的 .
                        可指定多次.
                        默认为空.
--prefer-source-code
                        对于已经编译好的拓展模块, 不论是源文件还是拓展模块, 都正常使用.
                        会比直接从可用源文件编译要好?(这里没懂).
                        如果不希望，有--noprefer-source-code 来禁用有关它的警告。
                        默认 off.

**控制跟踪导入的模块**

什么叫跟踪导入? 见: :ref:`CR_Python_跟踪导入`

--follow-stdlib=<{yes,no}>
                        是否包含整个 Python 标准库, 会增加很多时间.
                        默认关闭. 值为 yes/no.
--nofollow-imports      仅编译源代码，而不会尝试跟踪导入的任何模块/包.
                        使用此选项时, 若代码依赖于其他库或模块，则必须手动将它们包含在编译后的二进制文件中。
                        通常情况下，只有在确定所有依赖项都已正确安装并且您不需要将代码打包到独立的可执行文件中时，
                        才应使用此选项。
                        默认关闭.
--follow-imports, -f    跟踪所有导入的模块/包，并将它们也编译为二进制文件.
                        若程序依赖于其他库或模块，则必须使用此选项以确保所有依赖项都被正确地编译到生成的可执行文件中。
                        这个选项可以确保你的程序能够完全独立运行，而不需要依赖于任何外部库或环境。
                        默认关闭.
--follow-import-to=<MODULE/PACKAGE>
                        指定搜索模块时的搜索路径, 从当前路径开始,
                        详见: follow-import-to_
                        可多次指定, 默认为空.
--nofollow-import-to=<MODULE/PACKAGE>
                        不从路径导入.
                        可指定多个, 默认为空.

**数据文件**

这里的数据文件通常是指 **必要的资源文件** , 如图片, 配置文件.

--include-package-data=PACKAGE
                        包含指定 PACKAGE 下的所有数据文件. 支持通配符
                        By default Nuitka does not
                        unless hard coded and vital for operation of a package.
                        文件应该是非 dll 文件, 非 拓展模块.
                        默认为空.
--include-data-files=<DESC>
                        包含分布下指定描述的所有数据文件,
                        存在许多运行的格式, eg:
                        `--include-data-files=/path/to/file/*.txt=folder_name/some.txt`,
                        将会复制为单个文件, 多文件将会有警告.
                        `--include-data-files=/path/to/files/*.txt=folder_name/`,
                        将会将所有匹配的文件复制到 folder_name 文件夹下.
                        若需要递归拷贝, 使用
                        `--include-data-files=/path/to/scan=folder_name=**/*.txt`
                        同时还会保留原有目录结构.
                        默认空.
--include-data-dir=DIRECTORY
                        包含指定目录下的所有文件. 这是递归的.
                        若不需递归, 使用 --include-data-files.
                        eg: '--include-data-dir=/path/some_dir=data/some_dir'
                        将会拷贝一个普通的全文件副本.
                        如果需要排除某些文件, 使用 --noinclude-data-files.
                        默认为空.
--noinclude-data-files=PATTERN
                        不包含符合 PATTERN 匹配的文件.
                        仅针对文件名而非源路径.
                        eg: `package_name`` 会匹配 `package_name/*.txt`.
                        默认空.

**DLL 文件**

--noinclude-dlls=PATTERN
                        不包含复合匹配的 dll 文件.
                        需指定到具体目标文件, eg:
                        "package_name/someDLL.*"
                        匹配 package_name 下包含 someDLL 的文件.
                        默认为空.

**其他**

举例:

--noinclude-pytest-mode=error     如果包含pytest模块报错
--noinclude-unittest-mode=error   如果包含unittest模块报错, 防止意外导入不需要的包.
--enable-plugin=<module>          直接添加你要的插件支持,
                                  如--enable-plugin=pyqt5,numpy,matplotlib
--plugin-list                     不清楚该模块是否有特定的插件支持，在cmd窗口输入后查询
--mingw64                         默认为已经安装的vs2017去编译，
                                  否则就按指定的比如mingw(官方建议),
                                  仅Win适用, 貌似
--windows-disable-console, -wdc   禁用Windows上的命令行窗口, 没有CMD控制窗口
--windows-icon-from-ico=<ico_p>   软件的图标, .ico图标文件
--windows-company-name=<com>      Windows下软件公司name
--windows-product-name=<product>  Windows下软件名称
--windows-file-version=<file>     Windows下软件的信息
--windows-product-version=<ver>   版本信息
--windows-file-description=<desc>
                                  Windows下软件的作用描述
--windows-uac-admin               Windows下用户可以使用管理员权限来安装
--linux-onefile-icon=<file>       Linux下的图标位置

YAML配置形式
====================

支持使用 YAML 配置文件通过 --user-package-configuration-file 来指定配置,
如以下配置::

  # sample configuration file for Nuitka

  # 输出路径
  output_dir: ./dist/

  # 递归处理所有模块
  recurse_all: true

  # 删除上一次的输出
  remove_output: true

  # 生成独立的文件
  standalone: true

  # 显示进度条
  show_progress: true

  # 跟踪导入
  follow_imports: true

  # python 版本
  python_version: 3.9

启动::

  nuitka --config-file=config.yml myscript.py

注意，配置文件中的选项会覆盖命令行选项

关于 --nofollow-imports 说明
========================================

--nofollow-imports 是 Nuitka 编译器的一个选项，它的含义是在编译过程中不对某些导入语句进行处理。
具体来说，如果使用了 --nofollow-imports 选项，则 Nuitka 编译器会忽略某些导入语句，
并将它们视为运行时动态导入（Runtime Dynamic Imports），而不是静态导入。

通常情况下，Python 中的导入语句是静态的，也就是说，在执行 Python 脚本之前，所有必要的模块都已经被导入并加载到内存中了。
然而，在某些情况下，我们可能需要根据运行时条件来动态导入某些模块，这就需要使用运行时动态导入。

使用 --nofollow-imports 选项可以让 Nuitka 编译器在编译过程中忽略某些导入语句，从而减少编译时间和输出文件大小。
但是，这也可能会导致某些代码无法正常编译或运行，因此建议在使用该选项时谨慎考虑。

例如，假设我们有一个 Python 脚本 main.py，其中包含以下导入语句::

  import module1
  from module2 import func

  if some_condition:
      import module3
  else:
      import module4

如果使用默认选项（即不添加 --nofollow-imports），
则 Nuitka 编译器会尝试静态地分析这些导入语句，并在编译过程中将所有必要的模块都包含在输出文件中。
如果使用 --nofollow-imports 选项，则 Nuitka 编译器会忽略其中一些导入语句，例如：

  nuitka --nofollow-imports main.py

由于该脚本中存在运行时条件导入语句，因此 Nuitka 编译器只能将它们视为运行时动态导入，而不是静态导入。

.. _follow-import-to:

关于 --follow-import-to 说明
========================================

指示编译器在遵循 import 语句时应该搜索哪些路径。

这个标志允许你指定要跟踪的目录或文件名，使得 Nuitka 在编译过程中可以找到需要的依赖项。

例如，如果使用::

  --follow-import-to=dir1:dir2

则 Nuitka 将首先搜索当前目录、然后再搜索 dir1 和 dir2 目录，以查找所需的模块。

follow_imports 说明
========================================

指示编译器是否应该跟踪导入并包含它们。

如果设置为 true，则 nuitka 将跟踪所有导入的模块，并将其包含在生成的可执行文件中。
这通常用于确保所有依赖项都包括在二进制文件中，以便在运行时可以访问它们。

如果设置为 false，则 nuitka 不会在编译过程中跟踪导入，因此生成的二进制文件可能会缺少一些必要的依赖项。

默认情况下，该选项的值为 false。

你可以通过以下命令行选项来设置 follow_imports ::

  nuitka --follow-imports myscript.py

或者在 YAML 配置文件中使用::

  follow_imports: true

来启用该选项。

增量编译
========================================

.. tip::

  来源于 ChatGpt

Nuitka是一个Python编译器，它将Python源代码编译成C++代码，以获得更快的执行速度。
默认情况下，Nuitka会进行完整的构建，这意味着每次更改源代码时都需要重新编译整个程序。

然而，Nuitka支持增量编译，它只会重新编译发生更改的源文件，而不是整个程序。
这可以通过使用--module-mode参数来实现。例如，要对名为example.py的源文件进行增量编译，请使用以下命令::

  nuitka --module-mode example.py

这将生成一个名为example.so的共享库文件，其中包含编译后的代码。
如果您对example.py进行了更改，则只需要重新运行此命令即可仅重新编译更改的部分，而无需重新编译整个程序。

请注意，增量编译可能会导致一些问题，因为某些更改可能会影响其他源文件。
在这种情况下，您可能需要重新编译整个程序，以确保所有部分都是最新的。

进程调试
====================

对于使用nuitka编译好的应用, 如何调试?

前提: **安装debug版的python**, 参考 :doc:`/docs/后端/python/教程/debug版本python安装`

首先, 源码中导入“ptvsd”模块并添加“ptvsd.enable_attach()”语句。
这个语句会在程序启动时暂停,等待调试器附加::

  import ptvsd

  # Enable debugger
  ptvsd.enable_attach('my_secret_password')

  # Program code
  ...

其次, 使用 nuitka 编译时, 增加debug和python-debug参数::

  # /usr/local/python/python3.9.10/bin/python3.9 -m nuitka --python-debug main.py
  python -m nuitka --debug --python-debug myprogram.py

然后, 启动构建好的应用程序。程序启动后会暂停等待调试器连接。

在PyCharm中,选择“Run” -> “Attach to Process...”,
然后在弹出窗口选择“Python Attach”并点击“Connect to process on host”选项。

在“Gateway”输入框中输入应用程序暂停时显示的“ptvsd”信息,包括密码。然后点击“Attach”。

PyCharm成功连接后,可以设置断点、查看变量、单步执行等进行调试。

完成调试后,点击“Detach”断开连接。程序将继续运行。

!! 经过多方测试, 不行, 只有使用gdb调..., mac下是lldb

特殊情况调试
====================

普通情况下 进程调试_ 已经能满足需求, 但是有时, 是从源码编译安装的Python,
就会有些库找不到等问题. 对于此种情况, 做一个说明.

假设主程序my_program.py，需要使用静态链接的 Python 库 /opt/python/lib/libpython3.9.a 进行编译。

方案一:
  可以先设置 NUITKA_PYTHON_LIB 环境变量::

    export NUITKA_PYTHON_LIB=/opt/python/lib/libpython3.9.a

  然后使用 nuitka 命令进行编译::

    nuitka --standalone my_program.py

  这将生成一个独立的可执行文件 my_program.bin，其中包含了静态链接的 Python 库。

方案二:
  另一种方式是在 nuitka 命令中直接指定 Python 库的路径和名称::

    nuitka --standalone --python-flag=-L/opt/python/lib --python-flag=-lpython3.9 my_program.py

  这将生成与上面相同的独立可执行文件。
  注意，--python-flag=-L 选项指定 Python 库所在的目录，--python-flag=-l 选项指定 Python 库的名称。

.. note::

  实际操作可能有不同, 我在ubuntu20上使用ubuntu16编译的python3.7, nuitka编译时指定--python-debug老是报错:
  libpython找不到或者当前python不支持::

    fatal: error, static libpython isnot found or not supported for this python installed

  试过加环境变量, 加命令行选项都不行, 故此小节有待更新.

原理/底层部分说明
====================

编译过程
--------------------

Nuitka的编译过程分为三个步骤：

- 分析：对Python代码进行语法和语义分析，并生成内部表示。
- 优化：对内部表示进行各种优化，包括常量折叠、无用代码消除、函数内联、循环展开等。
- 生成代码：将优化后的内部表示转化为C或机器码，并生成可执行文件。

C代码生成
--------------------

当选择将Python代码编译成C代码时，会生成一个.c和一个.h文件。
其中，.c文件包含了Python代码的C语言实现，.h文件包含了Python对象的定义、函数原型等信息。
这两个文件可以被编译成一个可执行文件。

需要注意的是，由于Python是一种动态语言，对象类型和大小在运行时才能确定。
因此，在生成C代码时，需要对每个对象进行类型检查，并根据类型分发到不同的实现中。
这导致了生成的C代码比较复杂，且不易阅读。

二进制代码生成
--------------------

当选择将Python代码编译成机器码时，会生成一个可执行文件。
与C代码生成相比，机器码生成不需要进行类型检查，因为机器码已经包含了对象类型和大小的信息。
这使得生成的可执行文件比较小，且执行速度更快。

需要注意的是，由于机器码是与硬件平台相关的，因此生成的可执行文件只能在同一平台上运行。

性能优化
--------------------

除了代码生成外，性能优化也是Nuitka的重要功能之一。
它通过各种编译技术和优化算法，对Python代码进行优化，从而提高程序的执行效率。

其中，最常用的优化算法包括：

- 常量折叠：将多次出现的常量合并成一个。
- 无用代码消除：删除不会被执行的代码。
- 函数内联：将函数调用替换成函数体。
- 循环展开：将循环拆分成多个重复代码块。

需要注意的是，在进行代码优化时，可能会改变原有的程序行为。因此，你需要仔细测试编译后的代码，确保其正确性和可靠性。

gcc相关环境变量
====================

主要是使用nuitka生成c代码之后, 会用到gcc将代码编译成执行文件.

相关环境变量, gcc本身的环境变量此处不做说明, 可见 :ref:`gcc_相关环境变量`

nuitka支持的相关环境变量:

- NUITKA_CC: 使用gcc编译时, 使用相关参数/选项,
  如 `export NUITKA_CC="gcc -I/path/to/header/files -L/path/to/library/files -lexample"`,
  -I参数指定头文件路径，-L参数指定库文件路径，-lexample参数指定要链接的库文件名.
  若同时指定了CC环境变量, NUITKA优先.
- NUITKA_EXTRA_CFLAGS: 指定额外的参数.
- NUITKA_EXTRA_CFLAGS: 指定链接器（如ld）的选项

报错找不到Python标准库文件
========================================

对于Python标准库的文件, 一般只要使用到, 编译的时候都是会自动导入,
但是有一种情况, 某些原因下可能没跟踪到所以不会导(比如你是在一个不会被跟踪的模块下导入),
这时候需要显示导入, 比如能跟踪到的地方写下导入语句, 比如bdb::

  import bdb

同时, 这种情况下是无法使用 ``--include-module=bdb`` 来处理的, 原因暂时未知.




