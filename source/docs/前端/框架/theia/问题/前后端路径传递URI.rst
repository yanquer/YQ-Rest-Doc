==================================
前后端路径传递URI/URL
==================================

- URI: 资源标识符
- URL: 具体的URI,包含了网络协议信息,如http,https等

前后端通信传递资源路径时,通常都建议使用 URI 而不是 URL

主要原因有:

1. URI表示资源标识符,只关注标识资源,而不限定使用的协议。这更通用。
2. URL是一种具体的URI,包含了网络协议信息,如http,https等。这对资源标识来说是非必需的。
3. 前后端可以使用不同的协议访问同一个资源标识符,URI可以兼容。
4. URI有一个通用的语法格式,方便解析处理。并且可以包含非网络资源,如本地文件路径。
5. URL编码有些字符如空格等会被编码,而URI可以保留原始字符。
6. URI可以方便地映射到不同的具体URL,为应用带来更大灵活性。
7. 许多程序库和框架也推荐使用URI格式表示资源标识符。

URI与URL的相互转换
==================================

.. note::

  此处的URI为 `vscode-uri` 模块下的 `URI`

  theia框架的URI为 ``import URI from '@theia/core/lib/common/uri'``

URI字符串, `scheme + path` 的形式, 如::

  const uriStr = file:///c:/users/bob

URL路径字符串, 如::

  const urlStr = /c:/users/bob

本地路径字符串, 纯路径如::

  const localPathStr = c:/users/bob

URI字符串 ==> URI对象::

  const uriIns = URI.parse(uriStr)

URI字符串 ==> URL对象::

  const urlIns = new URL(uriStr)

  // 如果要获取url字符串
  const urlStr = urlIns.pathname

URI对象转换为本地路径字符串, 比如theia框架有提供Path对象,
是对 ``import URI from 'vscode-uri'`` 进行的一个封装,
那么在theia中可以直接::

  const convertedStr = uriIns.path.fspath()

若非框架环境, 后面再说

URL字符串 ==> URI对象::

  const uriIns = URI.file(urlStr)

  // theia框架提供了
  const uriIns = URI.fromFilePath(urlStr)


.. note::

  有时候字符串可能是被URI编码了, 需要解码::

    // 两种好像都可以, 不记得了
    decodeURIComponent(urlStr)
    decodeURIComponent(uriStr)



.. todo:
  有个 ``import {format} from 'util'``
  格式化字符串。它可以替换字符串中的占位符为对应的参数值
  const msg = util.format('Log: %s %d', 'Message', 123);
  // Log: Message 123

什么时候需要转换?

当URI字符串有问题的时候, 先生成个URL对象, 然后再转换为URI对象::

  // 有个有问题的URI字符串, 比如 file:/c:/users/bob
  const issuesUriStr = 'file:/c:/users/bob'

  const urlStr = decodeURIComponent((new URL(issuesUriStr)).pathname)

  const uriIns = URI.file(urlStr)

theia不通过后端拼接路径
==================================

theia的URI封装的Path对象提供此功能::

  const _uriIns: URI
  const _baseName: string

  // 主要是这一步
  _path: Path = _uriIns.path.join(_baseName)

  _newUriIns: URI = URI.fromFilePath(_path.fspath())



