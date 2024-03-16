=========================
tarfile
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/tarfile.html

读写tar归档文件, 包括使用 gzip, bz2 和 lzma 压缩的归档

常用::

  with tarfile.open('xxx.tar.gz', 'r:gz') as tar:
    tar.extractall(path='./data_dir')





