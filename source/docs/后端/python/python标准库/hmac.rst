===========================
hmac
===========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/hmac.html

基于密钥的消息验证

此模块实现了 HMAC 算法，算法的描述参见 RFC 2104。

常用两个API

.. function:: hmac.new(key, msg=None, digestmod='')

  返回一个新的 hmac 对象。
  key 是一个指定密钥的 bytes 或 bytearray 对象。
  如果提供了 msg，将会调用 update(msg) 方法。
  digestmod 为 HMAC 对象所用的摘要名称、摘要构造器或模块。
  它可以是适用于 hashlib.new() 的任何名称。 虽然该参数位置靠后，但它却是必须的。

  在 3.4 版更改: 形参 key 可以为 bytes 或 bytearray 对象。
  形参 msg 可以为 hashlib 所支持的任意类型。 形参 digestmod 可以为某种哈希算法的名称。

  从版本 3.4 起弃用，在版本 3.8 中移除。:
  MD5 作为 digestmod 的隐式默认摘要已被弃用。
  digestmod 形参现在是必须的。 请将其作为关键字参数传入以避免当你没有初始 msg 时将导致的麻烦。

.. function:: hmac.digest(key, msg, digest)

  基于给定密钥 key 和 digest 返回 msg 的摘要。
  此函数等价于 HMAC(key, msg, digest).digest()，
  但使用了优化的 C 或内联实现，对放入内存的消息能处理得更快。
  形参 key, msg 和 digest 具有与 new() 中相同的含义。

  作为 CPython 的实现细节，优化的 C 实现仅当 digest 为字符串
  并且是一个 OpenSSL 所支持的摘要算法的名称时才会被使用。

  3.7 新版功能.

.. function:: hmac.compare_digest(a, b)

  返回 a == b。 此函数使用一种经专门设计的方式通过避免基于内容的短路行为来防止定时分析，
  使得它适合处理密码。
  a 和 b 必须为相同的类型：
  或者是 str (仅限 ASCII 字符，如 HMAC.hexdigest() 的返回值)，
  或者是 bytes-like object。

  备注 如果 a 和 b 具有不同的长度，或者如果发生了错误，
  定时攻击在理论上可以获取有关 a 和 b 的类型和长度信息 — 但不能获取它们的值。
  3.3 新版功能.

  在 3.10 版更改: 此函数在可能的情况下会在内部使用 OpenSSL 的 CRYPTO_memcmp()。



