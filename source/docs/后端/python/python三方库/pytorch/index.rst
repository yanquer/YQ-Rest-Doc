=============================
pytorch
=============================


.. post:: 2024-03-09 18:21:01
  :tags: python, python三方库, pytorch
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


参考: `60分钟快速入门 PyTorch <https://zhuanlan.zhihu.com/p/66543791>`_

PyTorch 是由 Facebook 开发，基于 Torch 开发，
从并不常用的 Lua 语言转为 Python 语言开发的深度学习框架，
Torch 是 TensorFlow 开源前非常出名的一个深度学习框架，
而 PyTorch 在开源后由于其使用简单，
动态计算图的特性得到非常多的关注，并且成为了 TensorFlow 的 最大竞争对手。

安装::

  pip3 install torch torchvision torchaudio

检测是否适用于当前机器显卡::

  import torch

  print(torch.cuda.is_available())

.. toctree::
  :maxdepth: 1

  API
  autograd
  神经网络
  实例-训练分类器

张量(Tensors)
=============================

相当于 Numpy 的多维数组(ndarrays)。两者的区别就是 Tensors 可以应用到 GPU 上加快计算速度

声明与定义

- torch.empty() 声明一个未初始化的 Tensors 矩阵
- torch.rand() 随机初始化一个矩阵
- torch.zeros() 创建数值皆为 0 的矩阵
- torch.ones() 创建数值皆为 1 的矩阵
- torch.tensor() 直接传递 tensor 数值来创建
- tensor.new_ones() 根据已有的 tensor 变量创建新的 tensor 变量
- torch.randn_like(old_tensor) 保留相同的尺寸大小
- tensor.size() 获取张量大小

关于API的详细说明, 见 :doc:`/docs/后端/python/python三方库/pytorch/API`

和 Numpy 数组的转换
=============================

Tensor 和 Numpy 的数组可以相互转换，
并且两者转换后共享在 CPU 下的内存空间，
即改变其中一个的数值，另一个变量也会随之改变。

Tensor 转换为 Numpy 数组
-----------------------------

实现 Tensor 转换为 Numpy 数组的例子如下所示，
调用 tensor.numpy() 可以实现这个转换操作::

  a = torch.ones(5)
  print(a)
  b = a.numpy()
  print(b)

输出结果::

  tensor([1., 1., 1., 1., 1.])
  [1. 1. 1. 1. 1.]

b 也随着 a 的改变而改变::

  a.add_(1)
  print(a)
  print(b)

输出结果::

  tensor([2., 2., 2., 2., 2.])
  [2. 2. 2. 2. 2.]

Numpy 数组转换为 Tensor
-----------------------------

转换的操作是调用 torch.from_numpy(numpy_array) 方法。
例子如下所示::

  import numpy as np
  a = np.ones(5)
  b = torch.from_numpy(a)
  np.add(a, 1, out=a)
  print(a)
  print(b)

输出结果::

  [2. 2. 2. 2. 2.]
  tensor([2., 2., 2., 2., 2.], dtype=torch.float64)

在 CPU 上，除了 CharTensor 外的所有 Tensor 类型变量，都支持和 Numpy数组的相互转换操作

CUDA 张量
=============================

Tensors 可以通过 .to 方法转换到不同的设备上，即 CPU 或者 GPU 上。
例子如下所示::

  # 当 CUDA 可用的时候，可用运行下方这段代码，采用 torch.device() 方法来改变 tensors 是否在 GPU 上进行计算操作
  if torch.cuda.is_available():
      device = torch.device("cuda")          # 定义一个 CUDA 设备对象
      y = torch.ones_like(x, device=device)  # 显示创建在 GPU 上的一个 tensor
      x = x.to(device)                       # 也可以采用 .to("cuda")
      z = x + y
      print(z)
      print(z.to("cpu", torch.double))       # .to() 方法也可以改变数值类型

输出结果，第一个结果就是在 GPU 上的结果，
打印变量的时候会带有 device='cuda:0'，而第二个是在 CPU 上的变量::

  tensor([1.4549], device='cuda:0')
  tensor([1.4549], dtype=torch.float64)




