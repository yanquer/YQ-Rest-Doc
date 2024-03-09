
=======================================
crawl
=======================================

.. _CmdCrawl:

**依赖项目目录**

运行指定的爬虫::

  scrapy crawl [options] $spiderName

支持option

.. -O file
..   将 输出 覆盖到file


--overwrite-output FILE, -O FILE
  将输出写入到文件(如果文件已存在则覆盖)
  dump scraped items into FILE, overwriting any existing file, to define format set a colon at the end of the output URI (i.e. -O FILE:FORMAT)

.. 将输出写入到文件(如果文件已存在则新增), 貌似仅支持 jsonl

--output FILE, -o FILE
  将 输出 增加到file (不会覆盖已存在的内容)

  但是新增模式不支持json(能写, 但是文件格式存在问题), 可以使用 jsonl

  jsonl
    JSON Lines 格式流式的, 支持新增内容更简单(没懂意思), 原文::

      The JSON Lines format is useful because it’s stream-like, you can easily append new records to it.
      It doesn’t have the same problem of JSON when you run twice.

    每一个记录是一个单独的行, 所以如果文件很大的时候, 可以直接逐行读取分析. 原文::

      Also, as each record is a separate line,
      you can process big files without having to fit everything in memory,
      there are tools like JQ to help do that at the command-line.

    jsonl 参考 `<https://jsonlines.org>`_

    .. In small projects (like the one in this tutorial), that should be enough.
    .. However, if you want to perform more complex things with the scraped items, you can write an Item Pipeline.
    .. A placeholder file for Item Pipelines has been set up for you when the project is created,
    .. in tutorial/pipelines.py.
    .. Though you don’t need to implement any item pipelines if you just want to store the scraped items.

-a args
  自定义爬虫参数,
  提供自定义参数列表给爬虫.

  格式::

    -a NAME=VALUE

  如::

    scrapy crawl quotes -O quotes-humor.json -a tag=humor

  代码::

    import scrapy

    class QuotesSpider(scrapy.Spider):
        name = "quotes"

        def start_requests(self):
            url = "https://quotes.toscrape.com/"
            tag = getattr(self, "tag", None)
            if tag is not None:
                url = url + "tag/" + tag
            yield scrapy.Request(url, self.parse)

        def parse(self, response):
            for quote in response.css("div.quote"):
                yield {
                    "text": quote.css("span.text::text").get(),
                    "author": quote.css("small.author::text").get(),
                }

            next_page = response.css("li.next a::attr(href)").get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)

  实际寻找的url就是::

    https://quotes.toscrape.com/tag/humor

--output-format FORMAT, -t FORMAT
  **已经废弃**, 定义当数据输出时的格式, 不能于 -O 一起用

-h, --help
  帮助消息

spiderName
  为定义在 spiders 目录下的具体的爬虫name ()

如::

  scrapy crawl itcast -O t.json

如::

  $ scrapy crawl myspider
  [ ... myspider starts crawling ... ]

  $ scrapy crawl -o myfile:csv myspider
  [ ... myspider starts crawling and appends the result to the file myfile in csv format ... ]

  $ scrapy crawl -O myfile:json myspider
  [ ... myspider starts crawling and saves the result in myfile in json format overwriting the original content... ]

  $ scrapy crawl -o myfile -t csv myspider
  [ ... myspider starts crawling and appends the result to the file myfile in csv format ... ]






