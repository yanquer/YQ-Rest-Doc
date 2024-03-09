==============
where
==============

显示符合搜索模式的文件位置。在默认情况下，搜索是在当前目录和 PATH 环境变量指定的路径中执行的

语法::

  WHERE [/R dir] [/Q] [/F] [/T] pattern...

参数列表::

  /R       从指定目录开始，递归性搜索并显示符合指定模式的文件。

  /Q       只返回退出代码，不显示匹配文件列表。(安静模式)

            匹配文件。(安静模式)

  /F       显示所有相配文件并用双引号括上。

  /T       显示所有相配文件的文件的文件。

  pattern  指定要匹配的文件的搜索模式。通配符 * 和 ? 可以用在模式中。
            也可以指定 "$env:pattern" 和 "path:pattern" 格式; 其中
            "env" 是环境变量，搜索是在 "env" 变量的指定的路径中执行的。
            这些格式不应该跟 /R 一起使用。此搜索也可以用将 PATHEXT 变
            量扩展名附加于此模式的方式完成。

    /?      显示此帮助消息。

注意:
如果搜索成功，此工具返回错误级别 0;
如果不成功，返回 1;
如果失败或发生错误，返回 2。

示例::

  WHERE /?
  WHERE myfilename1 myfile????.*
  WHERE $windir:*.*
  WHERE /R c:\windows *.exe *.dll *.bat
  WHERE /Q ??.???
  WHERE "c:\windows;c:\windows\system32:*.dll"
  WHERE /F /T *.dll
