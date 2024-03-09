==================
aiohttp
==================

:官网:: `Welcome to AIOHTTP <https://docs.aiohttp.org/en/stable/>`_

**异步的网络连接库** , 内部存在 asyncio 库的调用, 如 run_in_executor

安装::

  pip install aiohttp

默认的编码库 charset-normalizer 较慢, 可使用 cchardet 替代::

  $ pip install cchardet

算了, 现在 cchardet 已经没维护了, 不支持大于 3.10 的版本.

建议安装 aiodns 库, 更快的 dns 解析::

  pip install aiodns

aiohttp.web.Application
====================================

创建web服务器所用类

增加路径映射::

  app = Application()
  app.router.add_static()

除了 add_static, 还有 add_get 等

或者使用直接给整个路径的列表::

  app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
  ])

server处理
==================

一个server处理示例::

  from aiohttp import web

  async def handle(request):
      name = request.match_info.get('name', "Anonymous")
      text = "Hello, " + name
      return web.Response(text=text)

  app = web.Application()
  app.add_routes([web.get('/', handle),
                  web.get('/{name}', handle)])

在aiohttp的web应用中,handler函数接受的request是aiohttp.web.Request对象。

aiohttp.web.Request对象包含了客户端发来的HTTP请求的所有详情,我们可以从中获取:
- 请求方法(method)
- 请求URL(url)
- 请求头(headers)
- 请求体(body)
- Query参数(query)
- 等等

可以这样处理::

  async def handle_rpc(request: aiohttp.web.Request):
    method = request.method
    url = request.url
    headers = request.headers
    query = request.query  # 获取query参数

    # 获取请求体
    data = await request.text()  # 获取字符串
    data = await request.read()  # 获取byte流
    data = await request.json()  # 获取JSON

    # 构造响应
    response = aiohttp.web.Response(text='result')
    return response

举例
==================

客户端代码举例::

  import aiohttp
  import asyncio

  async def main():

      async with aiohttp.ClientSession() as session:
          async with session.get('http://python.org') as response:

              print("Status:", response.status)
              print("Content-type:", response.headers['content-type'])

              html = await response.text()
              print("Body:", html[:15], "...")

  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())

server 代码举例::

  from aiohttp import web

  async def handle(request):
      name = request.match_info.get('name', "Anonymous")
      text = "Hello, " + name
      return web.Response(text=text)

  app = web.Application()
  app.add_routes([web.get('/', handle),
                  web.get('/{name}', handle)])

  if __name__ == '__main__':
      web.run_app(app)

使用 get 请求举例::

  async def main_aiohttp():

    async with aiohttp.request(method='get', url='https://docs.aiohttp.org/en/stable/') as r:
        print(r)

  if __name__ == '__main__':
      import aiohttp
      asyncio.run(main_aiohttp())


一些说明
==================

最近开发的时候遇到网络库的问题, 背景如下:

公司自己有基于 C 的 GUI 库, 这个库被编译为了 Python 框架, 然后重写了 asyncio 的事件循环(为了结合这个框架的事件循环)

发现在使用 ``loop.run_in_executor`` 时, 且传入的函数为 requests 的调用时::

  def try_connect(address: str):
    try:
      with requests.get(address):
        return True
    expect:
      return False

且在 虚拟机/云桌面 运行时, 会存在异常, 此处的 expect 可以说是无效, 看着是这个异常导致后面哪有问题.
也看不了堆栈信息.

debug 又不会出现这个问题.

总结下来就是, 丢到线程池执行器内部执行, 且 requests.get 存在异常时, 且平台为虚拟机时, 一定会触发.
后面有空看看官方自己的事件循环有没有这个问题.

.. todo: 看看官方事件循环有没有问题

**最后换了 aiohttp 就解决了.**

还不确定是 requests 库本身的问题, 还是公司框架内部的事件循环有问题




