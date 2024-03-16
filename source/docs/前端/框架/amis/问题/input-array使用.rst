
===========================
input-array使用
===========================

.. post:: 2023-03-01 00:19:35
  :tags: 框架, amis, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn

必须有 `item` , 组件才知道怎么渲染::

  {
    type: 'input-array',
    items: {
        type: 'input-text'
    }
  }

如果是多个项作为一个组, 那么需要使用 `combo`::

  {
    type: 'input-array',
    items: {
          type: 'combo',
          controls: [
              {
                  type: 'input-text',
                  name: 'va',
                  label: 'va',
              },
              {
                  type: 'input-text',
                  name: 'vb',
                  label: 'vb',
              }
          ]
      }
  }

这时数据的定义::

  eaa: [
      {va: 1, vb: 11},
  ]

.. note::

  如果在 `input-array` 内部定义了子组件, 那么在这里面得
  `componentId`, `componentName`  可能只能调用到内部的组件,
  如果是外部组件多半就是找不到组件

列表长度交互
---------------------------

当列表数据大于等于1时, 禁止新增::

  {
    type: 'input-array',
    name: 'array1',
    label: '长度: ${COUNT(array1)}',
    addableOn: '${COUNT(array1) < 1}',
    items: {...}
  }

.. note::

  不知道为什么, 官网文档没有提到可以用 addableOn, 只写了 addable
