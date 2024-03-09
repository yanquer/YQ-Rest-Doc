====================
shell条件判断if
====================

**在条件表达式中进行字符串/数值比较**

字符串/数值判断(字符串判断时, shell一个等号与两个等号的效果是一致的)::

    str1 < str2         str1 排列在 str2 之前（取决于语言环境）
    str1 > str2         str1 排列在 str2 之后（取决于语言环境）
    str1 = str2         当两个串有相同内容、长度时为真
    str1 != str2	    当串str1和str2不等时为真
    -n str1             当串的长度大于0时为真(串非空)
    -z str1             当串的长度为0时为真(空串)
    str1                当串str1为非空时为真
    int1 -eq int2       两数相等为真
    int1 -ne int2       两数不等为真
    int1 -gt int2       int1大于int2为真
    int1 -ge int2       int1大于等于int2为真
    int1 -lt int2       int1小于int2为真
    int1 -le int2       int1小于等于int2为真

**在条件表达式中进行文件比较**

文件判断::

    -r file     用户可读为真
    -w file     用户可写为真
    -x file     用户可执行为真
    -f file     文件为普通文件为真
    -d file     文件为目录为真
    -c file     文件为字符特殊文件为真
    -b file     文件为块特殊文件为真
    -s file     文件大小非0时为真
    -t file     当文件描述符(默认为1)指定的设备为终端时为真
    -L file     文件存在符号链接为真
    -e file     文件是否存在
    -S file     存在 Socket 文件
    -p file     存在且为 FIFO（pipe）文件

    file1 -nt file2     file1 是否比 file2 新
    file1 -ot file2     file1 是否比 file2 旧
    file1 -ef file2     file1 和 file2 位于相同的设备上并且有相同的 inode 编号

判断符号::

    -a  与
    -o  或
    !   非

例, 比较两个字符串是否相等的办法::

    if [ "$test"x = "test"x ]; then

这里的关键有几点：

- 使用单个等号
- 注意到等号两边各有一个空格：这是unix shell的要求
- 注意到"$test"x最后的x，这是特意安排的，因为当$test为空的时候，上面的表达式就变成了x = testx，显然是不相等的。而如果没有这个x，表达式就会报错：``[: =: unary operator expected``

不带if的写法
====================

条件语法::

    command && if_success_run_this_command_too || true
    command || if_not_success_run_this_command_too || true

如下所示是多行脚本片段::

    if [ conditional_expression ]; then
    if_success_run_this_command
    else
    if_not_success_run_this_command
    fi

这里末尾的 `|| true` 是需要的，
它可以保证这个 shell 脚本在不小心使用了 `-e` 选项而被调用时不会在该行意外地退出



