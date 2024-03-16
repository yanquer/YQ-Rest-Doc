============================
rsync
============================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


rsync 是一个远程数据同步工具，可通过LAN/WAN快速同步多台主机间的文件。

rsync使用所谓的“rsync算法”来使本地和远程两个主机之间的文件达到同步，
这个算法只传送两个文件的不同部分，而不是每次都整份传送，因此速度相当快。
rsync是一个功能非常强大的工具，其命令也有很多功能特色选项，我们下面就对它的选项一一进行分析说明。

语法::

  rsync [OPTION]... SRC DEST
  rsync [OPTION]... SRC [USER@]host:DEST
  rsync [OPTION]... [USER@]HOST:SRC DEST
  rsync [OPTION]... [USER@]HOST::SRC DEST
  rsync [OPTION]... SRC [USER@]HOST::DEST
  rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]

对应于以上六种命令格式，rsync有六种不同的工作模式

拷贝本地文件
  当SRC和DES路径信息都不包含有单个冒号 ":" 分隔符时就启动这种工作模式.
  如::

    rsync -a /data /backup
本地->远程
  使用一个远程shell程序(如rsh、ssh)来实现将本地机器的内容拷贝到远程机器。

  当DST路径地址包含单个冒号":"分隔符时启动该模式.
  如::

    rsync -avz *.c foo:src
远程->本地
  使用一个远程shell程序(如rsh、ssh)来实现将远程机器的内容拷贝到本地机器。

  当SRC地址路径包含单个冒号":"分隔符时启动该模式.
  如::

    rsync -avz foo:src/bar /data
远程rsync服务->本地
  从远程rsync服务器中拷贝文件到本地机。

  当SRC路径信息包含"::"分隔符时启动该模式.
  如::

    rsync -av root@192.168.78.192::www /databack
本地->远程rsync服务
  从本地机器拷贝文件到远程rsync服务器中。

  当DST路径信息包含"::"分隔符时启动该模式.
  如::

    rsync -av /databack root@192.168.78.192::www
列远程机的文件列表
  类似于rsync传输，不过只要在命令中省略掉本地机信息即可.
  如::

    rsync -v rsync://192.168.78.192/www

选项
============================

-v, --verbose
  详细模式输出, 可以打印一些信息，比如文件列表、文件数量等
-q, --quiet
  精简输出模式。
-c, --checksum
  打开校验开关，强制对文件传输进行校验。
-a, --archive
  归档模式，表示以递归方式传输文件，并保持所有文件属性，等于 ``-rlptgoD``

  -a 选项后面可以跟一个 --no-OPTION，表示关闭 -r、-l、-p、-t、-g、-o、-D 中的某一个，比如::

    -a --no-l

  等同于::

    -r、-p、-t、-g、-o、-D 选项。
-r, --recursive
  表示以递归模式处理子目录，它主要是针对目录来说的，
  如果单独传一个文件不需要加 -r 选项，但是传输目录时必须加
-R, --relative
  使用相对路径信息。
-b, --backup
  创建备份，也就是对于目的已经存在有同样的文件名时，
  将老的文件重新命名为~filename。可以使用 --suffix 选项来指定不同的备份文件前缀。
--backup-dir
  将备份文件(如~filename)存放在在目录下。
--suffix=<SUFFIX>
  定义备份文件前缀(好像只有一个杠-suffix)。
-u, --update
  仅仅进行更新，也就是跳过所有已经存在于DST，并且文件时间晚于要备份的文件，
  或者说把 DEST 中比 SRC 还新的文件排除掉，不会覆盖
-l, --links
  保留软链接
-L, --copy-links
  表示像对待常规文件一样处理软链接.

  如果是 SRC 中有软链接文件，则加上该选项后，将会把软连接指向的目标文件复制到 DEST
--copy-unsafe-links
  仅仅拷贝指向SRC路径目录树以外的链接
--safe-links
  忽略指向SRC路径目录树以外的链接。
-H, --hard-links
  保留硬链接。
-p, --perms
  保持文件权限
-o, --owner
  保持文件属主信息
-g, --group
  保持文件属组信息
-D, --devices
  保持设备文件信息
-t, --times
  保持文件时间信息
-S, --sparse
  对稀疏文件进行特殊处理以节省DST的空间。
-n, --dry-run
  显示哪些文件将被传输。
-w, --whole-file
  拷贝文件，不进行增量检测。
-x, --one-file-system
  不要跨越文件系统边界。
-B, --block-size=SIZE
  检验算法使用的块尺寸，默认是700字节。
-e, --rsh=command
  指定使用rsh、ssh方式进行数据同步。
--rsync-path=PATH
  指定远程服务器上的rsync命令所在路径信息。
-C, --cvs-exclude
  使用和CVS一样的方法自动忽略文件，用来排除那些不希望传输的文件。
--existing
  仅仅更新那些已经存在于DST的文件，而不备份那些新创建的文件。
--delete
  删除那些 DST 中 SRC 没有的文件
--delete-excluded
  同样删除接收端那些被该选项指定排除的文件。
--delete-after
  传输结束以后再删除。
--ignore-errors
  及时出现IO错误也进行删除。
--max-delete=NUM
  最多删除NUM个文件。
-P, --partial
  保留那些因故没有完全传输的文件，加快随后的再次传输.
  参数允许恢复中断的传输.

  - 不使用该参数时, `rsync` 会删除传输到一半被打断的文件
  - 使用该参数后，传输到一半的文件也会同步到目标目录，下次同步时再恢复中断的传输。

  一般需要与 `--append` 或 `--append-verify` 配合使用
--force
  强制删除目录，即使不为空。
--numeric-ids
  不将数字的用户和组id匹配为用户名和组名。
--timeout=time
  ip超时时间，单位为秒。
-I, --ignore-times
  不跳过那些有同样的时间和长度的文件。
--size-only
  当决定是否要备份文件时，仅仅察看文件大小而不考虑文件时间。
--modify-window=NUM
  决定文件是否时间相同时使用的时间戳窗口，默认为0。
-T, --temp-dir=DIR
  在DIR中创建临时文件。
--compare-dest=DIR
  同样比较DIR中的文件来决定是否需要备份
-z, --compress
  对备份的文件在传输时进行压缩处理
--exclude=PATTERN
  指定排除不需要传输的文件模式, 等号后面跟文件名，可以是通配符模式（如 `*.txt`）
--include=PATTERN
  指定不排除而需要传输的文件模式。
--exclude-from=FILE
  排除FILE中指定模式的文件。
--include-from=FILE
  不排除FILE指定模式匹配的文件。
--version
  打印版本信息。
--address
  绑定到特定的地址。
--config=FILE
  指定其他的配置文件，不使用默认的rsyncd.conf文件。
--port=PORT
  指定其他的rsync服务端口。
--blocking-io
  对远程shell使用阻塞IO。
-stats
  给出某些文件的传输状态。
--progress
  表示在同步的过程中可以看到同步的过程状态，比如统计要同步的文件数量、 同步的文件传输速度等
--log-format=formAT
  指定日志文件格式。
--password-file=FILE
  从FILE中得到密码。
--bwlimit=KBPS
  限制I/O带宽，KBytes per second
-h, --help
  显示帮助信息
--append
  参数指定文件接着上次中断的地方，继续传输
--append-verify
  参数跟 `--append` 参数类似，但会对传输完成后的文件进行一次校验。
  如果校验失败，将重新发送整个文件。

对于初学者来说，记住最常用的几个即可，比如 -a、-v、-z、--delete 和 --exclude。

