=========================
command
=========================

command -v 可以判断一个命令是否支持，如果一个脚本需要，或者还要加if判断::

  if command -v python ;then
      echo yes
  fi

