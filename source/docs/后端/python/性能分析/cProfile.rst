==========================
cProfile
==========================


.. post:: 2023-02-20 22:06:49
  :tags: python, 性能分析
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


cProfile是Python标准库中内置的性能分析模块，C扩展，非侵入式，不需要修改代码。

使用方法::

  python -m cProfile [-s sort_order] myscript.py `

`-s` 指定输出的排序方法，可以传入tottime或者cumtime

- tottime表示该函数本身的执行时间，不包括该函数调用的子函数
- cumtime表示该函数累计执行时间，包括该函数调用的子函数

输出列含义
==========================

- ncalls是每个函数被调用次数
- tottime表示该函数本身的执行时间，不包括该函数调用的子函数
- 第一个percall表示tottime / ncalls
- cumtime表示该函数累计执行时间，包括该函数调用的子函数
- 第二个percall表示cumtime / primitive calls，primitive calls 表示除去递归后本函数被调用次数
- filename:lineno(function)表示函数所在的文件名，行号和函数名

cProfile是一种Deterministic Profiling.
Deterministic Profiling是指记录所有函数每次的执行状况，而不是通过采样的方式来记录.
通过采样的方式，性能开销会更小，但是记录可能会不够准确.

生成火焰图
==========================

使用 -o 选项生成cProfile的二进制性能结果::

  python -m cProfile [-o output_file] myscript.py

再用 flameprof 生成火焰图::

  flameprof requests.prof > requests.svg

图分成上下两部分，上部的图是按照函数调用栈和执行时间排列;
下部反方向的图按照函数执行时间比例从大到小排列.

上部的图中execute是最顶层的函数，往上是它调用的子函数，直到调用链最底层的函数;
宽度表示每个函数的执行时间占用的比例，越宽表示越耗时.



