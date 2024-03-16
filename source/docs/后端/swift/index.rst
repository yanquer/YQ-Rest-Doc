===============================
swift
===============================


.. post:: 2024-03-09 18:21:01
  :tags: swift
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: `https://www.swift.org`

官网API文档: `https://developer.apple.com/documentation/technologies`

官网教程只有英文

一个用于在Apple设备上开发的语言

现在基本是 Object-C 后的接替了

安装
  Mac上直接安装Xcode就行了, 自带Swift.

  其他平台可参考: `https://www.swift.org/install/`

Swift内置了一个包管理, 能够更简单的导入,
包索引查询: `https://swiftpackageindex.com`

一些网站
  - 民间(NGO, Non-Governmental Organization)中文社区: `https://swiftgg.team`
  - 民间Swift语法中文版(相对更新慢一点): `https://gitbook.swiftgg.team/swift/`
  - 民间Swift 基本约定译文: `https://github.com/SketchK/the-swift-api-design-guidelines-in-chinese`

.. note::

  swift 坑比较多, 资料也比较少...

  打算做一个快捷键的, 东西太少

  找到个可以借鉴的项目: ``git clone https://github.com/tkgka/Switcher.git``

  git地址: `https://github.com/tkgka/Switcher`

.. note::

  国内NGO就是社会组织

.. toctree::
  :maxdepth: 1

  swift3.x升级到5.x
  包管理工具pod
  官方库
  三方库
  基本语法
  命令行创建并运行项目
  增加依赖
  事件类型
  Apple证书类型
  swift结构体与类区别
  xcode15新功能
  DEBUG条件
  Xcode的Info配置
  Xcode-分发打包
  Xcode删除掉强制证书
  属性包装器
  异步

访问C头文件的几种方式

.. toctree::
  :maxdepth: 1

  使用modulemap导入C++框架
  桥接导入C
  使用SPM(Swift Package Manager)

备注
===============================

对于MacOS

- 要使App全局显示, 只有设置 Info 为 ``Application is agent (UIElement)``,
  比如显示在其他全屏App上.

  这是用其他语言暂时无法实现的...
- 单独的 `Swift-View` 如果要作为一个弹出窗体, 需要转换为 `NSWindow`
- 对于单独的 `NSWindow`, 直接给 `delegate` 会存在问题...
- 有个一直未解决的问题, 本地构建的App, 重新构建后, 识别不了上个版本获取的权限, 比如辅助功能...





