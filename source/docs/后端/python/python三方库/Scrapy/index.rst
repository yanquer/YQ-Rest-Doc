===============================
Scrapy
===============================

Python爬虫库

- 官网: `<https://scrapy.org>`_
- 文档: `<https://docs.scrapy.org/en/latest/>`_

Scrapy 是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架。

Scrapy 常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。

通常我们可以很简单的通过 Scrapy 框架实现一个爬虫，抓取指定网站的内容或图片。

.. toctree::

  架构
  使用
  选择器/index
  命令行工具/index
  API/index

安装::

  pip install Scrapy

.. note::

  建议安装在虚拟环境以避免冲突

相关库
  - :doc:`/docs/后端/python/python三方库/lxml`: 高效的 xml 和 html 解析器
  - parsel: 基于 lxml 编写的一个 HTML/XML 数据提取库
  - w3lib: 处理 URL 和网页编码的多用途助手
  - twisted: 异步网络框架
  - :doc:`/docs/后端/python/python三方库/cryptography`: 处理各种网络级安全需求
  - pyOpenSSL: 处理各种网络级安全需求

.. note::

  这些库可能依赖非Py库

相关工具

.. toctree::

  Scrapy shell




