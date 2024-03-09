==================================
update-alternatives
==================================

貌似只有GUI界面才有用 (DEBIAN系列专有)

用软链接的方式处理系统中软件版本的切换，使其多版本共存.
alternatives 的管理目录 `/etc/alternatives`

管理方式
==================================

主要是三层路径

第一层路径, 软链接, 一般是系统的默认PATH下, 主要是:
`/usr/bin` 下面或者 `/usr/local/bin` 下.
链接的目标为第二层路径.

第二层路径, 软链接, 为alternatives的管理目录 `/etc/alternatives`
链接目标为第三层.

第三层路径, 执行文件的真实路径, 可以为任意路径,
比如自己安装的Python
`/usr/local/mypython/bin/python`

用法
==================================

用法::

  update-alternatives [<选项> ...] <命令>

命令::

  --install <链接> <名称> <路径> <优先级> [--slave <链接> <名称> <路径>] ...
                            在系统中加入一组候选项。
  --remove <名称> <路径>   从 <名称> 替换组中去除 <路径> 项。
  --remove-all <名称>      从替换系统中删除 <名称> 替换组。
  --auto <名称>            将 <名称> 的主链接切换到自动模式。
  --display <名称>         显示关于 <名称> 替换组的信息。
  --query <名称>           机器可读版的 --display <名称>.
  --list <名称>            列出 <名称> 替换组中所有的可用候选项。
  --get-selections         列出主要候选项名称以及它们的状态。
  --set-selections         从标准输入中读入候选项的状态。
  --config <名称>          列出 <名称> 替换组中的可选项，并就使用其中哪一个，征询用户的意见。
  --set <名称> <路径>      将 <路径> 设置为 <名称> 的候选项。
  --all                    对所有可选项一一调用 --config 命令。

  <链接> 是指向 /etc/alternatives/<名称> 的符号链接。(如 /usr/bin/pager)
  <名称> 是该链接替换组的主控名。(就是/etc/alternatives/<名称>的<名称>, 如 pager)
  <路径> 是候选项目标文件的位置。(真实路径, 如 /usr/bin/less)
  <优先级> 是一个整数，在自动模式下，这个数字越高的选项，其优先级也就越高。
  ..........

install的说明, 举例,
将 `/path/to/javac` 设置为优先级为 100 的 `javac` 可替代项，
并将 `/usr/bin/java` 关联到主项 `/path/to/java` ::

  sudo update-alternatives --install /usr/bin/javac javac /path/to/javac 100 --slave /usr/bin/java java /path/to/java

以便于将从属项与主项关联起来，并在切换主项时自动更新从属项的链接

实际应用
==================================

当安装了多个编辑器或者多个不同版本的软件如JAVA时,
可以用来处理执行时使用哪个JAVA.

安装时候, 添加到管理::

  update-alternatives --install /usr/local/bin/java java /usr/local/myjava/bin/java 10

这个时候使用会自动按照优先级的顺序来选择,
可以看看java已经注册了哪些::

  update-alternatives --display java

如果需要手动选择, 可使用config打开一个交互式界面让用户手动选择::

  update-alternatives --config java

重新修改为自动::

  update-alternatives --auto java

如果需要直接设置::

  update-alternatives --set java /usr/local/myjava/bin/java
