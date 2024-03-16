===============================
yarn install 出现node-gyp报错
===============================


.. post:: 2024-03-08 23:31:08
  :tags: 框架, theia, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


报错内容大致如下::

  xxxx/node_module/nsfw: Command failed.
  Exit code: 1
  Command: node-gyp rebuild
  Arguments:

我用的是yarn, 试过直接::

  yarn global add node-gyp

失败

最终偶然发现::

  npm i -g node-gyp

解决了, 奇怪....

