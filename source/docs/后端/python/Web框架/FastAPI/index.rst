============================================
FastAPI
============================================


.. post:: 2024-03-09 18:21:01
  :tags: python, Web框架, FastAPI
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


- 官网文档: `FastAPI <https://fastapi.tiangolo.com/zh/>`_
- 菜鸟: `FastAPI教程 <https://www.runoob.com/fastapi/fastapi-tutorial.html>`_

.. note::

  如果你正在开发一个在终端中运行的命令行应用而不是 web API，不妨试下 `Typer <https://typer.tiangolo.com/>`_.
  Typer 是 FastAPI 的小同胞。它想要成为命令行中的 FastAPI。

关键特性
  - 快速：可与 NodeJS 和 Go 并肩的极高性能（归功于 Starlette 和 Pydantic）。最快的 Python web 框架之一。
  - 高效编码：提高功能开发速度约 200％ 至 300％。*
  - 更少 bug：减少约 40％ 的人为（开发者）导致错误。*
  - 智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
  - 简单：设计的易于使用和学习，阅读文档的时间更短。
  - 简短：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
  - 健壮：生产可用级别的代码。还有自动生成的交互式文档。
  - 标准化：基于（并完全兼容）API 的相关开放标准：OpenAPI (以前被称为 Swagger) 和 JSON Schema。

FastAPI 特点
  - 高性能： 基于Starlette和Pydantic，利用异步（asynchronous）编程，提供出色的性能。
  - 自动文档生成： 自动生成交互式API文档，支持Swagger UI和ReDoc，让API的理解和测试更加直观。
  - 类型注解支持： 利用Python的类型提示，提供更严格的输入验证和更好的代码提示。
  - 异步支持： 支持异步请求处理，使得处理IO密集型任务更加高效。
FastAPI 适用场景
  - 构建API后端： 用于构建RESTful API，支持前后端分离的Web应用。
  - 微服务架构： 可以作为微服务的后端框架，支持快速开发和部署。
  - 数据处理API： 适用于处理数据，接收和返回JSON数据。
  - 实时通信： 支持WebSocket，适用于实时通信场景。
为什么选择 FastAPI？
  - Pythonic： 使用Python的自然语法和类型提示，降低学习曲线。
  - 性能优越： 利用异步编程和底层的Starlette框架，提供卓越的性能。
  - 文档友好： 自动生成交互式文档，减少文档维护的工作量。
  - 生态系统： 基于Python生态系统，可以方便地集成各种库和工具。

.. toctree::
  :maxdepth: 1

  结构详解
  安装配置
  简单使用
  交互式API文档
  基本路由
  请求和响应
  FastAPI-Pydantic模型
  路径操作依赖项
  表单数据
  常见问题









