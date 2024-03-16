====================================
nteract
====================================


.. post:: 2024-03-12 19:49:08
  :tags: node, 三方库
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


安装::

  npm install -g nteract
  # yarn global add nteract

.. note::

  若想直接从源码启动::

    git clone https://github.com/nteract/nteract.git
    cd nteract
    yarn install
    yarn start

功能:
  一个比较高级点的node交互环境.
  与原生node的区别, 类似于 ipython 与 python

启动::

  nteract

也支持其他语言
====================================

可选安装Python kernel

Nteract原生支持JavaScript/Node.js,但可以通过额外的kernel packages添加Python等其他语言支持::

  pip install ipython
  pip install nteract-kernel



