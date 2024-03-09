=======================
tag
=======================

语法指令

创建tag::

  git tag -a tag-name(如v0.0.1)
                            # 增加一个tag, 下面的例子, 都以 v0.0.1 作为tag名
  git tag -a v0.0.1 cc16905
                            # 对某一提交的信息打tag标签，末尾是一个commit id
  git tag -a v0.0.1 -m "version 0.0.1, tag info"
                            # 创建tag带有说明信息
  git tag v0.0.1            # 创建轻量的标签tag(快速创建tag)
  git tag v0.0.2 be7a3e4    # 给提交的信息打tag，commit id为 be7a3e4

查看tag::

  git tag                   # 查看所有标签
  git show tag-name         # 查看指定的tag
  git show -s tag-name      # 查看指定的tag的hash值

推送到远程::

  git push origin v0.0.1    # 推送某一tag到远程仓库：

  git push origin --tags    # 一次推送多个标签
  git push --tags

删除标签::

  git tag -d v0.0.1

根据标签检出::

  git checkout v0.0.1

根据标签回退::

  # 先查看要回退的标签信息
  git show v0.0.1

  # 主干分支回退到某个版本(v0.0.1对应的前7为hash)
  git reset --hard cc16905

tag与commit区别

  - Git tag是一系列commit的中的一个点, 只能查看, 不能移动。branch是一系列串联的commit的线。
  - tag是静态的, branch是动态的, 要向前走。


tag分类

  - 轻量级: 仅为某个 commit 引用
  - 带附注: 存储在仓库中的独立对象, 包含有自身校验和信息等等 (常用)

创建tag

  ``git tag -a V0.1 -m 'release 0.1'``

tag选项参数

  - -a 	annotated, 一般都是版本号
  - -m 	备注信息
  - -d 	删除某一个tag
  - -v 	验证tag

用例:

  .. code-block:: sh

    # 创建一个 0.0.0 的tag, 这里只是测试, 一般建议 v0.0.0 作为标签名, v表示version, 0.0.0 表示语义化版本
    git tag -a 0.0.0 -m 'release 0.0.0, test some msg'

    # 查看有哪些tag
    git tag
    # 0.0.0

    # 查看某一个tag
    git show 0.0.0
    # tag 0.0.0
    # ... (就不贴出来了)

    # 推送
    git push origin --tags

    # 若需要删除
    git tag -d 0.0.0
    # 推一个空的上去覆盖掉, 达到删除目的
    git push origin :refs/tags/0.0.0

    # 其他删除方式
    # git push origin :0.0.0
    # 也可以这样
    # git push origin --delete tag 0.0.0

    # 获取指定tag
    git fetch origin tag 0.0.0


.. note::

  语义化版本规则

    版本格式：主版本号.次版本号.修订号, 版本号递增规则如下：

    - 主版本号：当你做了不兼容的 API 修改,
    - 次版本号：当你做了向下兼容的功能性新增,
    - 修订号：当你做了向下兼容的问题修正。

  一般都是从 0.1.0 开始
