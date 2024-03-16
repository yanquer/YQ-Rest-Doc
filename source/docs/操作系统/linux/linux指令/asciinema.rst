=======================
asciinema
=======================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


与 :doc:`/docs/操作系统/linux/linux指令/script` 类似

终端脚本录制工具, 支持多种方式安装,

pip安装::

  pip install asciinema

debian/ubuntu使用apt安装::

  apt install asciinema

终端执行的录制
=======================

开始录制::

  asciinema rec

然后像平常一样使用即可, 会自动被记录

结束录制(也可以不用 `exit` 而是直接 `Ctrl+D`)::

  exit

根据提示可选择上传或者保存到本地, 一般输出为 `.cast` 文件
(貌似)

