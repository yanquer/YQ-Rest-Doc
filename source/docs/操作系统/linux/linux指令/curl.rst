============================================
curl
============================================

curl 是常用的命令行工具，用来请求 Web 服务器。
它的名字就是客户端（client）的 URL 工具的意思。

它的功能非常强大，命令行参数多达几十种。如果熟练的话，完全可以取代 Postman 这一类的图形界面工具。

不带有任何参数时，curl 就是发出 GET 请求::

  $ curl https://www.example.com

-A
  `-A` 参数指定客户端的用户代理标头，即 `User-Agent` .
  curl 的默认用户代理字符串是 `curl/[version]`

  将 `User-Agent` 改成 Chrome 浏览器::

    $ curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' https://google.com

  移除 `User-Agent` 标头::

    $ curl -A '' https://google.com

  也可以通过 `-H` 参数直接指定标头，更改 `User-Agent`::

    $ curl -H 'User-Agent: php/1.0' https://google.com
-b
  `-b` 参数用来向服务器发送 Cookie

  生成一个标头`Cookie: foo=bar`，向服务器发送一个名为`foo`、值为`bar`的 Cookie::

    $ curl -b 'foo=bar' https://google.com

  发送两个 Cookie::

    $ curl -b 'foo1=bar;foo2=bar2' https://google.com

  读取本地文件`cookies.txt`，里面是服务器设置的 Cookie（参见`-c`参数），将其发送到服务器::

    $ curl -b cookies.txt https://www.google.com
-c
  `-c` 参数将服务器设置的 Cookie 写入一个文件。

  将服务器的 HTTP 回应所设置 Cookie 写入文本文件 `cookies.txt`::

    $ curl -c cookies.txt https://www.google.com
-d
  `-d` 参数用于发送 POST 请求的数据体

  使用`-d`参数以后，HTTP 请求会自动加上标头 `Content-Type : application/x-www-form-urlencoded`。
  并且会自动将请求转为 POST 方法，因此可以省略 `-X POST`::

    $ curl -d'login=emma＆password=123'-X POST https://google.com/login
    # 或者
    $ curl -d 'login=emma' -d 'password=123' -X POST  https://google.com/login

  `-d` 参数可以读取本地文本文件的数据，向服务器发送.
  如读取`data.txt`文件的内容，作为数据体向服务器发送::

    $ curl -d '@data.txt' https://google.com/login
--data-urlencode
  `--data-urlencode` 参数等同于 `-d`，发送 POST 请求的数据体，
  区别在于会自动将发送的数据进行 URL 编码。

  发送的数据 `hello world` 之间有一个空格，需要进行 URL 编码::

    $ curl --data-urlencode 'comment=hello world' https://google.com/login
-e
  设置 HTTP 的标头 `Referer`，表示请求的来源。

  将`Referer`标头设为 `https://google.com?q=example`::

    curl -e 'https://google.com?q=example' https://www.example.com

  `-H`参数可以通过直接添加标头`Referer`，达到同样效果::

    curl -H 'Referer: https://google.com?q=example' https://www.example.com
-F
  向服务器上传二进制文件

  给 HTTP 请求加上标头`Content-Type: multipart/form-data`，然后将文件`photo.png`作为`file`字段上传::

    $ curl -F 'file=@photo.png' https://google.com/profile

  `-F` 参数可以指定 MIME 类型。
  如指定 MIME 类型为`image/png`，否则 curl 会把 MIME 类型设为 `application/octet-stream`::

    $ curl -F 'file=@photo.png;type=image/png' https://google.com/profile

  `-F`参数也可以指定文件名。
  如原始文件名为`photo.png`，但是服务器接收到的文件名为 `me.png`::

    $ curl -F 'file=@photo.png;filename=me.png' https://google.com/profile
-G
  构造 URL 的查询字符串。

  发出一个 GET 请求，实际请求的 URL 为`https://google.com/search?q=kitties&count=20`。如果省略`--G`，会发出一个 POST 请求::

    $ curl -G -d 'q=kitties' -d 'count=20' https://google.com/search

  如果数据需要 URL 编码，可以结合 `--data--urlencode` 参数::

    $ curl -G --data-urlencode 'comment=hello world' https://www.example.com
-H
  添加 HTTP 请求的标头。
  添加 HTTP 标头 `Accept-Language: en-US`::

    $ curl -H 'Accept-Language: en-US' https://google.com

  添加两个 HTTP 标头::

    $ curl -H 'Accept-Language: en-US' -H 'Secret-Message: xyzzy' https://google.com

  添加 HTTP 请求的标头是 `Content-Type: application/json`，然后用`-d`参数发送 JSON 数据::

    $ curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' https://google.com/login
-i
  打印出服务器回应的 HTTP 标头

  收到服务器回应后，先输出服务器回应的标头，然后空一行，再输出网页的源码::

    $ curl -i https://www.example.com
