====================
html
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: `html --- 超文本标记语言支持 <https://docs.python.org/zh-cn/3/library/html.html>`_

该模块定义了操作HTML的工具。

.. function:: html.escape(s, quote=True)

  将字符串 s 中的字符``&`` 、 < 和 > 转换为安全的HTML序列。
  如果需要在 HTML 中显示可能包含此类字符的文本，请使用此选项。
  如果可选的标志 quote 为真值，则字符 (") 和 (') 也被转换；
  这有助于包含在由引号分隔的 HTML 属性中，如 <a href="...">。

  3.2 新版功能.


.. function:: html.unescape(s)

  将字符串 s 中的所有命名和数字字符引用 (例如 &gt;, &#62;, &#x3e;) 转换为相应的Unicode字符。
  此函数使用HTML 5标准为有效和无效字符引用定义的规则，以及 HTML 5 命名字符引用列表。

  3.4 新版功能.

html 包中的子模块是：

html.parser —— 具有宽松解析模式的HTML / XHTML解析器
html.entities -- HTML 实体定义

html.parser
====================

官网: `<https://docs.python.org/zh-cn/3/library/html.parser.html#module-html.parser>`_

简单的 HTML 和 XHTML 解析器

这个模块定义了一个 HTMLParser 类，为 HTML（超文本标记语言）和 XHTML 文本文件解析提供基础。

.. function:: class html.parser.HTMLParser(*, convert_charrefs=True)

  创建一个能解析无效标记的解析器实例。

  如果 convert_charrefs 为 True (默认值)，则所有字符引用( script/style 元素中的除外)都会自动转换为相应的 Unicode 字符。

  一个 HTMLParser 类的实例用来接受 HTML 数据，并在标记开始、标记结束、文本、注释和其他元素标记出现的时候调用对应的方法。要实现具体的行为，请使用 HTMLParser 的子类并重载其方法。

  这个解析器不检查结束标记是否与开始标记匹配，也不会因外层元素完毕而隐式关闭了的元素引发结束标记处理。

  在 3.4 版更改: convert_charrefs 关键字参数被添加。

  在 3.5 版更改: convert_charrefs 参数的默认值现在为 True。

html.entities
====================

HTML 一般实体的定义

该模块定义了四个词典， html5、 name2codepoint、 codepoint2name、以及 entitydefs。

html.entities.html5
  将 HTML5 命名字符引用 1 映射到等效的 Unicode 字符的字典，例如 html5['gt;'] == '>'。
  请注意，尾随的分号包含在名称中（例如 'gt;' ），但是即使没有分号，一些名称也会被标准接受，
  在这种情况下，名称出现时带有和不带有 ';'。另见 html.unescape()。

  3.3 新版功能.
html.entities.entitydefs
  将 XHTML 1.0 实体定义映射到 ISO Latin-1 中的替换文本的字典。
html.entities.name2codepoint
  将 HTML 实体名称映射到 Unicode 代码点的字典。
html.entities.codepoint2name
  将 Unicode 代码点映射到 HTML 实体名称的字典。

