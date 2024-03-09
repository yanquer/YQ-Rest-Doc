=====================
struct
=====================

与c底层数据做转换, 设计到了字节, 大小端, 数据流等的知识

常用函数:

- pack(fmt,v1,v2…)
  返回string. 按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
- unpack(fmt,v1,v2…..)
  返回tuple. 按照给定的格式(fmt)解析字节流,并返回解析结果
- calcsize(fmt)
  返回size of fmt. 计算给定的格式(fmt)占用多少字节的内存，注意对齐方式



:详情参见:: https://blog.csdn.net/qq_30638831/article/details/80421019

