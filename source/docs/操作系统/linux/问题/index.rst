============================================
问题
============================================


.. post:: 2024-03-09 18:21:01
  :tags: linux, 问题
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


.. toctree::
  :maxdepth: 1

  ssh重置计数器
  单次任务
  定时任务
  谁在系统
  警告所有人
  二进制数据访问
  root密码忘记
  Linux的一些内核参数
  获取所有变量与环境变量
  进程暂停与挂起
  linux参数过长
  debian10 iptables-restore 的 bug


关于 #!
============================================

表示当作为执行文件的时候，使用解释器路径，默认为当前登录shell

必须写在第一行才有用

当执行执行文件时，cd到所在目录后，执行需要加 ./ ，    ./test的./是为了承接现在所在的文件夹，
让现在所在的文件夹+文件，合并成该文件的完整路径，用于执行。

优先级
  当直接指定解释器的时候 比如 python xxx.py， xxx.py文件里的 #! 是不生效的，

只有作为执行文件的时候才会生效，比如  ./xxx.py

文件
============================================

登陆日志查看::

  /var/log/auth.log
  /var/log/secure.log

其他日志::

  /var/log/message  一般信息和系统信息
  /var/log/secure  登陆信息
  /var/log/maillog  mail记录
  /var/log/utmp
  /var/log/wtmp    登陆记录信息（last命令即读取此日志或者 who /var/log/wtmp）


