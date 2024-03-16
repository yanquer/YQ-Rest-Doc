==========================
line_profiler
==========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


性能调优模块, 有个类似的 :doc:`/docs/后端/python/python三方库/memory_profiler`

官网: `https://pypi.org/project/line-profiler/`

安装::

  pip install line_profiler

方法1
  使用 ``@profile`` 装饰器后::

    kernprof -lv script_to_profile.py

貌似也直接可以用代码::

  from line_profiler import LineProfiler

  def base_func3():
      for n in range(10000):
          print(f'当前n的值是：{n}')


  lp = LineProfiler()
  lp_wrap = lp(base_func3)
  lp_wrap()
  lp.print_stats()








