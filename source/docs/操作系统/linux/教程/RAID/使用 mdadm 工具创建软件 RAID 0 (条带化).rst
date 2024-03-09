========================================================
使用 mdadm 工具创建软件 RAID 0 (条带化)
========================================================

:参考::
  - 作者: `<Babin Lonston <http://www.tecmint.com/create-raid0-in-linux/>`_
  - 译者: `LCTT <https://linux.cn/lctt/>`_
  - 译者: `struggling <https://linux.cn/lctt/strugglingyouth>`_
  - <https://linux.cn/portal.php?mod=comment&id=6087&idtype=aid>`_

RAID 即廉价磁盘冗余阵列，其高可用性和可靠性适用于大规模环境中，相比正常使用，数据更需要被保护。
RAID 是一些磁盘的集合，是包含一个阵列的逻辑卷。驱动器可以组合起来成为一个阵列或称为（组的）集合。

创建 RAID 最少应使用2个连接到 RAID 控制器的磁盘组成，来构成逻辑卷，
可以根据定义的 RAID 级别将更多的驱动器添加到一个阵列中。
不使用物理硬件创建的 RAID 被称为软件 RAID。软件 RAID 也叫做穷人 RAID。

使用 RAID 的主要目的是为了在发生单点故障时保存数据，
如果我们使用单个磁盘来存储数据，如果它损坏了，
那么就没有机会取回我们的数据了，
为了防止数据丢失我们需要一个容错的方法。
所以，我们可以使用多个磁盘组成 RAID 阵列。

在 RAID 0 中条带是什么
========================================================

条带是通过将数据在同时分割到多个磁盘上。
假设我们有两个磁盘，如果我们将数据保存到该逻辑卷上，它会将数据保存在两个磁盘上。
使用 RAID 0 是为了获得更好的性能，但是如果驱动器中一个出现故障，我们将不能得到完整的数据。
因此，使用 RAID 0 不是一种好的做法。唯一的解决办法就是安装有 RAID 0 逻辑卷的操作系统来提高重要文件的安全性。

- RAID 0 性能较高。
- 在 RAID 0 上，空间零浪费。
- 零容错（如果硬盘中的任何一个发生故障，无法取回数据）。
- 写和读性能都很好。

要求
========================================================

创建 RAID 0 允许的最小磁盘数目是2个，但你可以添加更多的磁盘，
不过数目应该是2，4，6，8等的偶数。
如果你有一个物理 RAID 卡并且有足够的端口，你可以添加更多磁盘。

在这里，我们没有使用硬件 RAID，此设置只需要软件 RAID。
如果我们有一个物理硬件 RAID 卡，我们可以从它的功能界面访问它。
有些主板默认内建 RAID 功能，还可以使用 Ctrl + I 键访问它的界面。

关于 RAID 基本的概念: :doc:`RAID 的级别和概念`

我的服务器设置::

  - 操作系统  :  CentOS 6.5 FinalIP
  - 地址      :  192.168.0.225
  - 两块盘    :  20 GB each


这是9篇系列教程的第2部分，在这部分，我们将看看如何能够在 Linux 上创建和使用 RAID 0（条带化），以名为 sdb 和 sdc 两个 20GB 的硬盘为例。

第1步：更新系统和安装管理 RAID 的 mdadm 软件
========================================================

在 Linux 上设置 RAID 0 前，我们先更新一下系统，然后安装 `mdadm` 包。
mdadm 是一个小程序，这将使我们能够在Linux下配置和管理 RAID 设备::

  yum clean all && yum update### yum install mdadm -y

第2步：确认连接了两个 20GB 的硬盘
========================================================

在创建 RAID 0 前，请务必确认两个硬盘能被检测到，使用下面的命令确认::

  ls -l /dev | grep sd

一旦检测到新的硬盘驱动器，
同时检查是否连接的驱动器已经被现有的 RAID 使用，使用下面的 `mdadm` 命令来查看::

  mdadm --examine /dev/sd[b-c]

.. 从上面的输出我们可以看到，没有任何 RAID 使用 sdb 和 sdc 这两个驱动器。

第3步：创建 RAID 分区
========================================================

现在用 sdb 和 sdc 创建 RAID 的分区，使用 fdisk 命令来创建。
在这里，我将展示如何创建 sdb 驱动器上的分区::

  fdisk /dev/sdb

请按照以下说明创建分区。

- 按 `n` 创建新的分区。
- 然后按 `P` 选择主分区。
- 接下来选择分区号为1。
- 只需按两次回车键选择默认值即可。
- 然后，按 `P` 来显示创建好的分区。

请按照以下说明将分区创建为 Linux 的 RAID 类型。

