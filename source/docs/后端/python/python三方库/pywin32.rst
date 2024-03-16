=====================
pywin32
=====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


:pypi地址::
  `pywin32 <https://pypi.org/project/pywin32/>`_

安装::

  python -m pip install --upgrade pywin32

这下面包含的包有点多, 都是针对与windows的. 其他平台无法安装

- Win32gui: Windows图形界面接口模块。主要负责操作窗口切换以及窗口中元素id标签的获取
- Win32api: Windows开发接口模块。主要负责模拟键盘和鼠标操作,对win32gui获取的标签进行点击/获取值/修改值等操作
- Win32con: 全面的库函数，提供Win32gui和Win32api需要的操作参数
- win32event: 提供 互斥锁, 信号相关 windows Api . 参见: `github/wuxc/pywin32doc/win32event <https://github.com/wuxc/pywin32doc/blob/master/md/win32event.md>`_

win32event
=====================

CreateMutex
---------------------

.. function:: CreateMutex(MutexAttributes, InitialOwner, Name)

  创建信号量, 支持windows下的跨进程(主要依赖于 Name)

  **参数**

  MutexAttributes:
    对象描述符指针, 默认None
  InitialOwner: bool
    初始所有权标志.

    如果此值为 TRUE ，并且调用方创建了互斥体，则调用线程获取互斥体对象的初始所有权。
    否则，调用线程不会获取互斥体的所有权。
  Name: str
    互斥量命名, 可在其他进程中获取

  **返回**

  如果函数成功，则返回值是新创建的互斥体对象的句柄。

  如果函数失败，则返回值为 NULL。

  如果互斥体是命名互斥体，并且此函数调用之前存在对象，则返回值是现有对象的句柄， 并且 GetLastError 函数返回 ERROR_ALREADY_EXISTS。

可参见: `microsoft-createmutexa <https://learn.microsoft.com/zh-cn/windows/win32/api/synchapi/nf-synchapi-createmutexa>`_

ReleaseMutex
---------------------

释放互斥体



