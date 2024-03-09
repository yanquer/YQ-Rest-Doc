==============
pytest
==============

使用见: :doc:`/docs/后端/python/教程/Pytest`

语法::

  pytest [options] [file_or_dir] [file_or_dir] [...]

  # positional arguments:
  #   file_or_dir

选项参数
==============

general:
--------------

--capture=method      捕获消息的类型 fd|sys|no|tee-sys.
-s                    上面为no时的简写 --capture=no. 后面看到一个说法是输出包含stdout与stderr.
                      正常情况下,pytest会捕获测试中的stdout和stderr,并只在测试失败时才将其打印出来。
                      使用-s选项后,pytest将不会捕获stdout和stderr,而是直接打印。
                      这在调试测试用例时非常有用,可以直接在控制台看到print的输出,而不需要添加失败的断言来查看输出。
--show-capture=<{no,stdout,stderr,log,all}>
                      Controls how captured stdout/stderr/log is shown on
                      Write captured log messages to JUnit report: one of
-m<some_test>         指定要运行哪些测试
-m MARKEXPR           仅运行 @pytest.mark.MARKEXPR 装饰的测试.
                      如: -m 'mark1 and not mark2'.
-k EXPRESSION         仅执行匹配 EXPRESSION 的测试, 支持通配符, 多个使用引号包裹, or 隔开.
                      如: -k 'test_method or test_other' 表示
                      会执行所有 函数名/类名包含 'test_method' or 'test_other' 的测试;
                      -k 'not test_method' 表示仅执行不包含 'test_method' 的测试;
                      -k 'not test_method and not test_other' 表示两者之一被包含的测试会被排除.
--markers             show markers, 即上面 -m 的 MARKEXPR
-x, --exitfirst       当测试错误/执行失败, 立即退出执行, 不会运行后面的测试
--fixtures, --funcargs
                      show available fixtures, sorted by plugin appearance
                      (fixtures with leading '_' are only shown with '-v')
--fixtures-per-test   show fixtures per test
--pdb                 在错误或者键盘中断(Ctrl + C)时候, 开始一个交互式的 pdb debugger (终端).
--pdbcls=<modulename:classname>
                      使用 --pdb 来开启一个 debug 终端.
                      此时可加此选项来指定终端类型,
                      如:
                      --pdbcls=IPython.terminal.debugger:TerminalPdb
--trace               在运行每项测试时立即中断, 用于 debug.
--runxfail            报告标记 XFAIL 测试的结果, 就像他们没有被标记一样.
--lf, --last-failed   在最后一次运行时, 仅重新运行失败的测试(如果没有失败，则全部运行)
--ff, --failed-first  运行所有测试，但先运行最后的失败。
                      这可能会重新安排测试，从而导致
                      固件的重复 安装/卸载.
--nf, --new-first     首先运行最新的文件的测试,
                      然后按照文件的 mtime (修改时间) 顺序执行.
--cache-show=<[CACHESHOW]>
                      不执行测试收集/测试, 显示缓存内容.
                      Optional argument: glob (default: '*').
--cache-clear         测试开始前移除所有的缓存内容.
--lfnf=<{all,none}>, --last-failed-no-failures=<{all,none}>
                      在之前没有（已知）故障的情况下运行哪些测试?
                      原句:
                      which tests to run with no previously (known) failures.
--sw, --stepwise      当测试失败时退出, 下一次从次失败的测试开始执行
--sw-skip, --stepwise-skip
                      仅忽略第一个失败的测试, 即后续还有失败会停止
                      隐式启用 --stepwise.
-v                    启用冗长日志记录,会打印更详细的测试结果。
-vv                   启用更加详细的日志,会打印测试相关的所有输出,包括:
                      测试开始和结束的日志;
                      测试文件路径;
                      通过的测试用例名称;
                      失败的测试用例名称及失败原因;
                      跳过的测试用例名称及跳过原因;
                      所有打印的输出(类似-s选项);
                      用于记录测试结果的文件路径;

**``-m MARKEXPR`` 说明**:

