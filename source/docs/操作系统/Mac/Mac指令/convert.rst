=================================
convert
=================================


.. post:: 2023-02-20 22:06:49
  :tags: Mac, Mac指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


安装::

  brew install imagemagick

与 :doc:`/docs/操作系统/Mac/Mac指令/sips` 差不多

convert 是 **imagemagick** 程序包的命令,
convert 其实等价于 magick

执行转换命令只需要传入待转换的图片以及输出的图片文件名即可::

  convert aa.eps a.ico

支持几乎所有的位图/矢量图格式. 美中不足的一点就是转换的图片质量不高, pdf转png会丢失背景


参考: `https://blog.csdn.net/qq_41437512/article/details/122619375`



