====================
reflog
====================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


| reflog(Reference logs), 参考日志

查看本地git变更历史, 方便回滚, 与 log 的 区别是

- log 是向父级提交递归寻找, reflog记录所有变更
- reflog仅保存在本地, 记录的变更包括了rebase, reset等

一般使用, 查看reflog历史::

	# 会看到有 HEAD@ 的记录
	git reflog

根据记录判断需要回滚的是哪一个HEAD(还可以通过git show查看某HEAD的提交日志辅助判断), 然后reset回滚::

	# 如果是 HEAD@{9}
	git reset --hard HEAD@{9}

