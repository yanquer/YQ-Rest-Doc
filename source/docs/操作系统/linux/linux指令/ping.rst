======================
ping
======================


.. post:: 2024-03-04 22:04:43
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn



主要透过 icmp 封包 探索网络.
属于网络层的ICMP协议，只能检查 IP 的连通性或网络连接速度， 无法检测IP的端口状态。

可以测试主机之间网络的连通性

-c 数值
  表示执行ping的次数

-n
  不进行ip与主机名的反查，直接用ip输出（速度较快）

-s 数值
  发出去的 icmp 封包大小，预设为56bytes
-t 数值
  TTL的数值，预设是255，每经过一个节点就减一
-W 数值
  等待响应对方主机的秒数

-M [do|dont]
  主要在侦测网络的MTU数值大小

  do
    代表传送一个 DF（Dont Fragment）旗标，让封包不能重新拆包与打包
  dont
    代表不要传送 DF标志，表示封包可以在其他主机封包、打包


若不存在::

  apt-get install iputils-ping
