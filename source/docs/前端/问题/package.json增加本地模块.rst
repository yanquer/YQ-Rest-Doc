===================================
package.json增加本地模块
===================================


.. post:: 2023-02-26 21:30:12
  :tags: 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


方案一: 直接添加本地路径
===================================

如果不介意不使用语意化版本, 可以直接::

  yarn add link:./src/@ide/right-context-menu -W

或者::

  yarn add file:./src/@ide/right-context-menu -W

两个效果基本一致, `-W` 强制指定给根的package.json添加,

效果大概如下::

  "dependencies": {
    "@ide/right-context-menu": "link:./src/@ide/right-context-menu"
  }

或者::

  "dependencies": {
    "@ide/right-context-menu": "file:./src/@ide/right-context-menu"
  }

方案二: 使用语意化版本(这个不行, 看下一个)
======================================================================

但是如果想使用语意化版本, 如::

  "dependencies": {
    "@ide/right-context-menu": "0.1.0"
  }

.. 除了手动在 `package.json` 增加上述语意化版本配置外, 还需要在 `tsconfig.json` 增加路径配置:\:

..   "paths": {
..     //      "*": ["src/*"]
..     "@ide/hello-world-extension": ["src/@ide/right-context-menu"]
..   },

.. 然后:\:

..   yarn install

.. 即可

需要先在 `package.json` 增加上述语意化版本配置, 然后再链接::

  yarn add link:./src/@ide/right-context-menu -W

方案三: 使用语意化版本的另一种方式(问的AI)
======================================================================

如果要通过 yarn 来安装本地模块并生成语义化版本,可以这样操作:

- 在本地模块中定义版本号,例如在 `package.json` 中设置 "version": "1.0.0"
- 在主项目中,使用 yarn link 来链接本地模块:
  先注册本地模块, 在本地模块中执行::

    cd 本地模块所在路径
    yarn link

  然后返回项目根目录, 在主项目中执行::

    yarn link 模块名

- 这时可以在主项目中直接引用和使用本地模块了
- 通过 yarn add 保存依赖时,会自动读取到本地模块的版本号,
  并写入主项目的 package.json::

    yarn add 模块名

  package.json 中将会显示::

    "dependencies": {
      "模块名": "1.0.0"
    }

  .. note::

    有时候会有问题, add的时候还是从仓库去找, 而不是直接用本地的...

    所以这时候还是得手动加到package.json里面去...
    不记得之前是不是有手动加了...

这样就可以通过 yarn 实现在主项目中以语义化版本的方式安装和依赖本地模块。
主要利用了 yarn link 来关联本地模块,并通过 yarn add 来写入正确的依赖版本号。
同时要注意,本地模块的代码改动还会直接影响到主项目,要控制版本并发布,还需要采取额外的措施。 （已编辑）

本地模块的编译
===================================

默认情况下, yarn/npm只会处理主项目的构建等

比如本地模块如果是ts,
最笨的办法就是直接去模块目录手动执行 `tsc`

有一个叫 `lerna` 的模块, 可以递归编译, 从而达到编译所有本地模块的效果,
使用::

  lerna init
  lerna run build

编译报错-node_model的报错
-------------------------------------

如果构建的时候, 发现编译的确实是本地模块, 但是因为导包, 从而出现了
`node_modules` 下面模块的检查报错, 可以在 `tsconfig.json` 配置(根项目)::

  {
    "compilerOptions": {
      "skipLibCheck": true
    }
  }

或者配置 `learn.json` ::

  "command": {
    "build": {
      "typescript": {
        "tsConfigOverride": {
          "skipLibCheck": true
        }
      }
    }
  }

也可以直接命令行::

  tsc --skipLibCheck

.. note::

  想不通的一点是 tsc 没有报错, 但是learn触发的有这个报错;


编译问题-会在根目录拷贝一份源码到配置的outDir
--------------------------------------------------------------------------

解决: 去除根 `tscofig.json` 的以下内容::

  "compilerOptions": {
      "rootDir": "src",
      "outDir": "lib",
  }

  "include": [
      "src"
  ],

注释掉即可











