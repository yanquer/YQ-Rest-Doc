=============================
api配置-数据加载/刷新
=============================


.. post:: 2023-02-26 21:30:12
  :tags: 框架, amis
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


amis有数据域的概念, 数据域也可以从api加载.

普通的 `ajax` 请求
=============================

格式: [<method>:]<url>
  - method：get、post、put、delete，默认为 get
  - url：接口地址，即模板字符串

如::

  {
    "api": "get:/amis/api/initData", // get 请求
    "api": "post:/amis/api/initData", // post 请求
    "api": "put:/amis/api/initData", // put 请求
    "api": "delete:/amis/api/initData" // delete 请求
  }

注意接口返回格式::

  {
    "status": 0,
    "msg": "",
    "data": {
      ...其他字段
    }
  }

- status: 返回 0，表示当前接口正确返回，否则按错误请求处理；
- msg: 返回接口处理信息，主要用于表单提交或请求失败时的 toast 显示；
- data: 必须返回一个具有 key-value 结构的对象。

.. note::

  api默认发送当前数据域的数据, 可以在当前元素手动配置 `data` 来自定义发送的数据

预加载数据
=============================

使用 `initApi`, 基本可用于所有组件

.. note::

  实际使用的时候遇到一个问题, 写在 `form` 的上一层 `dialog` 组件, 没有生效,
  换到 `form` 组件, 就可以了, 不知是为何

  .. 难不成需要在支持数据域的组件才能使用?
  .. 官方没提到这个......



