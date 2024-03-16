====================================
XPath选择器
====================================


.. post:: 2023-03-01 22:50:22
  :tags: python, python三方库, Scrapy, 选择器
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


XPath 参考 :doc:`/docs/后端/python/教程/xpath/index`

概述::

  text()            获取文本
  @属性名           获取指定属性, 不跟表达式仅表示存在当前属性

  has-class         是否包含指定class
                    has-class("cl1")      是否包含 class属性 cl1 (仅Scrapy支持)


如有以下HTML::

  <!DOCTYPE html>

  <html>
    <head>
      <base href='http://example.com/' />
      <title>Example website</title>
    </head>
    <body>
      <div id='images'>
        <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
        <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
        <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
        <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
        <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
      </div>
      <div class='cl1 cl2'>
        Name: My image 5 <br />
        <img src='image5_thumb.jpg' alt='image5'/>
      </div>
    </body>
  </html>

选择title的内容::

  //title/text()

获取所有 a 标签的内容::

  //div[@id="images"]/a/text()

包含使用 contains ::

  contains(@id, "images")

比如有多个class属性的时候, =是不成立的, 只好用 contains,
参考 :ref:`XpathContain`::

  //div[contains(@class, "cl1")]/img/@src

可以发现使用 contains 是比较麻烦的,
且不易兼容所有情况,
所以有时还是使用 :doc:`/docs/后端/python/python三方库/Scrapy/选择器/CSS选择器`
更简单::

  .css("div.cl1").xpath("./img/@src")

可参考 :doc:`/docs/后端/python/教程/xpath/XPath运算符`

加不加括号的区别
====================================

举例::

  <ul class="list">
      <li>1</li>
      <li>2</li>
      <li>3</li>
  </ul>
  <ul class="list">
      <li>4</li>
      <li>5</li>
      <li>6</li>
  </ul>

不加括号(选择所有组节点)::

  //li[1]
  //ul/li[1]

  # 结果都是
  ['<li>1</li>', '<li>4</li>']

