======================================================
validations验证信息配置无效
======================================================

有时候表单信息需要配置字段验证

**只有在Form表单中才能验证字段**, 因为只有它才有提交功能,
验证一般只有提交或者活触发自动提交的时候才会触发;
成功触发一次后, 看效果后续都是此字段自动立刻校验了

例::

  {
      type: 'form',
      body: {
          type: 'input-text',
          name: 'eName',
          label: 'label0',
          mode: "horizontal",
          validations: {
              "isNumeric": true,
              "minimum": 10,          // 表示数字最小为10
          },
          // description: "请输入数字类型文本",
          validationErrors: {
              "isNumeric": '不是数字',
              "minimum": "同学，最少输入$1以上的数字哈"
          }
      },
      xs: 11
  },


