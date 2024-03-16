======================================================
disabledOn 表达式如果包含有 横杠 - 时会无效
======================================================


.. post:: 2023-03-01 00:19:35
  :tags: 框架, amis, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


提出于 `<https://github.com/baidu/amis/issues/9673>`_

原来是 - 会被当作 减号 , 需要转义处理::

  {
      "type": "checkbox",
      "name": "_enableEnvAll-bob",
      "label": "启用",
      // "mode": "horizontal",
      style: {
          justifyContent: 'center'
      },
  },
  {
      type: "input-text",
      name: "_enableEnvAll-bob",
      disabledOn: "${!_enableEnvAll\\-bob}",
  },


