==============================
content
==============================


.. post:: 2023-02-20 22:06:49
  :tags: css, css常用属性
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. note::

  源于AI

在 CSS 中，content 属性用于在伪元素（:before 和 :after）中插入生成的内容。它是一个用于生成内容的内联属性。

通过使用 content 属性，您可以在伪元素中插入文本、图标、计数器或其他生成的内容，从而改变或增强文档的呈现。

下面是一个示例，演示如何使用 content 属性在伪元素中插入文本内容::

  .element::before {
    content: "前缀：";
  }

  .element::after {
    content: "（后缀）";
  }

在上述示例中，我们在 .element 元素的 ::before 伪元素中插入了文本 "前缀："，
在 ::after 伪元素中插入了文本 "（后缀）"。
这样，每个 .element 元素都会在其内容之前和之后显示相应的文本。

content 属性可以接受不同类型的值，包括字符串、URL、计数器等。
您可以使用引号将字符串括起来，也可以使用 CSS 函数、变量或其他 CSS 值。

此外，content 属性还可以与其他 CSS 属性一起使用，
例如 display、position、background 等，以控制伪元素的显示和样式。

.. important::

  content 属性仅适用于伪元素（:before 和 :after），不能直接用于真实的 HTML 元素。







