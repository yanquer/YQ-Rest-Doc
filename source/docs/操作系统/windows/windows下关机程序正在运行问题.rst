=====================================
windows下关机程序正在运行问题
=====================================


.. post:: 2023-02-20 22:06:49
  :tags: windows
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


一般情况下直接不管就行，

我的问题是，发现有一个名叫 ``t`` 的程序但是我没执行过，于是就去任务管理器里找，一直没找到到。

``tasklist`` 也找了没有。

于是研究了一下， 发现这个提示的名称并不是进程名， 而是进程打开窗口的那个进程的 ``title``

这里感谢知友的这篇帖子： `Windows关机提示“这个应用阻止关机”，怎样确认是什么程序？？ <https://www.zhihu.com/question/376846935/answer/1971729138>`_

需要查看软件标题的话就需要工具了，比如： `nirsoft的GUIPropView <https://www.nirsoft.net/utils/gui_prop_view.html>`_

下载地址： `GUIPropView <https://www.nirsoft.net/utils/guipropview-x64.zip>`_

下载后解压点击title排序即可
