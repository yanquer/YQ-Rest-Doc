=============================
iptables-save
=============================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


批量导出Linux防火墙规则，

直接执行：显示当前启用的所有规则，按raw、mangle、nat、filter顺序列出

-c    指定在还原iptables表时候，还原当前的数据包计数器和字节计数器的值；

-t    指定表

      “#”号开头的表示注释；

      “\*表名”表示所在的表；

      “：链名默认策略”表示相应的链及默认策略，具体的规则部分省略了命令名“iptables”；

      “COMMIT”表示提交前面的规则设置；

.. note::

  备份恢复时，
  iptables-save、
  :doc:`/docs/操作系统/linux/linux指令/iptables`
  两个都需要搭配重定向符使用


以前记的, 现在不记得啥意思::

  # 这是注释
  *nat
  # 这表示下面这些是nat表中的配置
  :PREROUTING ACCEPT [5129516:445315174]
  # :PREROUTING ACCEPT，表示nat表中的PREROUTING 链默认报文策略是接受（匹配不到规则继续） ，

  # [5129516:445315174] 即[packet, bytes]，表示当前有5129516个包(445315174字节)经过nat表的PREROUTING 链
  :INPUT ACCEPT [942957:151143842]
  :OUTPUT ACCEPT [23898:3536261]
  :POSTROUTING ACCEPT [23898:3536261]
  -- 解释同上
  :DOCKER - [0:0]
  -- 解释同上（此条是自定义链）
  ---------- 下面开始按条输出所有规则----------
  [4075:366986] -A PREROUTING -m addrtype --dst-type LOCAL -j DOCKER
  -- [4075:366986]即[packet, bytes]，表示经过此规则的包数，字节数。 后面部分则是用iptables命令配置此规则的命令（详解选项可参考iptables帮助）。
  [0:0] -A OUTPUT ! -d 127.0.0.0/8 -m addrtype --dst-type LOCAL -j DOCKER
  [0:0] -A POSTROUTING -s 172.17.0.0/16 ! -o docker0 -j MASQUERADE
  [2:188] -A POSTROUTING -s 192.168.122.0/24 -d 224.0.0.0/24 -j RETURN
  [0:0] -A POSTROUTING -s 192.168.122.0/24 -d 255.255.255.255/32 -j RETURN
  [0:0] -A POSTROUTING -s 192.168.122.0/24 ! -d 192.168.122.0/24 -p tcp -j MASQUERADE --to-ports 1024-65535
  [0:0] -A POSTROUTING -s 192.168.122.0/24 ! -d 192.168.122.0/24 -p udp -j MASQUERADE --to-ports 1024-65535
  [0:0] -A POSTROUTING -s 192.168.122.0/24 ! -d 192.168.122.0/24 -j MASQUERADE
  [0:0] -A DOCKER -i docker0 -j RETURN
  --以上规则同第一条规则的解释
  COMMIT
  -- 应用上述配置
  # Completed on Tue Jan 15 15:42:32 2019

