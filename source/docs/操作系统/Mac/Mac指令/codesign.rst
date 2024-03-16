====================
codesign
====================


.. post:: 2023-02-20 22:06:49
  :tags: Mac, Mac指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


创建和管理证书

用法::

  codesign -s identity [-fv*] [-o flags] [-r reqs] [-i ident] path ...    # 签名
  codesign -v [-v*] [-R=<req string>|-R <req file path>] path|[+]pid ...  # 验证
  codesign -d [options] path ...          # 内容显示
  codesign -h pid ...                     # 主机路径显示
  codesign --validate-constraint path ... # 检查提供的约束plist (check the supplied constraint plist)

说明:

-s
  签名
-f
  force, 强制重新签名
-i
  表示修改签名参数 Identifier
-o
  修改flags
-d
  是display展示签名信息的意思
-v
  是verbose的意思，越多的verbose显示信息越多，通常3个就已经足够了 ``-vvv``
--entitlements
  授权机制 entitements信息

查看WeChat的签名::

  codesign -d -vvv WeChat.app

参考: `codesign的使用 <https://www.jianshu.com/p/0124f10b2e00>`_


