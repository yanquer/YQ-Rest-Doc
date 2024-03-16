===========================
seq
===========================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


以指定增量从首数开始打印数字到尾数

-f, --format=格式        使用printf 样式的浮点格式
-s, --separator=字符串   使用指定字符串分隔数字（默认使用：\n）
-w, --equal-width        在列前添加0 使得宽度相同

#%后面指定数字的位数 默认是%g，%3g那么数字位数不足部分是空格::

  #seq -f"%3g" 9 11
  9
  10
  11



