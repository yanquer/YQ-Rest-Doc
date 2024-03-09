=======================
logging
=======================

官网: `<https://docs.python.org/zh-cn/3/library/logging.html>`_

知乎有篇总结的貌似也可以: `<https://zhuanlan.zhihu.com/p/425678081>`_

算是内置的一个灵活的日志库

部分函数/模块使用说明
=======================

logging.basicConfig
-----------------------

最直接的使用是直接调用模块级别函数如::

  import logging
  logging.info('xxxx')

最简单的配置是使用 **logging.basicConfig** , 这会设置一个全局的日志配置, 如果多次调用, 以第一次的配置信息为准,
如设置日志::

    logging.basicConfig(filename='tmp_log.log', level=logging.DEBUG)

亦可设置日志格式::

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

.. _getLogger:

logging.getLogger
-----------------------

获取日志处理器

- 可传入一个字符串参数, 表示处理器名, 多次调用且使用同一个字符串时, 返回同一个handler
- 若不传入参数, 表示获取 root logger

logging.StreamHandler
-----------------------

**logging.StreamHandler()** 获取一个stream的handler, 可添加给上面 getLogger_ 获取到的 logger,
表示输出到控制台.

.. _FileHandler:

logging.FileHandler
-----------------------

.. function:: logging.FileHandler(filename='', mode='a')
  :noindex:

  获取一个文件handler, 表示将结果输出到文件

logging.Formatter
-----------------------

定义日志格式, 如::

  _formatter = \
  logging.Formatter('%(asctime)s - %{pathname}s[line:%{lineno}d] - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

设置好的 _formatter 可设置给handler(比如上面 FileHandler_ 的实例对象)

支持的格式字符串(部分):

- %(levelname)s: 日志级别(INFO、DEBUG、WARNING、ERROR等)
- %(filename)s: 发生日志记录的文件名称
- %(funcName)s: 发生日志记录的函数名称
- %(lineno)d: 发生日志记录的代码行数
- %(asctime)s: 日志记录的时间,默认格式为%Y-%m-%d %H:%M:%S
- %(message)s: 日志记录的消息正文
- %(name)s: Logger的名称
- %(threadName)s: 线程名称
- %(process)d: 进程ID
- %{pathname}s: 所执行程序所在路径, 绝对路径
- %(filename)s : 所执行程序所在路径, 相对路径

logging.handlers
-----------------------

logging.handlers模块提供了几种日志处理程序,用于处理日志记录。主要有以下几种:

- RotatingFileHandler:日志轮询处理,可以支持日志文件达到一定大小后自动切割为多个文件。
- TimedRotatingFileHandler:日志定期轮询,可以按时间切割日志文件。
- SMTPHandler:通过SMTP协议发送日志邮件。
- HTTPHandler:将日志记录发送到HTTP服务器。
- SocketHandler:将日志发送到网络套接字。
- QueueHandler: 将日志记录发送到队列,由其他进程从队列中获取日志记录进行处理。
- SysLogHandler:通过Syslog协议发送日志到syslog守护进程

RotatingFileHandler
+++++++++++++++++++++++

.. function:: logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False, errors=None)

  filename:
    设置日志文件名
  mode:
    设置日志文件的打开模式，默认为'a'（追加模式）
  maxBytes:
    设置每个日志文件的最大大小，单位是字节。当日志文件达到指定大小时，就会自动备份文件并创建新的日志文件
  backupCount:
    设置保留日志文件的数量。当日志文件达到指定数量时，就会循环覆盖最早的日志文件
  encoding:
    设置日志文件的编码格式
  delay:
    如果设置为True，则直到第一次使用handler来处理日志记录之前才会创建日志文件

如日志文件名为app.log, 最多10M, 保留最近5个日志文件::

  handler = RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5)

TimedRotatingFileHandler
++++++++++++++++++++++++++++++++++++++++++++++

.. function:: logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None, errors=None)
  :noindex:

  when 来指定 interval 的类型. 可能的值列表如下。 请注意它们不是大小写敏感的:

  .. csv-table::
    :header: 值, 间隔类型, 如果/如何使用 atTime

    'S',    秒,     忽略
    'M',    分钟,   忽略
    'H',    小时,   忽略
    'D',    天,     忽略
    'W0'-'W6',    工作日(0=星期一),                                           用于计算初始轮换时间
    'midnight',   如果未指定 atTime 则在午夜执行轮换，否则将使用 atTime。,    用于计算初始轮换时间

