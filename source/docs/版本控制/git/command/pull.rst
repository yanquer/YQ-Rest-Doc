=======================
pull
=======================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


从远程拉取并更新本地, 相当于::

	git fetch && git merge

.. note::

	记得Windows下安装git的时候会让选择pull时是选择merge还是rebase, 默认是merge.

	若后续需要以rebase的形式pull, 可以::

		git pull --rebase

	或者(等价的)::

		git fetch && git rebase

如拉取master::

	# 拉取
	git fetch origin master
	# 合并
	git merge FETCH_HEAD

	# 相当于
	# git pull origin master:master
	# git pull origin master
