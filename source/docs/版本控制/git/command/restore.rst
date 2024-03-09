=======================
restore
=======================

| 撤销工作区修改

.. code-block:: sh

  # git restore 指令使得在工作空间但是不在暂存区的文件撤销更改(内容恢复到没修改之前的状态)
  # git restore --staged 的作用是将暂存区的文件从暂存区撤出, 但不会更改文件的内容
  git restore $dir_or_file


