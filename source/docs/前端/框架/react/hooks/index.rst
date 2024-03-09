============================
hooks
============================

钩子函数?

主要是为了状态逻辑的复用

最常见的内置两种

- useState
- useEffect

.. note::

  貌似严格来说, 只有函数才算Hooks

函数组件拥有

.. toctree::
  :maxdepth: 1

  useState
  useEffect
  useRef
  forwardRef
  useImperativeHandle

类组件特有

.. toctree::
  :maxdepth: 1

  createRef

其他

.. toctree::
  :maxdepth: 1

  自定义Hook

Hook 的规则
============================

只在最顶层使用Hook:
  也就是不要在循环、条件或嵌套函数中调用Hook，这样可以做到各个hook 在每一次渲染中，调用的顺序是一致的.

  那为什么要保证 hook 调用顺序? 和React实现hook的原理有关, 每次渲染时，React把所有调用的 hook 用数组来储存.

只在React组件中才能调用:







