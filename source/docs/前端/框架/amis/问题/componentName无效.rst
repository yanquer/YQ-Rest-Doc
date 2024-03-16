===========================
componentName无效
===========================


.. post:: 2023-03-01 00:19:35
  :tags: 框架, amis, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


继续上一节 :doc:`/docs/前端/框架/amis/问题/combo无法指定更新某一个` ,
若当前项的 `name` 包含 ``.`` , 那么可能会把它做错数据来解析(链式调用),
导致 `componentName` 无法正确指向想要的属性.

所以, 控件 `name` 命名尽量不要使用 ``.``

