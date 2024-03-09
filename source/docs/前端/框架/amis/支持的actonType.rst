====================================
amis-支持的actonType(事件动作)
====================================

参考: https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/event-action

自定义JS
====================================

参考: `https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/event-action#自定义-js`

- actionType 为 **custom**
- script 为函数或者函数字符串,
  函数签名::

    script:(context,doAction,event)=>{}

  - context，渲染器上下文
  - doAction() 动作执行方法，用于调用任何 actionType 指定的动作
  - event，事件对象，可以调用 setData()、stopPropagation()、preventDefault()
    分别实现事件上下文设置、动作干预、事件干预，可以通过 `event.data` 获取事件上下文(应该叫数据域吧)

参考::

  {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "发送一个 http 请求",
        "level": "primary",
        "onEvent": {
          "click": {
            "actions": [
              {
                "actionType": "custom",
                "script": "doAction({actionType: 'ajax', args: {api: '/amis/api/mock2/form/saveForm'}});\n //event.stopPropagation();"
              }
            ]
          }
        }
      }
    ]
  }

.. note::

  对于 `button` 的点击事件, 直接在其同级写 ``actionType: "custom"`` 无效,
  需要定义 `onEvent -> click -> actions` 才行(如上).

存储数据
------------------------------------

有时在执行自定义 JS 的时候，希望该过程中产生的数据可以分享给后面的动作使用，
此时可以通过 `event.setData()` 来实现事件上下文的设置，这样后面动作都可以通过事件上下文来获取共享的数据。

注意：直接调用 `event.setData()` 将修改事件的原有上下文，
如果不希望覆盖可以通过 `event.setData({...event.data, ...{xxx: xxx}})` 来进行数据的合并。










