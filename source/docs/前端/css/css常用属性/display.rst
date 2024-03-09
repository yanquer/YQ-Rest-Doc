======================
display
======================

设置元素是否被视为块或者内联元素以及用于子元素的布局，例如流式布局、网格布局或弹性布局;
默认: inline

- none	此元素不会被显示
- block	此元素将显示为块级元素，此元素前后会带有换行符
- inline	默认。此元素会被显示为内联元素，元素前后没有换行符
- inline-block	行内块元素。（CSS2.1 新增的值）
- list-item	此元素会作为列表显示
- run-in	此元素会根据上下文作为块级元素或内联元素显示
- compact	CSS 中有值 compact，不过由于缺乏广泛支持，已经从 CSS2.1 中删除
- marker	CSS 中有值 marker，不过由于缺乏广泛支持，已经从 CSS2.1 中删除
- table	此元素会作为块级表格来显示（类似 <table>），表格前后带有换行符
- inline-table	此元素会作为内联表格来显示（类似 <table>），表格前后没有换行符
- table-row-group	此元素会作为一个或多个行的分组来显示（类似 <tbody>）
- table-header-group	此元素会作为一个或多个行的分组来显示（类似 <thead>）
- table-footer-group	此元素会作为一个或多个行的分组来显示（类似 <tfoot>）
- flow-root	生成一个块级元素盒，其会建立一个新的块级格式化上下文，定义格式化上下文的根元素
- table-row	此元素会作为一个表格行显示（类似 <tr>）
- table-column-group	此元素会作为一个或多个列的分组来显示（类似 <colgroup>）
- table-column	此元素会作为一个单元格列显示（类似 <col>）
- table-cell	此元素会作为一个表格单元格显示（类似 <td> 和 <th>）
- table-caption	此元素会作为一个表格标题显示（类似 <caption>）
- inherit	规定应该从父元素继承 display 属性的值
- flex: Flexible Box的缩写，意为"弹性布局"，用来为盒状模型提供最大的灵活性。
  设为Flex布局以后，子元素的float、clear和vertical-align属性将失效

对于 flex, 还有以下拓展属性

- flex-direction容器内元素的排列方向(默认横向排列)
- flex-wrap 容器内元素的换行(默认不换行)
- justify-content 元素在X轴上的排列.
  支持的值:

  - flex-start: Flex项向行头紧挨着填充。这个是默认值。
  - flex-end: Flex项向行尾紧挨着填充。
  - center: Flex项居中紧挨着填充。
  - space-between: Flex项平分剩余空间。
  - space-around: Flex项平分剩余空间,空间在Flex项之间。
  - space-evenly: Flex项平分剩余空间,空间在Flex项及边缘之间。
- align-items 元素在Y轴方向上的对齐方式
- align-content 在弹性容器内的元素没有占用交叉轴上所有可用的空间时对齐容器内的各项（垂直）

如 `parent` 下的子元素上下左右都居中::

  .parent {
    display: flex;
    justify-content: center;
    align-items: center;
  }

或者::

  .parent {
    display: flex;
    flex-direction: center;
    place-content: center;
    // justify-content: center;
    align-items: center;

    width: 100%;
    height: 100%;
  }

