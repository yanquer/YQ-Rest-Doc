=======================
获取win下管理员权限
=======================


.. post:: 2023-02-20 22:06:49
  :tags: python, 相关技术实现
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn



判断是否有管理员权限::

  import ctypes
  'is admin' if ctypes.windll.shell32.IsUserAnAdmin() else 'not admin'

涉及到win API: `IsUserAnAdmin <https://learn.microsoft.com/zh-cn/windows/win32/api/shlobj_core/nf-shlobj_core-isuseranadmin>`_

获取管理员权限::

  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

参数解析::

  runas 表示以管理员权限执行
  sys.executable 表示打开的执行文件. 这里一般都在python内跑就是 python.exe (python的安装路径)
  __file__ 执行文件跟的参数

.. note::

  如果是python2, 那么 ``sys.executable``, ``__file__`` 都需要加上 unicode, 如 ``unicode(__file__)``

  ``sys.version_info[0] == 3`` 判断python版本是否是 3

涉及到win API: `shellExecuteW <https://learn.microsoft.com/zh-cn/windows/win32/api/shellapi/nf-shellapi-shellexecutew>`_

