============================
openssl
============================

- 常用指令可见: https://www.gy328.com/ref/docs/openssl.html
  若无法访问可见: :download:`OpenSSL参考手册 </resources/pdf/OpenSSL 参考手册 & openssl 快速入门 - 菜鸟教程.pdf>`
- 官网: https://www.openssl.org

强大的安全套接字层密码库, 利用它的随机功能来生成可以用作密码的随机字母字符串::

  openssl rand -base64 10
  # nU9LlHO5nsuUvw==

  # standard 标准
  # digest 消化 摘要
  # cipher 加密

OpenSSL有两种运行模式：交互模式和批处理模式。

直接输入openssl回车进入交互模式，输入带命令选项的openssl进入批处理模式。

OpenSSL整个软件包大概可以分成三个主要的功能部分：密码算法库、SSL协议库以及应用程序。OpenSSL的目录结构自然也是围绕这三个功能部分进行规划的。

对称加密算法
============================

OpenSSL一共提供了8种对称加密算法，其中7种是分组加密算法，仅有的一种流加密算法是RC4。这7种分组加密算法分别是AES、DES、Blowfish、CAST、IDEA、RC2、RC5，都支持电子密码本模式（ECB）、加密分组链接模式（CBC）、加密反馈模式（CFB）和输出反馈模式（OFB）四种常用的分组密码加密模式。其中，AES使用的加密反馈模式（CFB）和输出反馈模式（OFB）分组长度是128位，其它算法使用的则是64位。事实上，DES算法里面不仅仅是常用的DES算法，还支持三个密钥和两个密钥3DES算法。

非对称加密算法
============================

OpenSSL一共实现了4种非对称加密算法，包括DH算法、RSA算法、DSA算法和椭圆曲线算法（EC）。DH算法一般用户密钥交换。RSA算法既可以用于密钥交换，也可以用于数字签名，当然，如果你能够忍受其缓慢的速度，那么也可以用于数据加密。DSA算法则一般只用于数字签名。

信息摘要算法
============================

OpenSSL实现了5种信息摘要算法，分别是MD2、MD5、MDC2、SHA（SHA1）和RIPEMD。SHA算法事实上包括了SHA和SHA1两种信息摘要算法，此外，OpenSSL还实现了DSS标准中规定的两种信息摘要算法DSS和DSS1。

密钥和证书管理
============================

密钥和证书管理是PKI的一个重要组成部分，OpenSSL为之提供了丰富的功能，支持多种标准。

首先，OpenSSL实现了ASN.1的证书和密钥相关标准，提供了对证书、公钥、私钥、证书请求以及CRL等数据对象的DER、PEM和BASE64的编解码功能。OpenSSL提供了产生各种公开密钥对和对称密钥的方法、函数和应用程序，同时提供了对公钥和私钥的DER编解码功能。并实现了私钥的PKCS#12和PKCS#8的编解码功能。OpenSSL在标准中提供了对私钥的加密保护功能，使得密钥可以安全地进行存储和分发。

在此基础上，OpenSSL实现了对证书的X.509标准编解码、PKCS#12格式的编解码以及PKCS#7的编解码功能。并提供了一种文本数据库，支持证书的管理功能，包括证书密钥产生、请求产生、证书签发、吊销和验证等功能。

事实上，OpenSSL提供的CA应用程序就是一个小型的证书管理中心（CA），实现了证书签发的整个流程和证书管理的大部分机制。

`<openssl用法详解> https://www.cnblogs.com/yangxiaolan/p/6256838.html`


使用openssl生成密码::

  ┌──(yanque㉿3675b5ebb8ce)-[~/test]
  └─$ openssl passwd -1 -salt admin 123456
  $1$admin$LClYcRe.ee8dQwgrFc5nz.

其中::

  passwd 表示生成密码
  -1 表示使用md5算法
  -salt 表示随机使用一个字符串加盐
  admin 用户名明文
  123456 用户密码明文

命令说明
============================

- req:生成证书签名请求(CSR)。用于申请证书。
- x509:X.509证书格式相关操作。如签名CSR生成证书、签名其他证书等。
- genrsa:生成RSA私钥和公钥。

