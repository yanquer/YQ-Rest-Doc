==============================
ssh-keygen
==============================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


生成公私密钥

如生成rsa秘钥::

  ssh-keygen -t rsa

还有个可以配对使用的, 复制公钥到需要的主机，或其它方式发送公钥过去改名为authorized_keys::

  ssh-copy-id user@host

.. note::

  ssh远程登录并执行指令的时候，authorized里的command参数需要加上 ``&/bin/bash`` 保持登陆::

    #authorized_keys
    command="ls -al & /bin/bash"

  更多可见 `<https://blog.csdn.net/alifrank/article/details/48241699>`_

参数选项
==============================

-m
  指定密钥的格式，PEM（也就是RSA格式）是之前使用的旧格式
-b
  指定密钥长度；
-e
  读取openssh的私钥或者公钥文件；
-C
  添加注释；
-f
  指定用来保存密钥的文件名；
-i
  读取未加密的ssh-v2兼容的私钥/公钥文件，然后在标准输出设备上显示openssh兼容的私钥/公钥；
-l
  显示公钥文件的指纹数据；
-N
  提供一个新密语；
-P
  提供（旧）密语；
-q
  静默模式；
-t
  指定要创建的密钥类型

关于authorized_keys与authorized_keys2
============================================================

authorized_keys vs authorized_keys2

In OpenSSH releases earlier than 3, the sshd man page said::

  The $HOME/.ssh/authorized_keys file lists the RSA keys that are permitted for RSA authentication in SSH protocols 1.3 and 1.5 Similarly,
  the $HOME/.ssh/authorized_keys2 file lists the DSA and RSA keys that are permitted for public key authentication (PubkeyAuthentication) in SSH protocol 2.0.

也就是说在ssh的3版本之前: **authorized_keys2多支持一个DSA加密算法**

中文翻译::

  在版本3之前的OpenSSH中，sshd手册页曾经说过：

  > $ HOME / .ssh / authorized_keys文件列出了SSH协议1.3和1.5中允许进行RSA身份验证的RSA密钥。
  类似地，$ HOME / .ssh / authorized_keys2文件列出了允许进行公共密钥身份验证的DSA和RSA密钥（ SSH协议2.0中的PubkeyAuthentication）。

版本3 的
`发行公告 <http://marc.info/?l=openssh-unix-dev&m=100508718416162&w=2>`_
指出已弃用authorized_keys2，并且所有密钥都应放在authorized_keys文件中。

实际使用过程中openssl 1.1.1的版本中即使只有一个authorized_keys2也可以使用的（其他版本未测试）

登录执行指令
==============================

在公钥文件前加上::

  command="/bin/sh xxx.sh" $pub_key

关于rsa格式秘钥在高版本的生成
==============================

现在使用命令 ``ssh-keygen -t rsa``  生成ssh，默认是以新的格式生成，
id_rsa的第一行变成了 ``“BEGIN OPENSSH PRIVATE KEY”``
而不在是 ``“BEGIN RSA PRIVATE KEY”`` ，
此时用来msyql、MongoDB，配置ssh登陆的话，
可能会报 ``“Resource temporarily unavailable. Authentication by key (/Users/youname/.ssh/id_rsa) failed (Error -16). (Error #35)”``
提示资源不可用，这就是id_rsa 格式不对造成的

解决方法（一）：
------------------------------

使用 ``ssh-keygen -m PEM -t rsa -b 4096`` 来生成

.. note::

  ``-m PEM`` 指定密钥的格式，PEM（也就是RSA格式）是之前使用的旧格式

  ``-b 4096`` 指定密钥长度为4096

  ``-t rsa`` 指定要创建的密钥类型为RSA

原文链接：https://blog.csdn.net/lsp84ch80/article/details/87861990




