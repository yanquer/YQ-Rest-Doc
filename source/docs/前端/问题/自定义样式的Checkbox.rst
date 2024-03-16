=============================
自定义样式的Checkbox
=============================


.. post:: 2023-02-26 21:30:12
  :tags: 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


比如圆形边框

默认情况下，input 元素的复选框（checkbox）的外观是由浏览器自身的样式决定的，
并且这些样式通常不允许直接通过 CSS 的 border-radius 属性来设置圆形边框。

先使用i标签实现一个简单的Checkbox::

  import React from 'react';

  interface CheckedProps{
      name?: string
      initChecked?: boolean
      description?: string
  }

  export class Checkbox extends React.Component<CheckedProps, any> {
      state = {
          boxChecked: false
      }

      protected changeChecked() {
          this.setState({boxChecked: !this.state.boxChecked})
      }

      render() {
          if (typeof this.props.initChecked === "boolean"){
              this.setState({boxChecked: this.props.initChecked})
          }

          const description = this.props.description

          return (
              <div className={'custom-checkbox-0'}>
                  <input
                      type={'checkbox'}
                      checked={this.state.boxChecked}
                  />
                  <i onClick={() => {this.changeChecked()}} />
                  <span />
                  {description ? (
                      <div>{description}</div>
                  ) : null}
              </div>
          );
      }
  }

主要是样式的设置::

  /*
      input标签样式
      input禁止掉默认的点击行为, 交给i标签
  */
  .custom-checkbox-0 > input[type="checkbox"] {
      position: absolute;
      clip: rect(1px, 1px, 1px, 1px);
      pointer-events: none;
  }

  /*
      普通状态下 **<i>标签内容** 的样式
      即没有打勾
  */
  .custom-checkbox-0 > i::before{
      content: "";
      position: absolute;
      left: 50%;
      top: 50%;

      border-color: whitesmoke;
      border-style: solid;
      border-width: 0 ;
      transform: translate(-50%, -90%) rotate(-40deg);
  }

  /*
      <i> 标签的样式

      此处是宝蓝色背景, 接管input的点击行为, 长宽设置为16
  */
  .custom-checkbox-0 > i {
      background-color: royalblue;
      display: inline-block;
      vertical-align: text-bottom;
      position: relative;
      pointer-events: all;

      width: 16px;
      height: 16px;
      cursor: pointer;
      border: 1px solid;

      border-radius: 50%;   /* 设置圆形 */
  }

  /*
      <i> 标签选中时的外观

      即打勾 (实现原理是只显示左边和右边的边框然后旋转, 看起来就是个勾了)
  */
  .custom-checkbox-0 > input:checked + i:before {
      width: 8px;
      height: 4px;
      border-width: 0 0 1px 1px;
  }


  /*.custom-checkbox-0 > input[disabled]:checked + i:before{*/
  /*    width: 0;*/
  /*    height: 0;*/
  /*    border-width: 0;*/
  /*}*/

.. note::

  好像很多东西的默认样式都不是很好改, 得借助其他元素

  且纯用css来更改很难





