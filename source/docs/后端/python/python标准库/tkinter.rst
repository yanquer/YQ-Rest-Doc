==============================
tkinter
==============================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


geometry的作用
==============================

- 设置窗口的宽和高，就算窗口已经通过resizable函数禁止调整宽高；
  还可以移动窗口在屏幕上的位置::

    root = tk.Tk()

    # 设置为禁止调整宽、高
    root.resizable(0,0)

    # 大小设置为 600 x 600
    root.geometry('600x600')

- 移动窗口位置, 加号风格, 第1个加号是距离屏幕左边的宽，
  第2个加号是距离屏幕顶部的高, 可为负数::

    root.geometry('+0+0')
    root.geometry('+300+400')

    # 为负数移动到屏幕外, 可以隐藏窗口
    root.geometry('+-3000+-4000')

    # 也可以一起设置
    root.geometry('300x250+500+240')

- 参数为None,
  获取窗口位置::

    root.geometry(None)
    # '300x250+336+55'


#### 布局管理器 grid、pack、place

| 参考: https://blog.csdn.net/Oh_Python/article/details/124196792

- grid表格布局，采用表格结构组织组件，子组件的位置由行和列的单元格确定，并且可以跨行和跨列，从而实现复杂的布局。

- pack按照组件的创建顺序将子组件添加到父组件中，按照垂直或者水平的方向自然排布，如果不指定任何选项，默认在父组件中自顶向下垂直添加组件。pack是代码量最少，最简单的一种，可以用于快速生成界面。

- place 布局管理器可以通过坐标精确控制组件的位置，适用于一些布局更加灵活的场景。



### other

task.cancel() 只能取消状态为 pending的任务, 否则将毫无作用
