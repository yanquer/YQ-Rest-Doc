===========================
React使用
===========================


.. post:: 2023-03-01 00:19:35
  :tags: 框架, amis, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


除了用json, 在 React 环境下使用 amis，还可以直接引入 amis 内置组件，
在 amis 项目源码 src/components 下的组件都是标准 React 组件，
可以在项目中直接引用，这样就能将 amis 当成纯粹 UI 库来使用::

  import {Button} from 'amis-ui';

  ...

  <Button
    onClick={() => {}}
    type="button"
    level="link"
    className="navbar-btn"
  >
    按钮
  </Button>


