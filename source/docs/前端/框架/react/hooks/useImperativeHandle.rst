===========================================
useImperativeHandle
===========================================

useImperativeHandle 可以让你在使用 ref 时 **自定义暴露给父组件的实例值**。
或者 **给不存在ref属性的函数组件, 增加ref属性**.
在大多数情况下，应当避免使用 ref 这样的命令式代码。
useImperativeHandle 应当与 :doc:`forwardRef` 一起使用

.. 在forwardRef例子中的代码实际上是不推荐的，
.. 因为无法控制要暴露给父组件的值，所以我们使用useImperativeHandle控制要将哪些东西暴露给父组件。

暴露DOM节点时自定义暴露属性
===========================================

useImperativeHandle 应当与 forwardRef 一起使用,
调用方式::

  useImperativeHandle(ref, createHandle, [deps])

- 接收一个ref
- 接收一个函数，这个函数返回的对象即是要暴露出的ref
- 类似useEffect，接收一个依赖数组

例子::

  const FancyInput=(props, ref) =>{
    const inputRef = useRef();
    useImperativeHandle(ref, () => ({
        focus: () => {
          inputRef.current.focus();
        }
      }));
      return <input ref={inputRef} />;
  }
  export default forwardRef(FancyInput);

渲染::

  <FancyInput ref={fancyInputRef} />

的父组件可以调用::

  fancyInputRef.current.focus()

.. _React-Hook_给非DOM函数组件增加ref属性:

给非DOM函数组件增加ref属性
===========================================

与 暴露DOM节点时自定义暴露属性_ 例子基本一致

.. note::

  函数组件默认没有ref属性. 仅DOM节点(原生提供的HTML节点)有

.. 不过不是对于DOM节点如 `input`, 而是自定义函数组件

不过上面还是用了DOM节点ref, 可能初学时存在混淆,
加个自定义函数组件作为例子::

  const PSelect00 = (props: any) => {

      return (
          <div>p00</div>
      )
  }

  // 调用子组件
  const PSelect0 = React.forwardRef((props, ref) => {

      // 定义暴露的 ref
      React.useImperativeHandle(ref, () => ({
          do1: do1
      }))

      const do1 = () => {console.log(1)}

      return (
          <PSelect00>p0</PSelect00>
      )
  })

  // 父组件
  const PSelect1 = () => {
      const refP0 = React.useRef()
      return <PSelect0 ref={refP0}/>
  }

.. warning::

  当 forwardRef 内容没有转发 DOM 节点时, 比如此处的::

    return (
        <PSelect00>p0</PSelect00>
    )

  必须使用 useImperativeHandle 来接收传入的 ref, 否则 ref 为 null.
  比如此处的::

    // 定义暴露的 ref
    React.useImperativeHandle(ref, () => ({
        do1: do1
    }))

  显而易见嘛, forward本来就是转发ref的, 你都不转发了, 再不声明useImperativeHandle,
  不就是null.

  那你可能会问, 如果两个都定义了ref呢?
  那就是在暴露DOM组件的基础上, 再控制需要暴露的内容.






