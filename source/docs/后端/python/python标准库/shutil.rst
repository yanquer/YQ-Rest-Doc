========================
shutil
========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/shutil.html

高阶文件操作

shutil 模块提供了一系列对文件和文件集合的高阶操作。
特别是提供了一些支持文件拷贝和删除的函数。 对于单个文件的操作，请参阅 os 模块。

一些常用

- copy, 文件的复制, 复制时, 如果是软链, 会自动找到真实的源文件, 然后把源文件复制过来,
  新的文件名与软链名保持一致, 可使用 `follow_symlinks=False` 达到与 `copy2` 一致
- copy2, 文件的复制, 复制时, 如果是软链, 仅复制此软链
- copy_tree, 目录的复制


.. function:: shutil.disk_usage(path)

  返回给定路径的磁盘使用统计数据，形式为一个 named tuple，
  其中包含 total, used 和 free 属性，分别表示总计、已使用和未使用空间的字节数。

  path 可以是一个文件或是一个目录。

.. function:: shutil.move(src, dst, copy_function=copy2)

  递归地将一个文件或目录 (src) 移至另一位置 (dst) 并返回目标位置。

  如果目标是已存在的目录，则 src 会被移至该目录下。 如果目标已存在但不是目录，它可能会被覆盖，具体取决于 os.rename() 的语义。

.. function:: shutil.rmtree(path, ignore_errors=False, onerror=None, *, dir_fd=None)

  删除一个完整的目录树；

  path 必须指向一个目录（但不能是一个目录的符号链接）。

  如果 ignore_errors 为真值，删除失败导致的错误将被忽略；
  如果为假值或是省略，此类错误将通过调用由 onerror 所指定的处理程序来处理，
  或者如果此参数被省略则将引发一个异常。

.. function:: shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

  递归地将以 src 为根起点的整个目录树拷贝到名为 dst 的目录并返回目标目录。
  所需的包含 dst 的中间目录在默认情况下也将被创建。

  目录的权限和时间会通过 copystat() 来拷贝，单个文件则会使用 copy2() 来拷贝



