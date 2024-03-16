============================
frida
============================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: `https://frida.re/docs/home/`

安装::

  pip install frida

frida是一款基于python + javascript 的hook框架，
可运行在androidioslinuxwinosx等各平台，主要使用动态二进制插桩技术

插桩技术
  插桩技术是指将额外的代码注入程序中以收集运行时的信息，可分为两种：

  - 源代码插桩[Source Code Instrumentation(SCI)]：额外代码注入到程序源代码中
  - 二进制插桩（Binary Instrumentation）：额外代码注入到二进制可执行文件中。

    - 静态二进制插桩[Static Binary Instrumentation(SBI)]：
      在程序执行前插入额外的代码和数据，生成一个永久改变的可执行文件
    - 动态二进制插桩[Dynamic Binary Instrumentation(DBI)]：
      在程序运行时实时地插入额外代码和数据，对可执行文件没有任何永久改变。

Frida 是一个用于动态分析和修改应用程序的工具，
它提供了一种在运行时注入代码到目标应用程序中的方式。
在 Python 中，Frida 提供了一个名为 "frida" 的模块，用于与 Frida 运行时进行交互。

使用 Frida，你可以在目标应用程序的运行过程中实时地监视和修改函数调用、修改内存中的数据、拦截网络通信等。
它支持多种平台，包括 Android、iOS、Windows、macOS 和 Linux。

在 Python 中，通过导入 "frida" 模块，
你可以编写代码来创建 Frida 会话、加载目标应用程序、注入 JavaScript 或者使用 Python API 进行交互。
这使得你可以利用 Frida 来进行应用程序的动态分析、逆向工程、漏洞挖掘等任务。

下面是一个示例代码片段，展示了如何使用 "frida" 模块创建 Frida 会话和加载目标应用程序::

  import frida

  # 创建 Frida 会话 , 也就是附加到进程
  session = frida.attach("app.exe")

  # 打印目标应用程序的进程 ID
  print("Process ID:", session.pid)

  # ...
  # 执行其他操作，如加载脚本、拦截函数调用等
  # ...

  # 关闭会话
  session.detach()

需要注意的是，Frida 还提供了其他语言的支持，
如 JavaScript、C#、Swift 等，
使得开发者可以根据自己的喜好和需求选择合适的编程语言进行应用程序的动态分析和修改。

.. note::

  比如侵入到微信进程中提取表情包: `https://github.com/K265/frida-wechat-sticker/tree/main`

FRIDA一般在系统层面的调用都是JS代码.
frida的注入脚本是JavaScript， 因此我们后面都是通过js脚本来操作设备上的Java代码的。

其他点:
  - 由于js代码注入时可能会出现超时的错误， 为了防止这个问题，
    我们通常还需要在最外面包装一层 ``setImmediate(function(){})`` 的代码。

frida-工具
============================

共有6个：

- frida CLI: 是一个交互式解释器（REPL），他的交互形式跟IPython很类似。
- frida-ps: 用于列出进程的一个命令行工具，当我们需要跟远程系统进行交互的时候，这个是非常有用的。
- frida-trace
- frida-discover
- frida-ls-devices
- frida-kill

常用输出
============================

console-普通打印
  与普通JS输出一致::

    console.log('xxx')
    console.warn('xxx')
    console.error('xxx')

hexdump-打印内存地址信息
  target参数可以是ArrayBuffer或者NativePointer,
  而options参数则是自定义输出格式可以填这几个参数offset、lengt、header、ansi。

  示例::

    var libc = Module.findBaseAddress('libc.so');
    console.log(hexdump(libc, {
      offset: 0,
      length: 64,
      header: true,
      ansi: true
    }));

send回调-Python
============================

send是在python层定义的on_message回调函数，
jscode内所有的信息都被监控script.on('message', on_message)，
当输出信息的时候on_message函数会拿到其数据再通过format转换，
其最重要的功能也是最核心的是能够直接将数据以json格式输出，
当然数据是二进制的时候也依然是可以使用send::

  # -*- coding: utf-8 -*-
  import frida
  import sys

  def on_message(message, data):
      if message['type'] == 'send':
          print("[*] {0}".format(message['payload']))
      else:
          print(message)

  jscode = """
      Java.perform(function ()
      {
          var jni_env = Java.vm.getEnv();
          console.log(jni_env);
          send(jni_env);
      });
  """

  process = frida.get_usb_device().attach('com.roysue.roysueapplication')
  script = process.create_script(jscode)
  script.on('message', on_message)
  script.load()
  sys.stdin.read()

运行脚本效果如下::

  roysue@ubuntu:~/Desktop/Chap09$ python Chap03.py
  [object Object]
  [*] {'handle': '0xdf4f8000', 'vm': {}}

可以看出这里两种方式输出的不同的效果，console直接输出了[object Object]，无法输出其正常的内容，因为jni_env实际上是一个对象，但是使用send的时候会自动将对象转json格式输出

参考:

- `FRIDA-API使用篇：rpc、Process、Module、Memory使用方法及示例 <https://zhuanlan.zhihu.com/p/101401252>`_
- `详解Hook框架frida，让你在逆向工作中效率成倍提升 <https://zhuanlan.zhihu.com/p/41662447>`_
- 看起来最推荐: `<https://juejin.cn/post/7308240524964134924>`_

待看

- `hook工具frida原理及使用, Java程序使用 <https://www.jianshu.com/p/51e6aef175a2>`_


