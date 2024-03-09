=======================
react直接执行ts
=======================

使用WebStrom创建的React的ts项目, 发现不需要手动tsc编译就可以直接运行::

  react-script start

创建时, 触发的实际指令::

  /usr/local/bin/npx --yes create-react-app . --template typescript

这里 `--yes ` 表示, 若有询问, 直接给 `yes`

后面研究了一下, 实际上是用了 `babel` 的 `@babel/preset-typescript`,
这个模块集成于 `babel` (>=7.0)内部, 在开发时, 可以在执行时候在内存中
将ts转换为js, 以实现类似ts直接执行的效果

见: `https://babeljs.io/docs/babel-preset-typescript`

.. note::

  可以看到项目目录下有个 `node_modules/.cache/babel-loader` 目录,
  相关缓存就是在这下面的.





