======================
update-index
======================

用于更新Git索引或暂存区的内容。下面是一些常见用法:

--assume-unchanged <file>
  将指定文件标记为“已忽略”（assume unchanged），即在以后的提交中忽略该文件的修改
  ( **告诉Git不要重复扫描该文件的状态，因此如果文件被修改了，Git仍然会提交这些修改** )::

    git update-index --assume-unchanged <file>

--no-assume-unchanged <file>
  取消指定文件的“已忽略”标记，这样Git将会跟踪所做的修改::

    git update-index --no-assume-unchanged <file>

--skip-worktree <file>
  类似于“已忽略”, **完全忽略文件的修改，即使文件被修改，也不会提交到版本库** ::

    git update-index --skip-worktree <file>

--no-skip-worktree <file>
  取消指定文件的“已忽略”标记，这样Git将会跟踪所做的修改::

    git update-index --no-skip-worktree <file>

--add <file>
  将指定文件添加到Git索引或暂存区中(仅能添加至暂存区)::

    git update-index --add <file>

--remove <file>
  从Git索引或暂存区中删除指定文件::

    git update-index --remove <file>

--chmod=(+|-)x <file>
  将指定文件标记为可执行::

    git update-index --chmod=+x <file>

通过使用`git update-index`命令，可以灵活地管理Git索引或暂存区中的文件，以满足特定的需求。


--skip-worktree和--assume-unchanged区别
============================================

- 以下来源于 ChatGpt

--skip-worktree的使用示例
--------------------------------------------

假设我们有一个包含敏感信息的文件config.yml，我们将它添加到版本库中并提交了一个初始版本。
接下来，我们在本地修改了该文件，但不希望这些修改被提交到版本库中。

首先，我们需要将config.yml文件标记为“已忽略”，以便Git在以后的提交中忽略它的修改。执行以下命令::

  git update-index --skip-worktree config.yml

然后，我们可以继续修改config.yml文件，不必担心这些修改会被提交到版本库中。如果我们需要取消这个标记，可以使用如下命令::

  git update-index --no-skip-worktree config.yml

需要注意的是，这个标记只会在本地起作用，不会从版本库中删除文件，也不会阻止其他人在其本地进行修改。

--assume-unchanged的使用示例
--------------------------------------------

假设我们有一个较大的日志文件log.txt，每次执行`git status`或其他Git命令时都需要扫描这个文件，导致速度变慢。
如果我们确定对这个文件的更改不会对版本库产生影响，我们可以将它标记为“已忽略”，加快Git命令的执行速度。

首先，使用如下命令将log.txt文件标记为“已忽略”::

  git update-index --assume-unchanged log.txt

然后，我们可以继续修改log.txt文件，但这些修改不会出现在`git status`命令的输出中。

如果我们需要取消这个标记，可以使用如下命令::

  git update-index --no-assume-unchanged log.txt

需要注意的是，`git update-index --assume-unchanged`
只是告诉Git不要重复扫描该文件的状态，
因此如果文件被修改了，Git仍然会提交这些修改。如果需要完全忽略文件的修改，
应该使用`git update-index --skip-worktree`命令。

如果 **不想取消标记提交** :

需要手动将修改的内容添加到Git暂存区中::

  git add <file>

在执行git commit命令时，需要使用--no-post-rewrite选项来防止Git重写提交历史::

  git commit -m "commit message" --no-post-rewrite

如果其他人在其本地修改了该文件，并提交了更改，您在拉取更新时可能会遇到冲突。
因此，虽然可以不取消对该文件的“已忽略”标记并提交修改，但不推荐这样做，因为可能会引起一些问题。
如果您确定需要将文件的修改提交到版本库中，请按照上述步骤进行操作，并确保在提交之前备份您的代码。