- 按 `L`，列出所有可用的类型。
- 按 `t` 去修改分区。
- 键入 `fd` 设置为 Linux 的 RAID 类型，然后按回车确认。
- 然后再次使用 `p` 查看我们所做的更改。
- 使用 `w` 保存更改。

.. note::

  请使用上述步骤同样在 sdc 驱动器上创建分区。

创建分区后，验证这两个驱动器是否正确定义 RAID，使用下面的命令::

  mdadm --examine /dev/sd[b-c]### mdadm --examine /dev/sd[b-c]1

第4步：创建 RAID md 设备
========================================================

现在使用以下命令创建 md 设备（即 /dev/md0），并选择 RAID 合适的级别::

  mdadm -C /dev/md0 -l raid0 -n 2 /dev/sd[b-c]1### mdadm --create /dev/md0 --level=stripe --raid-devices=2 /dev/sd[b-c]1

- -C – 创建
- -l – 级别
- -n – RAID 设备数

一旦 md 设备已经建立，使用如下命令可以查看 RAID 级别，设备和阵列的使用状态::

  cat /proc/mdstat

查看 RAID 级别::

  mdadm -E /dev/sd[b-c]1

查看 RAID 设备::

  mdadm --detail /dev/md0

查看 RAID 阵列

第5步：给 RAID 设备创建文件系统
========================================================

将 RAID 设备 /dev/md0 创建为 ext4 文件系统，并挂载到 /mnt/raid0 下::

  mkfs.ext4 /dev/md0

在 RAID 设备上创建好 ext4 文件系统后，现在创建一个挂载点（即 /mnt/raid0），并将设备 /dev/md0 挂载在它下::

  mkdir /mnt/raid0### mount /dev/md0 /mnt/raid0/

下一步，使用 df 命令验证设备 /dev/md0 是否被挂载在 /mnt/raid0 下::

  df -h

接下来，在挂载点 /mnt/raid0 下创建一个名为 `tecmint.txt` 的文件，
为创建的文件添加一些内容，并查看文件和目录的内容::

  touch /mnt/raid0/tecmint.txt
  echo "Hi everyone how you doing ?" > /mnt/raid0/tecmint.txt
  cat /mnt/raid0/tecmint.txt
  ls -l /mnt/raid0/

当你验证挂载点后，就可以将它添加到 /etc/fstab 文件中(*添加设备到 fstab 文件中*)::

  vim /etc/fstab

添加以下条目，根据你的安装位置和使用文件系统的不同，自行做修改::

  /dev/md0                /mnt/raid0              ext4    deaults         0 0

使用 mount 命令的 `-a` 来检查 fstab 的条目是否有误::

  mount -av

第6步：保存 RAID 配置
========================================================

最后，保存 RAID 配置到一个文件中，以供将来使用。
我们再次使用带有 `-s` (scan) 和 `-v` (verbose) 选项的 `mdadm` ::

  mdadm -E -s -v >> /etc/mdadm.conf### mdadm --detail --scan --verbose >> /etc/mdadm.conf  ### cat /etc/mdadm.conf

就这样，我们在这里看到，如何通过使用两个硬盘配置具有条带化的 RAID 0 。在接下来的文章中，我们将看到如何设置 RAID 1。


最新评论::

  - 来自北京的 Chrome 43.0|Windows 7 用户 2015-12-02 12:46.4 赞
    `<https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=36536&hash=5522402f>`_
    `回复 <https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=36536&aid=6087&idtype=>`_
    这年头还搞软raid，让硬件生产商如何生活

  - `XYJK1002 [Chrome 42.0|Windows 7\] <https://linux.cn/space/20893/>`_ 2015-10-03 19:139 赞
    `<https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=35399&hash=5522402f>`_
    `回复 <https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=35399&aid=6087&idtype=>`_
    讨论的这么激烈。。。

  - `linux [Chrome 44.0|Mac 10.10\] <https://linux.cn/space/1/>`_ 2015-08-28 09:013 赞
    `<https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=34761&hash=5522402f>`_
    `回复 <https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=34761&aid=6087&idtype=>`_
    系统崩溃时，输出的数据没准都是错误的，硬件 RAID 卡也无法防范这点。只是避免了在 IO 系统将数据送到 RAID 卡后的错误。

  - 来自云南昆明的 Chrome 41.0|Windows 7 用户 2015-08-26 11:274 赞
    `<https://linux.cn/portal.php?mod=review&action=postreview&do=support&idtype=aid&tid=6087&pid=34719&hash=5522402f>`_
    `回复 <https://linux.cn/portal.php?mod=portalcp&ac=comment&op=reply&cid=34719&aid=6087&idtype=>`_
    以前建 RAID5 时，重启后 /dev/md0 名字就变了，也不知道怎么改回来，后面才知道是 /etc/mdadm.conf 的问题






