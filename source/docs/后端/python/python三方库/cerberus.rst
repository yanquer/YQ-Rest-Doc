==========================
cerberus
==========================

前言
==========================

cerberus 是一个用于数据表单校验的三方包

支持选项
==========================

.. csv-table:: cerberus支持规则
  :align: center
  :header: 选项,

  type,		"类型, 如string, int, datetime"
  required,	"是否必填, True/False"
  minlength,	"数据最小长度"
  maxlength,	"数据最大长度"
  regex,		"数据使用正则规则校验, 如 '^0[0-9]{9}$'"
  coerce,		"数据转换, 如转换日期为某个需要的, 值为函数"
  allowed,	"列表, 只能为列表内有的值"
  allof,		"列表, 多个条件的列表, 其中的条件都需要满足"
  anyof,		"列表, 满足任一条件即可"
  noneof,		"列表, 多个条件的列表, 其中的条件都不需要满足"
  oneof,		"满足此约束"
  check_with,	"函数, 使用函数检查, 注意参数列表为: `field, value, error`"
  contains,	"列表或者字符串, 实际数据集需包含所有枚举"
  dependencies,	"值为另一个数据列, 当前列有值时, 另一个数据列必须有值"
  empty,		"True/False, 是否允许为空"
  excludes,	"字符串列表或者字符串, 实际值必不包含其中"
  forbidden,	"字符串列表或者字符串, 禁止填写的值, 与上一个类似"
  items,		"列表, 实际填写的值需与此处对应, 有顺序之分"
  keysrules,	"字典, 可填写其他规则, 规范定义数据字典的键"
  meta,		"一个描述, 不用与规则"
  min,		"数据最小值"
  max,		"数据最大值"
  nullable,	"True/False, 是否可为None"
  readonly,	"True, 数据字段是否只读"
  require_all,	"所有属性都必填"


.. tip::

  参考: `Validation Rules <https://docs.python-cerberus.org/en/stable/validation-rules.html>`_

如定义一个字典验证器::

  schema = {
      'name': {'type': 'string', 'required': True},
      'age': {'type': 'integer', 'min': 18, 'max': 99},
      'email': {'type': 'string', 'regex': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'}
  }

示例
==========================

.. literalinclude:: ../../../../../.test/t_cerberus.py
  :caption: 使用cerberus校验示例
  :language: python

.. literalinclude:: ../../../../../.test/t_cerberus_person.py
  :caption: 自定义校验器示例
  :language: python


