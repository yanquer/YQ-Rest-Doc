=============================
JSONField
=============================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


New in Django 3.1.

一个用于存储 JSON 编码数据的字段。在 Python 中，数据以其 Python 本地格式表示：字典、列表、字符串、数字、布尔值和 None::

  class JSONField(encoder=None, decoder=None, **options)

JSONField 在 MariaDB 10.2.7+、MySQL 5.7.8+、Oracle、PostgreSQL 和 SQLite（在 JSON1 扩展被启用的情况下）都支持。

JSONField.encoder
  一个可选的 json.JSONEncoder 子类，用于序列化标准 JSON 序列化器不支持的数据类型（例如 datetime.datetime 或 UUID ）。例如，你可以使用 DjangoJSONEncoder 类。

  默认为 json.JSONEncoder。
JSONField.decoder
  一个可选的 json.JSONDecoder 子类，用于反序列化从数据库中获取的值。
  该值将采用自定义编码器选择的格式（通常是字符串）。
  你的反序列化可能需要考虑到你无法确定输入类型的事实。
  例如，你有可能返回一个 datetime，实际上是一个字符串，而这个字符串恰好与 datetime 选择的格式相同。

  默认为 json.JSONDecoder。

如果你给字段一个 default，确保它是一个不可变的对象，
比如 str，或者是一个每次返回一个新的可变对象的可调用对象，
比如 dict 或一个函数。提供一个像 default={} 或 default=[] 这样的可改变的默认对象，在所有模型实例之间共享一个对象。

要在数据库中查询 JSONField，请看 查询 JSONField。

索引
  Index 和 Field.db_index 都创建了一个 B 树索引，在查询 JSONField 的时候并不是特别有用。仅在 PostgreSQL 上，可以使用 GinIndex 比较适合。

  PostgreSQL 用户
    PostgreSQL 有两种基于 JSON 的原生数据类型： json 和 jsonb。json 和 jsonb。
    它们之间的主要区别在于它们的存储方式和查询方式。
    PostgreSQL 的 json 字段是作为 JSON 的原始字符串表示来存储的，当根据键来查询时，必须同时进行解码。
    jsonb 字段是基于 JSON 的实际结构存储的，它允许索引。这样做的代价是在写入 jsonb 字段时增加了一点成本。JSONField 使用 jsonb。
  Oracle 用户
    Oracle 数据库不支持存储 JSON 标量值。只支持 JSON 对象和数组（在 Python 中使用 dict 和 list 表示)。


