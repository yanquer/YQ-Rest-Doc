=====================
nsis 指令
=====================

文件、目录操作
=====================

FileOpen/FileWrite/FileClose
--------------------------------------------

可用于创建文件, 写入文件::

  FileOpen $9 apachesrvin.bat w ;Opens a Empty File and fills it
  FileWrite $9 "cd $INSTDIR\apache$\r$\n"
  FileWrite $9 "apache -n Apache -k install$\r$\n"
  FileWrite $9 "net start Apache$\r$\n"
  FileWrite $9 "exit$\r$\n"
  FileClose $9 ;Closes the filled file

上面这段代码里的 ``$9`` 表示创建的文件指针赋给此变量, 类似::

  $9 = open('apachesrvin.bat')

.. _NSIS_File:

File
----------------------

作用: 释放文件到当前输出路径。

选项::

  /nonfatal 且当文件未找到时使用警告来代替错误
  /a        被添加的文件的属性将会保持
  /r        匹配的文件将会在子目录里被递归的搜索。如果目录名匹配则所有包含的内容都会被递归添加, 目录结构也会被保持
  /x        排除文件或目录

Delete
----------------------

作用: 从目标系统删除文件

例, 删除文件::

  Delete "$SMPROGRAMS\Test.exe"

Rename
----------------------

作用: 把源文件重命名为目标文件

例, 重命名文件::

  Rename $INSTDIR\file1 $INSTDIR\file2

CreateDirectory
----------------------

作用: 创建 (递归创建) 指定的目录。当目录不能创建时会放置一个错误标记。你也可以指定一个绝对路径。

例, 在默认Program Files目录下创建一个Temp目录::

  CreateDirectory "$SMPROGRAMS\Temp"

RMDir
----------------------

作用: 删除目录

例, 删除Resources及其子目录::

  RMDir /r $INSTDIR\Resources

SetOutPath
----------------------

作用: 设置输出路径($OUTDIR)且当路径不存在时创建(需要时会递归创建)。必须为绝对路径名, 通常都使用 $INSTDIR。

例, 将用户定义的解压路径作为输出目录::

  SetOutPath $INSTDIR

CreateShortCut
----------------------

作用: 创建快捷文件.lnk 目标文件

例, 设置Test.exe的快捷方式Test.lnk, 图标为Test.ico::

  CreateShortCut "$DESKTOP\Test.lnk" "$DESKTOP\Test.exe" "$DESKTOP\Icon\Test.ico"

.. _NSIS_注册表操作:

注册表操作
=====================

WriteRegStr/WriteRegExpandStr
--------------------------------------------

.. sidebar:: 关于Win64下写注册表时候的一些问题

  当使用nsis写入到 ``HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall`` 下时,
  系统的注册表编辑器并不会显示此项, 而是显示在
  ``HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall``,
  这是因为控制面板的“程序和功能”是基于注册表反射来实现的。对于64位系统,它只显示 Wow6432Node 下的注册表键,而不显示原生的64位键.

  要让卸载信息显示在控制面板中,nsis 在 64位系统下需要同时写入 Wow6432Node 下的对应键。一般的方法是:

  1. 首先写入原生键,如 HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\App
  2. 调用 SetRegView 64 来切换到 32位视图
  3. 写入 ``Wow6432Node\Software\Microsoft\Windows\CurrentVersion\Uninstall\App``
  4. 调用 SetRegView last 恢复注册表视图
  5. 继续写入原生的其他键

作用: 把字符串写入注册表。根键必须为下面列表之一:

- HKCR 或 HKEY_CLASSES_ROOT
- HKLM 或HKEY_LOCAL_MACHINE
- HKCU 或HKEY_CURRENT_USER
- HKU 或HKEY_USERS
- HKCC 或HKEY_CURRENT_CONFIG
- HKDD 或HKEY_DYN_DATA
- HKPD 或HKEY_PERFORMANCE_DATA
- SHCTX 或SHELL_CONTEXT

如果字串不能写入注册表则放置一个错误的标记。
字串的类型为 REG_SZ 对应 WriteRegStr, 或 REG_EXPAND_STR 对应 WriteRegExpandStr。
如果注册表键不存在则会自动创建。

