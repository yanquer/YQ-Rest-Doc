===============================
ts源码调试
===============================

例如在 `WebStrome` 工具,

需要在 `tsconfig.json` 设置 `sourceMap` 为 `true`

`sourceMap` 选项用于控制 `TypeScript` 编译时是否生成源码映射文件(.map 文件)

sourceMap 的作用主要有:

1. 源码调试 - sourceMap 提供了映射关系,可以在浏览器的调试工具中直接调试 TypeScript 源代码,而不是编译后的 JavaScript 代码。
2. 错误定位 - 通过 sourceMap 定位到 TypeScript 源码中的错误位置,而不是编译后的 JavaScript 中的位置。
3. 源码映射 - 在浏览器中可以映射回原始的 TypeScript 源码,方便调试分析。
4. 源码压缩 - 即使 JavaScript 代码被压缩/合并/精简过,也可以使用 sourceMap 映射回原始代码。
5. 更好的可读性 - 源码映射使得编译后的代码可读性更高。
6. 代码转换跟踪 - sourceMap 记录了代码转换的整个过程,可以看到代码转换前后的对应关系

.. note::

  这只是一个参考, 并不是开启了一定可以用

