==================================
选择器
==================================

主要是针对 HTML / XML 元素吧

选择器支持, 参考 `Selectors <https://docs.scrapy.org/en/latest/topics/selectors.html#selecting-attributes>`_

主要提供两种::

  response.css()
  response.xpath()

相关类是 :doc:`/docs/后端/python/python三方库/Scrapy/API/Selector`

除了调用response使用, 还可以直接实例使用::

  >>> from scrapy.selector import Selector
  >>> body = "<html><body><span>good</span></body></html>"
  >>> Selector(text=body).xpath("//span/text()").get()
  'good'

或者自己构造response (HtmlResponse 是 TextResponse 的子类)::

  >>> from scrapy.selector import Selector
  >>> from scrapy.http import HtmlResponse
  >>> response = HtmlResponse(url="http://example.com", body=body, encoding="utf-8")
  >>> Selector(response=response).xpath("//span/text()").get()
  'good'

Selector会自动解析 xml/html

实时交互解析, 建议使用 :ref:`scrapy shell <CmdShell>`

两种选择器详解(与Scrapy结合使用)

.. toctree::

  CSS选择器
  XPath选择器

甚至可以将 XPath 与 CSS 结合使用::

  # 对于 <img src='image4_thumb.jpg' alt='image4'/>
  response.css("img").xpath("@src")









