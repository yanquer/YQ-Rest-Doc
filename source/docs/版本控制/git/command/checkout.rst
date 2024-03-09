=======================
checkout
=======================

``git checkout $branch_name``			切换分支

``git checkout -b $new_branch_name``	新建分支并切换

-b <new_branch>
  新建并切换到新的分支new_branch
--theirs <fileName>
  检出另外分支的指定文件
--ours  <fileName>
  检出自己分支的指定文件

--ours和theirs一般是用于解决冲突时候使用的,
可以注意到有冲突时, 冲突部分会被箭头加多等号包裹,
中间以多等号隔开,
这个时候 **ours就是多等号上面的部分** ,
**theirs就是多等号下面的部分**.

eg::

  git checkout --ours <fileName>



