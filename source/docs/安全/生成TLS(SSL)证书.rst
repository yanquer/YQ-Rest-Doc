===========================
生成TLS(SSL)证书
===========================

openssl见: :doc:`/docs/操作系统/linux/linux指令/openssl`

- SSL: Secure Sockets Layer
- TLS: Transport Layer Security

TLS使用非对称加密算法, 通常是RSA算法. 公钥、私钥、签名信息共同组成证书.

签名信息包括如组织信息、CA机构、过期时间、版本等等一切能被客户端识别的信息

TLS
===========================

TLS全称Transport Layer Security，是⽤于在联⽹计算机之间建⽴经过身份验证和加密的链接的协议。
其前身是SSL(Secure Sockets Layer)，最初是由⽹景公司（Netscape）研发，
于1999年被IETF（The Internet Engineering Task Force - 互联⽹⼯程任务组）标准化，定义为TLS 1.0 。
⽬前最新版本为2018年发布的TLS 1.3，详情参⻅RFC 8446。

TLS运⾏在TCP/IP层之上、应⽤层之下，为应⽤程序提供加密数据通道。HTTPS实际上就是HTTP
over SSL，它使⽤默认端⼝443，⽽不是像HTTP那样使⽤端⼝80来和TCP/IP进⾏通信。HTTPS协
议使⽤SSL在发送⽅把原始数据进⾏加密，然后在接受⽅进⾏解密，加密和解密需要发送⽅和接受
⽅通过交换共知的密钥来实现，因此，所传送的数据不容易被⽹络⿊客截获和解密。

TLS(SSL)证书
===========================

TLS使⽤⾮对称加密算法，通常情况下是RSA算法，所以TLS中有私钥和公钥。
公钥、私钥和签名信息共同组成⼀个证书，此处的签名信息包含诸多杂项，
⽐如组织信息、CA机构、过期时间、版本等等⼀切能被客户端识别的信息。

TLS证书并⾮私有格式，⽽是使⽤X.509证书。X.509 是公钥证书、数字⽂档的标准格式，他遵循
链式签名原则。可安全地将加密密钥对与身份（如⽹站、个⼈或组织）相关联，详情参⻅RFC
5280。X.509证书使⽤场景相当⼴泛，包括但不限于以下⼏种：

•  ⽤于经过身份验证和加密的 Web 浏览的 SSL/TLS 和 HTTPS
•  通过 S/MIME 协议签名和加密的电⼦邮件
•  ⽂件签名
•  客户端认证
•  政府颁发的电⼦身份证

文件格式说明
===========================

使用PKCS（The Public-Key Cryptography Standards）标准:

CA：
  证书认证中心；
  收到证书后需要去CA验证正确性、真实性、有效期等. 所以在公网上的通信, 一般都是需要拿自己的 **.csr** 文件去官方CA机构签名的.
  CA自身的分发及安全保证，一般是通过一些权威的渠道进行的，比如操作系统会内置一些官方的CA、浏览器也会内置一些CA.

  根证书实际上是⾃签名证书，是CA机构颁发给⾃⼰的证书，是信任链的起始点。
X.509:
  一种通用的证书格式, 定义公钥证书格式的标准, 包含证书持有人的公钥, 加密算法等信息;
pkcs1 ~ pkcs12:
  公钥加密(非对称加密)的一种标准(Public Key Cryptography Standards), 一般存储为 `*.pN`, 是包含证书和密钥的封装格式;
.key:
  私钥文件，通常使用rsa算法，私钥需要自己保存，无需提交给CA机构
.csr:
  证书签名请求（证书请求文件, certificate signing request），含有持有人的信息如国家、邮件、域名等. 生成该文件时需要用到自己的私钥。
.crt:
  CA认证后的证书文件，certificate的缩写, 此格式一般用于 Linux;
  存储格式可以是 **.pem** 的Base64, 也可以是 **.der** 的二进制;
  存储内容为公钥信息 + 额外的其他信息（比如所属的实体，采用的加密解密算法等）;
.cer:
  与 **.crt** 一致(只是使用平台的差别), 都源于 "certificate", 一般用于 Windows;
.crl:
  证书吊销列表，Certificate Revocation List的缩写
.pem:
  "Privacy-Enhanced Mail", 直译过来就是“隐私增强邮件”.
  证书或密钥的Base64文本存储格式, 可以单独存放证书或密钥, 也可以同时存放证书和密钥, 使用特定的开头和结尾行来标识内容类型(证书/密钥)。
  (与windows下使用.pfx类似，不同的是.pem使用base64字符存储，而.pfx使用二进制存储).
.pfx:
  微软IIS的实现;
.jks:
  Java的keytool实现的证书格式;
.der:
  "Distinguished Encoding Rules"，直译为“可分辩编码规则”. 证书的二进制存储格式.
  最流行的编码格式.
  将 **.der** 转换为 **Base64** 编码则是 **.pem** 文件.

总得来说这些文件都与X.509证书和密钥文件有关，从文件编码上分，只有两大类:

* PEM格式：使用Base64 ASCII进行编码的纯文本格式
* DER格式：二进制格式

