
=======================================
shell
=======================================

.. _CmdShell:

**不依赖项目目录**

启动一个交互式的爬虫终端, 如果有ipython就会用ipython::

  scrapy shell $url

启动成功后, 在当前环境会有一个 **response** 变量, 代表爬虫的响应,
与爬虫类 parse 方法的第一个 response 参数一致.

支持选项

--spider=SPIDER
  使用指定爬虫的url
-c code
  执行指定的代码并输出
--no-redirect
  不重定向

Usage example::

  $ scrapy shell http://www.example.com/some/page.html
  [ ... scrapy shell starts ... ]

  $ scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'
  (200, 'http://www.example.com/')

  # shell follows HTTP redirects by default
  $ scrapy shell --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
  (200, 'http://example.com/')

  # you can disable this with --no-redirect
  # (only for the URL passed as command line argument)
  $ scrapy shell --no-redirect --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
  (302, 'http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F')


