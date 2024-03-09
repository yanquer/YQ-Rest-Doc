================================
Selector
================================

参考: `<https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList>`_

code::

  class scrapy.selector.Selector(*args: Any, **kwargs: Any)

用于修饰 response 选择器选择的内容.
response 是 HtmlResponse/XmlResponse 对象

支持参数:

text
  HTML/XML 字符串
type
  选择器类型, 支持 html 和 xml. 不给会自动选择最适合的

  支持的:

  - "html" for HtmlResponse type
  - "xml" for XmlResponse type
  - "html" for anything else

  设置后就不会自动找


属性
================================

selector

对象方法
================================

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

  选择器支持见 :doc:`../选择器/index`

  如果要获取属性, 比如 ::

    <a href="xxx"/>

  有两种方式::

    response.css("a").attrib["href"]

    response.css("a::attr('href')")

xpath(表达式): :doc:`/docs/后端/python/python三方库/Scrapy/API/SelectorList`
  使用 :doc:`/docs/后端/python/教程/xpath/index` 获取元素,
  返回 :doc:`/docs/后端/python/python三方库/Scrapy/API/SelectorList`

  方法::

    xpath(query: str, namespaces: Optional[Mapping[str, str]] = None, **kwargs: Any)→ SelectorList[_SelectorType]

  如::

    >>> t = response.xpath("//div[@class='tea_con']/div/ul/li")[0]
    >>> t
    <Selector query="//div[@class='tea_con']/div/ul/li" data='<li>\n\t\t\t\t\t<img src="images/teacher/ja...'>
    >>>
    >>> t.xpath("div/h4")
    [<Selector query='div/h4' data='<h4>高级讲师</h4>'>]
    >>>

  注意, 新的 xpath 表达式, 如果不带斜杠, 表示是从上一级继续找,
  比如例子 ``t.xpath("div/h4")`` 就是从上面的 query 继续找::

    //div[@class='tea_con']/div/ul/li/div/h4

  但是如果有斜杠, 上一层的query就没了(因为会视作绝对路径).
  如果非要用鞋杠, 需要加点::

    .//div/h4

  表示找相对路径

  包含使用 contains::

    contains(@class, "c1")

  可参考 :doc:`/docs/后端/python/教程/xpath/XPath运算符`




