=======================
merge
=======================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


合并代码

合并其他分支到当前所在分支::

	git merge $branch_name

合并时, 若有冲突需要手动处理, 处理好后使用continue选项::

	git merge --continue

若在过程中不想合并, 放弃此次合并, 回到合并前的状态::

	git merge --abort

.. note::

	像 merge, rebase 等都可以使用 continue 与 abort

其他选项
=======================

--ff			fast-forward模式, 不会创造一个新的commit节点. 默认使用此模式
--no-ff			即使可以使用fast-forward模式，也要创建一个新的合并节点。这是当git merge在合并一个tag时的默认行为。
--ff-only		除非当前HEAD节点已经up-to-date（更新指向到最新节点）或者能够使用fast-forward模式进行合并，否则的话将拒绝合并，并返回一个失败状态
--commit 		合并后自动调用git commit, 可以覆盖--no-commit
--no-commit 	合并后, 不自动commit
-m <msg>		合并时候的说明信息
--edit, -e		合并后弹出编辑器来编辑合并信息, 可在 -m 的基础上继续编辑
--no-edit		用于接受自动合并的信息（通常情况下并不鼓励这样做）
--log=<n> 		将在合并提交时，除了含有分支名以外，还将含有最多n个被合并commit节点的日志信息, 这里没大懂
--no-log		并不会列出该信息
--stat			在合并结果的末端显示文件差异的状态。文件差异的状态也可以在git配置文件中的merge.stat配置。
-n, --no-stat	不会显示文件差异的状态
--squash 		当一个合并发生时，从当前分支和对方分支的共同祖先节点之后的对方分支节点，一直到对方分支的顶部节点将会压缩在一起, 与 --no-ff 冲突
--verify-signatures 	用于验证被合并的节点是否带有GPG签名，并在合并中忽略那些不带有GPG签名验证的节点
--no-verify-signatures 	不验证GPG签名

:此处参考::
	`git-merge完全解析 <https://www.jianshu.com/p/58a166f24c81>`_



