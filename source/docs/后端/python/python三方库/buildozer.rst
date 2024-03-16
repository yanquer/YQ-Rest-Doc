============================
buildozer
============================


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


暂时找到的官网文档: https://buildozer.readthedocs.io/en/latest/installation.html

一个用于构建Python应用程序的命令行工具, 可以将python代码打包为安卓的APK或者IPhone的IPA.

.. note::

  这玩意儿一开始只是为了kivy这个开源跨平台GUI框架开发的, 后面升级了支持基本上所有的Python了,
  就是需要手动配置.

安装::

  pip install buildozer

主要特点
============================

跨平台支持：
  Buildozer可以在多个操作系统上使用，包括Windows、Linux和macOS等。
简单易用：
  用户只需要编辑buildozer.spec文件，即可轻松配置应用程序的构建选项和依赖项。
自动化依赖管理：
  Buildozer会自动下载和安装所需的依赖项和库，而无需手动干预。
支持Python 2和3：
  Buildozer可以进行Python版本选择，并在构建过程中自动处理不同版本的差异。
多种构建选项：
  Buildozer支持多种构建选项，例如debug和release版本、ARM和x86架构等。
高度可定制：
  Buildozer提供了大量的命令行选项和配置选项，以满足不同场景下的定制需求。

使用流程
============================

配置文件设置
----------------------------

**buildozer.spec**

创建一个新的buildozer.spec文件。
该文件包含应用程序的配置和相关信息，例如应用程序名称、作者、版本号和依赖项等。
可以使用命令::

  buildozer init

来创建一个默认的buildozer.spec文件. 编辑buildozer.spec文件以包含所需的构建配置。
可以在此文件中指定需要的权限、启动屏幕、应用程序图标等。

.. sidebar::

  应用的版本, 可以自动探测, 直接在文件入口的py文件加入::

     __version__ = "1.0.3"

  即可

**配置项说明**

- title：应用程序的名称。
- package.name：应用程序的包名。
- package.domain：应用程序的域名。
- source.dir：应用程序的源代码目录。
- requirements：应用程序所需的Python库和第三方库。
- android.permissions：应用程序需要的Android权限。
- android.api：应用程序需要的Android API级别。
- android.sdk：Android SDK的路径。
- ios.codesign.identity：iOS代码签名的身份。

APK构建(安卓使用)
----------------------------

.. sidebar:: 安卓编译需要的前置包

  debian/ubuntu20/22 ::

    sudo apt update
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    pip3 install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv

    # add the following line at the end of your ~/.bashrc file
    export PATH=$PATH:~/.local/bin/

  windows10/11, 需要打开 WSL的支持, 然后同样执行上述指令.

  MacOs::

    python3 -m pip install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv
    brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer autoconf automake

通过使用::

  buildozer android debug

命令来构建debug版本的APK文件，

或者使用::

  buildozer android release

命令来构建发布版本的APK文件。

这将会自动下载并构建所有必要的依赖项，生成二进制文件，并将其打包到一个APK文件中。

IPA构建(苹果使用)
----------------------------

构建iOS应用程序（可选）。
如果需要构建iOS应用程序，则需要在Mac OS系统上进行，并设置Xcode环境和相关证书等。
可以使用 buildozer ios debug 或 buildozer ios release 命令来构建iOS应用程序。


