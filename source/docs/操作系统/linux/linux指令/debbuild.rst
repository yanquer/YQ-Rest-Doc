============================
debbuild
============================


.. post:: 2023-02-27 21:24:23
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


deb完整构建可参考: :doc:`/docs/操作系统/linux/教程/本地构建deb包`

deb包需要的目录结构构建好后
(可使用 :doc:`/docs/操作系统/linux/linux指令/debmake` 来构建目录结构),
通过此命令来构建完整的deb包.

`debbuild` 读取软件包的源代码目录中的 `debian/rules`` 文件来执行构建过程，
并自动处理构建过程中的许多步骤，例如配置、编译和安装.
`debuild` 还会检查构建依赖关系并确保它们已满足，以及生成符合 Debian 软件包规范的二进制和源代码软件包.

相对而言 :doc:`/docs/操作系统/linux/linux指令/dpkg` 更底层一点, 只需要编译好的代码与目录结构即可.



