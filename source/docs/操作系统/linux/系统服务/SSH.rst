=========================================
SSH配置
=========================================

服务器远程访问和工具 (SSH, Secure Shell)

`Secure SHell <https://zh.wikipedia.org/wiki/Secure_Shell>`_ (SSH)
是因特网上的 **安全** 连接方式。
在 Debian 里面，有一个叫
`OpenSSH <http://www.openssh.org/>`_
的免费 SSH 版本，在 `openssh-client` 和 `openssh-server` 包里。

对于用户来讲, `ssh` 功能比 `telnet` 更加智能和安全.
不像 `telnet` 命令,  `ssh` 命令不会在遇到 `telnet` 的退出字符(初始默认是 CTRL-])时停止.

SSH 基础
=========================================

OpenSSH SSH 后台守护进程（daemon）只支持 SSH 2协议。

.. warning::

  如果想要运行 OpenSSH 服务， `/etc/ssh/sshd_not_to_be_run` 必须不存在。

  不要打开基于 rhost 的认证( `/etc/ssh/sshd_config` 中的 `HostbasedAuthentication` )。

处理其它 SSH 客户端
=========================================

其它平台上有一些免费的
`SSH <https://zh.wikipedia.org/wiki/Secure_Shell>`_ 客户端。

其它平台上免费 SSH 客户端列表::

  环境                  免费 SSH 程序
  Windows               puTTY (http://www.chiark.greenend.org.uk/~sgtatham/putty/) (GPL)
  Windows (cygwin)      cygwin 里的 SSH (http://www.cygwin.com/) (GPL)
  Macintosh 类          macSSH (http://www.macssh.com/) (GPL)
  Mac OS X              OpenSSH;在终端应用中使用 ssh (GPL)

建立 ssh 代理
=========================================

用密码来保护你的 SSH 认证私钥是安全的。
如果密码没有设置，使用 `ssh-keygen -p` 来设置。
把你的公钥 (比如： `~/.ssh/id_rsa.pub` ) 放到远程主机的
`~/.ssh/authorized_keys` ，这个远程主机使用上面描述的基于密码的连接方式::

  $ ssh-agent bash
  $ ssh-add ~/.ssh/id_rsa Enter passphrase for /home/*username*/.ssh/id_rsa: Identity added: /home/*username*/.ssh/id_rsa (/home/*username*/.ssh/id_rsa)

.. 可参考 :doc:`ssh-agent`

从这里执行接下来的命令，就不再需要密码::

  $ scp foo username@remote.host:foo

按 ^D 来终结 ssh 代理会话。

对于 X 服务端， 通常的 Debian 启动脚本会作为父进程执行 `ssh-agent` 。
所以你只需要执行一次 `ssh-add` 。进一步的信息，请阅读 `ssh-agent` 和 `ssh-add` .

怎样通过 SSH 关闭远程系统
=========================================

你可以使用 `at` 命令
(参见 `第 9.4.13 节 “单次任务时间安排” <https://www.debian.org/doc/manuals/debian-reference/ch09.zh-cn.html###_scheduling_tasks_once>`_ )
来从 SSH 终端里保护 `shutdown -h now`
(参见 `第 1.1.8 节 “怎样关闭系统” <https://www.debian.org/doc/manuals/debian-reference/ch01.zh-cn.html###_how_to_shutdown_the_system>`_
操作过程::

  ### echo "shutdown -h now" | at now

SSH 故障排查
=========================================

如果你遇到问题，检查配置文件的权限并用 `-v` 选项运行 `ssh`

如果你是 root 账户，并有使用防火墙，使用 `-p` 选项;
这可以避免使用1 — 1023 之间的服务端口.

如果 `ssh` 连接到远程站点突然停止工作，这也许是系统管理员胡乱操作的结果，
可能是在系统维护时改变了  `host_key` .
在确认这个情况后，并且没有人试图用聪明的黑客技术来篡改远程主机，
你可以在本机 `~/.ssh/known_hosts` 里删除 `host_key` 条目来重新获得连接

设置会话过期
=========================================

设置会话过期::

  # /etc/ssh/sshd_config

  ServerAliveInterval 60        # 单次发送包检查链接时间，单位是秒，为0表示不发
  ServerAliveCountMax 30        # 最大检查次数，超过后断开链接

ClientAliveInterval
  这个其实就是SSH Server与Client的心跳超时时间，
  也就是说，当客户端没有指令过来，
  Server间隔`ClientAliveInterval`的时间（单位秒）会发一个空包到Client来维持心跳，
  60表示每分钟发送一次，然后客户端响应，这样就保持长连接了保证Session有效, 默认是0, 不发送;
ClientAliveCountMax
  当心跳包发送失败时重试的次数，比如现在我们设置成了30，
  如果Server向Client连续发30次心跳包都失败了，就会断开这个session连接。

另一个地方::

  # /etc/profile
  TMOUT=60    # 空闲等待时间，默认值0，表示不超时

ssh的时候定义别名
=========================================

方法 1 – 使用 SSH 配置文件
-----------------------------------------

这是我创建别名的首选方法。

我们可以使用 SSH 默认配置文件来创建 SSH 别名。为此，
编辑 `~/.ssh/config` 文件（如果此文件不存在，只需创建一个）::

  $ vi ~/.ssh/config

添加所有远程主机的详细信息，如下所示::

  Host webserver
      HostName 192.168.225.22
      User sk

  Host dns
      HostName server.example.com
      User root

  Host dhcp
      HostName 192.168.225.25
      User ostechnix
      Port 2233

方法 2 – 使用 Bash 别名
-----------------------------------------

这是创建 SSH 别名的一种应急变通的方法，可以加快通信的速度。
你可以使用 :doc:`/docs/操作系统/linux/linux指令/alias` 使这项任务更容易。

打开 `~/.bashrc` 或者 `~/.bash_profile` 文件::

  alias webserver='ssh sk@server.example.com'
  alias dns='ssh sk@server.example.com'
  alias dhcp='ssh sk@server.example.com -p 2233'
  alias ubuntu='ssh sk@server.example.com -i ~/.ssh/id_rsa_remotesystem'

再次确保你已使用自己的值替换主机、主机名、端口号和 IP 地址。保存文件并退出。

然后，使用命令应用更改::

  $ source ~/.bashrc

或者::

  $ source ~/.bash_profile

在此方法中，你甚至不需要使用 `ssh 别名` 命令。相反，只需使用别名，如下所示。

  $ webserver
  $ dns
  $ dhcp
  $ ubuntu

**（方法2太慢了 alias debian9=“user@host” 然后 ssh debian9 太慢了 ）**




