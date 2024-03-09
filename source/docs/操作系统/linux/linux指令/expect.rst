==============================
expect
==============================

通过expect可以实现将交互式的命令变为非交互式执行，不需要人为干预(手动输入)

.. csv-table:: 用法
  :header: option , 含义
  :delim: |

  set timeout 30 | 设置超时时间30s
  spawn ${cmd}   | spawn是执行expect之后后执行的内部命令开启一个会话 #功能:用来执行shell的交互命令
  expect         | 相当于捕捉
  send           | 执行交互动作，将交互要执行的命令进行发送给交互指令，命令字符串结尾要加上“\r”，#---相当于回车
  interact       | 执行完后保持交互状态，需要等待手动退出交互状态，如果不加这一项，交互完成会自动退出
  exp_continue   | 继续执行接下来的操作

实战非交互式ssh连接::

  [root@qfedu script]# vim test.sh

  #!/bin/sh

  expect -c "
      set timeout 10
      spawn ssh root@localhost
      expect {
          \"yes/no\" { send \"yes\r\"; exp_continue }
          \"password:\" { send \"root\r\" }
      }
  "
  #注意花括号前一定要有空格

  [root@qfedu script]# chmod +x test.sh

  [root@qfedu script]# ./test.sh

  spawn ssh root@localhost

  root@localhost's password:

  Last login: Fri Aug 28 16:57:09 2019

  #如果添加interact参数将会等待我们手动交互进行退出。如果不加interact参数在登录成功之后会立刻退出。


