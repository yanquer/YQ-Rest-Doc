========================
hash
========================

每个SHELL都有一个独立的hash表, 初始时候为空, 可直接hash查看当前SHELL的hash表::

  hash

每当你执行过一条命令时，hash表会记录下这条命令的路径，就相当于缓存一样。
第一次执行命令shell解释器默认的会从PATH路径下寻找该命令的路径，
当你第二次使用该命令时，shell解释器首先会查看hash表，没有该命令才会去PATH路径下寻找

hash表的作用：大大提高命令的调用速率

不带参数, 查看当前已有的表, hash表会记录下执行命令的次数，以及该命令的绝对路径

选项:

-l
  既可以看到hash表命令的路径，也可以看到它的名字及别名
-p<cmd new_name>
  给已有的指令 `cmd` 重命名为 `new_name` (起别名),
  如::

    hash -p /bin/ls bb

  之后直接 `bb` 调用的就是ls了
-t<cmd>
  查看 `cmd` 在hash表中存储的路径, 没有就直接报错没找到
-r
  清空hash表
-d<cmd>
  仅清除某一个hash记录



