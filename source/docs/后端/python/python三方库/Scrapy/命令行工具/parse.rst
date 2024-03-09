==================================
parse
==================================

**依赖项目目录**

语法::

  scrapy parse <url> [options]

获取指定的 URL 数据, 并使用 parse 函数进行转换.

支持选项

--spider=SPIDER
  指定爬虫, 会自动检测url
--a args
  设定执行的参数

  格式::

    --a [NAME=VALUE]
--callback, -c
  回调方法, 默认使用 parse 函数
--meta, -m
  额外提供给 回调方法 的参数. 必须是json格式

  Example: –meta=’{“foo” : “bar”}’
--cbkwargs
  额外提供给 回调函数 的 关键字参数

  Example: –cbkwargs=’{“foo” : “bar”}’
--pipelines
  process items through pipelines
--rules, -r
  使用 CrawlSpider 规则发现 回调函数.

  没大懂, 原文::

    use CrawlSpider rules to discover the callback (i.e. spider method) to use for parsing the response
--noitems
  don’t show scraped items
--nolinks
  don’t show extracted links
--nocolour
  避免存在颜色输出.
  avoid using pygments to colorize the output
--depth, -d
  请求最多被递归调用多少次. 默认1.
  depth level for which the requests should be followed recursively (default: 1)
--verbose, -v
  输出每一个调用详情.
  display information for each depth level
--output, -o
  将结果输出到文件.
  dump scraped items to a file

New in version 2.3.

Usage example::

  $ scrapy parse http://www.example.com/ -c parse_item
  [ ... scrapy log lines crawling example.com spider ... ]

  >>> STATUS DEPTH LEVEL 1 <<<
  # Scraped Items  ------------------------------------------------------------
  [{'name': 'Example item',
  'category': 'Furniture',
  'length': '12 cm'}]

  # Requests  -----------------------------------------------------------------
  []

