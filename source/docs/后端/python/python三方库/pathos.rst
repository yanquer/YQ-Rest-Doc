==============
pathos
==============


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


:github地址::
  `pathos-github <https://github.com/uqfoundation/pathos>`_

:官方文档::
  `pathos-doc <https://pathos.readthedocs.io/en/latest/>`_

:官网下载文档(pdf)::
  :download:`pythos-pdf <../../../../resources/pdf/1202.1056.pdf>`

github开头就说提供一个并行的图形化管理... 没看懂...

下有用模块:

- dill: serialize all of Python
- pox: utilities for filesystem exploration and automated builds
- klepto: persistent caching to memory, disk, or database
- multiprocess: better multiprocessing and multithreading in Python
- ppft: distributed and parallel Python
- pyina: MPI parallel map and cluster scheduling
- pathos: graph management and execution in heterogeneous computing


有用的方法/类

- pathos.abstract_launcher [worker pool API 定义]
- pathos.pools [所有 pathos worker pools]
- pathos.core [高级命令接口]
- pathos.hosts [hostname 注册接口]
- pathos.serial.SerialPool [python 串行 worker pool]
- pathos.parallel.ParallelPool [python 并行 worker pool]
- pathos.multiprocessing.ProcessPool [the multiprocessing worker pool]
- pathos.threading.ThreadPool [the multithreading worker pool]
- pathos.connection.Pipe [the launcher base class]
- pathos.secure.Pipe [the secure launcher base class]
- pathos.secure.Copier [the secure copier base class]
- pathos.secure.Tunnel [the secure tunnel base class]
- pathos.selector.Selector [the selector base class]
- pathos.server.Server [the server base class]
- pathos.profile [profiling in threads and processes]
- pathos.maps [standalone map instances]

同时提供了两个命令, 支持便捷建立安全连接, 脚本已安装到环境变量下, 所以直接命令调用即可.

- portpicker [get the portnumber of an open port]
- pathos_connect [establish tunnel and/or RPC server]

使用 ``--help`` 获取帮助信息.

