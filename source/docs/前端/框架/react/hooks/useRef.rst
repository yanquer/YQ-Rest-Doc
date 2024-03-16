======================================
useRef
======================================


.. post:: 2024-03-08 23:31:08
  :tags: 框架, react, hooks
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


仅支持函数组件.

与 :doc:`/docs/前端/框架/react/hooks/createRef` 使用基本一致,
区别在于: **createRef 每次渲染都会返回一个新的引用，而 useRef 每次都会返回相同的引用。**

官方文档内容::

  useRef 返回一个可变的 ref 对象，其 .current 属性被初始化为传入的参数（initialValue）。返回的 ref 对象在组件的整个生命周期内保持不变。

换句话说, 在 **函数组件中** , 当触发重新渲染时,

- 使用 createRef 声明的变量, 会先销毁(变量重置为null), 然后再重新赋值 ( **在类组件中效果是正常的hook** )
- 使用 useRef 声明的变量, 第一次声明后就一直存在.
  useRef 适用于函数组件中需要在多次渲染之间保持引用的情况.

.. 区别例子



:参考::
  - `什么是 useRef , useRef 与 createRef 区别, 以及在什么情况下使用 useRef <https://cloud.tencent.com/developer/article/1586855>`_
  - `精读《useRef 与 createRef 的区别》 <https://zhuanlan.zhihu.com/p/110247813>`_
  - `useRef、createRef的区别及使用，及useRef妙用 <https://juejin.cn/post/6950845509137334309>`_


