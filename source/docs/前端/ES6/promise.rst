============================
Promise
============================

为什么要使用 Promise
============================

传统的异步请求如果存在多次处理, 那么结果就会是嵌套调用::

    const read_model = require('model');
    const _file = './name.txt'

    read_model.readFile(_file,'utf8',function(err,data){
        read_model.readFile(data, 'utf8',function(err,data){
            read_model.readFile(data,'utf8',function(err,data){
                console.log(data);
            });
        });
    });

使用 Promise 可以将其更改为链式调用::

    function read(filename) {
        return new Promise((resolve, reject) => {
            read_model.read_model(filename, 'utf-8', (err, data) => {
                if (err) {reject(err);}
                resolve(data);
            });
        });
    }

    read(_file).then((data) => {
        return read(data);
    }).then((data) => {
        return read(data);
    }).then((data) => {
        console.log(data);
    }, err => {
        console.log(err);
        }
    );

显著解决了异步编码风格问题, 嵌套调用的可读性维护性较差.

业界比较著名的实现 Promise 的类库有 bluebird、Q、ES6-Promise。

构造说明
============================

构造说明::

    new Promise((resolve, reject) => {})

- resolve 调用成功后执行, 如果是函数 resolve(success_data). 使用 value 保存成功状态的值.
- reject  调用失败后执行, 如果是函数 reject(err_msg). 使用 reason 保存失败状态的值.
- Promise 的状态不可逆，同时调用 resolve 函数和 reject 函数，默认会采取第一次调用的结果。
  promise 有三个状态：pending，fulfilled，or rejected. 默认状态是 pending;
  只能从pending到rejected, 或者从pending到fulfilled，状态一旦确认，就不会再改变;
- 调用 Promise , 会返回一个 Promise 对象
- promise 必须有一个then方法，then 接收两个参数，分别是 promise 成功的回调 onFulfilled,
  和 promise 失败的回调 onRejected.
  也可称为 thenable
- 如果调用 then 时，promise 已经成功，则执行onFulfilled，参数是promise的value；
- 如果调用 then 时，promise 已经失败，那么执行onRejected, 参数是promise的reason；
- 如果 then 中抛出了异常，那么就会把这个异常作为参数，传递给下一个 then 的失败的回调onRejected；


.. note::

    ``(resolve, reject) => {}`` 被称为 executor 函数

自定义 Promise , 实现需参考: `Promises/A+规范`_ :

.. literalinclude:: ../../../resources/code/promise.js
    :language: js

补充
============================

| Promise 表示一个异步操作的最终结果，与之进行交互的方式主要是 then 方法，
| 该方法注册了两个回调函数，用于接收 promise 的终值或本 promise 不能执行的原因。


.. _Promises/A+规范: <https://promisesaplus.com>`_

