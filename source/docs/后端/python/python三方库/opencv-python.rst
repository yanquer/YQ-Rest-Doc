======================
opencv
======================

安装::

  pip install opencv-python

印象里多用于深度学习下的图像处理, 一般与 :doc:`/docs/后端/python/python三方库/numpy` 一起使用

导入::

  import cv2

**opencv 获取的图像都是 numpy 的 ndarray 对象**
对于一个长宽分别为w、h的RGB彩色图像来说，它的每个像素值是由(B、G、R)的一个tuple组成，
opencv-python中每个像素三个值的顺序是(B、G、R)

读取图像-imread
======================

.. function:: cv2.imread(path_of_image, intflag)

  读取图像

  path_of_image:
    图像路径
  intflag:
    读取形式, 支持以下参数:

    - cv2.IMREAD_COLOR: 1, 加载彩色图像。任何图像的透明度都将被忽略。它是默认标志
    - cv2.IMREAD_GRAYSCALE: 0, 以灰度模式加载图像
    - cv2.IMREAD_UNCHANGED: -1, 保留读取图片原有的颜色通道

显示图像-imshow
======================

.. function:: cv2.imshow(windows_name, image)

  窗口显示图像

  windows_name: str
    窗口名称
  image:
    图片对象, 即上面 读取图像-imread_ 读取的对象. 类型为numpy中的ndarray

    支持使用 imutils.resize(image, size) 来调整大小

例::

  img = cv2.imread('img.png')
  cv2.imshow('image', imutils.resize(img, 800))
  if cv2.waitKey(0) == 27:
      cv2.destroyAllWindows()

保存图像-imwrite
======================

.. function:: cv2.imwrite(image_filename, image)

  将图片对象写入文件(保存)

  image_filename: str
    保存的图像名称
  image:
    图像对象，即上面 读取图像-imread_ 读取的对象. 类型是numpy中的ndarray类型

例::

  cv2.imwrite('img_1.jpg', img)   # 将图像保存成jpg文件
  cv2.imwrite('img_2.png', img)   # 将图像保存成png文件

放置文字-putText
======================

只能英文, 中文会乱码, 据说 opencv5.0 会解决这个问题, 截止目前尚未发布.

转换为PIL可添加中文: https://cloud.tencent.com/developer/article/2214890#


窗口销毁-destroyAllWindows/destroyWindow
============================================

.. function:: cv2.destroyWindow(windows_name)

  销毁单个特定窗口

  windows_name: str
    销毁窗口名, 由上面 显示图像-imshow_ 的第一个参数指定

.. function:: cv2.destroyAllWindows()

  销毁全部窗口，无参数

.. function:: cv2.waitKey(time_of_milliseconds)

  与上两个函数一起使用, 等待一段时间销毁窗口

  time_of_milliseconds: int
    - 大于0时, 表示等待多少毫秒销毁

    - 小于等于0时, 表示等待键盘敲击事件, 满足时销毁.
      如, 指定waitKey(0) == 27时当敲击键盘 Esc 时便销毁所有窗口::

        if cv2.waitKey(0) == 27: cv2.destroyAllWindows()

      当接收到键盘敲击A时，便销毁名称为'origin image'的图像窗口::

        if cv2.waitKey(-1) == ord('A'): cv2.destroyWindow('origin image')

图像色彩空间变换-cvtColor
============================================

.. function:: cv2.cvtColor(input_image, flag)

  图像色彩空间变换函数

  input_image:
    将要变换色彩的图像ndarray对象, 即上面 读取图像-imread_ 读取的对象
  flag:
    图像色彩空间变换的类型，常用的两种:

    - cv2.COLOR_BGR2GRAY: 表示将图像从BGR空间转化成灰度图，最常用
    - cv2.COLOR_BGR2HSV: 表示将图像从RGB空间转换到HSV空间

    获取全部274种空间转换类型::

      import cv2
      flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
      print(flags)

图像处理时, 经常将彩色图像转化成灰度图像, 因为图像颜色会因为光照因素而产生不同变化(即变成不同颜色图片).
而图像特征提取/识别过程，需要的是图像的梯度信息，也就是图像的本质内容，所以去除颜色对梯度干扰. 可以降低数据量, 增强处理效果.

图像绘制
======================

- 直线 cv2.line: 直线-line_
- 长方形 cv2.rectangle: 长方形-rectangle_
- 圆 cv2.circle: 圆-circle_
- 椭圆 cv2.ellipse: 椭圆-ellipse_
- 多边形 cv2.polylines: 多边形-polylines_

公共参数：

img:
  表示需要进行绘制的图像对象ndarray
color:
  表示绘制几何图形的颜色，采用BGR即上述说的(B、G、R)
thickness:
  表示绘制几何图形中线的粗细，默认为1，对于圆、椭圆等封闭图像取-1时是填充图形内部
lineType:
  表示绘制几何图形线的类型，默认8-connected线是光滑的，当取cv2.LINE_AA时线呈现锯齿状

直线-line
-----------------------

.. function:: cv2.line(image, starting, ending, color, thickness, lineType)

  starting:
    线的起点像素坐标
  ending:
    线的终点像素坐标

长方形-rectangle
-----------------------

.. function:: cv2.rectangle(image, top-left, bottom-right, color, thickness, lineType)

  top-left:
    表示长方形的左上角像素坐标
  bottom-right:
    表示长方形的右下角像素坐标

圆-circle
-----------------------

.. function:: cv2.circle(image, center, radius, color, thickness, lineType)
  :noindex:

  center:
    表示圆的圆心像素坐标
  radius:
    表示圆的半径长度

  圆绘制函数中当参数thickness = -1 时绘制的是实心圆，当thickness >= 0 时绘制的是空心圆

椭圆-ellipse
-----------------------

.. function:: cv2.circle(image, center, (major-axis-length, minor-axis-length), angle, startAngle, endAngle, color, thickness, lineType)
  :noindex:

  center:
    表示椭圆中心像素坐标
  major-axis-length:
    表示椭圆的长轴长度
  minor-axis-length:
    表示椭圆的短轴长度
  angle:
    表示椭圆在逆时针方向旋转的角度
  startAngle:
    表示椭圆从主轴向顺时针方向测量的椭圆弧的起始角度
  endAngle:
    表示椭圆从主轴向顺时针方向测量的椭圆弧的终止时角度

  当参数thickness = -1 时绘制的是实心椭圆，当thickness >= 0 时绘制的是空心椭圆

多边形-polylines
-----------------------

.. function:: cv2.polylines(image, [point-set], flag, color, thickness, lineType)

  point-set:
    表示多边形点的集合，如果多边形有m个点，则便是一个m*1*2的数组，表示共m个点
  flag: bool
    当flag = True 时，则多边形是封闭的，当flag = False 时，则多边形只是从第一个到最后一个点连线组成的图像，没有封闭

例::

  pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
  img = cv2.polylines(img,[pts],True,(0, 0, 0), 2)

对图像的简单像素操作
======================

对图像取反::

  gray_img = cv2.imread('img.jpg', 0)  # 加载灰度图像
  reverse_img = 255 - gray_img

对图像像素线性变换::

  for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
      random_img[i, j] = gray_img[i, j]*1.2

