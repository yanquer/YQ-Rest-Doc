============================
mac的包管理器brew
============================


.. post:: 2024-03-09 18:21:01
  :tags: 
  :category: 常用工具使用
  :author: YanQue
  :location: CD
  :language: zh-cn


自从升级到macos13之后, 使用brew下载就非常的慢, 稍微看了一下输出,
大概是国内源没有13版本的包, 所以最后还是去外面下载...
于是, 就找了一下有没有处理办法.

mac下包管理器最常用的有brew与macport, 网上说后者的包要多很多.

这里只谈brew, 官网: https://brew.sh/index_zh-cn

安装brew
============================

国内源下载::

  /bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"

把脚本搞下来了, :download:`/resources/code/homebrew_zh.sh`

一开始用的2清华源, 结果慢的要死. 然后换成1中科大的源, 快多了

卸载brew
============================

卸载脚本::

  /bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/HomebrewUninstall.sh)"

同样拉下来了, :download:`/resources/code/homebrew_uninstall_zh.sh`

一些说明
============================

- brew Homebrew 源代码仓库
- homebrew-core Homebrew 核心软件仓库
- homebrew-bottles Homebrew 预编译二进制软件包
- homebrew-cask MacOS 客户端应用
- Homebrew国内镜像源目前主要有中科大镜像、阿里镜像、清华镜像。

指令说明
============================

查看brew.git源::

  cd "$(brew --repo)" && git remote -v

查看 homebrew-core.git 当前源::

  cd "$(brew --repo homebrew/core)" && git remote -v


常见报错
============================

Command failed with exit 128: git
--------------------------------------

详细报错::

  fatal: not in a git directory
  Error: Command failed with exit 128: git

因为brew软件仓库实际是使用git来进行管理的, 所以会去本地的仓库目录
去找, 但是它又不是一个git仓库.

解决办法: 找到本地的安装仓库目录, 然后使用::

  git config --global --add safe.directory 目录

即可.

如果不知道自己安装在哪了, 可以使用find查找::

  yanque@yanquedembp ~ % find / -name "homebrew"  2>/dev/null
  /usr/local/Homebrew/Library/Taps/homebrew

然后看看有哪些::

  yanque@yanquedembp ~ % ls /usr/local/Homebrew/Library/Taps/homebrew
  homebrew-cask		homebrew-core		homebrew-services

然后加进去::

  yanque@yanquedembp ~ % git config --global --add safe.directory /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask
  yanque@yanquedembp ~ % git config --global --add safe.directory /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core
  yanque@yanquedembp ~ % git config --global --add safe.directory /usr/local/Homebrew/Library/Taps/homebrew/homebrew-services

试过不支持通配符.

