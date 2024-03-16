=============================
settings
=============================


.. post:: 2023-03-01 22:50:22
  :tags: python, python三方库, Scrapy, 命令行工具
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


**不依赖项目目录**

语法::

  scrapy settings [options]

获取配置信息

- 如果在项目下, 输出项目的配置
- 不在项目输出默认配置

Example usage::

  $ scrapy settings --get BOT_NAME
  scrapybot
  $ scrapy settings --get DOWNLOAD_DELAY
  0



