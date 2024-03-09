================
uuid
================

:官网文档::
  `uuid RFC 4122 定义的UUID对象 <https://docs.python.org/zh-cn/3/library/uuid.html>`_

.. _RFC 4122: https://datatracker.ietf.org/doc/html/rfc4122.html

提供了不可变的 UUID 对象 (UUID 类) 以及:

- uuid1_ ,
- uuid3_ ,
- uuid4_ ,
- uuid5_

等函数用于生成 `RFC 4122`_ 所定义的第 1, 3, 4 和 5 版 UUID.

使用方面:

- Python中没有基于DCE的，所以uuid2可以忽略；
- uuid4存在概率性重复，由无映射性，最好不用；
- 若在Global的分布式计算环境下，最好用uuid1；
- 若有名字的唯一性要求，最好用uuid3或uuid5。

主要的类
================

SafeUUID
----------------

.. function:: class uuid.SafeUUID

  safe
    该UUID是由平台以多进程安全的方式生成的.
  unsafe
    UUID不是以多进程安全的方式生成的.
  unknown
    该平台不提供UUID是否安全生成的信息.

.. function:: class uuid.UUID(hex=None, bytes=None, bytes_le=None, fields=None, int=None, version=None, *, is_safe=SafeUUID.unknown)

  .. （32位 *time_low* ，16位 *time_mid* ，16位 *time_hi_version* ，
      8位 *clock_seq_hi_variant* ，8位 *clock_seq_low* ，48位 *node* ）作为 *fields* 参数，
      或者一个128位整数作为 *int* 参数创建一个UUID.
      当给出一串十六进制数字时，大括号、连字符和URN前缀都是可选的.

  bytes
    一串32位十六进制数字、一串大端序16个字节作为 *bytes* 参数
  bytes_le
    一串16个小端序字节作为 *bytes_le* 参数、
  fields
    一个由六个整数组成的元组

    time_low: 32位;
    time_mid: 16位;
    time_hi_version: 16位;
    clock_seq_hi_variant: 8位;
    clock_seq_low: 8位;
    node: 48位.
  int
    一个128位整数

  当给出一串十六进制数字时，大括号、连字符和URN前缀都是可选的. 以上参数都是任选的.

  例如，这些表达式都产生相同的UUID::

    UUID('{12345678-1234-5678-1234-567812345678}')
    UUID('12345678123456781234567812345678')
    UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
    UUID(bytes=b'\x12\x34\x56\x78'*4)
    UUID(bytes_le=b'\x78\x56\x34\x12\x34\x12\x78\x56' +
                  b'\x12\x34\x56\x78\x12\x34\x56\x78')
    UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
    UUID(int=0x12345678123456781234567812345678)

  必须给出 hex、bytes、bytes_le、fields 或 int 中的唯一一个. version 参数是可选的；
  如果给定，产生的UUID将根据 `RFC 4122`_ 设置其变体和版本号，覆盖给定的 hex、bytes、bytes_le、fields 或 int 中的位.

  **UUID 对象的比较是通过比较它们的 UUID.int 属性进行的.** 与非 UUID 对象的比较会引发 TypeError.

  str(uuid) 返回一个 12345678-1234-5678-1234-567812345678 形式的字符串，其中 32 位十六进制数字代表 UUID.


具有的只读属性
================

UUID.bytes
  UUID是一个16字节的字符串（包含6个大端字节序的整数字段）.
UUID.bytes_le
  UUID 是一个 16 字节的字符串（其中 time_low、time_mid 和 time_hi_version 为小端字节顺序）.
UUID.fields
  以元组形式存放的UUID的6个整数域，有六个单独的属性和两个派生属性：

  .. csv-table::
    :header: 域, 含意

    time_low, UUID的前32位
    time_mid, 接前一域的16位
    time_hi_version, 接前一域的16位
    clock_seq_hi_variant, 接前一域的8位
    clock_seq_low, 接前一域的8位
    node, UUID的最后48位
    time, UUID的总长60位的时间戳
    clock_seq, 14位的序列号