作用为指定运行哪些测试用例, MARKEXPR 表示装饰器的标记, 多个使用引号包裹, or 隔开::

  pytest -m "test_run1 or test_run2 or test_run3"

表示仅运行以下装饰器修饰的测试::

  @pytest.mark.test_run1
  @pytest.mark.test_run2
  @pytest.mark.test_run3

**捕获方式 capture 说明** :

- fd, 文件描述符级别的捕获, 也就是写入到 ``1`` , ``2`` 标准输出/错误的内容会被捕获
- sys, 使用 ``sys.stdout`` , ``sys.stderr`` 输出的消息会被捕获
- no, 禁止捕获所有输出.
- tee-sys

个人理解:

这里的捕获, 即将本来应该立即输出到到控制台/文件的信息截取, 可以加一些自定义的操作.

默认是 all , 捕获所有信息, 所以不会实时输出而是结束后一起输出

如果想 **实时输出信息** 那么需要使用, ``-s`` 或者 ``--capture=no``, 实际测试也不是必须

日志选项
==============

可以 ``pytest -h`` 查看帮助文档, logging 相关部分内容如下::

  logging:
  --log-level=LEVEL     level of messages to catch/display.
                        Not set by default, so it depends on the root/parent log handler's effective level, where it is "WARNING" by default.
  --log-format=LOG_FORMAT
                        log format as used by the logging module.
  --log-date-format=LOG_DATE_FORMAT
                        log date format as used by the logging module.
  --log-cli-level=LOG_CLI_LEVEL
                        cli logging level.
  --log-cli-format=LOG_CLI_FORMAT
                        log format as used by the logging module.
  --log-cli-date-format=LOG_CLI_DATE_FORMAT
                        log date format as used by the logging module.
  --log-file=LOG_FILE   path to a file when logging will be written to.
  --log-file-level=LOG_FILE_LEVEL
                        log file logging level.
  --log-file-format=LOG_FILE_FORMAT
                        log format as used by the logging module.
  --log-file-date-format=LOG_FILE_DATE_FORMAT
                        log date format as used by the logging module.
  --log-auto-indent=LOG_AUTO_INDENT
                        Auto-indent multiline messages passed to the logging module. Accepts true|on, false|off or an integer.

有三种使用方式:

A::

  pytest test_xxx.py --log-cli-level=info

B, 编辑pytest.ini或tox.ini或setup.cfg文件::

  [pytest]
  log_cli = 1
  log_cli_level = INFO
  log_cli_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
  log_cli_date_format=%Y-%m-%d %H:%M:%S

C, 用pytest -o方式重写(pytest 3.4之后)::

  pytest test_xxx.py -o log_cli=true -o log_cli_level=INF

警告相关::

  pytest-warnings:
  -W PYTHONWARNINGS, --pythonwarnings=PYTHONWARNINGS
                        Set which warnings to report, see -W option of Python itself
  --maxfail=num         Exit after first num failures or errors
  --strict-config       Any warnings encountered while parsing the `pytest` section of the configuration file raise errors
  --strict-markers      Markers not registered in the `markers` section of the configuration file raise errors
  --strict              (Deprecated) alias to --strict-markers
  -c file               Load configuration from `file` instead of trying to locate one of the implicit configuration files
  --continue-on-collection-errors
                        Force test execution even if collection errors occur
  --rootdir=ROOTDIR     Define root directory for tests. Can be relative path: 'root_dir', './root_dir', 'root_dir/another_dir/'; absolute path:
                        '/home/user/root_dir'; path with variables: '$HOME/root_dir'.

使用pytest.ini文件
============================

使用 **pytest.ini** 文件配置测试用例

文件一般建立在项目根目录下. 也不是强制性, 在哪个目录下执行 pytest 命令,
就在哪个目录下寻找 **pytest.ini** , 不支持放在子目录下(除非去子目录跑测试)

一般配置模版:

  [pytest]
  # 然后写配置项

支持的配置选项(部分):

