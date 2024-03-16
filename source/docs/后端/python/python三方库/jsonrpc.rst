====================
jsonrpc
====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. note::

	这玩意儿不止一个, 看了一下, 有 jsonrpc, json-rpc, python-jsonrpc ...

	都觉得别人的轮子不好用要自己造是吧,

	没有技巧, 全是毒, 这一篇没啥具体要写的

基于json的跨语言远程调用协议.

调用的json格式::

	{
		"method": "方法名",
		"params": [“参数数组”],
		"id":  方法ID
	}

返回的json格式::

	{

		"jsonrpc": "2.0",
		"id": "1234",
		"result": null
	}


