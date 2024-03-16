===================================
CSS排除指定的选择器
===================================


.. post:: 2023-02-26 21:30:12
  :tags: 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


可参考 :doc:``

现有css类属性a,b,c;

- a下包含b和c,
- b下包含c

如何写css选择器, 选择 a下的 不属于b 的c::

  .a .c:not(.b .c)


