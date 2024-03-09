==========================
创建自己的IDE
==========================

其实跟着官方文档走就行了, 主要可能遇到的问题就是依赖包的问题,

可以直接按照官网文档给的来: `https://theia-ide.org/docs/composing_applications/` ,
复制文档最后一个 `package.json` 即可

不过这里的就过只是一个基于浏览器的版本,
如果想要使用 `Electron` 运行, 那么需要在依赖项中加入 `electron` 和 `@theia/electron`,
在 `theia` 项中加入目标为 `electron` 即可::

  "theia": {
    "target": "electron"
  }

还需要指定一下 `electron` 的main文件(启动文件)::

  "main": "lib/backend/electron-main.js",

如果是自定义的启动文件, 需要在自定义启动文件里手动 `require` 导入一下这个包.

.. sidebar::

  这里不需要手动去弄一个 `electron` 启动的js, 因为theia内部已经定义好了,
  只需要制定一下目标, 以及构建的时候也指定即可::

    theia rebuild:electron --cacheRoot ./.theia_build/cache

  这里加了 `cacheRoot` , 表示缓存目录, 下次再编的时候就会用这里的比对分析

最终的package.json内容大致如下::

  {
    "private": true,
    "name": "theia-ide",
    "main": "lib/backend/electron-main.js",
    "dependencies": {
      "@theia/callhierarchy": "latest",
      "@theia/electron": "^1.41.0",
      "@theia/file-search": "latest",
      "@theia/git": "latest",
      "@theia/markers": "latest",
      "@theia/messages": "latest",
      "@theia/navigator": "latest",
      "@theia/outline-view": "latest",
      "@theia/plugin-ext-vscode": "latest",
      "@theia/preferences": "latest",
      "@theia/preview": "latest",
      "@theia/search-in-workspace": "latest",
      "@theia/terminal": "latest",
      "@theia/vsx-registry": "latest",
      "electron": "^26.2.1"
    },
    "devDependencies": {
      "@theia/cli": "latest",
      "electron": "^26.2.1"
    },
    "scripts": {
      "prepare": "yarn run clean && yarn build && yarn run download:plugins",
      "clean": "theia clean",
      "build": "theia rebuild && theia build --mode development",
      "rebuild": "theia rebuild:electron --cacheRoot ./.theia_build/cache",
      "start": "theia start --plugins=local-dir:plugins",
      "download:plugins": "theia download:plugins"
    },
    "theia": {
      "target": "electron"
    },
    "theiaPluginsDir": "plugins",
    "theiaPlugins": {
      "vscode-builtin-extensions-pack": "https://open-vsx.org/api/eclipse-theia/builtin-extension-pack/1.50.1/file/eclipse-theia.builtin-extension-pack-1.50.1.vsix"
    },
    "theiaPluginsExcludeIds": [
      "ms-vscode.js-debug-companion",
      "vscode.extension-editing",
      "vscode.git",
      "vscode.git-ui",
      "vscode.github",
      "vscode.github-authentication",
      "vscode.microsoft-authentication"
    ]
  }

要启动的话, 直接 `yarn install` 然后 `yarn prepare` 编译构建下,
再 `yarn start` 启动即可, 注意解决这期间的报错等

如果需要ts, 在项目根手动创建 `tsconfig.json`, 内容大致如下, 按需修改::

  {
    "compilerOptions": {
      "baseUrl": ".",
      "emitDecoratorMetadata": true,
      "experimentalDecorators": true,
      "module": "commonjs",
      "moduleResolution": "node",
      "noImplicitAny": true,
      "paths": {
        //      "*": ["src/*"]
      },
      "removeComments": false,
      "sourceMap": true,
      "strict": true,
      "suppressImplicitAnyIndexErrors": true,
      "target": "esnext",
      "rootDir": "src",
      "outDir": "out",
      "jsx": "react"
    },
    "include": [
      "src"
    ],
    "exclude": [
      "node_modules"
    ]
  }

附: package.json 稍微完善一点的scripts::

  "scripts": {
    "build": "yarn -s compile && yarn -s bundle",
    "bundle": "yarn rebuild && theia build --mode development",
    "clean": "theia clean",
    "compile": "tsc -b",
    "lint": "theiaext lint",
    "rebuild": "theia rebuild:electron --cacheRoot ./.theia-build",
    "start": "theia start --plugins=local-dir:plugins",
    "start:debug": "yarn -s start --log-level=debug --remote-debugging-port=9222",
    "start:watch": "concurrently --kill-others -n tsc,bundle,run -c red,yellow,green \"tsc -b -w --preserveWatchOutput\" \"yarn -s watch:bundle\" \"yarn -s start\"",
    "test": "electron-mocha --timeout 60000 \"./lib/test/**/*.espec.js\"",
    "watch": "concurrently --kill-others -n tsc,bundle -c red,blue \"tsc -b -w --preserveWatchOutput\" \"yarn -s watch:bundle\"",
    "watch:bundle": "theia build --watch --mode development",
    "watch:compile": "tsc -b -w"
  }