加括号(将所有组合并一个组)::

  (//li)[1]
  (//ul/li)[1]

  # 结果都是
  ['<li>1</li>']

条件表达式下使用text
====================================

应该避免直接使用::

  .//text()

而是使用::

  .

因为前者在Scrapy框架会返回一个包含所有text文本的生成器结果集(yield []),
然后当其作为参数传递给 str的函数比如  contains(), starts-with(),
只会返回第一个结果

比如::

  >>> from scrapy import Selector
  >>> sel = Selector(
  ...     text='<a href="#">Click here to go to the <strong>Next Page</strong></a>'
  ... )

转换为 String 的结果集::

  >>> sel.xpath("//a//text()").getall()  # take a peek at the node-set
  ['Click here to go to the ', 'Next Page']
  >>> sel.xpath("string(//a[1]//text())").getall()  # convert it to string
  ['Click here to go to the ']

转换为字符串的节点会丢失后代节点::

  >>> sel.xpath("//a[1]").getall()  # select the first node
  ['<a href="#">Click here to go to the <strong>Next Page</strong></a>']
  >>> sel.xpath("string(//a[1])").getall()  # convert it to string, 丢失了后代
  ['Click here to go to the Next Page']

这时使用 ``.//text()`` 得不到任何结果::

  >>> sel.xpath("//a[contains(.//text(), 'Next Page')]").getall()
  []

但如果使用 ``.`` , 就可获取到::

  >>> sel.xpath("//a[contains(., 'Next Page')]").getall()
  ['<a href="#">Click here to go to the <strong>Next Page</strong></a>']


XPath表达式变量
====================================

XPath 允许你在表达式中引用变量, 语法::

  $varName

与SQL类似, 还支持使用 ``?`` 占位符, 来做变量替换::

  >>> # `$val` used in the expression, a `val` argument needs to be passed
  >>> response.xpath("//div[@id=$val]/a/text()", val="images").get()
  'Name: My image 1 '

又比如寻找 div 下包含 5 个孩子节点::

  >>> response.xpath("//div[count(a)=$cnt]/@id", cnt=5).get()
  'images'

任何变量必须使用的时候就给定值, 否则会报错 ``ValueError: XPath error: exception``

移除命名空间
====================================

有些爬虫项目获取到的 HTML/XML 是存在命名空间的,
但是我们并不关注这个, 只想处理元素,
所以可以直接移除::

  Selector.remove_namespaces()

比如以下的XML::

  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet ...
  <feed xmlns="http://www.w3.org/2005/Atom"
        xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
        xmlns:blogger="http://schemas.google.com/blogger/2008"
        xmlns:georss="http://www.georss.org/georss"
        xmlns:gd="http://schemas.google.com/g/2005"
        xmlns:thr="http://purl.org/syndication/thread/1.0"
        xmlns:feedburner="http://rssnamespace.org/feedburner/ext/1.0">
    ...

有一个默认的 ``http://www.w3.org/2005/Atom`` 和其他的
比如 ``gd:” prefix for “http://schemas.google.com/g/2005”``

当尝试选择 link 时, 获取不到结果::

  >>> response.xpath("//link")
  []

因为其存在于默认的命名空间内.
移除掉即可::

  >>> response.selector.remove_namespaces()
  >>> response.xpath("//link")
  [<Selector query='//link' data='<link rel="alternate" type="text/html" h'>,
      <Selector query='//link' data='<link rel="next" type="application/atom+'>,
      ...

为什么默认不直接移除?
  - 移除对整个文档所有节点操作, 代价大
  - 并非所有情况下都不会用到 namespace


使用 EXSLT 拓展
====================================

Scrapy选择器构建在lxml之上，支持一些EXCIBLE扩展，
并带有这些预注册的命名空间，可用于EXCIBLE表达式：

========  ========================================  ========================
prefix      namespace                                 usage
========  ========================================  ========================
re        http://exslt.org/regular-expressions        正则表达式
set       http://exslt.org/sets                       集合操作
                                                      (set manipulation)
========  ========================================  ========================

正则表达式支持
------------------------------------

默认 XPath 有提供字符串的 ``starts-with()`` 和  ``contains()`` 方法,
但是更复杂的匹配就不行了,  这时可以用 ``test()`` 方法

比如选择指定 class 的 li 标签下的 链接::

  >>> from scrapy import Selector
  >>> doc = """
  ... <div>
  ...     <ul>
  ...         <li class="item-0"><a href="link1.html">first item</a></li>
  ...         <li class="item-1"><a href="link2.html">second item</a></li>
  ...         <li class="item-inactive"><a href="link3.html">third item</a></li>
  ...         <li class="item-1"><a href="link4.html">fourth item</a></li>
  ...         <li class="item-0"><a href="link5.html">fifth item</a></li>
  ...     </ul>
  ... </div>
  ... """
  >>> sel = Selector(text=doc, type="html")
  >>> sel.xpath("//li//@href").getall()
  ['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
  >>> sel.xpath('//li[re:test(@class, "item-\d$")]//@href').getall()
  ['link1.html', 'link2.html', 'link4.html', 'link5.html']

.. warning::

  C库的 ``libxslt`` 并不提供 EXSLT 的支持,
  所以实际上匹配使用的是 Python 的 :doc:`/docs/后端/python/python标准库/re` .

  故, 存在性能问题是无法避免的

集合操作
------------------------------------

.. Set operations
.. set manipulation

有时候可能不想要文档的某个部分

比如 `<https://schema.org/Product>`_ 的以下内容, 存在
itemscopes 和 corresponding itemprops::

  >>> doc = """
  ... <div itemscope itemtype="http://schema.org/Product">
  ...   <span itemprop="name">Kenmore White 17" Microwave</span>
  ...   <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />
  ...   <div itemprop="aggregateRating"
  ...     itemscope itemtype="http://schema.org/AggregateRating">
  ...    Rated <span itemprop="ratingValue">3.5</span>/5
  ...    based on <span itemprop="reviewCount">11</span> customer reviews
  ...   </div>
  ...   <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
  ...     <span itemprop="price">$55.00</span>
  ...     <link itemprop="availability" href="http://schema.org/InStock" />In stock
  ...   </div>
  ...   Product description:
  ...   <span itemprop="description">0.7 cubic feet countertop microwave.
  ...   Has six preset cooking categories and convenience features like
  ...   Add-A-Minute and Child Lock.</span>
  ...   Customer reviews:
  ...   <div itemprop="review" itemscope itemtype="http://schema.org/Review">
  ...     <span itemprop="name">Not a happy camper</span> -
  ...     by <span itemprop="author">Ellie</span>,
  ...     <meta itemprop="datePublished" content="2011-04-01">April 1, 2011
  ...     <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
  ...       <meta itemprop="worstRating" content = "1">
  ...       <span itemprop="ratingValue">1</span>/
  ...       <span itemprop="bestRating">5</span>stars
  ...     </div>
  ...     <span itemprop="description">The lamp burned out and now I have to replace
  ...     it. </span>
  ...   </div>
  ...   <div itemprop="review" itemscope itemtype="http://schema.org/Review">
  ...     <span itemprop="name">Value purchase</span> -
  ...     by <span itemprop="author">Lucas</span>,
  ...     <meta itemprop="datePublished" content="2011-03-25">March 25, 2011
  ...     <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
  ...       <meta itemprop="worstRating" content = "1"/>
  ...       <span itemprop="ratingValue">4</span>/
  ...       <span itemprop="bestRating">5</span>stars
  ...     </div>
  ...     <span itemprop="description">Great microwave for the price. It is small and
  ...     fits in my apartment.</span>
  ...   </div>
  ...   ...
  ... </div>
  ... """
  >>> sel = Selector(text=doc, type="html")
  >>> for scope in sel.xpath("//div[@itemscope]"):
  ...     print("current scope:", scope.xpath("@itemtype").getall())
  ...     props = scope.xpath(
  ...         """
  ...                 set:difference(./descendant::*/@itemprop,
  ...                                .//*[@itemscope]/*/@itemprop)"""
  ...     )
  ...     print(f"    properties: {props.getall()}")
  ...     print("")
  ...

  current scope: ['http://schema.org/Product']
      properties: ['name', 'aggregateRating', 'offers', 'description', 'review', 'review']

  current scope: ['http://schema.org/AggregateRating']
      properties: ['ratingValue', 'reviewCount']

  current scope: ['http://schema.org/Offer']
      properties: ['price', 'availability']

  current scope: ['http://schema.org/Review']
      properties: ['name', 'author', 'datePublished', 'reviewRating', 'description']

  current scope: ['http://schema.org/Rating']
      properties: ['worstRating', 'ratingValue', 'bestRating']

  current scope: ['http://schema.org/Review']
      properties: ['name', 'author', 'datePublished', 'reviewRating', 'description']

  current scope: ['http://schema.org/Rating']
      properties: ['worstRating', 'ratingValue', 'bestRating']

主要是::

  set:difference(./descendant::*/@itemprop, .//*[@itemscope]/*/@itemprop)

``set:difference`` 表示使用一个集合减去另一个集合, 也就是::

  ./descendant::*/@itemprop

减去::

  .//*[@itemscope]/*/@itemprop

来分别看分析这两个的含义::

  ./descendant::*/@itemprop
    descendant 翻译过来就是后代,
    这里就是表示当前元素的所有后代元素(后代, 孙代...),

    总来说就是, 所有后代元素的 itemprop 属性


  .//*[@itemscope]/*/@itemprop
    选择所有包含 itemscope 属性的 itemprop 属性

整个表达式的含义是选择当前节点的所有后代节点中具有 itemprop 属性的属性节点，
然后从中排除当前节点下具有 itemscope 属性的元素节点的子节点中的 itemprop 属性节点，
最后返回剩余的元素节点集合

其他 XPath 拓展
====================================

Scrapy 选择器 还提供了 ``has-class``, 可用于判断是否包含 class 属性,

对于HTML::

  >>> from scrapy.http import HtmlResponse
  >>> response = HtmlResponse(
  ...     url="http://example.com",
  ...     body="""
  ... <html>
  ...     <body>
  ...         <p class="foo bar-baz">First</p>
  ...         <p class="foo">Second</p>
  ...         <p class="bar">Third</p>
  ...         <p>Fourth</p>
  ...     </body>
  ... </html>
  ... """,
  ...     encoding="utf-8",
  ... )

这样用::

  >>> response.xpath('//p[has-class("foo")]')
  [<Selector query='//p[has-class("foo")]' data='<p class="foo bar-baz">First</p>'>,
  <Selector query='//p[has-class("foo")]' data='<p class="foo">Second</p>'>]
  >>> response.xpath('//p[has-class("foo", "bar-baz")]')
  [<Selector query='//p[has-class("foo", "bar-baz")]' data='<p class="foo bar-baz">First</p>'>]
  >>> response.xpath('//p[has-class("foo", "bar")]')
  []


其中::

  //p[has-class("foo", "bar-baz")]

相当于 CSS的::

  p.foo.bar-baz

.. note::

  has-class 其实性能是比较慢的, 因为它是一个纯 Python 函数.

  故建议仅适用于, CSS选择器不容易描述的情况下

添加自定义 Python 方法
====================================

API::

  parsel.xpathfuncs.set_xpathfunc(fname: str, func: Optional[Callable]) -> None[source]

用于注册自定义 XPath 表达式方法

Register a custom extension function to use in XPath expressions.

fname
  方法名
func
  具体的执行方法, 为None回注册失败






