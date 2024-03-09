=========================
update-desktop-database
=========================

以GNOME桌面环境为例,

桌面环境的应用菜单并不是实时扫描所有的 .desktop 文件,而是维护一个桌面文件的数据库。
当 .desktop 文件发生变化时,需要运行 update-desktop-database 来刷新这个数据库

如扫描 /usr/share/applications 目录下的 .desktop 文件,并更新桌面环境的应用菜单数据库::

  update-desktop-database /usr/share/applications