-I
  向服务器发出 HEAD 请求，然会将服务器返回的 HTTP 标头打印出来。

  输出服务器对 HEAD 请求的回应::

    $ curl -I https://www.example.com

  `--head`参数等同于 `-I`::

    $ curl --head https://www.example.com
-k
  指定跳过 SSL 检测。

  不会检查服务器的 SSL 证书是否正确::

    $ curl -k https://www.example.com
-L
  让 HTTP 请求跟随服务器的重定向。
  curl 默认不跟随重定向::

    $ curl -L -d 'tweet=hi' https://api.twitter.com/tweet
--limit-rate
  `--limit-rate` 限制 HTTP 请求和回应的带宽，模拟慢网速的环境

  将带宽限制在每秒 200K 字节::

    $ curl --limit-rate 200k https://google.com
-o
  `-o` 参数将服务器的回应保存成文件，等同于 `wget` 命令

  将 `www.example.com` 保存成 `example.html`::

    $ curl -o example.html https://www.example.com
-O
  `-O` 参数将服务器回应保存成文件，并将 URL 的最后部分当作文件名。

  将服务器回应保存成文件，文件名为 `bar.html`::

    $ curl -O https://www.example.com/foo/bar.html
-s
  `-s` 参数将不输出错误和进度信息

  一旦发生错误，不会显示错误信息。不发生错误的话，会正常显示运行结果::

    $ curl -s https://www.example.com

  如果想让 curl 不产生任何输出，可以使用下面的命令::

    $ curl -s -o /dev/null https://google.com
-S
  `-S`参数指定只输出错误信息，通常与 `-s` 一起使用。

  命令没有任何输出，除非发生错误::

    $ curl -s -o /dev/null https://google.com
-u
  设置服务器认证的用户名和密码。

  设置用户名为 `bob`，密码为 `12345`， 然后将其转为 HTTP 标头 `Authorization: Basic Ym9iOjEyMzQ1`::

    $ curl -u 'bob:12345' https://google.com/login

  curl 能够识别 URL 里面的用户名和密码, 将其转为上个例子里面的 HTTP 标头::

    $ curl https://bob:12345@google.com/login

  只设置了用户名，执行后，curl 会提示用户输入密码::

    $ curl -u 'bob' https://google.com/login
-v
  输出通信的整个过程，用于调试::

    $ curl -v https://www.example.com

  `--trace` 参数也可以用于调试，还会输出原始的二进制数据::

    $ curl --trace - https://www.example.com
-x
  `-x` 参数指定 HTTP 请求的代理。

  指定 HTTP 请求通过 `myproxy.com:8080` 的 socks5 代理发出::

    $ curl -x socks5://james:cats@myproxy.com:8080 https://www.example.com

  如果没有指定代理协议，默认为 HTTP。

  请求的代理使用 HTTP 协议::

    $ curl -x james:cats@myproxy.com:8080 https://www.example.com
-X
  `-X` 参数指定 HTTP 请求的方法。

  对 `https://www.example.com` 发出 POST 请求::

    $ curl -X POST https://www.example.com

CURL状态码列表

