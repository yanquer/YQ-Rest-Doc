=====================
gzip
=====================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


压缩/解压文件, 压缩包后缀名一般为.gz

语法::

  gzip [选项] 被压缩文件

常用选项：

-d      解压
-r      压缩所有子目录

.. note::

  tar的 -z选项就是调用的gzip压缩
