==============================
ES6 Generator 函数
==============================


.. post:: 2023-02-20 22:06:49
  :tags: ES6
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


ES6 新引入了 Generator 函数，可以通过 yield 关键字，把函数的执行流挂起，
为改变执行流程提供了可能，从而为异步编程提供解决方案

Generator 函数组成
==============================

Generator 有两个区分于普通函数的部分:

- 一是在 function 后面，函数名之前有个 `*`
- 函数内部有 yield 表达式

其中 `*` 用来表示函数为 Generator 函数，yield 用来定义函数内部的状态::

  function* func(){
    console.log("one");
    yield '1';
    console.log("two");
    yield '2';
    console.log("three");
    return '3';
  }

执行机制
==============================

调用 Generator 函数和调用普通函数一样，在函数名后面加上()即可，
但是 Generator 函数不会像普通函数一样立即执行，而是返回一个指向内部状态对象的指针，
所以要调用遍历器对象Iterator 的 next 方法，指针就会从函数头部或者上一次停下来的地方开始执行

函数返回的遍历器对象的方法
==============================

next 方法

一般情况下，next 方法不传入参数的时候，yield 表达式的返回值是 undefined .
当 next 传入参数的时候，该参数会作为上一步yield的返回值。

yield* 表达式

yield* 表达式表示 yield 返回一个遍历器对象，用于在 Generator 函数内部，调用另一个 Generator 函数。







