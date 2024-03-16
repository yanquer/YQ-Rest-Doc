========================
submodule
========================


.. post:: 2023-02-26 21:30:12
  :tags: git, command
  :category: 版本控制
  :author: YanQue
  :location: CD
  :language: zh-cn



使用
========================

git submodule add $remote_git_addr $local_dir	添加子模块到本地的目录

git submodule update --remote $local_dir 更新某一个子模块

git submodule foreach 'git pull origin master' 更新多个子模块

git submodule update --init --recursive	初始化递归下载子模块（使用已有的最新commit id，建议使用）

git submodule update --remote --recursive 递归更新所有子模块（强制用master覆盖子模块，除非使用master，否则使用上一个好点）

注意： 时刻关注子模块的版本号， 提交时容易误修改此部分

补充： submodule只能是先在子模块提交代码，然后去主工程提交commit_id

注意： 默认使用 git submodule检出的是一个临时的分支（非master以及其他），所以要在主工程所在目录进去修改，需要先切换submodule到正常分支才可；
	同时，对于主工程而言，唯一识别子模块方式为commit id，而非branch，所以需要切换子模块的分支时，直接在子模块切换后，再返回主工程提交新的子模块commit id即可


删除
========================

删除子模块目录及源码::

	rm -rf 子模块目录

删除项目目录下.gitmodules文件中子模块相关条目::

	vim .gitmodules

删除配置项中子模块相关条目::

	vim .git/config

删除模块下的子模块目录，每个子模块对应一个目录，注意只删除对应的子模块目录即可

	rm .git/modules/子模块名

还原暂存区的添加(如果是刚添加的submodule)::

	git restore --staged .


