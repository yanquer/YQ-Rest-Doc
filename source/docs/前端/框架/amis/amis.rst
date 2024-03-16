============================
amis
============================


.. post:: 2023-02-26 21:30:12
  :tags: 框架, amis
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


Github地址: https://github.com/baidu/amis

Amis 是百度开源的一块前端低代码框架，
通过 JSON 配置就能生成各种后台页面，极大减少开发成本，甚至可以不需要了解前端。

使用
============================

原文: https://aisuda.bce.baidu.com/amis/zh-CN/docs/start/getting-started

有两种方式

原生JS脚本导入(SDK导入)
  直接 ``npm i amis``, 在 node_modules\amis\sdk 目录里就能找到;
  或者直接下载包文件 `https://github.com/baidu/amis/releases/download/3.5.2/sdk.tar.gz`, 手动解压.

  用例::

    <script src="sdk.js"></script>
    <script type="text/javascript">
      (function () {
        let amis = amisRequire('amis/embed');
        // 通过替换下面这个配置来生成不同页面
        let amisJSON = {
          type: 'page',
          title: '表单页面',
          body: {
            type: 'form',
            mode: 'horizontal',
            api: '/saveForm',
            body: [
              {
                label: 'Name',
                type: 'input-text',
                name: 'name'
              },
              {
                label: 'Email',
                type: 'input-email',
                name: 'email'
              }
            ]
          }
        };
        let amisScoped = amis.embed('#root', amisJSON);
      })();
    </script>

  默认 amis 渲染是单页模式

  如果是单页应用，在离开当前页面的时候通常需要销毁实例: ``amisScoped.unmount();``
React项目
  直接 ``npm i amis``

数据域初始化
============================

直接使用确定的数据
  使用 `data`::

    {
      "type": "page",
      "data": {
        "name": "zhangsan",
        "age": 20
      },
      "body": [
        {
          "type": "tpl",
          "tpl": "my name is ${name}"
        }
      ]
    }
从API获取初始化的数据
  使用 `initApi` ::

    {
      "type": "page",
      "initApi": "/amis/api/initData",
      "body": "Hello ${text}"
    }

  注意API的返回数据必定是这种格式::

    {
      "status": 0,
      "msg": "",
      "data": {
        "text": "World!"
        ...其他字段
      }
    }

  以上最外层字段必须有, 可以增加, 不能减少, `data` 类型必是字典

.. note::

  并不是所有组件都支持配置初始化接口来实现数据域初始化操作，
  对于那些 **不支持配置初始化接口的组件** 来说，一般会使用 Service 组件 来辅助实现数据域初始化；

  如果两种同时配置, 那么将会合并两种结果

.. important::

  什么叫, 具备数据域的组件?

  直白来说, 就是当经过这一层时候, 会创建新的数据域,
  这个时候 **当定义data时, 无法使用$来引用上层数据域的数据**, 而是直接将其当作字符串.

具备数据域的组件(或者说 `支持配置初始化接口` 的组件?):
  - App
  - Page
  - Cards
  - Chart
  - CRUD
  - CRUD2
  - Dialog
  - Drawer
  - List
  - Page
  - PaginationWrapper
  - Service
  - Wizard
  - Combo
  - InputArray
  - Table
  - Table2

.. note::

  一般对于不支持数据域的组件, 想使用数据域时, 往往是在外层包裹一层 `Service`

数据链
============================

一般情况下, 子层的数据域, 如果获取的值不存在, 会递归向上查找,
甚至可以拿到URL路径的参数(url 中的参数会进入顶层数据域)

默认行为, 预定义只找上层和上上层.

定义查找范围, 使用 `trackExpression`:

- trackExpression: "none" : 不追踪任何数据
- trackExpression: "${xxxVariable}" : xxxVariable 变化了更新当前组件的数据链
  可以监听多个变量比如: "${xxx1},${xxx2}"，还可以写表达式如 "${ xxx ? xxx : yyy}"。

  如果变量是数组，或者对象，会转成统一的字符串 [object Array] 或者 [object Object] ;
  这个其实会影响检测的，所以建议转成 json 字符串如。 ${xxxObject | json}。
  还有就是既然是监控上层数据，表达式中不要写当前层数据变量，是取不到的。

