===================================
createRef
===================================

与 函数组件 的 :doc:`useRef` 基本一致. 支持类组件和函数组件.

.. note::

  准确的说, 仅支持类组件, 因为 createRef 在函数组件中
  并没有 Hooks 的效果，其值会随着 FunctionComponent 重复执行而不断被初始化

  为什么 createRef 可以在 ClassComponent 正常运行呢？
  这是因为 ClassComponent 分离了生命周期，使例如 componentDidMount 等初始化时机仅执行一次。

React的数据流是自上而下的,
意味着如果想要从父组件更新自组件,
只有更新 `Props` 再触发重新渲染.

而 `Ref` 可以创建一个子组件的引用, 给父组件直接调用.

.. note::

  Props 是单向数据流，以 **声明式** 渲染组件；Ref 则是以 **命令式** 操作组件。

  命令式: 打破了 Props 的单向数据流，直接操作子元素。

从 React16.3 开始, 官方提供了 createRef::

  class Parent extends React.Component {
    constructor(props) {
      super(props);
      this.myRef = React.createRef();
    }

    componentDidMount() {
      const node = this.myRef.current;
      // 使用 ref 对象
    }

    render() {
      return <div ref={this.myRef}>Ref Example</div>;
    }
  }

ref可以直接指向定义的变量名, 但是使用的时候, 需要额外加个 current 才能获取当前引用实例.

.. important::

  ref不能挂到一个函数式组件

.. important::

  因为命令式破坏了原先的数据流，所以请不要滥用 Ref

  可以使用 Props 完成的，建议优先使用声明式的Props。
  例如：我们写一个“对话框组件“，最好使用 isOpen 属性控制开关，而不是暴露 close() 和 open() 方法。


.. note::

  React 会在组件挂载时给 current 属性传入 DOM 元素，
  并在组件卸载时传入 null 值。
  ref 会在 componentDidMount 或 componentDidUpdate 生命周期钩子触发前更新。
  这就是为什么ref.current总能拿到最新值的原因


不使用createRef
===================================

ref需要手动赋值::

  class MyComponent extends React.Component {
    constructor(props) {
      super(props);
      this.myRef = null;
    }

    componentDidMount() {
      const node = this.myRef;
      // 使用 ref 对象
    }

    render() {
      return <div ref={ref => (this.myRef = ref)}>Ref Example</div>;
    }
  }

效果感觉差不多.

.. 举例, 父组件调用子组件的方法
..   用到ref的hook, 做一个映射

..   子组件:\:

..     class Child extend React.Component{

..       state={name: 'child0'}

..       render(){
..         return <div>{this.state.name}</div>
..       }

..       setChildName(name: string){
..         this.setState({name: name})
..       }

..     }

..   父组件:\:

..     class Parent extend React.Component{
..       \_childView?: Child

..       render(){
..         return <Child
..           ref={view => {this._childView = view || undefined}}
..         />
..       }

..       // 调用子组件的函数
..       updateChildName(){
..         this._childView?.setChildName('parent->child')
..       }

..     }


.. 看有些地方也有这样用的:\:

..   const ref = React.useRef();
..   <Button ref={ref}>Click me!</Button>;



.. 参考: `react中ref使用方法 <https://juejin.cn/post/7047113456993959972>`_


