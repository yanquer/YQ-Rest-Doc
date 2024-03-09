========================
ttygif
========================

终端录屏工具

github地址: `https://github.com/icholy/ttygif`

debian安装::

  apt install ttygif

mac安装::

  brew install ttygif

用法::

  ttygif [option] <in_file> [out.gif]

in_file:
  从哪个 `text/x-script` 文件读取输入
out.gif:
  输出文件名, 默认为 `tty.gif`

选项(不同系统的貌似有点不一样):

-f, --fullscreen : include window border
-s, --speed : Set speed [1.0]
-h, --help : print this help
-v, --version : print version

终端录制
========================

开始录制::

  ttyrec <file_name>

若不给 `file_name`, 则默认生成的文件是 `ttyrecord`, 也可以使用
:doc:`/docs/操作系统/linux/linux指令/script` 或者
:doc:`/docs/操作系统/linux/linux指令/asciinema`, 都支持生成 `text/x-script` 文件

退出录制(或者直接 `Ctrl + D`)::

  exit

将 `text/x-script` 文件转换为gif::

  ttygif <file_name>

附一个完整的流程
========================

code::

  ttyrec out.cast

  echo this is a test

  exit
  # 这个时候就退出录制了 会在当前目录下生成out.cast

  # 转换为gif文件, 默认会在当前目录下生成tty.gif, 貌似不支持直接指定文件名
  ttygif out.cast

.. note::

  如果不是很需要, 建议使用小一点的终端, 不然全屏录制会比较占空间

