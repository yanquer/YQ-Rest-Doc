==================================================================
结合electron时候的报错
==================================================================

报错 ``Module did not self-register: '.../node_modules/drivelist/build/Release/drivelist.node'.``
==============================================================================================================

参考: https://github.com/balena-io-modules/drivelist/issues/389#issuecomment-850784173

issues 上面看到的是:

- Install ``electron-rebuild``
- run ``cd ./node_modules/drivelist && ../.bin/electron-rebuild``
- rebuild

其实与下面的应该是一个问题(可能也要删除lib, 下次遇到再试试)



报错 ``Cannot find module '../build/Debug/pty.node'``
==================================================================

参考: https://github.com/Microsoft/node-pty/issues/256#issuecomment-454292439

解决::

    npm install --save-dev electron-rebuild

然后在 package.json 的 scripts 增加::

    "scripts": {
      "rebuild:node": "electron-rebuild -f -w node-pty"
    }

删除项目根目录下 `lib`(可不删除也行好像), 执行 ``npm run rebuild:node``
在重写编译一下, 比如我这里是 ``npm run prepare`` 即可::

  "scripts": {
    "prepare": "yarn run clean && yarn build && yarn run download:plugins",
    "clean": "theia clean",
    "build": "theia rebuild:electron && theia build --mode development",
    "rebuild": "theia rebuild:electron --cacheRoot ./.theia_build/cache && theia build --mode development",
    "start": "theia start --plugins=local-dir:plugins --remote-debugging-port=9222",
    "download:plugins": "theia download:plugins",
    "rebuild:node": "electron-rebuild -f -w node-pty"
  }
