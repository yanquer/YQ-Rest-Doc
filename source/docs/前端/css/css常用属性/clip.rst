=======================
clip
=======================

clip 是一个 CSS 属性，用于指定元素的裁剪区域，即确定元素在页面上显示的部分。
它可以用来隐藏元素的一部分内容或者创建非矩形的可视区域。

**clip 属性需要配合 position: absolute; 或者 position: fixed; 使用**，
因为只有绝对定位或固定定位的元素才能裁剪。

clip 属性可以使用以下两种方式进行设置：

rect()
  使用 rect() 函数::

    .element {
      position: absolute;
      clip: rect(top, right, bottom, left);
    }

  其中，top、right、bottom 和 left 是裁剪区域的边界值，可以使用像素（px）或百分比（%）来指定。
auto
  使用 auto 关键字::

    .element {
      position: absolute;
      clip: auto;
    }


- 当使用 clip: auto; 时，元素将不会被裁剪，显示完整的内容。
- 当使用 clip: rect(auto, auto, auto, auto); 时，元素将根据其定位和尺寸进行自动裁剪。

.. note::

  clip 属性在 CSS3 中已被废弃，不推荐使用。
  推荐使用更强大和灵活的 clip-path 属性来实现更复杂的裁剪效果。



