============================
本地构建deb包
============================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 教程
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


debian官方文档: https://www.debian.org/releases/stable/amd64/index.zh-cn.html

control文件说明: https://www.debian.org/doc/debian-policy/ch-controlfields.html

文件结构
============================

.. sidebar::

  `DEBIAN` 下的这些文件, 安装后一般都可以在 `/var/lib/info` 下找到,
  如 `/var/lib/info/xxx.prerm*`

大概包目录结构如下::

  |----DEBIAN
        |-------control
        |-------postinst(postinstallation)
        |-------postrm(postremove)
        |-------preinst(preinstallation)
        |-------prerm(preremove)
        |-------copyright(版权)
        |-------changlog(修订记录)
        |-------conffiles
  |----etc
  |----usr
  |----opt
  |----tmp
  |----boot
        |-----initrd-vstools.img

.. sidebar::

  DEBIAN 下的文件大多都需要可执行权限

control文件
============================

官方字段说明见: `https://www.debian.org/doc/debian-policy/ch-controlfields.html`

deb包必须具备的描述性文件，以便于软件的安装管理和索引

内容字段说明

- Package 程序名称 中间不能有空格
- Version 版本
- Section 软件类别 utils, net, mail, text, x11
- Priority 软件对于系统的重要程度 required, standard, optional, extra等
- Essential 是否是系统最基本的软件包 yes/no，若为yes,则不允许卸载（除非强制性卸载）
- Architecture 软件所支持的平台架构 all, i386, amd64, m68k, sparc, alpha, powerpc等,
  支持的架构可参考: https://www.debian.org/releases/stable/amd64/ch02s01.zh-cn.html
- Source 软件包的源代码名称
- Depends 软件所依赖的其他软件包和库文件 若依赖多个软件包和库文件，采用逗号隔开
- Pre-Depends 软件安装前必须安装、配置依赖性的软件包和库文件 常用于必须的预运行脚本需求
- Recommends 推荐安装的其他软件包和库文件
- Suggests 建议安装的其他软件包和库文件
- Maintainer 维护者
- Description 程序说明
- Homepage 主页
- Installed-Size: 安装大概消耗的空间(预估值, 实际可能有所不同), 只写数字即可, 单位字节
- Download-Size: 大小需要下载的包的大小, 只写数字大小即可, 单位字节
- MimeType: 关联的文件类型, 比如vscode设置了 `inode/directory` 就可以右键选择其他应用打开的时候有vscode

MimeType支持的部分类型:

- inode/directory：普通文件夹
- text/plain: 文本文件
- application/x-gnome-saved-search：GNOME 桌面环境中保存的搜索结果文件夹
- inode/mount-point：挂载点，表示一个已挂载的设备或文件系统
- inode/blockdevice：块设备文件夹
- inode/chardevice：字符设备文件夹
- inode/socket：套接字文件夹
- inode/fifo：命名管道文件夹
- application/Xcode-workspace: xcode项目, 主要是苹果下面的

postinst文件
============================

在Deb包文件解包之前（即软件安装前），将会运行该脚本。可以停止作用于待升级软件包的服务，直到软件包安装或升级完成。

preinst文件
============================

负责完成安装包时的配置工作。如新安装或升级的软件重启服务。软件安装完后，执行该Shell脚本，一般用来配置软件执行环境，必须以“#!/bin/sh”为首行。

prerm文件
============================

该脚本负责停止与软件包相关联的daemon服务。它在删除软件包关联文件之前执行

postrm文件
============================

负责修改软件包链接或文件关联，或删除由它创建的文件。软件卸载后，执行该Shell脚本，一般作为清理收尾工作，必须以“#!/bin/sh”为首行

copyright文件
============================

changlog文件
============================

conffiles文件
============================


用例
============================

大概目录结构::

  .dist/deb_ev-deb/
  |-- DEBIAN
  |   `-- control
  |   `-- postinit
  `-- usr
      |-- local
      |   `-- life
      |       `-- ev-deb-1.0.1
      |           `-- main.bin
      `-- share
          |-- applications
          |   `-- life
          |       `-- ev-deb.desktop
          `-- icons
              `-- life
                `-- ic.png

其中:

