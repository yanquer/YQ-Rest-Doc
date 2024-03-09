========================
smartctl
========================

功能
========================

smartctl 工具用来实现操作系统上的 ATA/SATA 、SCSI/SAS、SSD 等物理设备的监控、分析及使用情况报告。

SMART 指的是对硬盘等设备的可靠性监控及预测磁盘可能存在的故障，并根据硬盘形态进行不同程度的自检。

smartctl 的版本可以兼容众多磁盘规范，例如 ACS-2、ATA8-ACS、ATA/ATAPI-7 及更早期的一些磁盘标准。

.. note::

	大多发行版已经内置, 若没有, 可手动安装: ``apt install smartmontools``

smartmontools 提供了两种使用模式

- 以服务模式运行: 通过 smartd 服务及配置文件来对服务器上的磁盘按照规则进行自检，需要开启 smartd.service 服务
- 以命令行模式运行: 以终端命令行的方式对磁盘进行自检，无需开启 smartd 服务

.. note::

	Mac可通过::

		brew install smartmontools

	来安装, 并查看固态寿命

选项参数
========================

.. csv-table:: 基本命令参数选项(部分)
	:align: center
	:header: 选项, 说明
	:delim: :

	-h, --help, --usage							: Display this help and exit
	-V, --version, --copyright, --license		: Print license, copyright, and version information and exit
	-i, --info									: 显示设备基本信息
	--identify[=[w][nvb]]						: Show words and bits from IDENTIFY DEVICE data (ATA)
	-g NAME, --get=NAME							: Get device setting. all, aam, apm, dsn, lookahead, security, wcache, rcache, wcreorder, wcache-sct
	-a, --all									: Show all SMART information for device
	-x, --xall									: Show all information for device
	--scan										: 查看系统所有设备
	--scan-open									: Scan for devices and try to open each device
	-H, --health								: 检查健康状态
	-t TEST, --test=TEST						: Run test. TEST. offline, short, long, conveyance, force, vendor,N, select,M-N, pending,N, afterselect,[on|off]

``-a`` 输出信息说明
------------------------

严重警告（Critical Warning）
	会显示控制器状态警告讯息，如果都显示0x00 就表示没事
温度（Temperature）
	会显示当前SSD 温度资讯
可用备用空间（Available Spare）
	SSD 剩余空间百分比
可用备用临界值（Available Spare Threshold）
	临界值全由厂商定义
寿命百分比（Percentage Used）
	目前SSD 寿命百分比数值，具体取决于实际设备使用情况和厂商对设备寿命的预测。
资料读取（Data Units Read）
	记录电脑从SSD读取512字节数据单元的总量，每1000个单元记录一次，即这项Raw数据1的值等于500KB。
资料写入（Data Units Read）
	如上，就是写入总量。
主机读取命令（Host Read Commands）
	主控收到的读取命令数量。
主机写入命令（Host Write Commands）
	主控收到的写入命令数量。
控制器忙碌时间（Controller Busy Time）
	主控忙于I/O命令的时间。
意外关机（Unsafe Shutdowns）
	纪录不正常断电次数
媒体和资料完整性错误（Media and Data Integrity Errors）
	主控检测得到的未恢复的数据完整性错误次数。
错误资料纪录（Number of Error Information Log Entries）
	主控总共收到的错误信息日志数量。

示例
========================

.. code-block:: sh

	# 检查磁盘健康状态
	smartctl -H /dev/sda

	# 然后查看磁盘详细情况
	smartctl -a /dev/sda

	# 再对磁盘进行短期测试
	smartctl -t short /dev/sda

	# 查看磁盘测试结果, 基本磁盘健康状态就可以定位出来
	smartctl -l selftest /dev/sda

	# 最后检查磁盘错误日志
	smartctl -l error /dev/sdb


