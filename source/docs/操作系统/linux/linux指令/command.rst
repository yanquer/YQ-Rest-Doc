=========================
command
=========================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


command -v 可以判断一个命令是否支持，如果一个脚本需要，或者还要加if判断::

  if command -v python ;then
      echo yes
  fi

