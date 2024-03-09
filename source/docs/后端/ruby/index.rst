===============================
Ruby
===============================

安装配置

安装::

  brew install ruby

配置::

  ###
  # ruby
  ###

  # export PATH="/usr/local/opt/ruby/bin:$PATH"

  # compilers to find ruby
  export LDFLAGS="-L/usr/local/opt/ruby/lib"
  export CPPFLAGS="-I/usr/local/opt/ruby/include"

  # pkg-config to find ruby
  export PKG_CONFIG_PATH="/usr/local/opt/ruby/lib/pkgconfig"

写到 `~/.zshrc`

配置源::

  # 查看当前源
  gem source -l

  # 移除
  gem source --remove https://rubygems.org/

  # 添加国内镜像
  gem source -a https://gems.ruby-china.com/




