===============
dpkg
===============

debian linux上安装、创建、管理软件包的工具

选项参数
===============

-i <package>, --install <package>
                    安装软件包 package
-r <package>, --remove <package>
                    删除软件包
-P <package>, --purge <package>
                    删除软件包的同时删除其配置文件
-L <package>, --listfiles <package>
                    显示软件包关联的文件
-l                  显示已安装软件包列表
--unpack            解开软件包
-c <package>        显示软件包内文件列表
--confiugre <package>
                    配置软件包
-s <package>, --status <package>
                    查看软件包信息，是否已安装之类
-S                  搜索
--list              查看所有已安装软件包
-b<dir deb_name>    打包软件包, 第一个参数为deb的构建目录, 第二个为包名
--info <package>    查看deb包信息
-x <package dir>    解压deb中所要安装的文件, 第一个参数为所要解压的deb包，第二个参数为将deb包解压到指定的目录
                    不过这个只能解出安装文件, desktop等文件解包的用 dpkg-deb -R
-e <package>    解压deb中所要安装的文件, 第一个参数为所要解压的deb包，第二个参数为将deb包解压到指定的目录

.. note::

    读取手册使用::

        man dpkg-query

    而不是::

        man dpkg


.. 在这些情况下，dpkg仅充当前端

.. 关于选项 l 的结果解析（可以通过 dpkg -l | head -n 3 查看）

dpkg -l 结果
===============

dpkg -l 结果结构解析::

    root@6378b4ca047d:/# dpkg -l
    Desired=Unknown/Install/Remove/Purge/Hold
    | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
    |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
    ||/ Name                        Version                 Architecture Description
    +++-===========================-=======================-============-===============================================================================
    ii  adduser                     3.118ubuntu2            all          add and remove users and groups
    ii  apt                         2.0.2                   amd64        commandline package manager

.. csv-table:: 第一列首字母含义
    :header: 首字母, 含义

    u  ,  未知
    i  ,  安装
    r  ,  删除/卸载
    p  ,  清除（删除包括配置文件）
    h  ,  ？？？保持？保留？

.. csv-table:: 第一列第二字母含义
    :header: 字母, 含义

    n  ,  未安装
    i  ,  安装
    c  ,  仅安装配置文件
    U  ,  已解压
    F  ,  由于某种原因配置失败（半配置）
    H  ,  由于某种原因安装失败（半安装）
    W  ,  等待触发器（程序包正在等待另一个程序包的触发器）
    t  ,  触发挂起（已经触发）

.. csv-table:: 第一列第三字母含义
    :header: 字母, 含义

    R  ,  需要重新安装（包损坏 需重装）

如:

- ii 表示软件正常安装
- rc表示软件已卸载，可是配置文件还在，可以通过以下命令进行清理::

    dpkg -l | grep ^rc | cut -d' ' -f3 | sudo xargs dpkg --purg