UUID.hex
  UUID 是一个 32 字符的小写十六进制数码字符串.

  与直接 str 转换的效果类似::

    a = uuid.uuid4()
    a
    Out[10]: UUID('a7de0199-3e5e-4d84-8fd3-5f65052db9b5')
    # convert a UUID to a string of hex digits in standard form
    str(a)
    Out[11]: 'a7de0199-3e5e-4d84-8fd3-5f65052db9b5'
    a.hex
    Out[12]: 'a7de01993e5e4d848fd35f65052db9b5'

UUID.int
  UUID是一个128位的整数.
UUID.urn
  在 `RFC 4122`_ 中定义的 URN 形式的 UUID.
UUID.variant
  UUID 的变体，它决定了 UUID 的内部布局.
  这将是 RESERVED_NCS_ , RFC_4122_ , RESERVED_MICROSOFT_ 或 RESERVED_FUTURE_ 中的一个.
UUID.version
  UUID 版本号（1 到 5，只有当变体为 RFC_4122_ 时才有意义）.
UUID.is_safe
  一个 SafeUUID_ 的枚举，表示平台是否以多进程安全的方式生成 UUID.

模块函数
================

uuid.getnode()
  获取 48 位正整数形式的硬件地址.
  第一次运行时，它可能会启动一个单独的程序，这可能会相当慢.
  如果所有获取硬件地址的尝试都失败了，我们会按照 `RFC 4122`_ 中的建议，选择一个随机的 48 位数字，
  其多播位 (第一个八进制数的最小有效位) 设置为 1.
  “硬件地址”是指一个网络接口的 MAC 地址. 在一台有多个网络接口的机器上，
  普遍管理的 MAC 地址 (即第一个八位数的第二个最小有效位是 未设置的) 将比本地管理的 MAC 地址优先，但没有其他排序保证.

  在 3.7 版更改: 普遍管理的MAC地址优于本地管理的MAC地址，因为前者保证是全球唯一的，而后者则不是.

.. _uuid1:

uuid.uuid1(node=None, clock_seq=None)
  **基于时间戳**

  根据主机 ID、序列号和当前时间生成一个 UUID.

  如果没有给出 node，则使用 getnode() 来获取硬件地址(MAC地址), 虽然保证了全球的唯一, 但会有安全问题(MAC地址唯一).
  所以局域网中 node 可以使用 ip 地址.

  如果给出了 clock_seq，它将被用作序列号；否则将选择一个随机的 14 比特位序列号.

.. _uuid3:

uuid.uuid3(namespace, name)
  **基于名字的MD5散列值**

  根据命名空间标识符（这是一个UUID）和名称（这是一个字符串）的MD5哈希值，生成一个UUID.

.. _uuid4:

uuid.uuid4()
  **基于随机数**

  生成一个随机的UUID. 由伪随机数得到，有一定的重复概率，该概率可以计算出来。

.. _uuid5:

uuid.uuid5(namespace, name)
  **基于名字的SHA-1散列值**

  与uuid3类似, 根据命名空间标识符（这是一个UUID）和名称（这是一个字符串）的SHA-1哈希值生成一个UUID.

.. note::

  其实还有一个uuid2, 基于分布式计算环境DCE, 不过python没有

  算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。实际中很少用到该方法。

命名空间标识符
================

uuid 模块定义了以下命名空间标识符，供 uuid3() 或 uuid5() 使用.

uuid.NAMESPACE_DNS
  当指定 namespace 为此值时, name值为域名(domain name)

  .. When this namespace is specified,
     the name string is a fully qualified domain name.

uuid.NAMESPACE_URL
  当指定这个命名空间时，name 字符串是一个 URL.
uuid.NAMESPACE_OID
  当指定这个命名空间时，name 字符串是一个 ISO OID.
uuid.NAMESPACE_X500
  当指定这个命名空间时，name 字符串是 DER 或文本输出格式的 X.500 DN.

uuid 模块为 variant 属性的可能值定义了以下常量:

.. _RESERVED_NCS:

uuid.RESERVED_NCS
  为NCS兼容性保留.

.. _RFC_4122:

uuid.RFC_4122
  指定 `RFC 4122`_ 中给出的 UUID 布局.

.. _RESERVED_MICROSOFT:

uuid.RESERVED_MICROSOFT
  为微软的兼容性保留.

.. _RESERVED_FUTURE:

uuid.RESERVED_FUTURE
  保留给未来的定义.



