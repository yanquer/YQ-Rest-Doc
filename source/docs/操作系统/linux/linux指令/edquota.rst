==============================
edquota
==============================

修改用户（群组）的磁盘配额

edit quota 缩写，用于修改用户和群组的配额限制参数，
包括磁盘容量和文件个数限制、软限制和硬限制值、宽限时间，
该命令的基本格式有以下 3 种::

  [root@localhost ~]# edquota [-u 用户名] [-g 群组名]
  [root@localhost ~]# edquota -t
  [root@localhost ~]# edquota -p 源用户名 -u 新用户名

此命令各常用选项及功能如下：

-u 用户名
  进入配额的 Vi 编辑界面，修改针对用户的配置值；
-g 群组名
  进入配额的 Vi 编辑界面，修改针对群组的配置值；

-t
  修改配额参数中的宽限时间；
-p
  将源用户（或群组）的磁盘配额设置，复制给其他用户（或群组）

例如，以用户 myquota 为例，通过如下命令配置此命令的 Quota::

  [root@localhost ~]# edquota -u myquota
  Disk quotas for user myquota (uid 710):
  Filesystem  blocks soft  hard inodes soft hard
  /dev/hda3     80   0   0   10   0   0

此命令的输出信息共 3 行，
第一行指明了针对哪个用户进行配额限制，
第二行是各个配额值的表头，
共分为 7 列，其每一列的含义

文件系统（filesystem）
  说明该限制值是针对哪个文件系统（或分区）；
磁盘容量（blocks）
  此列的数值是 quota 自己算出来的，单位为 Kbytes，不要手动修改；
磁盘容量的软限制（soft）
  当用户使用的磁盘空间超过此限制值，则用户在登陆时会收到警告信息，告知用户磁盘已满，单位为 KB；
磁盘容量的硬限制（hard）
  要求用户使用的磁盘空间最大不能超过此限制值，单位为 KB；
文件数量（inodes）
  同 blocks 一样，此项也是 quota自己计算出来的，无需手动修改；
文件数量的软限制（soft）
  当用户拥有的文件数量超过此值，系统会发出警告信息；
文件数量的硬限制（hard）
  用户拥有的文件数量不能超过此值。

注意，当 soft/hard 为 0 时，表示没有限制。
另外，在 Vi（或 Vim）中修改配额值时，填写的数据无法保证同表头对齐，
只要保证此行数据分为 7 个栏目即可。

【例 1】 修改用户 myquota 的软限制值和硬限制值::

  [root@localhost ~]# edquota -u myquota
  Disk quotas for user myquota (uid 710):
  Filesystem  blocks  soft  hard inodes soft hard
  /dev/hda3     80 250000 300000   10   0   0

【例 2】 修改群组 mygrpquota 的配额::

  [root@localhost ~]# edquota -g mygrpquota
  Disk quotas for group mygrpquota (gid 713):
  Filesystem  blocks  soft   hard inodes soft hard
  /dev/hda3    400 900000 1000000   50   0   0

【例 3】修改宽限天数::

  [root@localhost ~]# edquota -t
  Grace period before enforcing soft limits for users:
  Time units may be: days, hours, minutes, or seconds
  Filesystem     Block grace period   Inode grace period
  /dev/hda3        14days         7days



