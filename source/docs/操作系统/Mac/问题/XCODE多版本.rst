================================
Mac-Xcode 多版本
================================


.. post:: 2023-02-26 21:30:12
  :tags: Mac, 问题
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


github上有现成的项目方便切换,
地址: https://github.com/XcodesOrg/XcodesApp/tags

使用: 需要先手动登陆Apple ID

.. note::

  需要对应版本的command line

其他方式
  手动命令行操作, 参考地址: https://juejin.cn/post/7251792725070217275

  查看当前版本指令::

    # 或者 xcode-select -p
    gcc --version

  切换版本指令::

    sudo xcode-select --switch <xcode_folder_path>

**上述失败, 现在版本是Mac OS14.1, 能下载不能打开, 作罢**
