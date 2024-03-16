=======================
reset
=======================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


| 回退到某一个版本

reset直接回退, 丢失指定版本后的所有修改（直接修改HEAD指向）


.. code-block:: sh

  # 先查找需要回退的版本号, 然后指定版本号reset即可
  git log
  git reset --hard $version_num
  git push -f

参数选项

- --hard
  - 移动本地库HEAD指针
  - 重置暂存区
  - 重置工作区
- --mixed
  - 移动本地库HEAD指针
  - 重置暂存区
- --soft
  - 仅仅移动本地库HEAD指针


.. note::

  ps: Jb系列编辑器, 如 Pycharm Idea 右键 git 下有个 rollback 按钮, 实际触发的就是::

    git reset --hard HEAD^

  表示回退至最近一个版本.

reset还原单文件
=======================

如果使用git reset 命令回退某个文件，那么它只能暂存区被恢复。 所以还需要手动restore一下文件::

  git reset HEAD -- example.py
  git restore example.py

如果过程中查看状态会发现 reset 的时候就已经被自动add了, 所以restore后不需要手动add相关部分.


