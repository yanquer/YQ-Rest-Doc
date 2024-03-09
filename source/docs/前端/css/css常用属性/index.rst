======================
css常用属性
======================

.. toctree::
  :maxdepth: 1

  align-items
  background
  background-image
  background-color
  border-radius
  box-shadow
  clip
  color
  content
  cursor
  display
  float
  justify-content
  margin
  opacity
  outline
  padding
  place-content
  position
  text-align
  transform
  transition

place-content、justify-content、align-items 和 text-align 区别
========================================================================================

place-content：设置 Grid 布局元素在容器中的水平和垂直对齐方式
  place-content 属性是 CSS Grid 布局的一个简写属性，
  用于同时设置元素在容器中的水平和垂直方向上的对齐方式。
  它接受两个值，第一个值表示水平对齐方式，第二个值表示垂直对齐方式。
  例如：place-content: center center; 表示在容器中水平和垂直方向上居中对齐。

justify-content：设置 Flexbox 布局元素在容器主轴和交叉轴上的对齐方式
  justify-content 属性用于设置元素在容器的主轴（水平轴）上的对齐方式。
  它适用于使用 Flexbox 布局或 CSS Grid 布局的容器。
  常见的值包括 flex-start（默认值，左对齐）、flex-end（右对齐）、
  center（居中对齐）、space-between（两端对齐，项目之间平均分布）、space-around（项目周围平均分布）等。

align-items：设置 Flexbox 布局元素在容器主轴和交叉轴上的对齐方式
  align-items 属性用于设置元素在容器的交叉轴（垂直轴）上的对齐方式。
  它适用于使用 Flexbox 布局或 CSS Grid 布局的容器。
  常见的值包括 flex-start（默认值，顶部对齐）、flex-end（底部对齐）、
  center（居中对齐）、baseline（基线对齐，元素的基线对齐）等。

text-align：设置元素框内文本内容的水平对齐方式
  text-align 属性用于设置文本内容在元素框中的水平对齐方式。
  它适用于块级元素和一些内联元素。
  常见的值包括 left（默认值，左对齐）、right（右对齐）、
  center（居中对齐）、justify（两端对齐）等。该属性主要用于调整文本的对齐方式，而不是元素本身。

