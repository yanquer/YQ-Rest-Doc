====================
blame
====================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


用来追溯一个指定文件的历史修改记录,
能显示任何文件中每行最后一次修改的提交记录

用法::

  git blame filename

使用 -L 指定文件的行数范围::

  git blame -L n1,n2 filename

显示格式::

  commit ID  (代码提交作者  提交时间  代码位于文件中的行数)  实际代码




