================
apt-get
================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


支持的command
================

语法::

    apt-get <command> [options] [packages]

- update - 取回更新的软件包列表信息
- upgrade - 进行一次升级
- install - 安装新的软件包(注：软件包名称是 libc6 而非 libc6.deb)
- remove - 卸载软件包
- autoremove - 卸载所有自动安装且不再使用的软件包
- purge - 卸载并清除软件包的配置
- source - 下载源码包文件
- build-dep - 为源码包配置所需的编译依赖关系
- dist-upgrade - 发布版升级，见 apt-get(8)
- dselect-upgrade - 根据 dselect 的选择来进行升级
- clean - 删除所有已下载的包文件
- autoclean - 删除已下载的旧包文件
- check - 核对以确认系统的依赖关系的完整性
- changelog - 下载指定软件包，并显示其changelog
- download - 下载指定的二进制包到当前目录

选项参数
================

-h      本帮助文档。
-q      让输出可作为日志 - 不显示进度
-qq     除了错误外，什么都不输出
-d      仅仅下载 - 【不】安装或解开包文件
-s      不作实际操作。只是依次模拟执行命令
-y      对所有询问都回答是(Yes)，同时不作任何提示
-f      当出现破损的依赖关系时，程序将尝试修正系统
-m      当有包文件无法找到时，程序仍尝试继续执行
-u      显示已升级的软件包列表
-b      在下载完源码包后，编译生成相应的软件包
-V      显示详尽的版本号
-c<config>    读取指定配置文件
-o<config>    设置任意指定的配置选项，例如 -o dir::cache=/tmp


模拟安装::

    apt-get install -s $soft