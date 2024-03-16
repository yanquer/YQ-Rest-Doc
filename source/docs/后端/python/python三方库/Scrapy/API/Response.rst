======================================
Response
======================================


.. post:: 2023-03-01 22:50:22
  :tags: python, python三方库, Scrapy, API
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


位置::

  from scrapy.http import Response

对象方法

css(表达式): :doc:`/docs/后端/python/python三方库/Scrapy/API/SelectorList`
  根据表达式获取对应的 CSS 元素,
  **可以理解为一个 CSS 选择器**
  返回 :doc:`/docs/后端/python/python三方库/Scrapy/API/SelectorList`

  如获取 title 标签元素::

    # html
    <title>标题</title>

    # 元素
    response.css("title")

    # 文本
    response.css("title::text")

  详见 :doc:`/docs/后端/python/python三方库/Scrapy/API/SelectorList`

  选择器支持见 :doc:`../选择器/index`

xpath(表达式): :doc:`/docs/后端/python/python三方库/Scrapy/API/SelectorList`
  使用 :doc:`/docs/后端/python/教程/xpath/index` 获取元素,
  返回 :doc:`/docs/后端/python/python三方库/Scrapy/API/SelectorList`






