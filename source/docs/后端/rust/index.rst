==============================
Rust
==============================


.. post:: 2023-02-20 22:06:49
  :tags: rust
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


安装参考: `https://rustup.rs/`

国内源配置
==============================

Mac
------------------------------

更新配置文件::

  vim ~/.bash_profile

新增如下内容(使用中科大代理)::

  export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
  export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup

  # 使用 rsproxy 代理
  # export RUSTUP_DIST_SERVER="https://rsproxy.cn"
  # export RUSTUP_UPDATE_ROOT="https://rsproxy.cn/rustup"

让修改生效::

  source ~/.bash_profile

Windows10
------------------------------

设置如下环境变量::

  RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
  RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup

升级
==============================

code::

  rustup check
  rustup update

配置 Cargo 使用国内镜像
==============================

更新文件 `~/.cargo/config`（windows 10 下为 `C:\Users\<用户名>\.cargo\config` ），
没有就新建::

  [source.crates-io]
  registry = "https://github.com/rust-lang/crates.io-index"

  # 替换成要使用的镜像
  replace-with = 'rsproxy'

  # 中国科学技术大学
  [source.ustc]
  registry = "git://mirrors.ustc.edu.cn/crates.io-index"
  # 如果所处的环境中不允许使用 git 协议，可以把上述地址改为 https 协议
  #registry = "https://mirrors.ustc.edu.cn/crates.io-index"

  # 清华大学
  [source.tuna]
  registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"

  # 上海交通大学
  [source.sjtu]
  registry = "https://mirrors.sjtug.sjtu.edu.cn/git/crates.io-index"

  # rustcc 社区
  [source.rustcc]
  registry = "git://crates.rustcc.cn/crates.io-index"

  # rsproxy
  [source.rsproxy]
  registry = "https://rsproxy.cn/crates.io-index"
  [source.rsproxy-sparse]
  registry = "sparse+https://rsproxy.cn/index/"
  [registries.rsproxy]
  index = "https://rsproxy.cn/crates.io-index"

  [net]
  git-fetch-with-cli=true

若 使用 `cargo build` 命令仍然报错如下错误::

  blocking waiting for file lock on package(包) cache lock

可删除文件 `~/.cargo/.package-cache` 然后重试。