- `DEBIAN/control` 是包相关信息, 必有.
  配置内容大概::

    Package: ev-deb
    Version: 1.0.1
    Architecture: amd64
    Maintainer: yq
    Description: desc a every deb
- `DEBIAN/control` 这里用来做桌面图标设置相关脚本, 有GUI界面才需要设置
  内容::

    #!/bin/bash
    cp /usr/share/applications/life/ev-deb.desktop ~/Desktop

- 其他的比如 `usr` 是模仿linux系统结构来进行布局, 比如这里的是 `usr/local/life/ev-deb-1.0.1`,
  那么实际的安装位置就是 `/usr/local/life/ev-deb-1.0.1`.
- `usr/share/applications/life/ev-deb.desktop` , 主要是需要在 `/usr/share/applications` 创建一个
  `.desktop` 文件, 以便于在 GUI 界面的时候可以在桌面活着任务栏看到, 若是GUI应用必有. 配置内容大概::

    [Desktop Entry]
    Name=ev-deb
    Comment=desc a every deb
    Exec=.dist/deb_ev-deb/ev-deb-1.0.1/main.bin
    Icon=.dist/deb_ev-deb/usr/share/icons/life/ic.png
    Terminal=true
    Type=Application
    X-Ubuntu-Touch=true
    Categories=Development

  且必有可执行权限.

  Name 表示在桌面上显示的名称

- `usr/share/icons` , 图标位置, GUI界面必有, 用于 `.desktop` 文件.
  特别说明,

  - Exec字段指定的路径如果有空格, 可以用引号代替
  - Icon字段指定的图标路径不能有引号与空格, 否则 ``dpkg -b``
    打包的时候校验不通过(但是实际安装好后可以用空格, 不能用引号).

.. note::

  `usr/share/applications/` 下是系统的启动器默认的应用(桌面文件)存放位置,
  若放在其他位置如 `~/.local/share/applications/`, 可使用指令更新::

    update-desktop-database ~/.local/share/applications/

  这样就不需要手动 `右键 - 允许启动` 了

官方文档建议的打包工具
============================

- debmake: deb目录结构生成工具 (好像需要手动装)
- debbuild: 根据上一步构建好的结构, 生成包, 与 ``dpkg -b`` 类似, 不过 `dpkg` 更底层.
  `debbuild` 读取软件包的源代码目录中的 `debian/rules`` 文件来执行构建过程，
  并自动处理构建过程中的许多步骤，例如配置、编译和安装.
  `debuild` 还会检查构建依赖关系并确保它们已满足，以及生成符合 Debian 软件包规范的二进制和源代码软件包.

  ``dpkg -b`` 是一个更底层的工具，用于将已经构建好的二进制文件打包成一个 Debian 格式的软件包.
  它不会自动执行构建过程，而是需要手动提供已经构建好的文件和必要的控制信息（例如包名、版本号、依赖关系等）.
  ``dpkg -b`` 的优点是灵活性，允许用户手动控制软件包的构建流程和细节.

deb包配置右键单击支持使用其他应用打开
========================================================

只需配置 `desktop` 文件, 如上面的 `usr/share/applications/life/ev-deb.desktop`
还是用上面的例子::

  [Desktop Entry]
  Name=ev-deb
  Comment=desc a every deb
  Exec=.dist/deb_ev-deb/ev-deb-1.0.1/main.bin
  Icon=.dist/deb_ev-deb/usr/share/icons/life/ic.png
  Terminal=true
  Type=Application
  X-Ubuntu-Touch=true
  Categories=Development

有两个地方要改,  **一个是Exec改为需要增加参数** ::

  Exec=.dist/deb_ev-deb/ev-deb-1.0.1/main.bin %F

部分支持的参数:

- %F: 选中文件夹或文件的路径
- %U: 选中文件夹的路径

**另一个是增加 `MimeType`**, 与 control文件_ 的 `MimeType` 一致,
需要说明的是, 即使已经在 control文件_ 写了 `MimeType`,
还是得在 `desktop` 文件再写一次(多个用分号隔开), 两个地方的不共享.
表示哪些类型的文件可以右键选择用此应用打开.
比如::

  MimeType=text/plain;inode/directory;application/x-code-workspace;


