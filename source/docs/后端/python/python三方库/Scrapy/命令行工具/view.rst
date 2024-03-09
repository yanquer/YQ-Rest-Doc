================================
view
================================

**不依赖项目目录**

用浏览器打开指定的 url

语法::

  scrapy view <url>

选项

--spider=SPIDER
  自动探测指定爬虫的url
--no-redirect
  不重定向

Usage example::

  $ scrapy view http://www.example.com/some/page.html
  [ ... browser starts ... ]







