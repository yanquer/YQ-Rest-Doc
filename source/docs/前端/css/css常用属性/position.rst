======================
position
======================


.. post:: 2023-02-20 22:06:49
  :tags: css, css常用属性
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


规定元素的定位类型

- static: HTML 元素的默认值，即没有定位，遵循正常的文档流对象;
  静态定位的元素不会受到 top, bottom, left, right影响;
- relative: 相对位置, 元素的定位是相对其正常位置;
  移动相对定位元素，但它原本所占的空间不会改变;
- absolute: 绝对定位的元素的位置相对于最近的已定位父元素;
  如果元素没有已定位的父元素，那么它的位置相对于<html>;
- fixed: 元素的位置相对于浏览器窗口是固定位置;
  即使窗口是滚动的它也不会移动;
- sticky: 英文字面意思是粘，粘贴，所以可以把它称之为粘性定位;
  基于用户的滚动位置来定位;
  依赖于用户的滚动，在 position:relative 与 position:fixed 定位之间切换;
  行为就像 position:relative; 而当页面滚动超出目标区域时，它的表现就像 position:fixed;，它会固定在目标位置;
  元素定位表现为在跨越特定阈值前为相对定位，之后为固定定位;
  特定阈值指的是 top, right, bottom 或 left 之一，换言之，指定 top, right, bottom 或 left 四个阈值其中之一，才可使粘性定位生效。否则其行为与相对定位相同;
