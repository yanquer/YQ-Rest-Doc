=================
urllib
=================


url编码
=================

- parse.urlencode, 将python字典数据返回url格式的数据
- parse.quote, 将url格式数据编码
- parse.unquote, 上一个结果的解码, 返回普通url格式数据


例::

  data = {'a': 1, 'b': 2, }

  # 将python对象转换为url格式
  r = parse.urlencode(data)
  _logger.info(r)         # a=1&b=2

  # url 编码， & = 等字符都会被编码
  r = parse.quote(r)
  _logger.info(r)         # a%3D1%26b%3D2

  # url 解码， 仅转换为普通字符传拼接的形式
  r = parse.unquote(r)
  _logger.info(r)         # a=1&b=2

