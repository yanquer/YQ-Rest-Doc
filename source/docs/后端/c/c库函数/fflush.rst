===============================
fflush
===============================


.. post:: 2023-02-20 22:06:49
  :tags: c, c库函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. function:: int fflush(FILE *stream)

  清除读写缓冲区，用于需要立即把输出缓冲区的数据进行物理写入时

  fflush()会强迫将缓冲区内的数据写回参数stream 指定的文件中.
  如果参数stream 为NULL,fflush()会将所有打开的文件数据更新

