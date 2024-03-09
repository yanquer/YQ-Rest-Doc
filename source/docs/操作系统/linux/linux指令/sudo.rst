=======================
sudo
=======================

以系统管理者的身份执行指令

`sudo` 程序是为了使一个系统管理员可以给用户受限的 root 权限并记录 root 活动而设计的。
`sudo` 只需要一个普通用户的密码。
安装 `sudo` 软件包并通过设置 `/etc/sudoers` 中的选项来使用它

.. 参见 “ `/usr/share/doc/sudo/examples/sudoers` ” 和
.. `第 1.1.12 节 “sudo 配置” <https://www.debian.org/doc/manuals/debian-reference/ch01.zh-cn.html###_sudo_configuration>`_
.. 中的配置示例。

.. 我将 `sudo` 用于单用户系统
.. （参见 `第 1.1.12 节 “sudo 配置” <https://www.debian.org/doc/manuals/debian-reference/ch01.zh-cn.html###_sudo_configuration>`_ ）
.. 是为了防止自己可能做出的愚蠢行为。
.. 就我个人而言，我认为使用 `sudo` 会比使用 root 账号操作系统来得好。
.. 例如，下列命令将 “ `*some_file*` ” 的拥有者改变为 “ `*my_name*` ”::

..   sudo chown my_name some_file

.. 当然如果你知道 root 密码（比如自行安装 Debian 的用户所做的），
.. 任何用户账号都可以使用 “ `su -c` ” 让任何命令以 root 运行。

选项参数
=======================

-V 		显示版本编号
-h 		会显示版本编号及指令的使用方式说明
-l 		显示出自己（执行 sudo 的使用者）的权限
-L 		显示sudo设置
-v 		因为 sudo 在第一次执行时或是在 N 分钟内没有执行（N 预设为五）会问密码，这个参数是重新做一次确认，如果超过 N 分钟，也会问密码
-k 		将会强迫使用者在下一次执行 sudo 时问密码（不论有没有超过 N 分钟）
-b 		将要执行的指令放在背景执行
-p 		prompt 可以更改问密码的提示语，其中 %u 会代换为使用者的帐号名称， %h 会显示主机名称
-u 		username/#uid 不加此参数，代表要以 root 的身份执行指令，而加了此参数，可以以 username 的身份执行指令（#uid 为该 username 的使用者号码）
-s 		执行环境变数中的 SHELL 所指定的 shell ，或是 /etc/passwd 里所指定的 shell
-H 		将环境变数中的 HOME （家目录）指定为要变更身份的使用者家目录（如不加 -u 参数就是系统管理者 root ）
-i 		切换到root用户, 并加载root的环境变量(需要输入当前用户的密码)

直接加 command 既可以系统管理者身份（或以 -u 更改为其他人）执行该 command

.. tip::

	以root权限执行上一条命令::

		sudo !!

配置
=======================

可以在 `/etc/sudoers` 配置可使用sudo的用户::

	# /etc/sudoers
	ALL    ALL=(ALL:ALL) ALL

	# ALL        ALL=(ALL:ALL)         ALL
	# username    host=(user:group)    cmd 多个cmd规则以逗号分隔
	#             也可以仅写一个       设置免密，NOPASSWD:cmd
	#                                设置禁止, !cmd


	# The first ALL is the users allowed,    + % is group
	# The second one is the hosts
	# The third one is the user as you are running the command （root:root）user:group
	# The last one is the commands allowed

	# ALL 表示任何身份、主机、指令

