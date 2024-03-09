==================
pv
==================

.. 给执行的指令增加进度信息

Pipe Viewer 显示当前在命令行执行的命令的进度信息，管道查看器

-p, --progress           显示进度条
-t, --timer              显示已用时间
-e, --eta                显示预计到达时间 (完成)
-I, --fineta             显示绝对估计到达时间
                         (完成)
-r, --rate               显示数据传输速率计数器
-a, --average-rate       显示数据传输平均速率计数器
-b, --bytes              显示传输的字节数
-T, --buffer-percent     显示正在使用的传输缓冲区百分比
-A, --last-written NUM   显示上次写入的字节数
-F, --format FORMAT      将输出格式设置为FORMAT
-n, --numeric            输出百分比
-q, --quiet              不输出任何信息(不显示进度条)

-W, --wait               在传输第一个字节之前不显示任何内容
-D, --delay-start SEC    在SEC秒过去之前不显示任何内容
-s, --size SIZE          将估算的数据大小设置为SIZE字节
-l, --line-mode          计算行数而不是字节数
-0, --null               行以零结尾
-i, --interval SEC       每SEC秒更新一次
-w, --width WIDTH        假设终端的宽度为WIDTH个字符
-H, --height HEIGHT      假设终端高度为HEIGHT行
-N, --name NAME          在可视信息前面加上名称
-f, --force              将标准错误输出到终端
-c, --cursor             使用光标定位转义序列

-L, --rate-limit RATE    将传输限制为每秒RATE字节, -L<num>每秒打印的字节数
-B, --buffer-size BYTES  使用BYTES的缓冲区大小
-C, --no-splice          从不使用splice()，始终使用读/写
-E, --skip-errors        跳过输入中的读取错误
-S, --stop-at-size       传输--size字节后停止
-R, --remote PID         更新过程PID的设置

-P, --pidfile FILE       将进程ID保存在FILE中

-d, --watchfd PID[:FD]   监视进程PID,打开的文件FD
-h, --help               显示帮助
-V, --version            显示版本信息


示例
==================

匀速打印::

	echo "xxxxxxx" |   pv -qL 10

此示例参考: `linux有趣的命令 <https://blog.csdn.net/qq_38250124/article/details/79094129>`_
