=======================
log
=======================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn


查看日志

查看fetch最新的日志更新信息::

	# git fetch 后会有一个 FETCH_HEAD 指针指向最新
	git log -p FETCH_HEAD
