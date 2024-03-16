==============
apt-cache
==============


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


支持的command

- depends 查看该软件包需要哪些依赖包
- rdepends 查看该软件包被哪些包依赖

列出软件的安装来源

列::

	apt-cache madison $soft    # 搜索源里面的可用版本
	apt-cache policy $sofy    # 比上面那个详细一点
	apt-cache showpkg $soft    # 比上一个更详细，还会列出所有相关的


	apt-cache show $soft    # 显示指定包的详情 dpkg -s $soft也可以