.. sidebar:: 文件实际内容查看与转换

  假设有一个baidu.crt文件， 这个crt文件的实际格式其实是pem(Base64格式),
  有一个der格式的文件baidu.der(二进制格式)想要看到这两个文件的实际内容，可以使用命令::

    openssl x509 -in baidu.crt -text -noout
    openssl x509 -inform der -in baidu.der -text -noout

  两者文件的转化，使用命令::

    # pem转der
    openssl x509 -outform der -in baidu.pem -out baidu.der
    # der转pem
    openssl x509 -inform der -in baidu.der -out baidu.crt

而CRT, CER，KEY这几种证书和密钥文件，在存储为物理文件时，既可以是PEM格式，也可以DER格式。

* CER：一般用于windows的证书文件格式
* CRT：一般用于Linux的证书，包含公钥和主体信息
* KEY：一般用于密钥，特别是私钥

对文件的加密解密
===========================

生成公私钥对
---------------------------

  我们生成一个RSA的公钥和密钥对::

    openssl genpkey -algorithm rsa -out rsa_private.key

  从该文件中，提取出公钥::

    openssl rsa -pubout -in rsa_private.key  -out rsa_pub.key

文件加/解密
---------------------------

先生成一个测试文件::

  echo "a test" > text.txt

对该文件进行加密, 采用公钥对文件进行加密::

  openssl rsautl -encrypt -in text.txt -inkey rsa_pub.key -pubin -out text.en

采用私钥解密文件::

  openssl rsautl -decrypt -in text.en -inkey rsa_private.key
  a test

既然是非对称加密，那我们尝试下用私钥加密，用公钥解密。
这里需要注意的是，私钥加密在openssl中对应的是-sign这个选项，公钥解密对应的是-verify这个选项，如下：

用私钥对文件进行加密（签名）::

  openssl rsautl -sign -in text.txt -inkey rsa_private.key -out text.en

用公钥对文件进行解密（校验）::

  openssl rsautl -verify -in text.en -inkey rsa_pub.key -pubin
  this is a test

.. note::

  到这里可以看出这是有其他安全问题的: 公钥是公开分发的，
  你无法确定你收到的公钥是真实的, 是没有经过篡改的.

服务器证书的生成
===========================

生成CA根证书(模拟一个CA机构)
------------------------------------------------------

步骤:
  a. 生成CA私钥（.key）
  #. 生成CA证书请求（.csr）
  #. 自签名得到根证书（.crt）

大致指令如下::

  # Generate CA private key
  openssl genrsa -out ca.key 2048

  # Generate CSR
  # 这一步生成.csr文件时，需要在提示下输入组织相关的信息
  openssl req -new -key ca.key -out ca.csr

  # Generate Self Signed certificate（CA 根证书）
  openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt

.. note::

  一般内网使用就使用自签名的证书, 公网用才会向CA机构申请

生成用户证书
---------------------------

步骤:
  a. 生成私钥（.key）
  #. 生成证书请求（.csr）
  #. 用CA根证书签名得到证书（.crt）

大致指令如下::

  # private key, 可以通过 `-passout pass:密码` 来指定密钥密码
  $openssl genrsa -des3 -out server.key 1024

  # 若需要生成公钥
  $openssl rsa -in server.key -pubout -out server_public.pem

  # generate csr
  $openssl req -new -key server.key -out server.csr

  # generate certificate
  # 使用了根证书ca.crt以及对应的私钥ca.key来进行签名，而不是用户的私钥server.key
  $openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key

.. note:: 生成.pem文件

  有时需要用到pem格式的证书，可以用以下方式合并证书文件（crt）和私钥文件（key）来生成::

    cat server.crt server.key > server.pem

在创建证书的时候，各个值的设定可以是任意的，但是”Common Name“的值通
常要包含服务器的 DNS 主机名。如果你只是在本机测试，那么就使用”localhost“，否
则使用服务器的域名。

:参考:: https://zhuanlan.zhihu.com/p/423506052

或者用最少指令完成从ca签发到服务器证书生成::

  # 生成CA证书和私钥, -nodes表示不加密, 默认是会加密的(就得输入密码才能进入下一步)
  # 若不是用 -nodes, 可以直接在命令行设置密码: `-passout pass:密码`
  # openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ca.key -out ca.crt
  # -x509 表示直接使用该CSR生成自签名证书,而不需要第三方CA签名
  # -newkey表示生成新的私钥, rsa:2048 表示指定rsa算法, 长度为2048
  openssl req -x509 -days 365 -newkey rsa:2048 -keyout ca.key -out ca.crt

  # 作为CA,签名客户端证书
  openssl req -newkey rsa:2048 -nodes -keyout server.key -out server.csr
  openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -days 365 -out server.crt

还可以启动一个SSL/TLS服务器(不过不知道咋用)::

  # 或者服务器指定CA证书和私钥,以CA身份运行,验证客户端证书
  # 本地启动一个SSL/TLS服务器，并在这个服务器上提供4433端口用于加密通信
  openssl s_server -accept 4433 -cert ca.crt -key ca.key

