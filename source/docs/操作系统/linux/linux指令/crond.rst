==============================
crond
==============================

crontab服务
==============================

Linux下的任务调度分为两类： **系统任务调度** 和 **用户任务调度**

系统任务调度
------------------------------

系统周期性所要执行的工作，比如写缓存数据到硬盘、日志清理等。
在 `/etc` 目录下有一个 crontab 文件，这个就是系统任务调度的配置文件。

`/etc/crontab` 文件包括下面几行::

  SHELL=/bin/bash
  PATH=/sbin:/bin:/usr/sbin:/usr/bin
  MAILTO=""HOME=/

  # run-parts
  51 * * * * root run-parts /etc/cron.hourly
  24 7 * * * root run-parts /etc/cron.daily
  22 4 * * 0 root run-parts /etc/cron.weekly
  42 4 1 * * root run-parts /etc/cron.monthly

前四行是用来配置crond任务运行的环境变量
  - 第一行SHELL变量指定了系统要使用哪个shell，这里是bash
  - 第二行PATH变量指定了系统执行命令的路径
  - 第三行MAILTO变量指定了crond的任务执行信息将通过电子邮件发送给root用户，
    如果MAILTO变量的值为空，则表示不发送任务执行信息给用户，
  - 第四行的HOME变量指定了在执行命令或者脚本时使用的主目录。

用户任务调度
------------------------------

用户定期要执行的工作，比如用户数据备份、定时邮件提醒等。
用户可以使用 crontab 工具来定制自己的计划任务。
所有用户定义的crontab文件都被保存在 `/var/spool/cron` 目录中。
其文件名与用户名一致，使用者权限文件如下::

  /etc/cron.deny     该文件中所列用户不允许使用crontab命令
  /etc/cron.allow    该文件中所列用户允许使用crontab命令
  /var/spool/cron/   所有用户crontab文件存放的目录,以用户名命名

crontab文件的含义
  用户所建立的crontab文件中，每一行都代表一项任务，每行的每个字段代表一项设置，它
  的格式共分为六个字段，前五段是时间设定段，第六段是要执行的命令段，格式如下::

    minute   hour   day   month   week   command     顺序：分 时 日 月 周

  其中：

  - minute： 表示分钟，可以是从0到59之间的任何整数。
  - hour：表示小时，可以是从0到23之间的任何整数。
  - day：表示日期，可以是从1到31之间的任何整数。
  - month：表示月份，可以是从1到12之间的任何整数。
  - week：表示星期几，可以是从0到7之间的任何整数，这里的0或7代表星期日。
  - command：要执行的命令，可以是系统命令，也可以是自己编写的脚本文件。

  在以上各个字段中，还可以使用以下特殊字符：

  - 星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。
  - 逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，“1,2,5,7,8,9”
  - 中杠（-）：可以用整数之间的中杠表示一个整数范围，例如“2-6”表示“2,3,4,5,6”
  - 正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。

crond服务-指令
==============================

常用::

  /sbin/service crond start    # 启动服务
  /sbin/service crond stop     # 关闭服务
  /sbin/service crond restart  # 重启服务
  /sbin/service crond reload   # 重新载入配置

查看crontab服务状态::

  service crond status

手动启动crontab服务::

  service crond start

查看crontab服务是否已设置为开机启动，执行命令::

  ntsysv

加入开机自动启动::

  chkconfig –level 35 crond on

centos版本适用

cron表达式中问号(?)的使用
==============================

cron表达式详解其中问号 ``?`` 只能用在 ``DayofMonth`` 和 ``DayofWeek`` 两个域，
由于指定日期( ``DayofMonth`` )和指定星期( ``DayofWeek`` )存在冲突，
所以当指定了日期( ``DayofMonth`` )后（包括每天），星期( ``DayofWeek`` )必须使用 ``?``，
同理，指定星期( ``DayofWeek`` )后，日期( ``DayofMonth`` )必须使用问号 ``?``.