逻辑函数
============================

- IF(condition, consequent, alternate) -> consequent | alternate
  相当于三目表达式.
- AND(expression1, expression2, ...expressionN) -> bool
- OR(expression1, expression2, ...expressionN) -> bool
- XOR(condition1, condition2, ...expressionN) -> bool
- IFS(condition1, result1, condition2, result2,...conditionN, resultN) -> any
  相当于多个 else if 合并成一个

数学函数
============================

- ABS(num) -> number
  求绝对值
- MAX(num1, num2, ...numN) -> number
  如果只有一个参数且是数组，则计算这个数组内的值, 下同
- MIN(num1, num2, ...numN) -> number
- SUM(num1, num2, ...numN) -> number
- INT(num) -> number
- MOD(num, divisor) -> number
  返回两数相除的余数，参数 number 是被除数，divisor 是除数。
- PI() -> number
  圆周率
- ROUND(num[, numDigits = 2]) -> number
  将数字四舍五入到指定的位数，可以设置小数位
- FLOOR(num[, numDigits=2])
  向下取整
- CEIL(num[, numDigits=2]) -> number
  将数字向上取整到指定的位数，可以设置小数位
- SQRT(num) -> number
  开平方，参数 number 为非负数
- AVG(num1, num2, ...numN) -> number
  平均值
- DEVSQ(num1, num2, ...numN) -> number
  返回数据点与数据均值点之差（数据偏差）的平方和，如果只有一个参数且是数组，则计算这个数组内的值。
- AVEDEV(num1, num2, ...numN) -> number
  数据点到其算术平均值的绝对偏差的平均值
- HARMEAN(num1, num2, ...numN) -> number
  数据点的调和平均值，如果只有一个参数且是数组，则计算这个数组内的值
- LARGE(array, k) -> number
  数据集中第 k 个最大值
- UPPERMONEY(num) -> string
  将数值转为中文大写金额
- RAND() -> number
  返回大于等于 0 且小于 1 的均匀分布随机实数。每一次触发计算都会变化
- LAST(array) -> any
  取数组最后一个
- POW(base, exponent) -> number
  基数 base 的指数次幂

文本函数
============================

参考: https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/expression#新表达式语法

日期函数
============================

数组函数
============================

编码函数
============================

- ENCODEJSON({name: 'amis'})
  将JS对象转换成JSON字符串
- DECODEJSON('{\"name\": "amis"}')
  解析JSON编码数据，返回JS对象

其他函数
============================

- GET(obj:any, path:string, defaultValue:any)
  根据对象或者数组的path路径获取值。 如果解析 value 是 undefined 会以 defaultValue 取代
- ISTYPE(obj:any, type: string)
  判断是否为类型支持：string, number, array, date, plain-object
  如::

    ISTYPE([{a: '1'}, {b: '2'}, {a: '1'}], 'array')

图标使用
============================

详细见: https://aisuda.bce.baidu.com/amis/zh-CN/components/icon

导入CSS::

  @fortawesome/fontawesome-free/css/all.css

react安装::

  yarn add @fortawesome/fontawesome @fortawesome/react-fontawesome @fortawesome/fontawesome-free --save

通过名称使用::

  {
    "type": "page",
    "body": {
      "type": "icon",
      "icon": "cloud"
    }
  }

也支持用url::

  {
    "type": "page",
    "body": {
      "type": "icon",
      "icon": "https://suda.cdn.bcebos.com/images%2F2021-01%2Fdiamond.svg"
    }
  }

icon 默认支持fontawesome v4(vendor默认为 "fa" 表示v4)，
如果想要支持 v5 以及 v6 版本的 fontawesome 请设置 vendor 为空字符串::

  {
    "type": "icon",
    "icon": "far fa-address-book",
    "vendor": ""
  },

v5 用 far/fas 等表示前缀;
详细V5图标库见: https://fontawesome.com/v5/search?m=free

v6 用 fa-regular / fa-solid 等表示前缀::

  {
    "type": "icon",
    "icon": "fa-regular fa-address-book",
    "vendor": ""
  },

详细V6图标库见: https://fontawesome.com/icons/list
