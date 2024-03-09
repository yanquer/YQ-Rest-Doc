==========================
css常见使用技巧
==========================

元素从左到右排列
==========================

这些从左到右的元素设置 `display` 为 `flex` 即可::

  .container {
    display: flex;
  }

在这个基础上, 如果要再实现最后一个元素靠右, 那么可以::

  .item-right {
      /* 会移动到最右边 */
      margin-left: auto;
  }

div结构::

  <div class="container">
    xxx1
    <div class="item">xxx2</div>
    <div class="item-right">xxx3</div>
  </div>

.. figure:: ../../../resources/images/2023-10-27-13-57-03.png
  :width: 480px

  效果





