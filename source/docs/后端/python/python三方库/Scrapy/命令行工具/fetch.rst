=============================
fetch
=============================

**不依赖项目目录**

语法::

  scrapy fetch <url>

使用 Scrapy downloader 下载给定的URL, 下载结果在标准输出

- 如果在项目内, 与爬虫获取到的页面是一致的(会使用配置的属性如 USER-AGENT)
- 如果在其他目录, 使用默认的配置属性

支持选项

--spider=SPIDER
  指定执行的爬虫, 没有就自动探测
--headers
  打印 HTTP 响应的消息头, 而不是打印 body
--no-redirect
  如果获取消息时, 遇到 3xx 的重定向, 就放弃(默认会跟着重定向到新地址)

Usage examples::

  $ scrapy fetch --nolog http://www.example.com/some/page.html
  [ ... html content here ... ]

  $ scrapy fetch --nolog --headers http://www.example.com/
  {'Accept-Ranges': ['bytes'],
  'Age': ['1263   '],
  'Connection': ['close     '],
  'Content-Length': ['596'],
  'Content-Type': ['text/html; charset=UTF-8'],
  'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
  'Etag': ['"573c1-254-48c9c87349680"'],
  'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
  'Server': ['Apache/2.2.3 (CentOS)']}


