=======================
revert
=======================

| 反做某一个版本.

比如有版本1,  2,  3,  版本2存在问题, 需要撤销版本2, 保留版本3,  那么会重新生成一个符合要求的版本4.

适用于想撤销之前的某一版本, 但是又想保留该版本后面的版本.

.. code-block:: sh

	# 先找需要revert反做的版本
	git log
	git revert -n $version_num
	git commit -m 'xxx'
	git push
