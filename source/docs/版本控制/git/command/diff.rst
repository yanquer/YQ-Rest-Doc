=======================
diff
=======================

| 比较差异

git diff 命令比较文件的不同，即比较文件在暂存区和工作区的差异。

git diff 命令显示已写入暂存区和已经被修改但尚未写入暂存区文件的区别。

- 尚未缓存的改动：git diff
- 查看已缓存的改动： git diff --cached
- 查看已缓存的与未缓存的所有改动：git diff HEAD
- 显示摘要而非整个 diff：git diff --stat

显示暂存区和工作区的差异::

	$ git diff [file]

显示暂存区和上一次提交(commit)的差异::

	$ git diff --cached [file]

或::

	$ git diff --staged [file]

显示两次提交之间的差异::

	$ git diff [first-branch]...[second-branch]
