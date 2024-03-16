=========================
pillow(PIL)
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


安装::

  pip install pillow

导入::

  imprt PIL

PIL，全称 Python Imaging Library, 图像处理库.

PIL 仅支持到Python 2.7，加上年久失修，于是一群志愿者在 PIL 的基础上创建了兼容 Python 3 的版本，名字叫 Pillow ，
可以通过安装 Pillow 来使用 PIL。

打开、保存、显示图片
=========================

打开、保存、显示图片::

  from PIL import Image

  image = Image.open('img.jpg')
  image.show()
  image.save('1.jpg')
  print(image.mode, image.size, image.format)
  # RGB (481, 321) JPEG

- mode 为图片的模式，RGB 代表彩色图像，L 代表光照图像也即灰度图像等
- size 为图片的大小(宽度，长度)
- format 为图片的格式，如常见的 PNG、JPEG 等

转换图片模式
=========================

转换图片模式::

  image.show()
  grey_image = image.convert('L')
  grey_image.show()

通道分离合并
=========================

通道分离合并::

  r, g, b = image.split()
  im = Image.merge('RGB', (b, g, r))

彩色图像可以分离出 R、G、B 通道，但若是灰度图像，则返回灰度图像本身。然后，可以将 R、G、B 通道按照一定的顺序再合并成彩色图像。

图片裁剪、旋转和改变大小
=========================

图片裁剪、旋转和改变大小::

  # 对角坐标, 左上(x, y), 右下(x, y)
  box = (100, 100, 300, 300)
  region = image.crop(box)
  # 翻转180度
  region = region.transpose(Image.ROTATE_180)
  image.paste(region, box)
  image.show()

或者::

  im = image.resize((300, 300))
  im = image.rotate(45)  # 逆时针旋转 45 度
  im = image.transpose(Image.FLIP_LEFT_RIGHT) # 左右翻转
  im = im.transpose(Image.FLIP_TOP_BOTTOM)# 上下翻转

像素值操作
=========================

像素值操作::

  out = image.point(lambda i: i * 1.2) # 对每个像素值乘以 1.2

  source = image.split()
  out = source[0].point(lambda i: i > 128 and 255) # 对 R 通道进行二值化

和Numpy数组之间的转化
=========================

和 Numpy 数组之间的转化::

  array = np.array(image)
  print(array.shape) #(321, 481, 3)
  out = Image.fromarray(array)

图像缩放滤波器-Pillow库
=========================

在Pillow库中，常用的图像缩放滤波器有以下几种：

Image.NEAREST:
  最近邻滤波器。它选择距离缩放后位置最近的像素作为新像素值，缩放速度快但效果较差。
Image.BOX:
  均值滤波器。它计算在缩放前覆盖每个输出像素的所有输入像素的平均值，并使用该平均值作为新像素值。比最近邻滤波器更平滑，但也可能导致图像失真。
Image.BILINEAR:
  双线性滤波器。它通过对距离缩放后位置最近的四个像素进行加权平均来计算新像素值。比均值滤波器和最近邻滤波器更平滑，但可能会丢失一些细节。
Image.HAMMING:
  汉明窗口函数滤波器。它将输入像素与一个汉明窗口函数进行卷积，以平滑图像并减少锯齿状失真。具有较高的计算复杂性，但效果很好。
Image.BICUBIC:
  双三次插值滤波器。它通过在距离缩放后位置最近的16个像素上应用双三次插值来计算新像素值。比双线性滤波器更平滑，但可能会丢失一些细节。
Image.LANCZOS:
  兰索斯滤波器。它通过在距离缩放后位置最近的若干个像素上应用一个基于兰索斯函数的卷积核来计算新像素值。它提供了最高的质量，但计算复杂度也最高。

每种滤波器都有其适用的场景和优缺点。
通常，如果需要快速处理大量图像，则可以使用Image.NEAREST或Image.BOX滤波器。
如果需要减少锯齿状失真并保留更多的细节，则可以使用Image.BILINEAR或Image.BICUBIC滤波器。
如果您需要最高质量的缩放，例如用于摄影或印刷品，那么可以使用Image.LANCZOS滤波器，但需要注意它的计算复杂度较高。

ps: 现在高版本使用的是 Image.Resampling.xxx , 如缩放时使用 LANCZOS 滤波器::

  with Image.open(img_file) as im:
    # 计算缩放后的图片大小
    # im.convert('RGB')
    width, height = im.size
    new_width, new_height = int(width * scale), int(height * scale)
    size = (new_width, new_height)

    # 缩放图像
    resized_im = im.resize(size, resample=Image.Resampling.LANCZOS)

