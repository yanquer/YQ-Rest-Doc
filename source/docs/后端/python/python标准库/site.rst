=========================
site
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/site.html

获取本地三方包路径::

  $ python3 -m site --user-site
  /home/user/.local/lib/python3.3/site-packages

--user-base
  输出用户基本的路径。
--user-site
  输出用户site-packages目录的路径。