.. csv-table::
  :header: 状态码, 状态原因, 解释
  :delim: |

  0   | 正常访问         |
  1   | 错误的协议       | 未支持的协议。此版cURL 不支持这一协议。
  2   | 初始化代码失败   | 初始化失败。
  3   | URL格式不正确    | URL 格式错误。语法不正确。
  4   | 请求协议错误     |
  5   | 无法解析代理     | 无法解析代理。无法解析给定代理主机。
  6   | 无法解析主机地址 | 无法解析主机。无法解析给定的远程主机。
  7   | 无法连接到主机   | 无法连接到主机。
  8   | 远程服务器不可用 | FTP 非正常的服务器应答。cURL 无法解析服务器发送的数据。
  9   | 访问资源错误     | FTP 访问被拒绝。服务器拒绝登入或无法获取您想要的特定资源或目录。最有可 能的是您试图进入一个在此服务器上不存在的目录。
  11  | FTP密码错误      | FTP 非正常的PASS 回复。cURL 无法解析发送到PASS 请求的应答。
  13  | 结果错误         | FTP 非正常的的PASV 应答，cURL 无法解析发送到PASV 请求的应答。
  14  | FTP回应PASV命令  | FTP 非正常的227格式。cURL 无法解析服务器发送的227行。
  15  | 内部故障         | FTP 无法连接到主机。无法解析在227行中获取的主机IP。
  17  | 设置传输模式为二进制  | FTP 无法设定为二进制传输。无法改变传输方式到二进制。
  18  | 文件传输短或大于预期  | 部分文件。只有部分文件被传输。
  19  | RETR命令传输完成 | FTP 不能下载/访问给定的文件， RETR (或类似)命令失败。
  21  | 命令成功完成     | FTP quote 错误。quote 命令从服务器返回错误。
  22  | 返回正常         | HTTP 找不到网页。找不到所请求的URL 或返回另一个HTTP 400或以上错误。 此返回代码只出现在使用了-f/--fail 选项以后。
  23  | 数据写入失败     | 写入错误。cURL 无法向本地文件系统或类似目的写入数据。
  25  | 无法启动上传     | FTP 无法STOR 文件。服务器拒绝了用于FTP 上传的STOR 操作。
  26  | 回调错误         | 读错误。各类读取问题。
  27  | 内存分配请求失败 | 内存不足。内存分配请求失败。
  28  | 访问超时         | 操作超时。到达指定的超时期限条件。
  30  | FTP端口错误      | FTP PORT 失败。PORT 命令失败。并非所有的FTP 服务器支持PORT 命令，请 尝试使用被动(PASV)传输代替！
  31  | FTP错误          | FTP 无法使用REST 命令。REST 命令失败。此命令用来恢复的FTP 传输。
  33  | 不支持请求       | HTTP range 错误。range "命令"不起作用。
  34  | 内部发生错误     | HTTP POST 错误。内部POST 请求产生错误。
  35  | SSL/TLS握手失败  | SSL 连接错误。SSL 握手失败。
  36  | 下载无法恢复     | FTP 续传损坏。不能继续早些时候被中止的下载。
  37  | 文件权限错误     | 文件无法读取。无法打开文件。权限问题？
  38  | LDAP可没有约束力 | LDAP 无法绑定。LDAP 绑定(bind)操作失败。
  39  | LDAP搜索失败     | LDAP 搜索失败。
  41  | 函数没有找到     | 功能无法找到。无法找到必要的LDAP 功能。
  42  | 中止的回调       | 由回调终止。应用程序告知cURL 终止运作。
  43  | 内部错误         | 内部错误。由一个不正确参数调用了功能。
  45  | 接口错误         | 接口错误。指定的外发接口无法使用。
  47  | 过多的重定向     | 过多的重定向。cURL 达到了跟随重定向设定的最大限额跟
  48  | 无法识别选项     | 指定了未知TELNET 选项。
  49  | TELNET格式错误   | 不合式的telnet 选项。
  51  | 远程服务器的SSL证书 | peer 的SSL 证书或SSH 的MD5指纹没有确定。
  52  | 服务器无返回内容    | 服务器无任何应答，该情况在此处被认为是一个错误。
  53  | 加密引擎未找到      | 找不到SSL 加密引擎。
  54  | 设定默认SSL加密失败 | 无法将SSL 加密引擎设置为默认。
  55  | 无法发送网络数据    | 发送网络数据失败。
  56  | 衰竭接收网络数据    | 在接收网络数据时失败。
  57  |                  |
  58  | 本地客户端证书   | 本地证书有问题。
  59  | 无法使用密码     | 无法使用指定的SSL 密码。
  60  | 凭证无法验证     | peer 证书无法被已知的CA 证书验证。
  61  | 无法识别的传输编码  | 无法辨识的传输编码。
  62  | 无效的LDAP URL   | 无效的LDAP URL。
  63  | 文件超过最大大小    | 超过最大文件尺寸。
  64  | FTP失败          | 要求的FTP 的SSL 水平失败。
  65  | 倒带操作失败     | 发送此数据需要的回卷(rewind)失败。
  66  | SSL引擎失败      | 初始化SSL 引擎失败。
  67  | 服务器拒绝登录   | 用户名、密码或类似的信息未被接受，cURL 登录失败。
  68  | 未找到文件       | 在TFTP 服务器上找不到文件。
  69  | 无权限           | TFTP 服务器权限有问题。
  70  | 超出服务器磁盘空间  | TFTP 服务器磁盘空间不足。
  71  | 非法TFTP操作     | 非法的TFTP 操作。
  72  | 未知TFTP传输的ID | 未知TFTP 传输编号(ID)。
  73  | 文件已经存在     | 文件已存在(TFTP) 。
  74  | 错误TFTP服务器   | 无此用户(TFTP) 。
  75  | 字符转换失败     | 字符转换失败。
  76  | 必须记录回调     | 需要字符转换功能。
  77  | CA证书权限       | 读SSL 证书出现问题(路径？访问权限？ ) 。
  78  | URL中引用资源不存在 | URL 中引用的资源不存在。
  79  | 错误发生在SSH会话   | SSH 会话期间发生一个未知错误。
  80  | 无法关闭SSL连接     | 未能关闭SSL 连接。
  81  | 服务未准备       |
  82  | 无法载入CRL文件  | 无法加载CRL 文件，丢失或格式不正确(在7.19.0版中增加) 。
  83  | 发行人检查失败   | 签发检查失败(在7.19.0版中增加) 。


