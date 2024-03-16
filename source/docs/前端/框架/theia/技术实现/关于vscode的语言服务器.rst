====================================
关于vscode的语言服务器
====================================


.. post:: 2024-03-08 23:31:08
  :tags: 框架, theia, 技术实现
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


主要是与插件相关的吧.

vscode为了解决以下问题:

- 语言服务器若要同时兼容所有语言, 太过臃肿
- 浪费资源
- 与编辑器标准不一致, 导致每个语言的服务器都要适配一种编辑器

所有制定了语言服务器标准协议LSP(Language Server Protocol), 保证了

- 每一种语言服务器都能适配所有遵照此LSP标准的编辑器

相关github地址:

- https://github.com/Microsoft/vscode-languageserver-node

原文介绍:

- https://code.visualstudio.com/api/language-extensions/language-server-extension-guide#why-language-server

实现自定义的语言服务器
====================================

主要两个方面:

- 语言服务器客户端: 需要实现vscode的相应api
- 语言服务器服务端: 实际的语法分析(单独的进程)



