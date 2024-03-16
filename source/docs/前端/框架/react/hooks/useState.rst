============================
useState
============================


.. post:: 2024-03-07 22:13:39
  :tags: 框架, react, hooks
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


为组件添加 State

例子::

  import React, { useState } from 'react';

  function Example() {
    // 声明一个state count
    const [count, setCount] = useState(0);

    // 使用count进行渲染，并绑定点击时间，使count+1
    return (
      <div>
        <p>You clicked {count} times</p>
        <button onClick={() => setCount(count + 1)}>
          Click me
        </button>
      </div>
    );
  }

.. note::

  当有多个state时，使用多个state变量，而不是一个,
  这样把无关逻辑分离，便于增删改state