例, 将程序信息写入注册表::

  Section -Post

    WriteUninstaller "$INSTDIR\uninst.exe"
    WriteRegStr HKLM "PRODUCT_DIR_REGKEY" "" "$INSTDIR\Test.exe"
    WriteRegStr PRODUCT_UNINST_ROOT_KEY "{PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
    WriteRegStr PRODUCT_UNINST_ROOT_KEY "{PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
    WriteRegStr PRODUCT_UNINST_ROOT_KEY "{PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\Test.exe"
    WriteRegStr PRODUCT_UNINST_ROOT_KEY "{PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
    WriteRegStr PRODUCT_UNINST_ROOT_KEY "{PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
    WriteRegStr PRODUCT_UNINST_ROOT_KEY "{PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"

  SectionEnd

ReadRegDWORD/ReadRegStr
--------------------------------------------

作用: 读取注册表信息

例, 在注册表中读取.net 版本::

  Function GetNetFrameworkVersion

    Push $1
    Push $0

    ReadRegDWORD $0 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full" "Install"
    ReadRegDWORD $1 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full" "Version"

    StrCmp $0 1 KnowNetFrameworkVersion +1

    ReadRegDWORD $0 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v3.5" "Install"
    ReadRegDWORD $1 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v3.5" "Version"

    StrCmp $0 1 KnowNetFrameworkVersion +1

    ReadRegDWORD $0 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v3.0\Setup" "InstallSuccess"
    ReadRegDWORD $1 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v3.0\Setup" "Version"

    StrCmp $0 1 KnowNetFrameworkVersion +1

    ReadRegDWORD $0 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v2.0.50727" "Install"
    ReadRegDWORD $1 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v2.0.50727" "Version"

    StrCmp $1 "" +1 +2
    StrCpy $1 "2.0.50727.832"
    StrCmp $0 1 KnowNetFrameworkVersion +1

    ReadRegDWORD $0 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v1.1.4322" "Install"
    ReadRegDWORD $1 HKLM "SOFTWARE\Microsoft\NET Framework Setup\NDP\v1.1.4322" "Version"

    StrCmp $1 "" +1 +2
    StrCpy $1 "1.1.4322.573"
    StrCmp $0 1 KnowNetFrameworkVersion +1

    ReadRegDWORD $0 HKLM "SOFTWARE\Microsoft\.NETFramework\policy\v1.0" "Install"
    ReadRegDWORD $1 HKLM "SOFTWARE\Microsoft\.NETFramework\policy\v1.0" "Version"

    StrCmp $1 "" +1 +2
    StrCpy $1 "1.0.3705.0"
    StrCmp $0 1 KnowNetFrameworkVersion +1
    StrCpy $1 "not .NetFramework"

    KnowNetFrameworkVersion:

    Pop $0
    Exch $1

  FunctionEnd

DeleteRegKey
----------------------

作用: 删除一个注册表键。如果指定了 /ifempty, 则该注册表键仅当它无子键时才会被删除(否则, 整个注册表键将被删除).
有效的根键值在后面的 WriteRegStr 列出。如果该键不能被删除(或如果它不存在)则会放置一个错误的标记。

例, 清除注册表信息::

  DeleteRegKey PRODUCT_UNINST_ROOT_KEY "{PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true

INI文件操作
=====================

ReadINIStr
----------------------

语法::

  ReadINIStr 用户变量(输出) INI文件 区段 项

作用: 读取INI文件。从 “INI文件” 的 “区段” 区段读取 “项” 的值并把该值输出到用户变量。
如果该项未找到时会放置一个错误标记且该用户变量被赋为空值。

例, 读取TimeZoneZh.ini文件中Field 1区段的State项, 将值输出到$0::

  ReadINIStr $0 "PLUGINSDIR\TimeZoneZh.ini" "Field 1" "State"


调用外部程序
======================

Exec
----------------------

作用: 执行一个指定的程序并且立即继续安装, 就是直接执行一个程序。

.. note::

  - 指定的文件必须存在于目标系统上, 而不是编译系统上
  - ``$OUTDIR`` 设置工作目录. 如果无法启动进程，则会设置错误标志
  - 如果命令可以有空格, 则应将其放在引号中以从参数中分隔它

例, 安装Microsoft.NET.exe, 程序不等待继续执行下个步骤::

  Exec '$INSTDIR\Microsoft.NET.exe'

.. _NSIS_ExecShell:

ExecShell
----------------------

启动 ShellExecute 执行.

语法::

  ExecShell action command [parameters] [SW_SHOWNORMAL | SW_SHOWMAXIMIZED | SW_SHOWMINIMIZED | SW_HIDE]

action有:

