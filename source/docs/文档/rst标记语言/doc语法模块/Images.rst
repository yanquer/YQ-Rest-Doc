============================
Images
============================

Image
============================

支持类型 image

支持的命令选项:

alt: text
  当应用不能加载图片时, 显示的文字
height: length
  图片高度
width: length or percentage of the current line width
  图片宽度
scale: integer percentage (the "%" symbol is optional)
  图片缩放, 以百分比的形式, 默认 100%
align: "top", "middle", "bottom", "left", "center", or "right"
  图片位置
target: text (URI or reference name)
  图片可被点击, 支持两种形式:
  - url, 点击跳转到url
  - 可以通过类似这样 \`a name\`_ 跳转

and the common options class and name.

示例, 源码::

  .. image:: ../../resources/images/2023-02-02-15-11-21.png
    :alt: test_image
    :scale: 50%
    :align: center
    :target: https://www.baidu.com

.. image:: ../../../../resources/images/2023-02-02-15-55-24.png
  :alt: test_image
  :scale: 50%
  :align: center
  :target: https://www.baidu.com


Figure
============================

命令类型: figure

与image的区别是, 可以在图片下标注文字段落(可选).

源码::

  .. figure:: ../../../resources/images/2023-02-02-15-55-24.png
    :scale: 50 %
    :alt: map to buried treasure

    This is the caption of the figure (a simple paragraph).

    The legend consists of all elements after the caption.  In this
    case, the legend consists of this paragraph and the following
    table:

    +----------------------------------------------------------------+-----------------------+
    | Symbol                                                         | Meaning               |
    +================================================================+=======================+
    | .. image:: ../../../resources/images/2023-02-02-15-55-24.png   |                       |
    |    :scale: 30%                                                 | Campground            |
    |                                                                |                       |
    +----------------------------------------------------------------+-----------------------+
    | .. image:: ../../../resources/images/2023-02-02-15-55-24.png   |                       |
    |    :scale: 30%                                                 | Lake                  |
    |                                                                |                       |
    +----------------------------------------------------------------+-----------------------+
    | .. image:: ../../../resources/images/2023-02-02-15-55-24.png   |                       |
    |    :scale: 30%                                                 | Mountain              |
    |                                                                |                       |
    +----------------------------------------------------------------+-----------------------+

    .. csv-table::
      :header: Symbol, Meaning

      .. image:: ../../../resources/images/2023-02-02-15-55-24.png , Campground
      .. image:: ../../../resources/images/2023-02-02-15-55-24.png , Lake
      .. image:: ../../../resources/images/2023-02-02-15-55-24.png , Mountain

**效果**

.. figure:: ../../../../resources/images/2023-02-02-15-55-24.png
  :scale: 50 %
  :alt: map to buried treasure

  This is the caption of the figure (a simple paragraph).

  The legend consists of all elements after the caption.  In this
  case, the legend consists of this paragraph and the following
  table:

  +-------------------------------------------------------------------+-----------------------+
  | Symbol                                                            | Meaning               |
  +===================================================================+=======================+
  | .. image:: ../../../../resources/images/2023-02-02-15-55-24.png   |                       |
  |    :scale: 30%                                                    | Campground            |
  |                                                                   |                       |
  +-------------------------------------------------------------------+-----------------------+
  | .. image:: ../../../../resources/images/2023-02-02-15-55-24.png   |                       |
  |    :scale: 30%                                                    | Lake                  |
  |                                                                   |                       |
  +-------------------------------------------------------------------+-----------------------+
  | .. image:: ../../../../resources/images/2023-02-02-15-55-24.png   |                       |
  |    :scale: 30%                                                    | Mountain              |
  |                                                                   |                       |
  +-------------------------------------------------------------------+-----------------------+

  .. csv-table::
    :header: Symbol, Meaning

    .. image:: ../../../../resources/images/2023-02-02-15-55-24.png , Campground
    .. image:: ../../../../resources/images/2023-02-02-15-55-24.png , Lake
    .. image:: ../../../../resources/images/2023-02-02-15-55-24.png , Mountain

支持命令选项, 除了支持image的所有选项外, 还支持以下选项:

align: "left", "center", or "right"
  此处列出主要说明只支持以上三个参数
figwidth: "image", length, or percentage of current line width
  注意更改的是所在区域的宽度而非图片宽度.

  当参数值为图片路径时: 若图片不存在, 则忽略此选项; 若存在则使用该图片的真实宽度值(依赖python的Imaging库).

  实际运作可参考下图::

    +---------------------------+
    |        figure             |
    |                           |
    |<------ figwidth --------->|
    |                           |
    |  +---------------------+  |
    |  |     image           |  |
    |  |                     |  |
    |  |<--- width --------->|  |
    |  +---------------------+  |
    |                           |
    |The figure's caption should|
    |wrap at this width.        |
    +---------------------------+
figclass: text
  设置 classes 属性, 暂时不知道有什么用




