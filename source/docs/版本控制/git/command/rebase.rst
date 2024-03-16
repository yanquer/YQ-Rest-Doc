=======================
rebase
=======================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


变基
-----------------------

目前来看变基有两个作用,

.. topic:: 一是合并多次commit:

	``git rebse -i HEAD~$n``

.. topic:: 二是改变当前分支基于某个分之的基础版本(不一定是master,看是从哪个分支新建分支)

	.. code-block:: sh
		:caption: 基于master的变基

		git checkout master && git pull
		git checkout test
		git rebase master


变基存在问题需要回滚
-----------------------

.. code-block:: sh

	git reflog		# 会显示所有节点 比如 HEAD@{0}

	# 选择上面有的节点 如 HEAD{3}, 回退到此节点所指向的commit, 也可以用 commit_id
	git reset --hard HEAD@{3}
