===============================
GenericIPAddressField
===============================

IPv4 或 IPv6 地址，字符串格式（如 192.0.2.30 或 2a02:42fe::4 ）。该字段的默认表单部件是一个 TextInput::

  class GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)

IPv6 地址规范化遵循 RFC 4291#section-2.2 第 2.2 节，
包括使用该节第 3 段建议的 IPv4 格式，如 ::fffff:192.0.2.0。
例如，2001:0::0:01 将被标准化为 2001::1，::fffff:0a0a:0a0a 将被标准化为 ::fffff:10.10.10.10。所有字符都转换为小写。

GenericIPAddressField.protocol
  将有效输入限制为指定协议。接受的值是 'both' （默认）、'IPv4' 或 'IPv6'。匹配是不分大小写的。
GenericIPAddressField.unpack_ipv4
  解压 IPv4 映射地址，如 ::fffff:192.0.2.1。如果启用该选项，该地址将被解压为 192.0.2.1。默认为禁用。只有当 protocol 设置为 'both' 时才会启用。

  如果允许空值，就必须允许 null 值，因为空值会被存储为 null。

