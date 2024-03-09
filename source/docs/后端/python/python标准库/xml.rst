============================
xml
============================

官网: https://docs.python.org/zh-cn/3/library/xml.html

处理 XML 的模块.

.. warning::

   XML 模块对于错误或恶意构造的数据是不安全的。
   如果你需要解析不受信任或未经身份验证的数据，请使用 defusedxml 包::

    pip install defusedxml

XML 处理子模块包括:

- xml.etree.ElementTree： ElementTree API，一个简单而轻量级的XML处理器
- xml.dom：DOM API 定义
- xml.dom.minidom：最小的 DOM 实现
- xml.dom.pulldom：支持构建部分 DOM 树
- xml.sax：SAX2 基类和便利函数
- xml.parsers.expat：Expat解析器绑定

暂时只说常用的 xml.etree.ElementTree

xml.etree.ElementTree
============================

详见: https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

实现了一个简单高效的API，用于解析和创建XML数据。

阻塞获取文件数据::

  import xml.etree.ElementTree as ET

  tree = ET.parse('country_data.xml')
  root = tree.getroot()

如果XML数据直接是字符串::

  root = ET.fromstring(country_data_as_string)

root 具有标签和属性字典::

  >>> root.tag
  'data'

  >>> root.attrib
  {}

ElementTree方法:

- find()
- iterfind()
- findtext()
- iterparse()

命令空间的说明
============================

在 XML 文档中,xmlns:s 和 xmlns 都用于定义命名空间,但有以下区别:

**xmlns:s 定义的是命名空间前缀** ,语法是::

  xmlns:s="http://www.w3.org/ns/example"

这定义了一个名称为 "s" 的命名空间前缀,指向 "http://www.w3.org/ns/example" 这个命名空间。
然后在元素中,使用 "s:" 前缀来指示这个元素属于这个命名空间::

  <s:name>John</s:name>

**xmlns 定义的是默认命名空间** ,语法是::

  xmlns="http://www.w3.org/ns/example"

这定义了默认命名空间为 "http://www.w3.org/ns/example"。
然后该默认命名空间作用域内的所有元素都属于这个命名空间,无须使用前缀::

  <name>John</name>

**当 XML 文档中只定义一个命名空间时,通常使用默认命名空间。当定义多个命名空间,又想区分元素属于哪个命名空间时,才需要使用命名空间前缀.**
如果一个元素既定义了默认命名空间,又定义了命名空间前缀,此时:

- 无前缀的元素属于默认命名空间
- 使用前缀的元素属于相应的命名空间

命名空间的处理
============================

若使用映射字典::

  namespaces = {
      's': 'http://schemas.xmlsoap.org/soap/envelope/',
      'u': 'urn:schemas-upnp-org:service:ContentDirectory:1'
  }
  body = envelope.find('Body', namespaces)

这里,我们传入了一个字典,将前缀`s`映射到SOAP envelope命名空间,前缀`u`映射到UPnP ContentDirectory服务的命名空间。
这样,在查找元素时,我们可以使用前缀来限定命名空间,例如::

  browse = body.find('{urn:schemas-upnp-org:service:ContentDirectory:1}Browse')

等同于::

  browse = body.find('u:Browse', namespaces)
