==============================
ausearch
==============================

使用ausearch命令可以搜索审计记录，必须以root用户身份执行ausearch命令。

安装::

  yum install audit
  # 要么
  up2date install audit

  #debian
  apt install auditd

语法格式::

  ausearch [参数]

**选项含义**

-f<文件名>
  基于文件名的搜索
-c<命令行名称>
  基于命令行名称的搜索
-n<计算机名称>
  基于计算机名称的搜索
-p<进程ID>
  基于进程ID的搜索
-k<键字段>
  基于键字段的搜索
-m<消息类型>
  基于消息类型的搜索
-x<可执行文件名>
  基于可执行文件名的搜索
-a<审计事件ID>
  基于审计事件ID的搜索
-o<SELinux对象上下文>
  基于对象上下文的搜索
-e<退出代码>
  基于系统调用退出代码的搜索
-r
  完全未格式化输出

-ga<所有组群的ID>
  基于所有组群GID的搜索
-ha<主机名>
  基于远程主机名的搜索
-ui<用户UID>
  基于用户UID的搜索
-tm<终端>
  基于终端的搜索
-sv<成功值>
  基于系统调用或事件成功值的搜索
-pp<父进程ID>
  基于父进程ID的搜索
-ul<用户登录ID>
  基于用户登录ID的搜索
-ue<有效UID>
  基于有效UID的搜索
-ge<有效GID>
  基于有效GID的搜索
-session<登录会话ID>
  基于登录会话ID的搜索
-sc<系统调用的名称>
  基于系统调用的名称或对象编号的搜索
-se<SELinux上下文>
  基于任何主体或对象的上下文搜索
-ts<开始日期><开始日期>, --start<开始日期><开始日期>
  基于开始时间、开始时间的搜索
-ua<所有用户的UID>
  基于所有的用户UID的搜索
-te<结束时间><结束时间>
  基于结束时间、结束时间的搜索
-su<SELinux上下文>
  基于主题的上下文的搜索

**例**

基于用户root搜索审计记录::

  [root@localhost ~]# ausearch  -ui 0

基于终端tty1搜索审计记录::

  [root@localhost ~]# ausearch -tm tty1

基于进程号1779搜索审计记录::

  [root@localhost ~]# ausearch -p 1779



