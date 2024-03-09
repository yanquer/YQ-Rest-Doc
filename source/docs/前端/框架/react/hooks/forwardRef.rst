================================================
forwardRef
================================================

官网: `<https://zh-hans.react.dev/reference/react/forwardRef>`_

React.forwardRef 会创建一个React组件，这个组件能够将其接受的 ref 属性转发到其组件树下的另一个组件中。
这种技术并不常见，但在以下两种场景中特别有用：

- 转发 refs 到 DOM 组件
- 在高阶组件中转发 refs

转发 DOM 组件(内置组件节点)
================================================

一般情况下, **ref不能挂到一个函数式组件**, 使用 fowardRef 就可以支持::

  const App: React.FC = () => {
    const ref = useRef(null);

      useEffect(() => {
        ref.current.focus();
      }, []);

      return (
        <>
          <Child ref={ref} />
        </>
      );
  };

  const Child = forwardRef((props, ref: Ref<any>) => {
    return <input type="text" name="child" ref={ref} />;
  });

.. note::

  React.forwardRef参数必须是function，而这个API通常用来解决HOC（高阶组件）中丢失ref的问题。

useImperativeHandle
================================================

见: :ref:`React-Hook_useImperativeHandle`


参考:

- `useRef、createRef的区别及使用，及useRef妙用 <https://juejin.cn/post/6950845509137334309>`_
- `react中ref、createRef、useRef、forwardRef以及useImperativeHandle <https://www.cnblogs.com/gg-qq/p/15078913.html>`_


