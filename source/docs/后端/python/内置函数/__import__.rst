=============================
__import__
=============================

用于动态加载类和函数

参数

__import__(name, globals=None, locals=None, fromlist=(), level=0)
  name: str
    导入的模块名, 当 fromlist 为空时, 返回的是顶层模块
  globals: None/globals()/locals()
    模块作用范围, 全局变量或局部变量.
    默认None, 一般不用设置
  fromlist: list
    导入子模块的集合.
  level: int
    0表示绝对导入, 为正使用相对导入, 相对于调用__import __()的模块目录







