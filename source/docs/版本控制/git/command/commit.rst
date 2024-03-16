=======================
commit
=======================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


--amend 				触发编辑器打开, 可修改最近一次的提交信息

修改最新一次提交作者信息::

	git commit --amend --author="Author Name <email@address.com>"

直接修改最近一次提交的注释信息::

	git commit --amend

