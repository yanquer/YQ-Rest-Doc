===================
lsof
===================

强大的查询工具，-i几乎万能（自吹）

关键选项
默认 : 没有选项，lsof列出活跃进程的所有打开文件
组合 : 可以将选项组合到一起，如-abc，但要当心哪些选项需要参数

-a    结果进行“与”运算（而不是“或”）
-l    在输出显示用户ID而不是用户名
-h    获得帮助
-t    仅获取进程ID
-U    获取UNIX套接口地址
-F    格式化输出结果，用于其它命令。
      可以通过多种方式格式化，如-F pcfn（用于进程id、命令名、文件描述符、文件名，并以空终止）
-i    条件查询连接, 如指定协议: lsof -i tcp:$port     -i（4,6，协议，：端口，@ip）
-c    查看指定的命令正在使用的文件与网络连接    -c vim
-u    显示指定用户打开了什么
-u<user>
      消灭指定用户的所有东西    kill -9 `lsof -t -u luyi`
-p    指定进程ID(pid)已经打开的文件    -p 643
+d    查看某目录文件信息    不加d也可以，但是可能不全
+D    递归查看某目录文件信息

更详细的描述以及恢复被删除的文件，某种情况
可参考: https://www.cnblogs.com/sparkbj/p/7161669.html


mac下查看指定端口是否有占用, 如查询 tcp的8080是否占用::

  lsof -i tcp:8080

使用这个主要是因为 mac 的 netstat 跟linux下有点不一样
