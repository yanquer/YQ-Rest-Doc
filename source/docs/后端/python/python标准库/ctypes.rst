========================
ctypes
========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


常用于加载C(++)模块

C与Python与ctypes类型
========================

.. table::
	:name: C与Python与ctypes类型对应关系sv表格

	==============================   ==============================          =====================
 	C Type                             Python Type                                 ctypes Type
	==============================   ==============================          =====================
	char                                1-character string                         c_char
	wchar_t                             1-character Unicode string                 c_wchar
	char                                int/long                                   c_byte
	char                                int/long                                   c_ubyte
	short                               int/long                                   c_short
	unsigned short                      int/long                                   c_ushort
	int                                 int/long                                   c_int
	unsigned int                        int/long                                   c_uint
	1ong                                int/long                                   c_long
	unsigned long                       int/long                                   c_ulong
	long long                           int/long                                   c_longlong
	unsigned long long                  int/long                                   c_ulonglong
	float                               float                                      c float
	double                              float                                      c_double
	char * (NULL terminated)            string or none                             c_charp
	wchar_t * (NULL terminated)         unicode or none                            c_wchar_p
	void *                              int/long or none                           c_void_P
	==============================   ==============================          =====================

搜索库
========================

模糊搜索本地存在的库::

	In [2]: from ctypes.util import find_library

	In [3]: find_library('SensApi')		# 本地没有

	In [4]: find_library('pthread')
	Out[4]: '/usr/lib/libpthread.dylib'

加载
========================

加载dll, 如Windows下存在 `SensApi.dll`, 试加载::

	In [5]: import ctypes

	In [6]: ctypes.cdll.LoadLibrary('SensApi')
	---------------------------------------------------------------------------
	OSError                                   Traceback (most recent call last)
	Cell In [6], line 1
	----> 1 ctypes.cdll.LoadLibrary('SensApi')

	File /usr/local/Cellar/python@3.9/3.9.10/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py:452, in LibraryLoader.LoadLibrary(self, name)
		451 def LoadLibrary(self, name):
	--> 452     return self._dlltype(name)

	File /usr/local/Cellar/python@3.9/3.9.10/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py:374, in CDLL.__init__(self, name, mode, handle, use_errno, use_last_error, winmode)
		371 self._FuncPtr = _FuncPtr
		373 if handle is None:
	--> 374     self._handle = _dlopen(self._name, mode)
		375 else:
		376     self._handle = handle

	OSError: dlopen(SensApi, 0x0006): tried: 'SensApi' (no such file), '/System/Volumes/Preboot/Cryptexes/OSSensApi' (no such file), '/usr/local/lib/SensApi' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/usr/local/lib/SensApi' (no such file), '/usr/local/lib/SensApi' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/usr/local/lib/SensApi' (no such file), '/usr/lib/SensApi' (no such file, not in dyld cache), 'SensApi' (no such file), '/usr/local/lib/SensApi' (no such file), '/usr/lib/SensApi' (no such file, not in dyld cache)

	In [7]: ctypes.cdll.LoadLibrary('libpthread.dylib')
	Out[7]: <CDLL 'libpthread.dylib', handle 485a6f120 at 0x107bac220>

	In [8]: ctypes.cdll.LoadLibrary('/usr/lib/libpthread.dylib')
	Out[8]: <CDLL '/usr/lib/libpthread.dylib', handle 485a6f120 at 0x1081f3a60>

	In [9]:

可以看出, 若只给一个模糊路径, 会在环境变量下查找是否存在, 不存在就报错.

若存在, 用绝对路径还是相对路径加载差距不大(除非在多个环境变量下包含同名库的不同实现).

定义结构体
========================

C级别::

	/* A C data structure */
	typedef struct Point {
		double x,y;
	} Point;

Python级别, 以类的形式定义, `_fields_` 定义其内变量::

	import ctypes
	# struct Point { }
	class Point(ctypes.Structure):
		_fields_ = [
			('x', ctypes.c_double),
			('y', ctypes.c_double)]

访问C级别函数
========================

注: 此处的 `Point` 已在上定义.

C函数::

	/* Function involving a C data structure */
	double distance(Point *p1, Point *p2) {
		return hypot(p1->x - p2->x, p1->y - p2->y);
	}

Python加载::

	# _mod = ctypes.cdll.LoadLibrary(_path)
	# double distance(Point *, Point *)
	distance = _mod.distance
	distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
	distance.restype = ctypes.c_double

使用动态库
========================

示例-使用动态库libc打印输出::

  # 系统: Mac

	from ctypes import CDLL, c_char_p
	from ctypes.util import find_library


	def do_c_print(data: str):
			# libc = CDLL("/Library/Developer/CommandLineTools/usr/lib/libclang.dylib")
			libc = CDLL("libc.dylib")
			lib_path = find_library("libc.dylib")

			# 正确输出
			libc.printf(b"do_c_print0: %s\n", c_char_p(bytes(data, 'utf8')))
			libc.printf(b"do_c_print1: %s\n", bytes(data, 'utf8'))
			libc.printf(b"do_c_print1: %s\nlib path: %s\n", bytes(data, 'utf8'), bytes(lib_path, 'utf8'))

			# 不行, 必须转换为字节
			libc.printf("do_c_print: %s\n\n", data)


	if __name__ == '__main__':
			do_c_print("it is a c print message")

可能是C那边是字节处理的原因, 所以调用的时候, Python的Unicode风格字符串
必须 **转换为字节** 才能被正常调用.

另外, find_library 好像找路径有点问题, 打印出来的结果是::

	/usr/lib/libc.dylib

但是实际系统找不到::

	$ ls /usr/lib/libc.dylib
	ls: /usr/lib/libc.dylib: No such file or directory

.. note::

	argtypes 绑定形参列表类型

	restype 绑定函数返回类型

	注意类型签名绑定是比较重要的, 否则可能代码不能正常运行, 甚至导致整个Python解释器挂掉, 故建议进行签名绑定.


