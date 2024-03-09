======================================================
disabledOn 表达式如果包含有 横杠 - 时会无效
======================================================

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


