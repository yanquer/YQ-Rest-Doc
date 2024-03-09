=========================================
配置文件
=========================================

有些东西时间一长就忘了, 想半天也不一定能想起来,
故还是记录一下吧.

- /etc/hosts 查看本地域名与地址映射, 内容为 地址与域名的映射, 参见: :doc:`etc-hosts`
- /etc/resolv.conf 配置本机使用dns服务器, 以nameserver开头, 可多行. 参见: :doc:`etc-resolv-conf`
- /etc/hostname 设置当前主机名, 可通过 hostnamectl 修改, 重启生效

.. toctree::

  etc-hosts
  etc-resolv-conf

bash的配置文件
=========================================

持久保存用户配置

profile类
  为交互式登陆用户提供配置

  功能：设定环境变量，运行命令或脚本::

    /etc/profile    #全局
    /etc/profile.d/*.sh   #全局
    ~/.bash_profile    #个人配置，当前用户有效

bashrc类
  非交互式登陆用户提供配置

  功能：设定本地变量，定义命令别名::

    /etc/bashrc     #全局
    ~/.bashrc     #个人


