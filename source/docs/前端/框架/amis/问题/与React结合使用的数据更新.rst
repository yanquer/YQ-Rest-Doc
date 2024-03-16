======================================================
与React结合使用的数据更新
======================================================


.. post:: 2023-03-01 00:19:35
  :tags: 框架, amis, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


这个算是一个小坑, `React` 的数据域, 向来都是通过 `state` 来控制渲染.

原以为 `amis` 已经内置处理了这个问题, 结果没有, 还是得 `state` 出马::

  import {render as renderAmis} from 'amis';

  export class MyComponent extends React.Component<any, any> {
    state = {
        _envData: {
            1: 5,
            2: 6,
        }
    }

    render(){
      return (
        <div>
          {renderAmis(
            {
              type: 'page',
              title: '简单页面',
              data:  {
                  envData: this.state._envData,
              },
              body: [...]
            }
          )}
        </div>
      )
    }

  }

