========================
文件格式-toml
========================


.. post:: 2024-03-09 18:21:01
  :tags: 
  :category: 常用工具使用
  :author: YanQue
  :location: CD
  :language: zh-cn


一般都是这么写的::

  [data1]
  key1 = v1
  key2 = v2

相当于定义了一个名为data1的字典.

那如果key1的值是字典呢?
目前为止只知道一个可以 **单行** 字典定义::

  [data1]
  key1 = {name='bob', age=20}
  key2 = v2




