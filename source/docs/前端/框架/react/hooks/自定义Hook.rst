============================
自定义Hook
============================


.. post:: 2024-03-07 22:13:39
  :tags: 框架, react, hooks
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


举个例子，我们写一个 hook 实时获取页面的宽度::

  // 创建一个名为useWidth的hook
  function useWidth () {
    // 1. 声明一个宽度的state
    const [width, setWidth] = useState(window.innerWidth);
    useEffect(() => {
      function handleResize() {
        // 2. 每当屏幕resize时，更新width
        setWidth(window.innerWidth);
      }

      // 3. 添加监听事件
      window.addEventListener("resize", handleResize);
      // 4. 返回一个移出事件的函数
      return () => window.removeEventListener("resize", handleResize);
    }, []);
    return width;
  }

使用::

  function App () {
    // 使用自定义hook
    const width = useWidth();
    return <div>当前屏幕宽度为{width}</div>
  }

自定义的useWidth，实时获取屏幕宽度
另外，很重要的几点提示：

- hook在各个组件中的state状态是隔离的，这个跟js函数的概念是一致的；
- React Hooks不是用来在多组件中复用状态，而是在多组件中复用状态逻辑；



