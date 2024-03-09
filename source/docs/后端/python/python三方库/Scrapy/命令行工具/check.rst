====================================
check
====================================

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




