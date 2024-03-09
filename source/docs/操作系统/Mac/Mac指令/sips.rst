==========================
sips
==========================

sips, 图像处理脚本(scriptable image processing system),
支持进行图片的格式转换, 以及图片的裁剪旋转等各种常用操作.
是MacOS自带的图片处理命令, 功能强大. 质量高,pdf转png会丢失背景,且不能处理ico文件

.. note::

  有个更简单的只能转换类型的 :doc:`/docs/操作系统/Mac/Mac指令/convert` ,
  不过清晰度不高.

图像处理脚本(scriptable image processing system)::

  This tool is used to query or modify raster image files and ColorSync ICC profiles.
  Its functionality can also be used through the "Image Events" AppleScript suite.

命令格式简洁版(下面太长)::

  sips -z 新图片宽度 新图片高度 原图片名 --out 临时.iconset/新图片完整名

Usages::

  sips [image-functions] imagefile ...
  sips [profile-functions] profile ...

Profile query functions::

  -g, --getProperty key
  -X, --extractTag tag tagFile
      --verify
  -1, --oneLine

Image query functions::

  -g, --getProperty key
  -x, --extractProfile profile
  -1, --oneLine

Profile modification functions::

  -s, --setProperty key value
  -d, --deleteProperty key
      --deleteTag tag
      --copyTag srcTag dstTag
      --loadTag tag tagFile
      --repair
  -o, --out file-or-directory

Image modification functions:::

  -s, --setProperty key value
  -d, --deleteProperty key
  -e, --embedProfile profile
  -E, --embedProfileIfNone profile
  -m, --matchTo profile
  -M, --matchToWithIntent profile intent
      --deleteColorManagementProperties
  -r, --rotate degreesCW
  -f, --flip horizontal|vertical
  -c, --cropToHeightWidth pixelsH pixelsW
      --cropOffset offsetY offsetH
  -p, --padToHeightWidth pixelsH pixelsW
      --padColor hexcolor
  -z, --resampleHeightWidth pixelsH pixelsW     裁剪图片, 指定宽度、高度
      --resampleWidth pixelsW                   裁剪图片, 指定宽度
      --resampleHeight pixelsH                  裁剪图片, 指定高度
  -Z, --resampleHeightWidthMax pixelsWH         裁剪图片, 指定宽度(高度自适应)
  -i, --addIcon
      --optimizeColorForSharing
  -o, --out file-or-directory
  -j, --js file

Other functions::

      --debug           Enable debugging output
  -h, --help            Show help
  -H, --helpProperties  所有键值参数(Show help for properties)
      --man             Generate man pages
  -v, --version         Show the version
      --formats         列出支持的格式(Show the read/write formats)

用例
==========================

图片格式转换
--------------------------

pdf->png::

  sips -s format png old.pdf -o new.png

pdf->jpg::

  sips -s format jpeg old.pdf -o new.jpg

jpg->gif::

  sips -s format gif old.jpg -o new.gif

.. note::

  ico格式(图标)不能通过sips实现, 只能通过imagemagick来操作.

修改图片为指定像素
--------------------------

修改图片为20000像素宽, 高度为自适应(Z大写)::

  sips -Z 20000 a.jpg

修改图片为200*200像素::

  sips -z 200 200 a.jpg

旋转/翻转图片
--------------------------

顺时针旋转图片180°::

  sips -r 180 a.jpg

水平/垂直翻转图片::

  sips -f horizontal  a.jpg
  sips -f vertical  a.jpg



