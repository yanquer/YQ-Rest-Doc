=======================
windows shell
=======================

有一篇总结还可以的: `Windows 批处理命令教程（不追求看完，只要求看懂） <https://hellokandy.blog.csdn.net/article/details/78065145?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-78065145-blog-122614610.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-78065145-blog-122614610.pc_relevant_default>`_

变量
=======================

与linux使用 ``$`` 不同, windows 使用双 ``%`` 引用来表示变量, 如a变量::

  %a%

批处理有一个变量延迟机制, 可以通过设置 变量延迟拓展(延迟环境变量拓展) 来处理::

  setlocal enabledelayedexpansion

如::

  @echo off
  set a=4
  set a=5&echo %a%
  pause

的结果是 4

而::

  @echo off
  setlocal enabledelayedexpansion
  set a=4
  set a=5&echo !a!
  pause

的结果是 5

.. note::

  开启了变量延迟拓展可以按照正常的编码流畅来编码, 不过注意变量定义为使用 **两个 ``!`` 包裹**

另外,
在 **cmd窗口** 中，for之后的形式变量I必须使用单百分号引用，即 ``%I`` ;
而在 **批处理文件** 中，引用形式变量I必须使用双百分号，即 ``%%``

echo
=======================

打印变量::

  echo %APPDATA%

或者使用 ``@echo`` , 区别是 加了 @ 不会显示这条命了本身

几种echo::

  echo off    接下来的命令(不包括当前命令),只打印结果,不打印命令.
  @ECHO OFF   接下来的命令(包括本命令)，只打印执行结果，不打印命令本身
  ECHO ON     接下来的命令(不包括本命令)，执行命令前会先把命令打印出来

在批处理文件中，如果命令前加@，表示这条命令不打印出来，只把结果打印出来，即@是关闭命令本身的回显


注释
=======================

``::`` 在批处理中表示注释某一行::

  :: 这是注释信息

也可以使用 rem, 区别是 rem 支持回显::

  rem 这是支持回显的注释信息

数值范围
=======================

类似于 Python 的 range 吧, 使用::

  /L  (start,step,end)  step=<end

也叫开关(此处大小写不敏感), 例::

  setlocal enabledelayedexpansion

  for /l %%1 in (1, 1, 10) do(
    set "k=%%1"
    echo !k!
  )

获取命令行参数
=======================

约定::

  获得第i个参数：%i，0<=i && i <=参数最大数量

条件判断
=======================

if条件判断, 变量 l 是否已经赋值::

  if defined l(
    echo "已赋值l"
  )else(
    echo "未赋值l"
  )

支持 not::

  if not defined xxx

与 或 非的实现:
-----------------------

与(and)::

  if 1==1 if 2==2 echo Ok

  :: if 1==1 (if 2==2 echo Ok)

或(or), 这里只谈最便捷的 goto::

  if "%1"=="" goto printHelp
  if "%2"=="" goto printHelp

  :printHelp
    @echo This is a help message, please refere to ...

非(not)::

  if not 1==1 echo OK


循环
=======================

for循环, 语法::

  for 循环条件 do (
    内容
  )

在cmd窗口中::

  for %I in (command1) do command2

在批处理文件中::

  for %%I in (command1) do command2

**高级使用** , 寻找指定目录下的文件(不寻找其下子目录), 但是排除指定内容::

  @echo off

  set home=C:\Users
  set exclude_list="_ video music image img.png ttt.py"

  for /f "delims=*" %%i in ('dir /b %home% ^| findstr /v /i /x %exclude_list%') do (
    echo %home%\"%%i"
    rem rd /s %home%\"%%i"
  )

简单说明, for 中使用 单引号 包裹表示需要执行的指令, 这时管道需要加 ``^`` 转义

:doc:`/docs/操作系统/windows/windows_shell/dir` : /b 表示值列出目录/文件 字符串; 可加 /s 递归查找下面所有子目录

:doc:`/docs/操作系统/windows/windows_shell/findstr` : /v 反向匹配; /i 忽略大小写; /x 全词匹配

连接符号
=======================

连接符号有: ``; & && | ||`` ::

  ;   顺序执行多条命令，而不管命令是否执行成功.
  &   与上等同. bash中某条命令后面跟上 &, 用来将命令至于后台执行，避免其占用命令行
  &&  顺序执行多条命令，当碰到执行出错的命令后将不执行后面的命令
  |   管道命令
  ||  顺序执行多条命令，当碰到执行正确的命令后将不执行后面的命令

管道
=======================

与 linux 下 ``|`` 表示管道一般情况下一致,

但是在 for 循环中需要使用 ``^`` 进行 **转义** , 即 ``^|`` 表示管道

有一种说法解释见: `是不是只有for的('')中的特殊字符前必须要用^对其转义  我看过^不是在要输出特殊字符才用^ <http://bbs.bathome.net/viewthread.php?tid=1290&page=2#pid6306>`_

