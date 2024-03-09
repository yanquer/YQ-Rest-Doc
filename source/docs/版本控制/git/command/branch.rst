=======================
branch
=======================

默认查看本地所有分支

选项参数:


.. csv-table:: branch options
  :align: center
  :delim: :

  -a, --all:			list both remote-tracking and local branches
  -r, --remote:		查看远程所有分支
  -d, --delete:		delete fully merged branch
  -D:					delete branch (even if not merged)
  -m, --move:			move/rename a branch and its reflog
  -M:					move/rename a branch, even if target exists
  -c, --copy:			copy a branch and its reflog
  -C:					copy a branch, even if target exists
  -l, --list:			list branch names
  --show-current:		show current branch name
  --create-reflog:	create the branch's reflog
  --edit-description:	edit the description for the branch
  -f, --force:			force creation, move/rename, deletion
  --merged <commit>:		print only branches that are merged
  --no-merged <commit>:	print only branches that are not merged
  --column[=<style>]:		list branches in columns
  --sort <key>:			field name to sort on
  --points-at <object>:	print only branches of the object
  -i, --ignore-case:		sorting and filtering are case insensitive
  --recurse-submodules:	recurse through submodules
  --format <format>:		format to use for the output

