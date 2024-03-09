===================================
cryptography
===================================

- 项目地址: `<https://github.com/pyca/cryptography/>`_
- 官网文档: `<https://cryptography.io/en/latest/>`_

翻译就是 密码学

密码学可研究下101: `CRYPTO101 <https://www.crypto101.io>`_

一个新的标准Python加密库

为什么建立一个新的Python密码库？
  现有的Python密码库，如M2Crypto, PyCrypto, or PyOpenSSL，存在一些问题：

  - 缺少PyPy和Python 3支持
  - 缺少维护
  - 使用了差评的算法实现（例如旁路攻击side-channel attacks）
  - 缺少高级（易于使用）的APIs
  - 缺少AES-GCM和HKDF等算法
  - 经不住测试
  - 错误百出的APIs

特性
  Cyptography密码库包括两个部分：cryptographic recipes and primitives.这是本密码库非常有意思的地方，很多现有的其他密码库并没有这个特点。cryptographic recipes，直接翻译为密码学菜谱。其实个人也一时找不出合适的词语来解释。cryptographic primitives，即为密码学原语，也就是基本的密码概念，如加密、签名、Hash等算法。但是直接使用密码学原语容易出错，在实际应用中无法保证安全性。基于这一点，该库对密码学原语进行了安全集成，形成了更高层次的“密码学菜谱”。这么说吧，密码学原语像是做菜的原材料，对于初学者来说，虽然手里都有，但是不懂得如何去制作；如果有了“密码学菜谱”，初学者直接按照说明，制作菜肴就可以了。

安装::

  pip install cryptography

用例
===================================

Cryptography密码库实现了一个集成的对称密码函数，称之为Fernet。它可以保证信息无法被篡改和破解。

加解密
-----------------------------------

加解密的例子::

  >>>from cryptography.fernet import Fernet

  >>>key = Fernet.generate_key()    # 产生加密所需的密钥key，它通过调用相关函数而产生随机数。

  >>>key

  Out[3]: 'x10qxCPeNGhddcP5fASy5XB1JedmwXJeAF1gS-zeuvw='

  >>>f = Fernet(key)    # 实例化Fernet

  >>>f

  Out[6]: <cryptography.fernet.Fernet at 0xb969668>

  >>>token = f.encrypt(b"my deep dark secret")     # 加密消息

  >>>token

  Out[8]: 'gAAAAABYnKtVmGpMe6rM39jzSYFTlBxjXBwbCix8nZ2DBzsFh6BVzwtrYx0qDyohXQ3xqj232_DJsdN8bR9sMUQbEcPenZD-MAWqR-YkOdg7prc9e0QnMA4='

  >>>f.decrypt(token)     # 加密消息

  Out[9]: 'my deep dark secret'

密钥轮换（Key rotation）
-----------------------------------

密钥轮换（Key rotation）的例子

MultiFernet的输入为多个key的列表，它总是以第一个密钥加密消息，而在解密时，依次使用每个密钥。

Key rotation机制使得替代旧的密钥变得容易。
个人可以将新的密钥添加在key列表的第一个，开始加密新的消息，而在解密以前的密文后，如果旧的密钥不再需要则丢弃::

  >>>from cryptography.fernet import Fernet, MultiFernet

  >>>key1 = Fernet(Fernet.generate_key())

  >>>key2 = Fernet(Fernet.generate_key())

  >>>f = MultiFernet([key1, key2])

  >>>token = f.encrypt(b"Secret message!")

  >>>token
  Out[6]: 'gAAAAABYnKzqNxRAbwP6hMMGmB4eIBhiAR2oVG136Dpive8AhNBdtjwKKiOj_Zaxv8e1dHWp1_WpvktTCT5lRnm9ZnBIK4AoMw=='

  >>>f.decrypt(token)
  Out[7]: 'Secret message!'

  >>>key3 = Fernet(Fernet.generate_key())

  >>>f = MultiFernet([key3, key1, key2])

  >>>f.decrypt(token)
  Out[10]: 'Secret message!'

参考: `<https://zhuanlan.zhihu.com/p/25168804>`_
