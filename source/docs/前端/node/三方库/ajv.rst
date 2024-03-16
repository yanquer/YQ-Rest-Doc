===========================
ajv
===========================


.. post:: 2023-02-20 22:06:49
  :tags: node, 三方库
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


json-schema: 用来描述 `json` 长什么样数据格式

ajv 是一个校验 `json-schema` 的数据格式工具

json-schema 默认含有下面 6 种数据结构

- string
- number
- object
- array
- boolean
- null

使用用例::

  const Ajv = require("ajv")
  const ajv = new Ajv()

  const schemaStr = '{"type":"object","description":"Windows specific launch configuration attributes.","properties":{"env":{"additionalProperties":{"type":"string"},"default":{},"description":"Environment variables defined as a key value pair. Property ends up being the Environment Variable and the value of the property ends up being the value of the Env Variable.","type":"object","pattern":"^(?!.*\\\\$\\\\{(env|config|command)\\\\.)","patternErrorMessage":"\'env.\', \'config.\' and \'command.\' are deprecated, use \'env:\', \'config:\' and \'command:\' instead."}},"pattern":"^(?!.*\\\\$\\\\{(env|config|command)\\\\.)","patternErrorMessage":"\'env.\', \'config.\' and \'command.\' are deprecated, use \'env:\', \'config:\' and \'command:\' instead."}'

  const schema = JSON.parse(schemaStr)
  // const schema = {
  //   type: "object",
  //   description: 'test o',
  //   properties: {
  //     env: {
  //       additionalProperties: {type: 'string'},
  //       default: {},
  //       description: 'env o',
  //       type: 'object',
  //       pattern: "^(?!.*\\$\\{(env|config|command)\\.)"
  //     }
  //   },
  //   pattern: "^(?!.*\\$\\{(env|config|command)\\.)"
  // }

  const data = {env: {"1": "1"}}
  // const valid = ajv.validate(schema, data)
  const validRule = ajv.compile(schema)
  const valid = validRule(data)
  if (!valid) console.log(ajv.errors); else console.log('suc', valid)







