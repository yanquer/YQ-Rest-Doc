=====================
unicodedata
=====================

定义了以下函数

.. function:: unicodedata.lookup(name)

  按名称查找字符。如果找到具有给定名称的字符，则返回相应的字符。 如果没有找到，则 KeyError 被引发。

  在 3.3 版更改: 已添加对名称别名 1 和命名序列 2 的支持。

.. function:: unicodedata.name(chr[, default])

  返回分配给字符 chr 的名称作为字符串。
  如果没有定义名称，则返回 default ，如果没有给出，则 ValueError 被引发。

.. function:: unicodedata.decimal(chr[, default])

  返回分配给字符 chr 的十进制值作为整数。
  如果没有定义这样的值，则返回 default ，如果没有给出，则 ValueError 被引发。

.. function:: unicodedata.digit(chr[, default])

  返回分配给字符 chr 的数字值作为整数。
  如果没有定义这样的值，则返回 default ，如果没有给出，则 ValueError 被引发。

.. function:: unicodedata.numeric(chr[, default])

  返回分配给字符 chr 的数值作为浮点数。
  如果没有定义这样的值，则返回 default ，如果没有给出，则 ValueError 被引发。

.. function:: unicodedata.category(chr)

  返回分配给字符 chr 的常规类别为字符串。

.. function:: unicodedata.bidirectional(chr)

  返回分配给字符 chr 的双向类作为字符串。如果未定义此类值，则返回空字符串。

.. function:: unicodedata.combining(chr)

  返回分配给字符 chr 的规范组合类作为整数。如果没有定义组合类，则返回 0 。

.. function:: unicodedata.east_asian_width(chr)

  返回分配给字符 chr 的东亚宽度作为字符串。

.. function:: unicodedata.mirrored(chr)

  返回分配给字符 chr 的镜像属性为整数。
  如果字符在双向文本中被识别为“镜像”字符，则返回 1 ，否则返回 0 。

.. function:: unicodedata.decomposition(chr)

  返回分配给字符 chr 的字符分解映射作为字符串。如果未定义此类映射，则返回空字符串。

.. function:: unicodedata.normalize(form, unistr)

  返回 Unicode 字符串 unistr 的正常形式 form 。
  form 的有效值为 'NFC' 、 'NFKC' 、 'NFD' 和 'NFKD' 。

  Unicode 标准基于规范等价和兼容性等效的定义定义了 Unicode 字符串的各种规范化形式。
  在 Unicode 中，可以以各种方式表示多个字符。
  例如，字符 U+00C7 （带有 CEDILLA 的 LATIN CAPITAL LETTER C ）也可以表示为序列
  U+0043（ LATIN CAPITAL LETTER C ）U+0327（ COMBINING CEDILLA ）。

  对于每个字符，有两种正规形式：正规形式 C 和正规形式 D 。
  正规形式D（NFD）也称为规范分解，并将每个字符转换为其分解形式。
  正规形式C（NFC）首先应用规范分解，然后再次组合预组合字符。

  即:

  - NFC 表示字符应该是整体组 成 (比如可能的话就使用单一编码)
  - NFD 表示字符应该分解为多个组合字符表示

  除了这两种形式之外，还有两种基于兼容性等效的其他常规形式。
  在 Unicode 中，支持某些字符，这些字符通常与其他字符统一。
  例如， U+2160（ROMAN NUMERAL ONE）与 U+0049（LATIN CAPITAL LETTER I）完全相同。
  但是， Unicode 支持它与现有字符集（例如 gb2312 ）的兼容性。

  正规形式KD（NFKD）将应用兼容性分解，即用其等价项替换所有兼容性字符。
  正规形式KC（NFKC）首先应用兼容性分解，然后是规范组合。

  即使两个 unicode 字符串被规范化并且人类读者看起来相同，如果一个具有组合字符而另一个没有，则它们可能无法相等。

.. function:: unicodedata.is_normalized(form, unistr)

  判断 Unicode 字符串 unistr 是否为正规形式 form。 form 的有效值为 'NFC', 'NFKC', 'NFD' 和 'NFKD'。

  3.8 新版功能.

此外，该模块暴露了以下常量：

unicodedata.unidata_version
  此模块中使用的 Unicode 数据库的版本。
unicodedata.ucd_3_2_0
  这是一个与整个模块具有相同方法的对象，
  但对于需要此特定版本的 Unicode 数据库（如 IDNA ）的应用程序，则使用 Unicode 数据库版本 3.2 。







