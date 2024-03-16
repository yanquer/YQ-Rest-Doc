====================
import与require
====================


.. post:: 2023-02-26 21:30:12
  :tags: 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


import与require 是前端导包使用的方式, 遵循两种不同的规范

- import
  - import/export 是ES6引入的新规范，因为浏览器引擎兼容问题，需要在node中用babel将ES6语法编译成ES5语法
  - import 是编译时调用，所以必须放在文件的开头
  - import 是解构过程。使用import导入模块的属性或者方法是引用传递。且import是read-only的，值是单向传递的。default是ES6 模块化所独有的关键字，export default {} 输出默认的接口对象，如果没有命名，则在import时可以自定义一个名称用来关联这个对象
- require
  - require/exports 是 CommonJS/AMD 中为了解决模块化语法而引入的
  - require 是运行时调用，所以理论上可以运作在代码的任何地方
  - require 是赋值过程，其实require的结果就是对象、数字、字符串、函数等，再把结果赋值给某个变量。它是普通的值拷贝传递。
  - 通过require引入基础数据类型时,属于复制该变量
  - 通过require引入复杂数据类型时, 属于浅拷贝该对象
  - 出现模块之间循环引用时, 会输出已执行的模块, 未执行模块不会输出
  - CommonJS规范默认export的是一个对象,即使导出的是基础数据类型


写法
====================

require/exports 方式的写法比较统一::

    // exports
    export.fs = fs
    module.exports = fs

    // require
    const module = require('module')


import/export 方式的写法就相对丰富些::

    // export
    export default fs;
    export const fs;
    export function part;
    export { part1, part2 };
    export * from 'fs';

    // import
    import fs  from 'fs';
    import { newFs as fs } from 'fs';  // ES6语法, 将fs重命名为newFs, 命名冲突时常用
    import { part } from fs;
    import fs, { part } from fs;


