=========================
dpkg-deb
=========================

dpkg-deb 提供了完整的 deb 包创建和操作功能,
提供打包、解包、查询 deb 信息等功能
是 deb 包管理不可或缺的工具

常见用法和选项包括:

解包 deb::

  dpkg-deb -x package.deb unpack/ :解压 deb 到指定目录
  dpkg-deb -R package.deb unpack/ :递归解压 deb 及数据到指定目录

打包 deb::

  dpkg-deb -b directory package.deb :将目录打包生成 deb 文件
  dpkg-deb -Z gzip -b dir package.deb :打包时使用 gzip 压缩

查看信息::

  dpkg-deb -I package.deb :显示 deb 的详细信息
  dpkg-deb -c package.deb :列出 deb 中的文件列表
  dpkg-deb -f package.deb :显示打包文件名

验证::

  dpkg-deb -W package.deb:验证 deb 文件的完整性

控制字段::

  --field=Field:Name :设置指定控制字段为 Name
  --field=Field: :删除指定控制字段

解压使用-x与-R区别
=========================

使用 -x解压的vscode包没有 DEBIAN目录, 使用 -R解压的有

解包行为略有不同:

- -x 选项进行解包时,只会解压 deb 包中的 `data.tar.*` 文件,也就是软件的实际文件。
- 而 -R 选项解包时,不仅会解压 `data.tar.` ,还会额外解压 `control.tar.` 文件。

`control.tar.*` 中包含了 deb 包的控制信息,其中就包括 `/DEBIAN` 目录和 `control` 等文件。

这主要是因为在多数情况下,我们解包只是为了获取软件文件本身,而不需要控制信息。
所以 -x 提供了更简单的解包方式。
但在需要完整解压调试 deb 包内部结构时,-R 解包则可以提供完整的内容。





