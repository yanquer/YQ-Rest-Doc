==============================
IDA-问题总结
==============================


.. post:: 2024-03-09 18:21:01
  :tags: 逆向工程
  :category: 安全
  :author: YanQue
  :location: CD
  :language: zh-cn


Mac下调试需要权限
==============================

Mac下一般使用默认的本地调试器, 由于权限问题无法启动

.. figure:: ../../../resources/images/2023-12-27-11-21-11.png
  :width: 480px

官方建议的解决方案是使用 **远程调试**

就是启动::

  /Applications/IDA\ Pro\ 7.5/idabin/dbgsrv/mac_server64

后在IDA Pro中选择 **Remote Mac OS X debugger**

参考: `<https://hex-rays.com/wp-content/static/tutorials/mac_debugger_primer2/mac_debugger_primer2.html>`_

但是这个要求IDA Pro, 个人免费版不支持remote debug...