- open  ,  正常打开, 支持exe文件, bat脚本等能直接运行的文件
- print
- runas ,  以管理员权限打开文件(会弹出一个申请提权的弹窗)



若 action 为空表示使用默认动作

``command`` 表示执行命令, 内容为 **可执行文件全路径** .

parameters 为 ``command`` 的参数, 可为重定向符号如::

  2>&1 > log.txt

- SW_HIDE 隐藏执行命令打开的窗口

ExecWait
----------------------

执行一个指定的程序并且 **等待运行处理结束**

语法::

  ExecWait command [user_var(exit code)]

例, 静默安装并等待结束::

  ExecWait '"$INSTDIR\someprogram.exe /quiet /norestart"' $0

若执行产生错误, 可使用 IfErrors_ 来进行判断, 此时:

- 若指定了 ``[user_var(exit code)]`` , 则 ExecWait 会把变量设为返回代码.
  即 ``user_var = exit code``
- 若未指定 ``[user_var(exit code)]`` , 则 ExecWait 会放置一个错误标记.

.. note::

  若命令存在空格, 使用引号包裹

ReserveFile
----------------------

作用: 把文件保存在稍后使用的数据区块用于下面的调用。有时, 预先打包文件, 方便安装加速释放之用。

语法::

  ReserveFile [/nonfatal] [/r] [/x file|wildcard [...]] file [file...]

例::

  ReserveFile "TimeZoneZh.ini"

RegDLL
----------------------

作用: 载入指定的 DLL 并且调用 DllRegisterServer (或入口点名称, 当指定之后).
当产生一个错误的时候会置一个错误标记
(例如不能载入 DLL, 不能初始化 OLE, 不能找到入口点, 或者函数返回任何其它错误 ERROR_SUCCESS (=0)).

其实就是注册或加载你要的插件!

例::

  SetOutPath $INSTDIR
  RegDLL $INSTDIR\foo.dll

UnRegDLL
----------------------

作用: 注销DLL插件

例, 注销TIMProxy.dll插件::

  UnRegDLL $INSTDIR\foo.dll

!include
----------------------

作用: 包含头文件

例, 引用"MUI.nsh"头文件::

  !include "MUI.nsh"

!insertmacro
----------------------

作用: 插入宏

例, 通过宏插入欢迎页面::

  !insertmacro MUI_PAGE_WELCOME

字符串操作
======================

StrCpy
----------------------

作用: 复制字符串

语法::

  StrCpy user_var(destination) str [maxlen] [start_offset]

- str 可以包含其他变量
- maxlen 设置截取 str 的长度, 默认全部长度;
  为负数表示截取至此位置.

maxlen为负数表示截取至此位置, eg::

  StrCpy $1 "D:\Program Files\test\Example One\uninstall.exe"

  StrCpy $6 $1 -13
  MessageBox MB_OK "0 res $6"

结果就是::

  D:\Program Files\test\Example One\

StrCmp
----------------------

作用: 比较(不区分大小写)“字串1”和“字串2”, 如果两者相等, 跳转到“相同时跳转的标记”, 否则跳转到“不相同时跳转的标记”。

语法::

  StrCmp str1 str2 jump_if_equal [jump_if_not_equal]

StrLen
----------------------

作用：获取str的长度

例如::

  StrLen $0 "123456"  # $0 = 6

其他字符串操作, 需要先导入 WordFunc.nsh::

  !include WordFunc.nsh

WordFind
----------------------

WordFind, 在给定字符串中查找使用指定的分隔符分隔的字符串, 如从字符串 "first;second;third;forth" 中查找第二个字符串::

  ${WordFind} "first;second;third;forth" ";" +2 $R0   # $R0 = second

WordFind2X
----------------------

WordFind2X, 在给定字符串中查找使用指定的两个分隔符包围的字符串, 如
从字符串 ``<System>|<Guest>|<User>`` 中查找第三个字符串，也就是倒数第一个，即User::

  ${WordFind2X} "<System>|<Guest>|<User>" "<" ">" -1 $R0

WordFind3X
----------------------

WordFind3X, 与WordFind2X比较相似，用于在给定字符串中查找使用指定的两个分隔符包围且含有指定字符串的字符串

语法::

  ${WordFind3X} "[string]" "[delimiter1]" "[center]" "[delimiter2]" "[E][options]" $var

如查找 ``[/install=11], [/update=22], [/start=33]`` 中 ``/update`` 的整个内容::

  ${WordFind3X} "[/install=11], [/update=22], [/start=33]" "[" "/update" "]" +1 $0
  # $0 = "/update=22"

