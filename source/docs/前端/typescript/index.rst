=============================
TypeScript
=============================

TypeScript 微软开发, 自由、开源的编程语言; 是 JavaScript 的一个超集

TypeScript 是 JavaScript 的超集，扩展了 JavaScript 的语法，
因此现有的 JavaScript 代码可与 TypeScript 一起工作无需任何修改，TypeScript 通过类型注解提供编译时的静态类型检查。
TypeScript 可处理已有的 JavaScript 代码，并只对其中的 TypeScript 代码进行编译。

执行方式:

- 方法1: 先用 `tsc` 编译为js, 然后执行
- 方法2: 使用 `ts-node` 直接执行ts文件(需要安装typescript ts-node @types/node tslib库)

语法

.. toctree::

  基础语法
  基础类型
  函数
  问号与叹号
  ts源码调试

相关指令

.. toctree::

  tsc

条件语句
=============================

- if [else [if ...]]
- switch...case

循环
=============================

普通的for,
eg::

  for ( init; condition; increment ){
      statement(s);
  }

for...in语句::

  for (var val in list) {
      //语句
  }

其他如for…of 、every 和 some 循环

while语句::

  while(condition)
  {
    statement(s);
  }

do...while::

  do
  {
    statement(s);
  }while( condition );

请注意，条件表达式出现在循环的尾部，所以循环中的 statement(s) 会在条件被测试之前至少执行一次

命令空间使用
=============================

命名空间的名称可以与类名一致,
但是

- 如果类是 export, 命名空间也要 export
- 类要先命名空间声明



