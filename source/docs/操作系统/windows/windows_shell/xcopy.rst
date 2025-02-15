==========
xcopy
==========

复制文件和目录树::

  XCOPY source [destination] [/A | /M] [/D[:date]] [/P] [/S [/E]] [/V] [/W]
                            [/C] [/I] [/Q] [/F] [/L] [/G] [/H] [/R] [/T] [/U]
                            [/K] [/N] [/O] [/X] [/Y] [/-Y] [/Z] [/B] [/J]
                            [/EXCLUDE:file1[+file2][+file3]...] [/COMPRESS]

    source       指定要复制的文件。
    destination  指定新文件的位置和/或名称。
    /A           仅复制有存档属性集的文件，
                  但不更改属性。
    /M           仅复制有存档属性集的文件，
                  并关闭存档属性。
    /D:m-d-y     复制在指定日期或指定日期以后更改的文件。
                  如果没有提供日期，则只复制源时间比目标时间新的文件。
    /EXCLUDE:file1[+file2][+file3]...
                指定含有字符串的文件列表。每个字符串
                在文件中应位于单独的一行。如果任何
                字符串与复制文件的绝对路径的任何部分相符，
                则排除复制该文件。例如，
                指定如 \obj\ 或 .obj 的字符串会分别
                排除目录 obj 下面的所有文件或带有
                .obj 扩展名的所有文件。
    /P           创建每个目标文件之前均进行提示。
    /S           复制目录和子目录，不包括空目录。
    /E           复制目录和子目录，包括空目录。
                  与 /S /E 相同。可以用来修改 /T。
    /V           验证每个新文件的大小。
    /W           提示在复制前按键。
    /C           即使有错误，也继续复制。
    /I           如果目标不存在，且要复制多个文件，
                  则假定目标必须是目录。
    /Q           复制时不显示文件名。
    /F           复制时显示完整的源文件名和目标文件名。
    /L           显示要复制的文件。
    /G           允许将加密文件复制到
                  不支持加密的目标。
    /H           隐藏文件和系统文件也会复制。
    /R           覆盖只读文件。
    /T           创建目录结构，但不复制文件。不
                  包括空目录或子目录。/T /E 包括
                  空目录和子目录。
    /U           只复制已经存在于目标中的文件。
    /K           复制属性。一般的 Xcopy 会重置只读属性。
    /N           用生成的短名称复制。
    /O           复制文件所有权和 ACL 信息。
    /X           复制文件审核设置(隐含 /O)。
    /Y           取消提示以确认要覆盖
                  现有目标文件。
    /-Y          触发提示，以确认要覆盖
                  现有目标文件。
    /Z           在可重新启动模式下复制网络文件。
    /B           复制符号链接本身与链接目标。
    /J           复制时不使用缓冲的 I/O。推荐复制大文件时使用。
    /COMPRESS    如果适用，在传输期间请求网络
                  压缩。

开关 /Y 可以预先在 COPYCMD 环境变量中设置。
这可能被命令行上的 /-Y 覆盖。


