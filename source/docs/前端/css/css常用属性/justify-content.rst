======================
justify-content
======================


.. post:: 2023-02-20 22:06:49
  :tags: css, css常用属性
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


设置 **Flexbox** 布局元素在容器主轴和交叉轴上的对齐方式

justify-content 属性用于设置元素在容器的主轴（水平轴）上的对齐方式。
它适用于使用 **Flexbox** 布局或 CSS **Grid** 布局的容器。

当你将一个元素的 :doc:`/docs/前端/css/css常用属性/display` 属性设置为 `flex` 或 `inline-flex` 时，
该元素成为一个 `flex` 容器，它的子元素成为 `flex` 项目。

常见的值包括：

- flex-start: 将 flex 项目靠主轴起始位置对齐（默认值，左对齐）。
- flex-end: 将 flex 项目靠主轴末尾位置对齐（右对齐）。
- center: 将 flex 项目在主轴上居中对齐（居中对齐）。
- space-between: 将 flex 项目均匀分布在主轴上，首个项目靠起始位置，末尾项目靠末尾位置（两端对齐，项目之间平均分布）。
- space-around: 将 flex 项目均匀分布在主轴上，项目之间和首末项目与容器边界之间的间距相等（项目周围平均分布）。
- space-evenly: 将 flex 项目均匀分布在主轴上，包括首末项目与容器边界之间的间距都相等。

示例::

  .flex-container {
    display: flex;
    justify-content: center;
  }

将 `justify-content` 设置为 `center`, `flex` 容器内的项目将在主轴上居中对齐。
