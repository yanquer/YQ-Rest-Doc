
======================================================
类disabled属性只能识别数据链对象
======================================================

.. post:: 2023-03-01 00:19:35
  :tags: 框架, amis, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


比如有一个 checkbox 控件 name 为: ``com.app.enable`` ::

  {
    "type": "checkbox",
    "name": "com.app.enable"
  }

同时有一个相关的 input-text 控件的 disabledOn 属性与其相关联::

  {
    "type": "input-text",
    "name": "com.app.version"
    "disabledOn": "${!com.app.enable}"
  }

表示只有 checkbox 选择的时候 text 才可用

但是因为属性是包含 ``.`` 的, 所以内部默认会识别为(数据块1)::

  {
    com: {
      app: {
        version: "",
        enable: "",
      }
    }
  }

其中, 组件的 name 可以自动识别直接给的链式数据(数据块2)::

  {"com.app.enable": false}

而组件的 ``disabledOn`` 只能识别解析后的数据, 也就是只能识别 (数据块1),
效果就是, 当 ``disabledOn``  包含点时候,
第一次使用没问题,
但是当数据域已有 (数据块2) 形式数据时, ``disabledOn``  属性将失效

得将点替换为其它才能保证正常使用.

.. note::

  这个问题触发的调教貌似比较苛刻, 目前只在使用 apiInit 的时候遇到过

还有一点, 好像是模版语法还是啥, 支持使用this, 比如有数据域::

  data: {
    isOne: true
  }

disabledOn支持直接设置为::

  disabledOn: "!this.isOne"

但是 **数据域里不能这样用** , 比如::

  type: "select",
  source: {
    url: "xxx/xxx/xxx?a=${a}",
    data: {
      a: "this.a"
    }
  }


