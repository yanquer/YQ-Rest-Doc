=============================
tqdm
=============================

也是用来做进度控制的

关于进度条可参见: :ref:`ProgressInPy`

安装::

  pip install pqdm

例子::

  from tqdm import tqdm, trange

  def print_hi():
      n = 10000
      # 也可以
      # for i in trange(n):
      for i in tqdm(range(n)):
          for j in range(n):
              j += i

效果::

  100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:02<00:00, 4132.14it/s]

还可以跟 :doc:`/docs/后端/python/python三方库/rich` 一起弄彩色进度条

也可以与 notebook, tk等一起::

  # 彩色进度
  from tqdm.rich import tqdm, trange
  # 兼容 jupyter
  from tqdm.notebook import tqdm, trange
  # tk进度条
  from tqdm.tk import tqdm, trange

如果是非循环代码的进度条, 直接定义tqdm对象即可::

  bar = tqdm(total=100)
  ...
  bar.update(10)
  ...
  bar.update(30)
  ...
  ...



