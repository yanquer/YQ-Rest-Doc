===============================
yarn install 出现node-gyp报错
===============================

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

