
==========================
Python性能分析
==========================

查了一下, 主要的有以下几种

- cProfile: Python标准库中内置的性能分析模块，非侵入式.
  cProfile生成的结果可以进一步导出成火焰图
- line_profiler: 主要做函数内每行语句的性能分析，需要侵入代码.
  如果已经知道哪个函数是瓶颈，需要对函数进一步分析，可以使用这个.
- pyflame: 只能生成火焰图.
- pyinstrument: 使用采样方法对函数的执行时间进行记录，开销比cProfile要小.

.. toctree::
  :maxdepth: 1

  cProfile
  pyflame

