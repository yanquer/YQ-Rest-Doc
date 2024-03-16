==========================
tsc
==========================


.. post:: 2023-02-20 22:06:49
  :tags: typescript
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. note::

  考虑过是不是直接放在linux指令下面,
  想了下只是TypeScript适用, 罢手

编译ts文件为js文件, 支持同时多个文件

安装::

  npm install typescript -g

选项/参数

--help
  显示帮助信息
--module
  载入扩展模块
--target
  设置 ECMA 版本
--declaration
  额外生成一个 .d.ts 扩展名的文件

  如生成 ts-hw.d.ts、ts-hw.js 两个文件::

    tsc ts-hw.ts --declaration

--removeComments
  删除文件的注释
--out
  编译多个文件并合并到一个输出的文件
--sourcemap
  生成一个 sourcemap (.map) 文件.
  sourcemap 是一个存储源代码与编译代码对应位置映射的信息文件
--module noImplicitAny
  在表达式和声明上有隐含的 any 类型时报错
--watch
  在监视模式下运行编译器。会监视输出文件，在它们改变时重新编译。

tsconfig.json配置
==========================

strictPropertyInitialization
  严格检查类属性是否有初始值

  不知道是否是更新了ts版本的缘故, 使用依赖注入框架时候, 如果
  没给初始值, 会误报, tsconfig中配置此属性值为false, 来不进行这种检查.