- addopts, 额外命令行选项, 可以更改默认命令行选项, 即在命令行补充参数, 如果有一样的选项, 尽量合并(看效果是)
- testpaths, 执行用例的目录
- python_file, 执行文件名
- python_classes, 执行的类名
- python_functions, 执行方法名
- usefixtures, 指定使用哪些固件.
- cache_dir, 缓存目录
- log_level, 日志等级, 默认是 --log-level 的 warring
- log_format, 日志格式
- log_file_date_format, 日志日期格式
- log_auto_indent, 日志缩进
- pythonpath, 将路径加入到 sys.path
- minversion, pytest最低版本
- required_plugins, 需要加载的插件

支持的环境变量
============================

environment variables:

- PYTEST_ADDOPTS,   额外命令行选项
- PYTEST_PLUGINS,   启动时加载的插件, 多个使用逗号分隔
- PYTEST_DISABLE_PLUGIN_AUTOLOAD,   设置不加载的插件
- PYTEST_DEBUG,     调试相关, set to enable debug tracing of pytest's internals

自定义mark装饰器
============================

比如::

  @pytest.mark.mytest

直接使用这种自定义的mark表示, 会有警告::

  pytest.unknown_mark_warning

.. note::

  使用 pycharm测试时, 会自动加上 -q 等参数, 所以看不到警告, 暂时没找到怎么覆盖这些配置,
  只有手动跑才能看到了

但是实际是自己有使用的, 这个时候需要将这个配置项添加到pytest.ini文件::

  [pytest]
  markers =
    mytest: 表示一个自定义mark标记

格式为自定义表示的名称name, 与含义说明.

若不方便配置ini文件, 可以在conftest.py中手动使用config写入::

  # conftest.py
  # coding: utf-8
  from _pytest.config import Config

  def pytest_configure(config: Config):
      config.addinivalue_line(
          'markers',
          'mytest1: mark_mytest1',
      )

第一个参数就是上面说的name, 第二个参数就是描述,

.. note::

  像这种在代码中补充配置的, 必须在插件的注册阶段使用, 所以
  必使用pytest_configure定义在conftest.py,
  无法写在具体的固件@fixture中, 即使fixture定义在conftest.

一些其他指令
============================

查看所有预定义固件::

  pytest --fixtures

查看所有预定义标记::

  pytest --markers

一些使用技巧
============================

跳过所有测试用例
----------------------------

直接命令行设置::

  pytest -m ""

但是有时候不方便直接修改命令行, 还可以在 **pytest.ini** 设置::

  [pytest]
  addopts = -m ""

.. note::

  实际使用中发现, 在有些版本 ``-m ""`` 表示会执行所有的测试用例,
  而有些版本全都不会运行.

有时禁用所有测试会导致测试错误, 这时候也可使用 ``-k`` 指定一个耗时少的测试::

  -k "测试函数名/文件名"



实时打印日志
----------------------------

日志使用可参考: 日志选项_

还是使用 :doc:`/docs/后端/python/python标准库/logging` 模块. 与平时使用无差别,
测试时加启动参数 ``--capture=no`` 即可, 或者 ``-s`` 效果一致::

  _logger = logging.getLogger(__name__)

  _logger.setlevel(logging.INFO)
  _logger.info('xxx')

实际就是::

  pytest test_xxx.py --log-cli-level=info --capture=no
  pytest test_xxx.py --log-cli-level=info -s

打印乱码问题

在最高级别的conftest.py添加如下代码即可::

  def pytest_collection_modifyitems(items):
      """
      测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
      :return:
      """
      for item in items:
          item.name = item.name.encode("utf-8").decode("unicode_escape")
          item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

隐藏警告
----------------------------

可在 **pytest.ini** 文件中添加以下行来隐藏警告::

  addopts = -p no:warnings

这将禁用所有警告.

如果您只想隐藏特定的警告，可以使用filterwarnings选项。
例如，以下配置将忽略所有用户警告和与正则表达式匹配的特定弃用警告，但将所有其他警告转换为错误::

  filterwarnings = ignore::UserWarning regex:DeprecationWarning

其他后续补充...
============================

.. toctree::

  pytest/index