见: `nsis:WordFind3X <https://nsis.sourceforge.io/WordFind3X>`_

WordReplace
----------------------

WordReplace, 从字符串中替换或删除词语, 语法::

  # ${WordReplace} "[字符串]" "[词语1]" "[词语2]" "[E][选项]" $输出变量
  ${WordReplace} "[string]" "[word1]" "[word2]" "[E][options]" $var

选项这里的第几个下标从1开始, 例::

  Section
    ${WordReplace} "C:\io.sys C:\logo.sys C:\WINDOWS" "SYS" "bmp" "+2" $R0
    ; $R0="C:\io.sys C:\logo.bmp C:\WINDOWS"
  SectionEnd

见: `nsis:WordReplace <https://nsis.sourceforge.io/WordReplace>`_

WordAdd
----------------------

WordAdd, 从选项中指定的 字符串2 添加词语到 字符串1(如果不存在)，或删除词语(如果存在)。语法::

  ${WordAdd} "[字符串1]" "[分隔符]" "[E][选项]]" $输出变量

WordInsert
----------------------

WordInsert, 在字符串中插入词语。语法::

  ${WordInsert} "[字符串]" "[分隔符]" "[词语]" "[E][选项]]" $输出变量

StrFilter
----------------------

StrFilter, 转换字符串为大写或小写；设置符号过滤。语法::

  ${StrFilter} "[字符串]" "[选项]" "[符号1]" "[符号2]" $输出变量

VersionCompare
----------------------

VersionCompare, 用来比较版本号的大小。例如，比较1.1.0.1和1.1.1.0的大小。语法::

  ${VersionCompare} "[版本1]" "[版本2]" $输出变量

VersionConvert
----------------------

VersionConvert, 将带字母的版本转换为可用于比较的十进制数版本号。语法::

  ${VersionConvert} "[版本]" "[字符列表]" $输出变量

用法示例::

  ${VersionConvert} "9.0c" "" $R0  # $R0 = 9.0.03 .这样转换后可以用于和别的版本如9.0a比较。

数学计算
======================

IntOp
----------------------

10减去2, eg::

  IntOp $0 10 - 2

效果是计算 ``10-2`` , 将结果8赋值给 ``$0``.

文件目录遍历
======================

FindFirst/FindNext/FindClose
--------------------------------------------

这三个一般一起使用

FindFirst语法::

  FindFirst user_var(handle output) user_var(filename output) filespec

- 第一个 handle output 是搜索的文件句柄
- 第二个 filename output 是找到的文件名(不包含前缀目录)
- filespec 是搜索的路径描述, 支持简单通配符

eg::

  FindFirst $0 $1 $INSTDIR\*.txt
  loop:
    StrCmp $1 "" done
    DetailPrint $1
    FindNext $0 $1
    Goto loop
  done:
  FindClose $0

逻辑操作
======================

IfAbort
----------------------

如果调用abort，它将“返回”为true。

语法::

  IfAbort label_to_goto_if_abort [label_to_goto_if_no_abort]

如果用户选择对无法创建（或覆盖）的文件进行中止，或者用户手动中止，则会发生这种情况。只能从instfiles 页面的leave函数调用此函数::

  Function instfilesLeave
    IfAbort 0 +2
      MessageBox MB_OK "user aborted"
  FunctionEnd

.. _NSIS_IfErrors:

IfErrors
----------------------

错误时跳转

语法::

  jumpto_iferror [jumpto_ifnoerror]

检测并清除错误标记, 如果设了错误标记, 则跳转到“错误时跳转的标记”, 否则跳转到“没有错误时跳转的标记”。

可使用 ClearErrors_ 在之前清除其他地方的错误标记

IfFileExists
----------------------

语法::

  IfFileExists file_to_check_for jump_if_present [jump_otherwise]

检测 ``file_to_check_for`` 是否存在(可以用通配符, 或目录)

- 当文件存在时跳转到 ``file_to_check_for``
- 否则跳转到 ``jump_otherwise`` .

例1, 官网例子::

  IfFileExists $WINDIR\notepad.exe 0 +2
  MessageBox MB_OK "notepad is installed"

.. _goto_example:

例2::

  IfFileExists $WINDIR\notepad.exe fileExists fileNotExists

  fileExists:
    # do something
    Goto done
  fileNotExists:
    Abort
  done:

Goto
----------------------

作用: 跳转到指定标记。

nsi脚本常常使用相对跳转表示条件分枝

