====================================
vscode项目的编译运行
====================================


.. post:: 2023-02-26 21:30:12
  :tags: 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


克隆项目::

  git clone https://github.com/microsoft/vscode.git

项目根目录下载插件, node模块::

  yarn

编译::

  yarn run compile

运行::

  bash scripts/code.sh

看了网上几年前的帖子说调试需要 ``yarn run watch`` 来debug, 但是之要watch了, 就跑不了code.sh,
后面发现, watch要等到跑完才行, 跑到::

  Finished compilation extensions xxx

更新
====================================

clone后下面默认有一个 `.vscode/launch.json` , 可以使用vscode来完美的断点调试(默认第一个就是)

webstorm 试了半天没搞懂怎么调断点. 参考了 `.vscode/launch.json` , 大致看了一下, 有些步骤没搞懂.