举个例子::

  # 生成2048位RSA私钥
  openssl genrsa -out key.pem 2048

  # 生成CSR
  openssl req -out csr.pem -newkey rsa:2048 -nodes -keyout key.pem

  # 使用CA证书和私钥签名CSR生成证书
  openssl x509 -req -in csr.pem -CA ca.crt -CAkey ca.key -out cert.pem

通用选项:

-in       从哪个文件读取输入, 比如 server.key
-out      指定将结果输出到文件

genrsa
----------------------------

生成RSA私钥和公钥

-des3     指定使用des3算法
-aes256   使用aes256对密钥文件进行对称加密

rsa
----------------------------

-pubout   当需要根据私钥生成公钥时, 使用此选项
-aes256   使用aes256对密钥文件进行对称加密

req
----------------------------

请求生成证书签名请求文件

-new        指定新生成证书签名请求文件
-key        指定签名时, 使用的私钥, 如server.key
-keyout     直接一步生成证书或证书请求与密钥时, 使用此选项指定密钥名称
-nodes      指定密钥文件不加密
-passout    若需要加密, 命令行指定密码, 格式: ``pass:密码`` , 否则可在交互式界面手动输入
-newkey     指定算法, 格式: ``<algorithm>:<bits>``,
            即 ``<算法>:<长度>``, 若不指定加密方式encryption,
            私钥将以明文保存, 所以通常会使用如aes256的对称加密算法进行私钥的加密, 提高安全性.
            如: rsa:3048, ec:2048.

其他::

  -x509       直接使用该CSR生成自签名证书, 而不需要第三方CA签名(-out的结果就是证书)

ca
----------------------------

作为ca机构对 `证书签名请求文件` 进行签名

-cert               使用的证书
-keyfile            使用的私钥

x509
----------------------------

X.509证书格式相关操作。如签名CSR生成证书、签名其他证书等。

-CAform     指定证书格式
-CA         ca机构所使用的证书, 需要为PEM格式, 否则需用-CAform指定格式
-CAkeyform  指定密钥格式
-CAkey      ca机构所使用的私钥, 需要为PEM格式, 否则需用-CAkeyform指定格式
-days       指定证书有效期
-signkey    自签名时, 使用此选项指定ca密钥
-text       输出证书信息
-noout      不输出证书, 一般与 -text一起使用
-CAcreateserial
            在签发新证书时自动创建证书序列号文件
            为了简化 OpenSSL 中证书签发流程,自动完成序列号文件的创建
            (在ubuntu上测试时srl后缀的文件)

例如查看证书信息::

  openssl x509 -in xxx.crt -text -noout

version
----------------------------

查看版本及相关信息

如linux查看openssl安装目录(不适用mac)::

  openssl version -a | grep OPENSSLDIR

用例: Mac 上制作 SSL 证书
============================

背景: 搭建burpsuite服务时，可选使用证书

环境: MacOS 12.5, openssl

生成rsa私钥，des3算法，1024位强度，ssl.key是秘钥文件名::

  openssl genrsa -des3 -out ssl.key 1024

根据提示输入密码。当前文件夹下生成一个 ssl.key 文件。

删除密码, 这里目录和生成私钥的目录一致::

  openssl rsa -in ssl.key -out ssl.key

生成 CSR（证书签名请求）. 根据根据刚刚生成的 key 文件来生成证书请求文件::

  openssl req -new -key ssl.key -out ssl.csr

依次输入国家、地区、城市、组织、组织单位、Common Name、Email 和密码。
其中 Common Name 应该与域名保持一致。密码我们已经删掉了,直接回车即可。

.. note::

  Common Name 就是证书对应的域名地址，我们开发微信小程序时必须要让我们的外链的 https 的域名和证书统一才行。

生成自签名证书。根据以上 2 个文件生成 crt 证书文件，终端执行下面命令::

  openssl x509 -req -days 3650 -in ssl.csr -signkey ssl.key -out ssl.crt

这里3650是证书有效期(单位：天)。这个大家随意。最后使用到的文件是key和crt文件。
到这里我们的证书(ssl.key 和 ssl.crt) 就已经创建成功了可以直接用到 https 的 server 中了。

在代码中使用证书::

  https
      .createServer(
          {
              key: fs.readFileSync("./cert_key/ssl.key"),
              cert: fs.readFileSync("./cert_key/ssl.crt")
          },
          app
      )
      .listen(1993);

详情介绍
============================

见:

.. toctree::

  openssl/index



