============================
zenity
============================

Zenity是一个使用GTK+库开发的工具，用于创建图形用户界面（GUI）对话框(信息框)

.. sidebar::

  一般 `GNOME` 桌面系统会预装.

  `GNOME` 是一个基于 `GTK+` 的桌面环境.
  由于 `zenity` 与 `GNOME` 密切相关，因此大多数基于GNOME的Linux发行版，
  包括Ubuntu、Fedora和Debian等，都会默认安装Zenity。

安装::

  apt install zenity

常用选项:

--info
  信息框
--width <num>
  弹出框宽度
--title <str>
  标题
--text
  主区域文本
--window-icon <icon_file>
  设置窗体图标

如弹出宽500的信息框::

  zenity --info --title "标题" --text "文本" --width=500



