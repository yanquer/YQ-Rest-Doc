======================
transform
======================


.. post:: 2023-03-01 00:19:35
  :tags: css, css常用属性
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


允许你旋转，缩放，倾斜或平移给定元素(包括2D/3D)。这是通过修改 CSS 视觉格式化模型的坐标空间来实现的。

示例: https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform

说明: https://www.w3school.com.cn/cssref/pr_transform.asp

常见的 transform 属性值及其作用
============================================

平移（Translate）
  translate() 函数用于在水平和垂直方向上平移元素::

    transform: translate(100px, 50px);

  上述代码将把元素向右平移 100 像素，向下平移 50 像素。
旋转（Rotate）
  rotate() 函数用于按指定角度旋转元素::

    transform: rotate(45deg);

  上述代码将元素顺时针旋转 45 度。
缩放（Scale）
  scale() 函数用于按指定比例缩放元素::

    transform: scale(1.5);

  上述代码将元素的尺寸放大到原始尺寸的 1.5 倍。

  支持不同方向的缩放, 比如仅缩放高度::

    transform: scaleY(1.5);

倾斜（Skew）
  skew() 函数用于按指定角度倾斜元素::

    transform: skew(30deg, -10deg);

  上述代码将元素水平方向倾斜 30 度，垂直方向倾斜 -10 度。
其他
  矩阵变换（matrix()）、透视效果（perspective()）