通过TimedRotatingFileHandler每天做日志文件轮询,实现日志文件按日切割的功能::

  import logging
  from logging.handlers import TimedRotatingFileHandler

  logger = logging.getLogger(__name__)
  logger.setLevel(logging.INFO)

  # 每天做日志轮询
  handler = TimedRotatingFileHandler('app.log', when='D', interval=1, backupCount=7)
  logger.addHandler(handler)

  logger.info('Start')

SMTPHandler
+++++++++++++++++++++++

通过SMTPHandler将日志发送邮件的方式进行处理::

  import logging
  from logging.handlers import SMTPHandler

  logger = logging.getLogger(__name__)
  logger.setLevel(logging.ERROR)

  # 通过SMTP发送日志邮件
  mail_handler = SMTPHandler(mailhost='smtp.gmail.com',
                            fromaddr='from@example.com',
                            toaddrs=['to@example.com'],
                            subject='Application Error',
                            credentials=credentials)
  logger.addHandler(mail_handler)

  logger.error('Error occurred')

日志级别
=======================

日志等级::

  critical > error > warning > info > debug

级别越高打印的越少.

- debug		: 打印 debug, info, warning, error, critical 级别的日志
- info 		: 打印 info, warning, error, critical 级别的日志
- warning 	: 打印 warning, error, critical 级别的日志
- error 	: 打印 error, critical 级别的日志
- critical 	: 打印 critical 级别

.. note::

  默认只打印大于等于warning级别的日志

自定义配置(可选)
=======================

logging标准模块支持三种配置方式:

- dictConfig
  dictConfig 是通过一个字典进行配置 Logger，Handler，Filter，Formatter；
- fileConfig
  fileConfig 则是通过一个文件进行配置；
- listen
  listen 则监听一个网络端口，通过接收网络数据来进行配置。

除此之外, 也可以直接调用 Logger，Handler 等对象中的方法在代码中来显式配置, 如::

  import logging
  _logger = logging.getLogger(__name__)

  # 之后调用跟普通调用一样
  _logger.info('info msg')

说明: logger只是一个日志器, 真正处理的的handler, 然后handler可以设置 Filter 和 Formatter

:参考:: https://zhuanlan.zhihu.com/p/425678081


将单独的logger记录到日志文件
==============================================

无论对 logging.getLogger('someLogger') 进行多少次调用，都会返回同一个 logger 对象的引用。
不仅在同一个模块内如此，只要是在同一个 Python 解释器进程中，跨模块调用也是一样。

同样是引用同一个对象，应用程序也可以在一个模块中定义和配置一个父 logger，
而在另一个单独的模块中创建（但不配置）子 logger，对于子 logger 的所有调用都会传给父 logger。


比如在一个单独的logger下添加到其他位置:

定义一个普通logger::

  logger = logging.getLogger(__name__)
  logger.setLevel(logging.DEBUG)

定义一个文件处理logger::

  logger_file_handler = logging.FileHandler('log_test.log')
  logger_file_handler.setLevel(logging.DEBUG)

定义一个流handler的logger::

  logger_stream_handler = StreamHandler()
  logger_stream_handler.setLevel(logging.INFO)

可以先设置一下格式::

  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  logger_file_handler.setFormatter(formatter)
  logger_stream_handler.setFormatter(formatter)

将文件和流的logger作为子logger加入到最开始的普通logger::

  logger.addHandler(logger_file_handler)
  logger.addHandler(logger_stream_handler)

:详细见::
  `logging --- Python 的日志记录工具 <https://docs.python.org/zh-cn/3/library/logging.html>`_
  `日志操作手册 <https://docs.python.org/zh-cn/3/howto/logging-cookbook.html#logging-cookbook>`_

日志没输出到控制台
==============================================

从两个方面看:

- 设置日志输出级别
- 设置流式输出(即控制台输出)的handler

例::

  # 获取处理器
  _logger = logging.getLogger(__name__)

  # 实例 stream handler
  _console_handler = logging.StreamHandler()

  # 给处理器增加handler
  _logger.addHandler(_console_handler)

  # 设置日志级别
  _logger.setLevel(logging.INFO)



