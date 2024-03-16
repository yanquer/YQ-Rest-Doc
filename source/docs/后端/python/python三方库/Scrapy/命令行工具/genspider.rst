==============================
genspider
==============================


.. post:: 2023-03-01 22:50:22
  :tags: python, python三方库, Scrapy, 命令行工具
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


**不依赖项目目录**


生成一个爬虫文件.

- 如果当前位置是非项目目录, 生成到当前目录下.
- 如果当前位置是项目目录, 生成到 spiders 目录.

语法::

  scrapy genspider [-t template] <name> <domain or URL>

name
  设置爬虫的 name 属性, 文件名也是这
domain or URL
  可选. 如果指定了, 会在爬虫类生成 allowed_domains 和 start_urls 属性

-t template
  指定生成时使用的模版.

  如::

    $ scrapy genspider -l
    Available templates:
      basic
      crawl
      csvfeed
      xmlfeed

    $ scrapy genspider example example.com
    Created spider 'example' using template 'basic'

    $ scrapy genspider -t crawl scrapyorg scrapy.org
    Created spider 'scrapyorg' using template 'crawl'

比如创建一个 名为 mydomain 的爬虫, 爬取 `mydomain` 地址::

  scrapy genspider mydomain mydomain.com

