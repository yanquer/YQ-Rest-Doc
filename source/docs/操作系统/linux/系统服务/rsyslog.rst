===============================
rsyslog
===============================

rsyslog服务

rsyslog日志服务简介
===============================

rsyslog是一个基于C/S架构的服务，Linux系统中分类两个日志：

- klogd：kernel，记录内核相关日志
- syslogd：service，记录应用程序相关日志

rsyslog是centos6 以后系统使用的日志系统。

记录格式::

  日期时间 主机进程[pid]： 事件内容

rsyslog配置详解
===============================

- 程序包：rsyslog
- 配置文件：/etc/rsyslog.conf /etc/rsyslog.d/
- 主程序：/usr/sbin/rsyslogd
- 模块路径：/usr/lib64/rsyslog/
- unit file: /usr/lib/systemd/system/rsyslog.service

相关术语:
  - facility：设施、信道
  - priority：日志级别

命令使用
===============================

日志存储在mysql
===============================





