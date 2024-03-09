===============================
低代码框架amis
===============================

低代码框架旨在仅用极少的配置信息来表述一个页面

关于amis, 个人觉得,
最好的适用情况是: 已经有完备的后端api, 只需要简单的规划前端JSON即可

像与React结合这种, 个人不建议使用JSON的形式, 因为有一些交互是需要代码实例变量介入的,
实在要介入, 要么React类变量等不参与JSON的数据流转,
要么, 感觉直接使用amis提供好的组件以JSX的形式使用.

当然, 个人观点.

.. toctree::

  amis
  api配置
  表达式语法
  支持的actonType
  表单校验
  问题/index

痛点-数据域的更新
===============================

- 当子层更新数据域后,上层不会收到更新(数据域向上更新);
- 当某次更新数据域后, 下次打开还是旧的(当前数据域数据保存);

必须通过api来更新, 坑点...

请求适配器
===============================

可用于对请求数据的过滤等操作, 见: `https://aisuda.bce.baidu.com/amis/zh-CN/docs/types/api#配置请求适配器`

组件的简单自定义
===============================

官方原文见: `https://aisuda.bce.baidu.com/amis/zh-CN/docs/extend/custom-react`

例子::

  {
      // type: 'custom-kv-text',
      name: 'envDD',
      label: 'label-d',
      mode: "horizontal",
      asFormItem: true,
      children: ({value, onChange, data}: any) => (
          <React.Fragment>
              <p>这个是个自定义组件</p>
              {/*<p>当前值：{value}</p>*/}
              <input type='text' value={typeof value === 'object' ? JSON.stringify(value) : value}
                      onChange={(e) => {
                          let curData = e.target.value
                          try {
                              curData = JSON.parse(curData)
                              data.envData = curData
                          } catch (err) {
                              console.log('not json schema')
                              // return
                          }
                          onChange(curData)
                      }}
              />
          </React.Fragment>
      )
  },

