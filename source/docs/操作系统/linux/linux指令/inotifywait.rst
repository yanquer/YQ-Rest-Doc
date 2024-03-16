=============================
inotifywait
=============================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


监控文件夹变化, 适用于Linux

安装::

  brew install inotify-tools

使用inotifywait命令来监听文件夹变化的基本示例::

  inotifywait -m -r -e create,modify,delete /path/to/directory

  # -e create,modify,delete
  #   指定要监听的事件类型，包括文件的创建、修改和删除。
  # /path/to/directory：要监听的目标文件夹的路径。

-m
  保持监听状态，持续监视文件夹的变化。
-r
  递归地监听子目录。

运行以上命令后，inotifywait会一直运行并监听指定目录中的文件变化。
当有新文件被创建、文件被修改或文件被删除时，它会输出相应的事件信息。



