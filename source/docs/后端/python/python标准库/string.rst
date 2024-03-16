===============================
string
===============================


.. post:: 2024-02-21 21:55:17
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: `<https://docs.python.org/zh-cn/3/library/string.html>`_

常见的字符串操作

字符串常量
===============================

此模块中定义的常量为：

string.ascii_letters
  下文所述 ascii_lowercase 和 ascii_uppercase 常量的拼连。 该值不依赖于语言区域。
string.ascii_lowercase
  小写字母 'abcdefghijklmnopqrstuvwxyz'。 该值不依赖于语言区域，不会发生改变。
string.ascii_uppercase
  大写字母 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'。 该值不依赖于语言区域，不会发生改变。
string.digits
  字符串 '0123456789'。
string.hexdigits
  字符串 '0123456789abcdefABCDEF'。
string.octdigits
  字符串 '01234567'。
string.punctuation
  由在 C 区域设置中被视为标点符号的 ASCII 字符所组成的字符串::

    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
string.printable
  由被视为可打印符号的 ASCII 字符组成的字符串。 这是 digits, ascii_letters, punctuation 和 whitespace 的总和。
string.whitespace
  由被视为空白符号的 ASCII 字符组成的字符串。 其中包括空格、制表、换行、回车、进纸和纵向制表符。

自定义字符串格式化
===============================






