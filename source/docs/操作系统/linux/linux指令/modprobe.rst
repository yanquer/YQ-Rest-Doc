==========================
modprobe
==========================

内核模块可见: :doc:`/docs/操作系统/linux/系统服务/内核模块`

-a, --all
  载入全部的模块。
-c, --show-conf
  显示所有模块的设置信息。
-d, --debug
  使用排错模式。
-l, --list
  显示可用的模块。
-r, --remove
  若在命令指定模块,则删除指定模块,否则,指定"自动清除"模式
-t, --type
  指定模块类型。
-v, --verbose
  执行时显示详细的信息。
-V, --version
  显示版本信息。
-help
  显示帮助。
-C, --configconfig file
  指定配置文件.默认使用/etc/modules.conf文件为配置文件
-c
  列出目前系统所有的模组！(更详细的代号对应表)
-l
  列出目前在/lib/modules/`uname-r`/kernel当中的所有模组完整档名；
-f
  强制载入该模组；
-r
  类似 :doc:`rmmod` ，就是移除某个模组啰～
