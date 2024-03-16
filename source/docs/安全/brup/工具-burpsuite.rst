=====================================
工具-burpsuite
=====================================


.. post:: 2023-02-20 22:36:38
  :tags: brup
  :category: 安全
  :author: YanQue
  :location: CD
  :language: zh-cn


BurpSuite 安装
=====================================

- `官网 <https://portswigger.net/burp/releases>`_ 下载官方包
- 下载注册机
  - `<https://raw.githubusercontent.com/x-Ai/BurpSuite/main/BurpSuiteLoader.jar>`_
  - `<https://raw.githubusercontent.com/x-Ai/BurpSuite/main/burp-keygen-scz.jar>`_
  - `汉化文件 <https://github.com/funkyoummp/BurpSuiteCn/releases/download/V2.0/BurpSuiteCnV>`_

破解
-------------------------------------

打开安装包镜像后，将安装文件单独拉出来（拉出来才可以修改）

右键显示包内容 进入 `Contents/Resources/app` ， 将上述三个jar包复制进去

编辑 `Contents/Info.plist`
在 `<string>-Dexe4j.moduleName=$APP_PACKAGE</string>` 之后插入以下语句::

  <string>-noverify</string>
  <string>-javaagent:$APP_PACKAGE/Contents/Resources/app/BurpSuiteLoader.jar</string>

安装好后复制三个文件到 `/Applications/Burp Suite Enterprise Edition/burp`
（有 burpsuite_pro_v2022.8.1.jar 的目录下）

安装成功后会在应用程序里有一个burp的文件夹，不同版本好像名称有差异

启动::

  cd /Applications/Burp Suite Enterprise Edition/burp; java -noverify -javaagent:BurpSuiteCnV2.0.jar -javaagent:BurpSuiteLoader.jar -Xmx2048m -jar burpsuite_pro_v2022.8.1.jar

此时会有提示激活的图形化界面， 打开 `burp-keygen-scz.jar` 注册机，来做相应的激活

burpsuite使用证书
=====================================

搭建burpsuite服务时，可选使用证书

环境/工具

- MacOS 12.5
- openssl

步骤, 部分可参考 :doc:`/docs/安全/生成TLS(SSL)证书`::

  # 生成rsa私钥，des3算法，1024位强度，ssl.key是秘钥文件名。
  openssl genrsa -des3 -out ssl.key 1024

  # 根据提示输入密码。当前文件夹下生成一个 ssl.key 文件。

  # 删除密码。
  # 这里目录和生成私钥的目录一致
  openssl rsa -in ssl.key -out ssl.key

  # 生成 CSR（证书签名请求）。根据根据刚刚生成的 key 文件来生成证书请求文件
  openssl req -new -key ssl.key -out ssl.csr

  # 依次输入国家、地区、城市、组织、组织单位、Common Name、Email 和密码。其中 Common Name 应该与域名保持一致。密码我们已经删掉了,直接回车即可。

  # 提示：Common Name 就是证书对应的域名地址，我们开发微信小程序时必须要让我们的外链的 https 的域名和证书统一才行。

  # 生成自签名证书。根据以上 2 个文件生成 crt 证书文件，终端执行下面命令：
  # 这里3650是证书有效期(单位：天)。这个大家随意。最后使用到的文件是key和crt文件。
  openssl x509 -req -days 3650 -in ssl.csr -signkey ssl.key -out ssl.crt

  # 到这里我们的证书(ssl.key 和 ssl.crt) 就已经创建成功了可以直接用到 https 的 server 中了。


  # 在代码中使用证书：
  https
      .createServer(
          {
              key: fs.readFileSync("./cert_key/ssl.key"),
              cert: fs.readFileSync("./cert_key/ssl.crt")
          },
          app
      )
      .listen(1993);







