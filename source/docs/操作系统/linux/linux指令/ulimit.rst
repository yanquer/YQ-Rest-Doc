==============================
ulimit
==============================


.. post:: 2023-02-26 21:30:12
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


限制系统最大打开文件数

ulimit 系统linux中进行资源限制

-a 显示当前系统所有limit信息
-n 查看进程可以打开的最大文件描述符的数量
-u 用户最大可用的进程数

可以在文件/etc/security/limits.config中配置

配置规则::

  <domain> <type> <item> <value>

  (含义：domain用户主体，*表示所有；type限制类型；item限制资源名称；value限制资源的具体数值)

eg::

  *          soft    nproc     40960  软限制最大进程数
  *          hard    nproc     40960  硬限制最大进程数
  root       soft    nproc     unlimited
  *	   soft    nofile    262144 软限制最大文件数
  *	   hard    nofile    262144  硬限制最大文件数

.. note::

  可以通过ulimit -n [value]修改每个文件可打开的最大进程数目，缺省值是1024，可以写入在/etc/profile里然后source重新载入

session设置::

  ulimit -a #查看所有
  ulimit -S -n1024 #设置当前会话打开的文件数软连接数为1024
  ulimit -H -n1024 #设置当前会话打开的文件数硬链接数为1024
  ulimit -n 1024 #设置当前会话打开的文件数软连接数&&硬连接数都为1024

