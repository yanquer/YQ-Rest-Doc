=============================
settings
=============================

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



