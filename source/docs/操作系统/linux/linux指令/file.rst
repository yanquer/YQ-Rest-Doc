=============================
file
=============================

辨识文件类型

语法::

	file [-bcLvz][-f <名称文件>][-m <魔法数字文件>...][文件或目录...]

选项参数
=============================

常用::

	-b		列出辨识结果时，不显示文件名称。
	-c		详细显示指令执行过程，便于排错或分析程序执行的情形。
	-f<名称文件>		指定名称文件，其内容有一个或多个文件名称时，让file依序辨识这些文件，格式为每列一个文件名称。
	-L				直接显示符号连接所指向的文件的类别。
	-m<魔法数字文件>	指定魔法数字文件。
	-v				显示版本信息。
	-z				尝试去解读压缩文件的内容。
	[文件或目录...] 	要确定类型的文件列表，多个文件之间使用空格分开，可以使用shell通配符匹配多个文件。

所有

--help                 display this help and exit
-v, --version              output version information and exit
-m, --magic-file LIST      use LIST as a colon-separated list of magic
						number files
-M LIST                    use LIST as a colon-separated list of magic
						number files in place of default
	LIST                    use LIST as a colon-separated list of magic
						number files in place of default
-z, --uncompress           try to look inside compressed files
-Z, --uncompress-noreport  only print the contents of compressed files
-b, --brief                do not prepend filenames to output lines
-c, --checking-printout    print the parsed form of the magic file, use in
						conjunction with -m to debug a new magic file
						before installing it
-d                         use default magic file
					use default magic file
-e, --exclude TEST         exclude TEST from the list of test to be
						performed for file. Valid tests are:
						apptype, ascii, cdf, compress, csv, elf,
						encoding, soft, tar, json, text,
						tokens
--exclude-quiet TEST         like exclude, but ignore unknown tests
-f, --files-from FILE      read the filenames to be examined from FILE
-F, --separator STRING     use string as separator instead of :
-i                         do not further classify regular files
					do not further classify regular files
-I, --mime                 output MIME type strings (--mime-type and
						--mime-encoding)
--extension            output a slash-separated list of extensions
--mime-type            output the MIME type
--mime-encoding        output the MIME encoding
-k, --keep-going           don't stop at the first match
-l, --list                 list magic strength
-L, --dereference          follow symlinks
-h, --no-dereference       don't follow symlinks (default)
-n, --no-buffer            do not buffer output
-N, --no-pad               do not pad output
-0, --print0               terminate filenames with ASCII NUL
-p, --preserve-date        preserve access times on files
-P, --parameter            set file engine parameter limits
							bytes 1048576 max bytes to look inside file
							elf_notes     256 max ELF notes processed
							elf_phnum    2048 max ELF prog sections processed
							elf_shnum   32768 max ELF sections processed
							encoding   65536 max bytes to scan for encoding
							indir      50 recursion limit for indirection
							name      60 use limit for name/use magic
							regex    8192 length limit for REGEX searches
-r, --raw                  don't translate unprintable chars to \ooo
-s, --special-files        treat special (block/char devices) files as
						ordinary ones
-S, --no-sandbox           disable system call sandboxing
-C, --compile              compile file specified by -m
-D, --debug                print debugging messages

用例
=============================

查看文件相关信息::

	yanque@yanquedembp Downloads % file *
	$RECYCLE.BIN:  directory
	movie:         directory
	mushenji2.txt: Non-ISO extended-ASCII text, with very long lines (638), with CRLF line terminators

查看文件编码::

	yanque@yanquedembp Downloads % file --mime-encoding *

	$RECYCLE.BIN:  binary
	movie:         binary
	mushenji2.txt: unknown-8bit
	mushenji.txt:  utf-8