语法::

  Goto label_to_jump_to | +offset| -offset| user_var(target)

- ``+offset``  表示从当前位置往前跳转 ``offset`` 条语句,
- ``-offset``  表示从当前位置往后跳转 ``offset`` 条语句.
- ``user_var`` 表示跳转到指定变量标记位置.

例, 按数字跳转::

  Goto +4 ; 跳转以下4条语句
  Goto -3 ; 跳转到前3条语句

例, 按标记跳转: goto_example_

ClearErrors
======================

当程序运行产生错误时, 可以使用 :ref:`NSIS_IfErrors` 判断, 返回 true/false , 表示存在错误.

ClearErrors 可以清除当前已有的错误标记

堆栈操作
======================

其实 也属于逻辑操作

NSIS 脚本没有 reture 这种返回值, 只能使用 栈 的方式在函数之前传递参数(或者全局变量)

- Pop_
- Push_
- Exch_

Pop
----------------------

从栈顶取出一个参数.

如将栈顶元素取出, 赋值给 ``$0`` ::

  Pop $0

Push
----------------------

向栈种压入参数.

如压入 ``"change"`` ::

  Push "change"

Exch
----------------------

语法::

  Exch [user_var|stack_index]

默认交换栈顶的两个元素, 如::

  Push 1
  Push 2
  Exch
  Pop $0 # = 1

若指定了 ``[user_var|stack_index]`` :

- 若指定了用户变量, 使用用户变量与栈顶元素交换

  如::

    Push 2
    Exch $0 # = 2

- 若指定了整型(int), 即栈的索引, 使用索引位置的元素与栈顶元素交换

  注意, 索引从0开始, 栈顶索引为0

  如::

    Push 1
    Push 2
    Push 3
    Exch 2
    Pop $0 # = 1

如果需要交换的元素个数不足, 如索引越界等, 报错

获取命令行参数
======================

官网地址: `GetOptions <https://nsis.sourceforge.io/GetOptions>`_

- GetParameters
- GetOptions

``GetParameters`` 语法::

  ${GetParameters} $var

例::

  ${GetParameters} $R0 ; $R0="[parameters]"

``GetOptions`` 语法::

  ${GetOptions} "[Parameters]" "[Option]" $var
  "[Parameters]"     ; command line parameters
                     ;
  "[Option]"         ; option name
                     ;
  $var               ; Result: option string

例::

  !include "FileFunc.nsh"
  !insertmacro GetOptions
  !insertmacro GetParameters

  Section
    ${GetOptions} "-INSTDIR=C:\Program Files\Common Files -SILENT=yes" "-INSTDIR="  $R0
    ;$R0=C:\Program Files\Common Files
  SectionEnd

不能写到一起, 比如以下这条语句是错误的::

  ${GetOptions} ${GetParameters} "-INSTDIR="  $R0

例2, 命令行为::

  foo.exe /S /USERNAME=Bar /D=C:\Program Files\Foo

脚本内容为::

  !include FileFunc.nsh
  !insertmacro GetParameters
  !insertmacro GetOptions

  Function .onInit
    ${GetParameters} $R0
    ClearErrors
    ${GetOptions} $R0 /USERNAME= $0
  FunctionEnd

效果: 将 ``/USERNAME=`` 后的值赋值给 ``$0`` , 这样就支持了自定义命令行参数.

关于 `/S` (静默安装参数)的判断
============================================

静默安装系统有提供默认的判断, 不需要手动去获取命令行了::

  Function .onInit
    IfSilent jumpToSlient jumpNotSilent
    jumpToSlient:
      ; 静默安装的操作
      Goto done
    jumpNotSilent:
      ; 非静默安装操作
      Goto done
    done:
  FunctionEnd

也可以直接定义全局变量吧

静默安装实现
======================

- ``/S`` 参数 执行的时候使用, 如 ``xxx.exe /S``
- SetSilent_
- SilentInstall_ and SilentUninstall_

SetSilent
----------------------

脚本里设置::

  SetSilent silent | normal

只能在 ``.onInit.`` 被使用

SilentInstall
----------------------

用法::

  SilentInstall normal|silent|silentlog

SilentUninstall
----------------------

用法::

  SilentUnInstall normal|silent

判断是否是静默安装
----------------------

使用 ``IfSilent`` ::

  IfSilent +2
    ExecWait '"$INSTDIR\nonsilentprogram.exe"'

这里没懂 ``+2`` 是什么意思
