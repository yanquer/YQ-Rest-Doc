===============================================
函数组件无ref属性
===============================================


.. post:: 2024-03-08 23:31:08
  :tags: 框架, react, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


函数组件默认没有ref属性,
.. 需要使用forwardRef来传递ref:
需要使用 forwardRef 包装::

  const PSelect00 = (props: any, ref) => {

      return (
          <div ref={ref}>p0</div>
      )
  }

  const PSelect0 = React.forwardRef((props, ref) => {
      return (
          <PSelect00 ref={ref}>p0</PSelect00>
      )
  })

  const PSelect1 = () => {
      const refP0 = React.useRef()
      return <PSelect0 ref={refP0}/>
  }

还有就是暴露自定义组件实例, 自定义暴露内容, 见

- :doc:`/docs/前端/框架/react/hooks/forwardRef`
- :doc:`/docs/前端/框架/react/hooks/useImperativeHandle`



