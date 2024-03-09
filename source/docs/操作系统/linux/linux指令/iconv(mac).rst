========================
iconv
========================

iconv 转换指定文件的编码，默认输出到标准输出设备，亦可指定输出文件

使用::

	iconv [options] [file]

选项参数
========================

-f, --from-code=encode-name		原始文本编码
-t, --to-code=encode-name		输出编码
-l, --list				列举所有已知的字符集
-c						从输出中忽略无效的字符
-o, --output=FILE		输出文件
-s, --silent			关闭警告
--verbose 				打印进度信息

用例
========================

将文件以 gbk 编码读出, 并转化为 utf8 编码, 重定向到 b.txt::

	# 有次mac下载了一本小说, 打开乱码, page的自动识别编码没法用
	# 又没有notpad++这种工具, vscode倒是可以切换编码, 但是保存的时候存在问题.
	# 只好用命令转换了
	iconv -f gbk -t utf8 -c mushenji2.txt >b.txt


