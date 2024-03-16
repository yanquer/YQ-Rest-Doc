=========================
rich
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


关于进度条可参见: :ref:`ProgressInPy`

安装::

  pip install rich

与 :doc:`/docs/后端/python/python三方库/tqdm`
一起弄彩色进度条::

  from tqdm.rich import tqdm, trange

  def print_hi():
      n = 10000
      for i in trange(n):
          for j in range(n):
              j += i

效果

.. figure:: ../../../../resources/images/2024-02-07-14-00-38.png
  :width: 480px

