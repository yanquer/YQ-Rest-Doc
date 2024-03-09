=========================
Mac
=========================

.. toctree::

  Mac指令
  Mac环境变量
  打印运行时加载的动态库
  图标制作
  Mac-Vmware磁盘修复
  问题/index

brew
=========================

包管理器brew (HomeBrew)

查看配置::

  brew config

输出::

  $ brew config
  HOMEBREW_VERSION: 4.1.24
  ORIGIN: https://github.com/Homebrew/brew
  ...

更换镜像(忽略)::

  # 替换 brew.git
  cd "$(brew --repo)"
  git remote set-url origin https://mirrors.ustc.edu.cn/brew.git

  # 替换 homebrew-core.git
  # cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
  # git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
  # 新版没有这目录

参考: `https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/`
  设置环境变量::

    export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"
    export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
    export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
    export HOMEBREW_PIP_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"

  针对 macOS 系统上的 Homebrew::

    # 手动设置
    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"

    # 注：自 brew 4.0 起，大部分 Homebrew 用户无需设置 homebrew/core 和 homebrew/cask 镜像，只需设置 HOMEBREW_API_DOMAIN 即可。
    # 如果需要使用 Homebrew 的开发命令 (如 `brew cat <formula>`)，则仍然需要设置 homebrew/core 和 homebrew/cask 镜像。
    # 请按需执行如下两行命令：
    brew tap --custom-remote --force-auto-update homebrew/core https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
    brew tap --custom-remote --force-auto-update homebrew/cask https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git

    # 除 homebrew/core 和 homebrew/cask 仓库外的 tap 仓库仍然需要设置镜像
    brew tap --custom-remote --force-auto-update homebrew/cask-fonts https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-fonts.git
    brew tap --custom-remote --force-auto-update homebrew/cask-versions https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-versions.git
    brew tap --custom-remote --force-auto-update homebrew/command-not-found https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-command-not-found.git
    brew tap --custom-remote --force-auto-update homebrew/services https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-services.git
    brew update

    # 或使用下面的几行命令自动设置
    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
    for tap in core cask{,-fonts,-versions} command-not-found services; do
        brew tap --custom-remote --force-auto-update "homebrew/${tap}" "https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-${tap}.git"
    done
    brew update

  也可直接使用上面的链接安装.