大概意思是, 在for循环中, 如果不进行转义, 如::

  for /f "delims=*" %%i in ('dir /b %home% | findstr /v /i /x %exclude_list%')

会把前面的所有, 即::

  for /f "delims=*" %%i in ('dir /b %home%

当成一个指令, 但你又没有这个指令, 所以需要转义.

程序返回码
=======================

变量errorlevel::

  %errorlevel%

可以通过其值判断上一个指令是否正常执行(正常为0).

相当于 linux 的 ``$?``

判断是文件/目录
=======================

判断是文件/目录::

  if exist "%%i" (
      if exist "%%i\*" (
          echo "%%i is a folder"
      ) else (
          echo "%%i is a file"
      )
  )

查看帮助信息

查看帮助信息::

  command /?

路径拼接引号问题
=======================

引号介绍:
  bat脚本中单引号(')是无效的，必须使用双引号(")来定义字符串。
  在bat脚本中，双引号和空格都需要进行转义处理

定义变量时, 单引号双引号包裹的字符串是不一样的, 不过在bat脚本内部定义时候, 可以不加任何引号表示一个变量

一般单引号只用于 for 循环的时候处理命令;

双引号的话, 举个例子, 如果bat脚本需要传递包含空格的路径参数, 那么为了避免空格把参数分隔, 比如本来是路径是参数1::

  set app_path=%1

但是由于存在空格, 比如: ``C:/user/ho me`` 你又没有在命令行调用时加引号::

  xxx.bat C:/user/ho me

那么最终获取的参数就是(不带引号)::

  C:/user/ho

而当使用::

  xxx.bat "C:/user/ho me"

得到的结果又为(带引号)::

  "C:/user/ho me"

**不带引号可能会引起路径丢失的问题, 带引号可能会引起后面参数拼接时候路径不可用问题**

带引号时出现问题, 可以从两个方案处理:

**方案1: 后面定义的其他部分的路径也加引号** , 如::

  rem 接受参数的时候就不要加引号了
  set app_path=%1

  rem 定义一个带一个引号的路径
  set tmp_path="_"

  set new_path=%app_path%\%tmp_path%

还是以上面的路径为例, 传入的路径为 ``"C:/user/ho me"`` , 最后的拼接结果为::

  "C:/user/ho me"/"_"

这个时候虽存在引号, 但是各部分都是独立的, 可以被系统识别此路径

至于是不是多层独立的引号也可以识别, 感兴趣的可以自己试试::

  ""C:/user/ho me""/""_""

**方案二: 去掉所有的引号** , 这个可能会有其他的问题, 如文件如果包含引号怎么处理?
但是一般人不会这个起名.

去除变量的引号::

  set var=%var:"=%

如::

  set p="C:/user/ho me"/"_"
  echo %p%
  set p=%p:"=%
  echo %p%

输出::

  "C:/user/ho me"/"_"
  C:/user/ho me/_



对于Windows下路径而言

批处理程序删除自己
=======================

一般来说直接删除就行::

  :: 一些其他代码
  del %0

但是有时候指令会更新所在路径, 比如::

  move . tmp\

这时候可以利用管道::

  del %0 | move . tmp\

输出重定向
=======================

将错误输出, 标准输出重定向到 1.txt

注意顺序不能错

输出重定向::

  t.bat >1.txt 2>&1

跨盘移动的坑
=======================

使用 :doc:`/docs/操作系统/windows/windows_shell/move` 跨盘移动文件夹时, 会报错 **拒绝访问**

管理员权限也无法.

目前所知的解决方案只有先复制过去然后删除::

  xcopy /H /E /Y  原有的文件夹 移动到的文件夹

  rd /s /q 原有的文件夹

获取绝对路径文件名
=======================

如果路径不是传入的参数, 那么需要使用类似函数的方式::

  @echo off

  echo 盘符: %~dp0
  echo 当前脚本路径: %~dp0

  echo 参数1盘符: %~dp1
  echo 参数1当前脚本路径: %~dp1
  echo 参数1文件名称: %~n1

  set p1=C:\Users\tt\1.txt
  echo %p1%
  call :get_base_name %p1%

  goto :eof

  :get_base_name
    set file_path=%~dp1
    echo %file_path%
    rem 获取到文件名称
    set file_name=%~n1
    echo %file_name%
    rem 获取到文件后缀
    set suffix=%~x1
    echo %suffix%
  goto :eof

获取用户名
=======================

code::

  %username%

if与循环
=======================

if语句不能包含循环语句, 不过可以使用goto处理::

  @echo off

  set var=hello
  if "%var%"=="hello" goto loop
  goto end

  :loop
  echo doing something...
  goto loop_end

  :loop_end
  echo done
  goto end

  :end

指令
=======================

.. toctree::
  :glob:

  ./windows_shell/*

