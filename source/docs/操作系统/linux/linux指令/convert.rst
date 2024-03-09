===================
convert
===================

转换图片格式，支持JPG, BMP, PCX, GIF, PNG, TIFF, XPM和XWD等类型

mac安装::

	brew install imagemagick

获取图片尺寸::

	 identify ABCD.png

输出::

	ABCD.png PNG 339x362 339x362+0+0 8-bit DirectClass 76.2kb

说明：图片ABCD.png的格式为PNG，宽、高分别为339和362，位深度8-bit，大小76.2kb；下文主要涉及宽、高的信息。

将jpeg转成png文件::

	convert  xxx.jpg  xxx.png

将gif转换成bmp图像::

	convert  xxx.gif   xxx.bmp

将tiff转换成pcx图像::

	convert  xxx.tiff    xxx.pcx

将图像的像素改为1024*768，注意1024与768之间是小写字母x::

	convert -resize 1024x768  xxx.jpg   xxx1.jpg

将图像的缩减为原来的50%*50%::

	convert -sample 50%x50%  xxx.jpg  xxx1.jpg

将图像顺时针旋转270度::

	convert -rotate 270 sky.jpg sky-final.jpg

使用-draw选项还可以在图像里面添加文字::

	convert -fill black -pointsize 60 -font helvetica -draw 'text 10,80 "Hello, World!" ‘  hello.jpg  helloworld.jpg

在图像上加上文字说明, 比如版权::

	# 支持用 -font 指定字体，需要安装Ghostscript支持: http://www.cs.wisc.edu/~ghost/
	# 或者用 composite 命令在所有图片上加上水印: http://www.imagemagick.org/script/composite.php
	convert 1.png -fill white -pointsize 13 -draw “text 10,15 ‘lifesinger 2006＇” 2.png


:参考::
	`Linux之convert命令 <https://www.cnblogs.com/yymn/p/4479805.html>`_
	`巧用linux工具之convert简介 <https://www.jianshu.com/p/cb13af56ba49#>`_

