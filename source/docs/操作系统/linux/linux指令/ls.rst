===============================
ls
===============================


.. post:: 2023-02-26 21:30:12
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


查看目录文件信息

-l
  详细信息
-t
  按时间排序
-i
  输出innode信息
--block-size
  --block-size=m 以M为单位 --block-size=G 以G为单位

`ls -l` 输出的第一个字符列表

.. csv-table:: 输出列含义
  :header: 字符, 说明

  -    ,普通文件
  d    ,目录
  l    ,符号链接
  c    ,字符设备节点
  b    ,块设备节点
  p    ,命名管道
  s    ,套接字



