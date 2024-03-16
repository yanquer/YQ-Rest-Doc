======================
async 函数
======================


.. post:: 2023-02-20 22:06:49
  :tags: ES6
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


async
======================

async 是 ES7 才有的与异步操作有关的关键字，和 Promise ， Generator 有很大关联的。

语法

.. function:: async function name([param[, param[, ... param]]]) { statements }

  name
    函数名称
  param
    要传递给函数的参数的名称
  statements
    函数体语句

返回值

async 函数返回一个 Promise 对象，可以使用 then 方法添加回调函数

await
======================

await 操作符用于等待一个 Promise 对象, 它只能在异步函数 async function 内部使用。

返回值

返回 Promise 对象的处理结果。如果等待的不是 Promise 对象，则返回该值本身。

await针对所跟不同表达式的处理方式：

- Promise 对象：await 会暂停执行，等待 Promise 对象 resolve，然后恢复 async 函数的执行并返回解析值。
- 非 Promise 对象：直接返回对应的值。
