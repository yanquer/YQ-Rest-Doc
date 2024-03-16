============================
useEffect
============================


.. post:: 2024-03-07 22:13:39
  :tags: 框架, react, hooks
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


为组件添加副作用的操作

比如，每次渲染之后，修改网站的标题::

  function Example() {
    const [count, setCount] = useState(0);

    useEffect(() => {
      document.title = `You clicked ${count} times`;
    });
  }

觉得每次渲染都执行开销太大, 还可以仅在count更新的时候执行(使用第二个参数即可)::

  useEffect(() => {
    document.title = `You clicked ${count} times`;
  }, [count]);

表示只有当count变化的时候，重新执行副作用

有时候我们会希望useEffect只在第一次渲染时候执行一次，
例如 componentDidMount ，第二个参数设置成空数组::

  useEffect(() => {
      console.log('组件Mounted');
  }, []);

.. note::

  可以使用多个 `useEffect` 作为不同的 hooks 让逻辑分离

  如果需要消除 `effect`, 返回函数即可


