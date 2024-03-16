============================
test
============================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


判断

跟shell的if语句差不多::

  -nt    newer than    判断 file1 是否比 file2 新
  -ot    older than    判断 file1 是否比 file2 旧
  -ef    判断 file1 和 file2 是否为同一文件，可用在判断 hard link 的判定。即，判定两个文件是否指向同一个 inode

如::

  test file -nt file2

