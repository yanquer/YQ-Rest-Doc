==========================
API
==========================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库, pytorch
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


torch提供的API
==========================

torch.empty()
  声明一个未初始化的 Tensors 矩阵.

  如创建一个 5*3 的矩阵::

    x = torch.empty(5, 3)
torch.rand()
  随机初始化一个矩阵

  创建一个随机初始化的 5*3 矩阵::

    rand_x = torch.rand(5, 3)
torch.zeros()
  创建数值皆为 0 的矩阵

  创建一个数值皆是 0，类型为 long 的矩阵::

    zero_x = torch.zeros(5, 3, dtype=torch.long)
torch.ones()
  创建数值皆为 1 的矩阵
torch.tensor()
  直接传递 tensor 数值来创建

  tensor 数值是 [5.5, 3]::

    tensor1 = torch.tensor([5.5, 3])
    print(tensor1)

  输出结果::

    tensor([5.5000, 3.0000])
tensor.new_ones()
  除了上述几种方法，还可以根据已有的 tensor 变量创建新的 tensor 变量，
  这种做法的好处就是可以保留已有 tensor 的一些属性，
  包括尺寸大小、数值属性，除非是重新定义这些属性。相应的实现方法如下::

    tensor.new_ones()   # new_*() 方法需要输入尺寸大小

  如显示定义新的尺寸是 5*3，数值类型是 torch.double::

    tensor2 = tensor1.new_ones(5, 3, dtype=torch.double)  # new_* 方法需要输入 tensor 大小
    print(tensor2)

  输出结果::

    tensor([[1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.]], dtype=torch.float64)
torch.randn_like(old_tensor)
  保留相同的尺寸大小
tensor.size()
  torch.Size 是元组(tuple)类型，所以支持所有的元组操作

torch.add()
  加法实现::

    torch.add(tensor1, tensor2, [out=tensor3])
    tensor1.add_(tensor2)     # 直接修改 tensor 变量, 有后缀 _

  或者直接::

    tensor3 = tensor1 + tensor2

  .. note::

    可以改变 tensor 变量的操作都带有一个后缀 _, 例如::

      x.copy_(y)
      x.t_()

    都可以改变 x 变量
torch.view()
  修改 tensor 尺寸

  如::

    x = torch.randn(4, 4)
    y = x.view(16)
    # -1 表示除给定维度外的其余维度的乘积
    z = x.view(-1, 8)
    print(x.size(), y.size(), z.size())

  输出结果::

    torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])

  如果 tensor 仅有一个元素，可以采用 .item() 来获取类似 Python 中整数类型的数值::

    x = torch.randn(1)
    print(x)
    print(x.item())

  输出结果::

    tensor([0.4549])
    0.4549027979373932
torch.from_numpy(numpy_array)
  Numpy 数组转换为 Tensor

  在 CPU 上，除了 CharTensor 外的所有 Tensor 类型变量，都支持和 Numpy数组的相互转换操作
torch.device("cuda")
  定义一个 CUDA 设备对象

计算平均值mean
==========================

不带参数, 表示计算所有元素平均值

dim
  - None, 表示计算所有元素平均值
  - 0, 表示在张量的第一个维度（列）上进行操作
  - 1, 表示在张量的第二个维度（行）上进行操作

如::

  # 创建一个示例张量
  x = torch.tensor([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]], dtype=torch.float64)

  # 计算整个张量的平均值
  mean_all = x.mean()
  print(mean_all)  # 输出: tensor(5., dtype=torch.float64)

  # 沿着特定维度计算平均值
  mean_dim0 = x.mean(dim=0)
  print(mean_dim0)  # 输出: tensor([4., 5., 6.], dtype=torch.float64)

  mean_dim1 = x.mean(dim=1)
  print(mean_dim1)  # 输出: tensor([2., 5., 8.], dtype=torch.float64)

torch.nn
==========================

torch.nn.conv2d(in_channels: int, out_channels: int, kernel_size: _size_2_t,)
  卷积函数

  in_channels
    输入通道
  out_channels
    输出通道
  kernel_size
    卷积核大小




