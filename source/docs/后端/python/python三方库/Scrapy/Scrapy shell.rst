=====================================
Scrapy shell
=====================================

交互式终端工具

参考: `<https://docs.scrapy.org/en/latest/topics/shell.html#topics-shell>`_

如果有安装 `IPython`, 就会使用 `IPython`, 否则使用默认 Python 的交互式终端

启动::

  scrapy shell <url>

url
  想爬取的 url 地址.

  也支持本地的 html 文件::

    # UNIX-style
    scrapy shell ./path/to/file.html
    scrapy shell ../other/path/to/file.html
    scrapy shell /absolute/path/to/file.html

    # File URI
    scrapy shell file:///absolute/path/to/file.html

支持的指令

view
  从浏览器打开::

    >>> view(response)
    True



