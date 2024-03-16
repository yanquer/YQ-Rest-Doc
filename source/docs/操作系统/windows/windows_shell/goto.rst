==============
goto
==============


.. post:: 2023-02-20 22:06:49
  :tags: windows, windows_shell
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


将 cmd.exe 定向到批处理程序中带标签的行。

GOTO label

  label   指定批处理程序中用作标签的文字字符串。

**标签必须单独一行，并且以冒号打头。**

例::

  if %1 == 1 (
    goto do1
  ) else (
    goto done
  )

  :do1
    echo 1
  :done
    echo done

实际使用::

  if %1 == 1 (
    goto do1
  ) else (
    goto done
  )

也可以, 不知道为啥.

如果命令扩展被启用，GOTO 会如下改变:

GOTO 命令现在接受目标标签 :EOF，这个标签将控制转移到当前批脚本文件的结尾。
不定义就退出批脚本文件，这是一个容易的办法。
有关能使该功能有用的 CALL 命令的扩展描述，请键入CALL /?。

看到有种说法是::

  rem  goto:eof 相当于函数的} 结尾标记，返回到调用者位置, 如果没有调用者直接就到末尾结束了
  rem  exit /b 0  结束当前cmd，返回exitCode 0



