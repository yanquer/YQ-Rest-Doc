==================================
Linux下配置DLAN服务
==================================

DLAN是一个适用于多媒体的传输协议

安装 minidlna::

  sudo apt-get install -y minidlna

编辑 minidlna 的配置文件 `/etc/minidlna.conf` ::

  media_dir=/path/to/media
  db_dir=/var/lib/minidlna
  log_dir=/var/log/minidlna
  friendly_name=DLNA Server
  port=8200

其中 `media_dir` 是您媒体文件所在的目录，可以指定多个目录；`friendly_name` 是服务器名称；`port` 是服务监听的端口号。

启动 minidlna 服务::

  sudo service minidlna start

添加共享文件夹::

  sudo minidlna -R

此命令将重新扫描 `media_dir` 中的媒体文件，并添加到 DLNA 服务器中。

测试 DLNA 服务器是否正常工作：

使用支持 DLNA 协议的设备或软件，
例如 VLC 播放器、Windows Media Player 等，连接到 DLNA 服务器的 IP 地址和端口号即可访问。

如果一切正常，则应该可以浏览、搜索和播放媒体文件了。




