==============================
dd
==============================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


复制文件并对原文件的内容进行转换和格式化处理::

  bs=<字节数>：将ibs（输入）与obs（输出）设成指定的字节数；
  cbs=<字节数>：转换时，每次只转换指定的字节数；
  conv=<关键字>：指定文件转换的方式；
  count=<区块数>：仅读取指定的区块数；
  ibs=<字节数>：每次读取的字节数；
  obs=<字节数>：每次输出的字节数；
  if=<文件>；代表输入文件
  of=<文件>：输出到文件；
  seek=<区块数>：一开始输出时，跳过指定的区块数；
  skip=<区块数>：一开始读取时，跳过指定的区块数；
  --help：帮助；
  --version：显示版本信息。


例如生成10g的大文件::

  dd if=/dev/zero of=test bs=1M count=0 seek=10000    #不占空间
  dd if=/dev/zero of=test bs=10G count=1

读取位于地址 0x1000 的 4 字节数据::

  # /dev/mem 代表物理内存
  dd if=/dev/mem bs=4 count=1 skip=$((0x1000)) status=none | od -t x4 -An

拓展-Win下读取指定内存地址数据
  使用 **WinDbg 调试器**

  WinDbg 是 Windows 平台上使用的强大调试器工具。
  使用 WinDbg，您可以打开一个进程的内存空间并读取指定地址的数据。

  示例命令，在 WinDbg 中读取地址 0x1000 的 4 字节数据::

    > .open <进程名或进程ID>
    > db 0x1000 L4





