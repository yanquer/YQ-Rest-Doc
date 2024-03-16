====================================
check
====================================


.. post:: 2023-03-01 22:50:22
  :tags: python, python三方库, Scrapy, 命令行工具
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


**依赖项目目录**

语法::

  scrapy check [-l] <spider>

运行检查::

  $ scrapy check -l
  first_spider
    * parse
    * parse_item
  second_spider
    * parse
    * parse_item

  $ scrapy check
  [FAILED] first_spider:parse_item
  >>> 'RetailPricex' field is missing

  [FAILED] first_spider:parse
  >>> Returned 92 requests, expected 0..4




