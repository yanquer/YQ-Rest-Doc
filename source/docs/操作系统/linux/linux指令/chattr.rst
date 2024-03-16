===================
chattr
===================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


Linux chattr命令用于改变文件属性。

这项指令可改变存放在ext2文件系统上的文件或目录属性，这些属性共有以下8种模式：

- a：让文件或目录仅供附加用途。
- b：不更新文件或目录的最后存取时间。
- c：将文件或目录压缩后存放。
- d：将文件或目录排除在倾倒操作之外。
- i：不得任意更动文件或目录, 预防被删除, 也不能更改文件权限。
- s：保密性删除文件或目录。
- S：即时更新文件或目录。
- u：预防被修改。
- e: 允许设置拓展属性
  (通过 :doc:`/docs/操作系统/linux/linux指令/setfattr`
  和 :doc:`/docs/操作系统/linux/linux指令/getfattr` )

语法::

  chattr [-RV][-v<版本编号>][+/-/=<属性>][文件或目录...]

选项:

-R
  递归处理，将指定目录下的所有文件及子目录一并处理。
-v<版本编号>
  设置文件或目录版本。
-V
  显示指令执行过程。

+<属性>
  开启文件或目录的该项属性。
-<属性>
  关闭文件或目录的该项属性。
=<属性>
  指定文件或目录的该项属性。

实例
===================

用chattr命令防止系统中某个关键文件被修改::

  chattr +i /etc/resolv.conf
  lsattr /etc/resolv.conf

会显示如下属性::

  ----i-------- /etc/resolv.conf

让某个文件只能往里面追加数据，但不能删除，适用于各种日志文件::

  chattr +a /var/log/messages

这就给 file 文件添加了一个自定义的 user.email 扩展属性::

  chattr +e file
  setfattr -n user.email -v "test@example.com" file
  getfattr -n user.email file




