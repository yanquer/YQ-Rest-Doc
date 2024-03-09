=========================
ES6
=========================

基本上参照 `菜鸟教程-ES6教程 <https://www.runoob.com/w3cnote/es6-tutorial.html>`_

ES6， 全称 ECMAScript 6.0 ，是 JavaScript 的下一个版本标准，2015.06 发版。
ES6 主要是为了解决 ES5 的先天不足，比如 JavaScript 里并没有类的概念，
但是目前浏览器的 JavaScript 是 ES5 版本，大多数高版本的浏览器也支持 ES6，不过只实现了 ES6 的部分特性和功能。

JavaScript 的正式名称是 ECMAScript

语法基础:

.. toctree::
  :maxdepth: 1

  基本数据类型
  变量声明
  Map与Set
  Reflect与Proxy
  字符串操作
  数值
  对象
  数组
  函数
  类
  模块
  Promise 对象
  promise
  Generator 函数
  async 函数

一些相关工具
=========================

Node.js
-------------------------

Node.js 是运行在服务端的 JavaScript，它对 ES6 的支持度更高

在 Node.js 环境中运行 ES6::

  $ node
  > let sitename="runoob"
  undefined
  > console.log(sitename)
  runoob
  undefined
  >

webpack
-------------------------

webpack 是一个现代 JavaScript 应用程序的静态模块打包器 (module bundler) .
当 webpack 处理应用程序时，它会递归地构建一个依赖关系图 (dependency graph) ,
其中包含应用程序需要的每个模块，然后将所有这些模块打包成一个或多个 bundle 。

webpack 主要有四个核心概念:

入口 (entry)
  入口会指示 webpack 应该使用哪个模块，来作为构建其内部依赖图的开始.
  进入入口起点后，webpack 会找出有哪些模块和库是入口起点（直接和间接）依赖的.
  在 webpack 中入口有多种方式来定义:

  - 单个入口（简写）
    语法::

      const config = {
        entry: "./src/main.js"
      }

  - 对象
    语法::

      const config = {
        app: "./src/main.js",
        vendors: "./src/vendors.js"
      }

输出 (output)
  output 属性会告诉 webpack 在哪里输出它创建的 bundles ，
  以及如何命名这些文件，默认值为 ./dist::

    const config = {
      entry: "./src/main.js",
      output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, 'dist')
      }
    }

loader
  loader 让 webpack 可以去处理那些非 JavaScript 文件（ webpack 自身只理解 JavaScript ）.
  loader 可以将所有类型的文件转换为 webpack 能够有效处理的模块，
  例如，开发的时候使用 ES6 ，通过 loader 将 ES6 的语法转为 ES5 ，如下配置::

    const config = {
      entry: "./src/main.js",
      output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, 'dist')
      },
      module: {
        rules: [
          {
              test: /\.js$/,
              exclude: /node_modules/,
              loader: "babel-loader",
              options: [
                presets: ["env"]
              ]
          }
        ]
      }
    }

插件 (plugins)
  loader 被用于转换某些类型的模块，而插件则可以做更多的事情.
  包括打包优化、压缩、定义环境变量等等.
  插件的功能强大，是 webpack 扩展非常重要的利器，可以用来处理各种各样的任务.
  使用只需要 require() ，然后添加到 plugins 数组中::

    // 通过 npm 安装
    const HtmlWebpackPlugin = require('html-webpack-plugin');
    // 用于访问内置插件
    const webpack = require('webpack');

    const config = {
      module: {
        rules: [
          {
              test: /\.js$/,
              exclude: /node_modules/,
              loader: "babel-loader"
          }
        ]
      },
      plugins: [
        new HtmlWebpackPlugin({template: './src/index.html'})
      ]
    };

gulp
-------------------------

基于流的自动化构建工具




