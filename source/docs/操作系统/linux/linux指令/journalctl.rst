=============================
journalctl
=============================


.. post:: 2023-02-26 21:30:12
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


在 `systemd` 下, 内核和系统的信息都通过日志服务 `systemd-journald.service` (又名 `journald`)来记录，
放在 `/var/log/journal` 下的不变的二进制数据，
或放在"`/run/log/journal/`"下的变化的二进制数据.
这些二进制日志数据，可以通过 `journalctl` 命令来访问。

例如，你可以显示从最后一次启动以来的日志，按如下所示::

  journalctl -b

  操作										命令片段
  查看从最后一次启动开始的系统服务和内核日志	"journalctl -b --system"
  查看从最后一次启动开始的当前用户的服务日志	"journalctl -b --user"
  查看从最后一次启动开始的 "$unit" 工作日志	"journalctl -b -u $unit"
  查看从最后一次启动开始的 "$unit"的工作日志 ("tail -f" 式样)												"journalctl -b -u $unit -f"


