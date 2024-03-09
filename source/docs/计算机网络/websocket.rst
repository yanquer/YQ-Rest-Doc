=============================
websocket
=============================

url表示常以 `ws` 开头, 或 `wss` 开头, 如::

  wss://127.0.0.1:8080/

`ws` 与 `wss` 区别就是后者多了个加密, 就像 `http` 与 `https` 一样

包含的消息头
=============================

Sec-Websocket-key
  WebSocket握手过程中的一个关键消息头.

  - 标识这是一个WebSocket连接请求,而不是普通的HTTP请求
  - 用来计算Sec-WebSocket-Accept的值,以验证连接.
    在WebSocket握手时,客户端发送一个请求到服务器,请求中包含一个随机生成的Sec-WebSocket-Key.
    服务器收到这个key后,需要按照一定算法计算出一个hash值,放到Sec-WebSocket-Accept响应头中返回给客户端.
    客户端收到响应后,会用相同的算法计算hash值,并比对是否和服务器返回的一致。如果一致,则说明服务器支持WebSocket,握手成功.
    这个过程可以防止普通HTTP客户端意外接入WebSocket服务器.


