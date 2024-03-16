================================
view
================================


.. post:: 2023-03-01 22:50:22
  :tags: python, python三方库, Scrapy, 命令行工具
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


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







