============================
Object原型方法
============================


.. post:: 2023-02-26 21:30:12
  :tags: 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


对象拷贝-Object.assign()
============================

Object.assign()
  浅拷贝对象属性, 返回新的对象

如果需要深拷贝, 可以::

  JSON.parse(JSON.stringify(obj))

