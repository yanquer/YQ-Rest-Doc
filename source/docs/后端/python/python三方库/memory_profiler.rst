====================================
memory_profiler
====================================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


性能调优模块, 有个类似的 :doc:`/docs/后端/python/python三方库/line_profiler`

官网: `https://pypi.org/project/memory-profiler/`

安装::

  pip install memory_profiler

最简单的使用就是使用装饰器::

  from memory_profiler import profile

  @profile
  def count():
    a += 1
    ...

输出头的含义::

  Line #    Mem usage    Increment  Occurrences   Line Contents

分别为: 代码所在行; 内存总共占用, 增加的内存; 运行次数; 代码内容

- 找内存泄漏，直接看Increment;
- 如果想找内存瓶颈，就看Mem usage

mprof指令
====================================

安装此模块时候, 一般会同时安装以下mprof指令,
可以用来绘制内存变化图

先执行(app,py内先要有@profile装饰器, 如上)::

  mprof run app.py

然后会生成一个 ``mprofile_xxxxxxxxxxxx.dat`` 文件,
通过此文件画出内存变化图::

  mprof plot mprofile_xxxxxxxxxxxxxxxx.dat


