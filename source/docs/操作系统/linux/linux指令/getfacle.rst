======================================
getfacle
======================================

查看acl权限::

  getfacle $filename

例::

  [root@localhost /]# getfacl project
  #查看/prpject目录的ACL权限
  #file: project <-文件名
  #owner: root <-文件的属主
  #group: tgroup <-文件的属组
  user::rwx <-用户名栏是空的，说明是属主的权限
  user:st:r-x <-用户st的权限
  group::rwx <-组名栏是空的，说明是属组的权限
  mask::rwx <-mask权限
  other::--- <-其他人的权限

关于ACL权限参考: :doc:`/docs/操作系统/linux/系统服务/ACL权限控制`





