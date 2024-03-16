===================
AnchorJS
===================


.. post:: 2023-02-20 22:06:49
  :tags: node, 三方库
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


针对文档项目的索引吧. 官网: `anchorjs-doc <https://www.bryanbraun.com/anchorjs/>`_

安装/使用
===================

npm::

  // npm install anchor-js

  import AnchorJS from 'anchor-js';
  const anchors = new AnchorJS();
  anchors.add();

cdn::

  <script src="https://cdn.jsdelivr.net/npm/anchor-js/anchor.min.js"></script>
  <script>
    anchors.add();
  </script>

js file::

  import 'https://cdn.jsdelivr.net/npm/anchor-js/anchor.min.js';

  anchors.add();

一些方法
===================

.. function:: anchors.add()

  将一些链接加入以便便捷查找.

  参数为 css选择器 字符串. 比如::

    h1
    .title  // 类选择器

  多个合并为一个字符串, 使用逗号分隔.

  当不带参数时, 默认寻找::

    h2, h3, h4, h5, h6

建议在文档全部加载完成之前使用::

  <!-- Add anchors before the closing body tag. -->
    <script>
      anchors.add();
    </script>
  </body>

或者::

  // Add anchors on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', function(event) {
    anchors.add();
  });


.. 没有一个效果啥的, 不好理解, 后面有空了弄
