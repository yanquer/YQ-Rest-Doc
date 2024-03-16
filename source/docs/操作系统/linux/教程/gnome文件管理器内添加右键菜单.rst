================================
GNOME文件管理器内添加右键菜单
================================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 教程
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


目前已测试适用与 ``Ubuntu20``

.. sidebar:: nautilus

  `nautilus` 是 `GNOME` 自带的文件管理器, 可以理解为Win的文件管理器

使用系统自带的 `.local/share/nautilus/scripts` 只能在右键单击文件时候弹出所添加的脚本

目前经过多方搜索, 暂时只确定了使用额外的包 `nautilus-actions` 辅助解决,
新版本是 `filemanager-actions`. 其实核心都是一样的, 就是 `nautilus` 在
新版更名为 `filemanager`.

旧版本安装::

  apt install nautilus-actions

新版本安装::

  apt install filemanager-actions

安装后带开图形界面进行右键菜单的编辑,

选择新建菜单/新建动作即可, 注意默认是有一个 `filemanager` 的根菜单,
如果不想要, 在 `编辑-首选项-运行时首选项-Nautils菜单布局` 下取消勾选即可.

新版 `filemanager` 的配置文件在 `~/.config/filemanager-actions` 下面,
而自定义的配置的文件位置在 `~/.local/share/nautilus/file-manager/actions` 下.

`~/.local/share/nautilus/file-manager/actions` 下还是 `.desktop` 文件,
例::

  [Desktop Entry]
  Type=Action
  Name=菜单项名称
  Icon=/path/to/your/icon.png
  Exec=/path/to/your/command "%F"
  Name[en_US]=菜单项名称

  [Desktop Action 菜单项名称]
  Name=子菜单项名称
  Exec=/path/to/your/command "%F"
  Icon=/path/to/your/icon.png






