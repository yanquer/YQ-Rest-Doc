====================================
PS1 提示符定义
====================================

参考: `linux PS1 提示符定义 <https://www.cnblogs.com/starspace/archive/2009/02/21/1395382.html>`_

PS1
  就是用户平时的提示符。
PS2
  第一行没输完，等待第二行输入的提示符。

Linux系统提示符是用系统变量PS1来定义的。
一般系统默认的形式是：[username@host 工作目录]$.

用 echo $PS1 可以得到PS1的值，即::

  PS1="[\u@\h \w]"\$

登录后可以更改PS1的显示样式，但是当退出重启登录进入系统后，
样式又变成系统默认的样式了，如果要彻底改变它的样式，只能从配置文件中改。

PS是在用户根目录下的.bash_profile中定义的。

如::

  # .bash_profile

  # Get the aliases and functions

  if [ -f ~/.bashrc ]; then

  . ~/.bashrc

  fi

  # User specific environment and startup programs

以下是设定的PS1的值::

  PS1="[\u@\h \w]\$"

  PATH=$PATH:$HOME/bin

使用export把PS1输出，以使它可以在子shell中生效,这会造成ROOT用户的也采用此样式,
export PS1 要慎用::

  export PATH

  unset USERNAME

下面简单说说环境下默认的特殊符号所代表的意义::

  \d: 代表日期，格式为weekday month date，例如："Mon Aug 1"
  \H: 完整的主机名称。例如：我的机器名称为：fc4.linux，则这个名称就是fc4.linux
  \h: 仅取主机的第一个名字，如上例，则为fc4，.linux则被省略
  \t: 显示时间为24小时格式，如：HH：MM：SS
  \T: 显示时间为12小时格式
  \A: 显示时间为24小时格式：HH：MM
  \u: 当前用户的账号名称
  \v: BASH的版本信息
  \w: 完整的工作目录名称。家目录会以 ~代替
  \W: 利用basename取得工作目录名称，所以只会列出最后一个目录
  \#: 下达的第几个命令
  \$: 提示字符，如果是root时，提示符为：# ，普通用户则为：$

我们可以通过设置PS1变量使提示符成为彩色。
在PS1中设置字符序列颜色的格式为::

  \[\e[F;Bm\]
  # 其实 \e[Fm 即可

  # 其中 F 为字体颜色，编号30~37； B 为背景色，编号40~47。
  # 可通过 \e[0m 关闭颜色输出；特别的，当B为1时，将显示加亮加粗的文字，

颜色表与代码表见 :doc:`/docs/操作系统/linux/概念性/颜色表与代码表`




