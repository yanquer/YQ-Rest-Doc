=============================
config
=============================

格式::

  git config [–local|–global|–system] -l

查看仓库级的config::

    git config –local -l

查看全局级的config::

  git config –global -l

查看系统级的config::

  git config –system -l

编辑全局级的config( –edit, -e)::

  git config –global -e

配置全局代理(如下是clash工具的默认端口)::

  git config --global http.proxy 'http://127.0.0.1:7890'

仅配置某一个地址的代理, 如github::

  git config --global http.https://github.com.proxy http://127.0.0.1:7890

.. note::

  Git 的 http 代理配置项只有 ``http.proxy``，并不支持 ``https.proxy``，这种写法是不存在/无用的。
  参考 `https://git-scm.com/search/results?search=http.proxy`

socket形式::

  git config --global http.proxy socks5://127.0.0.1:7890
  git config --global http.https://github.com.proxy socks5://127.0.0.1:7890

.. note::

  没有https选项, 如果要设置, http后面的地址跟https地址即可
