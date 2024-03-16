===============================
open
===============================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


打开文件等

在MacOS上用法
===============================

说明
  从命令行打开文件.
  默认情况下, 会使用该文件对应设置的默认打开方式打开;
  如果是格式化的URL, 将打开URL

用法::

  open [-e] [-t] [-f] [-W] [-R] [-n] [-g] [-h] [-s <partial SDK name>][-b <bundle identifier>] [-a <application>] [-u URL] [filenames] [--args arguments]

选项::

  -a                    使用指定的程序打开
  --arch ARCH           使用给定的cpu架构类型和子类型打开
  -b                    使用指定的 应用程序标识符 打开
  -e                    使用文本编辑器打开
  -t                    使用默认文本编辑器打开
  -f                    从标准输入读取输入并使用 TextEdit 打开
  -F  --fresh           Launches the app fresh, that is, without restoring windows. Saved persistent state is lost, excluding Untitled documents.
  -R, --reveal          Selects in the Finder instead of opening.
  -W, --wait-apps       Blocks until the used applications are closed (even if they were already running).
      --args            All remaining arguments are passed in argv to the application's main() function instead of opened.
  -n, --new             Open a new instance of the application even if one is already running.
  -j, --hide            Launches the app hidden.
  -g, --background      Does not bring the application to the foreground.
  -h, --header          Searches header file locations for headers matching the given filenames, and opens them.
  -s                    For -h, the SDK to use; if supplied, only SDKs whose names contain the argument value are searched.
                        Otherwise the highest versioned SDK in each platform is used.
  -u, --url URL         Open this URL, even if it matches exactly a filepath
  -i, --stdin  PATH     Launches the application with stdin connected to PATH; defaults to /dev/null
  -o, --stdout PATH     Launches the application with /dev/stdout connected to PATH;
      --stderr PATH     Launches the application with /dev/stderr connected to PATH to
      --env    VAR      Add an enviroment variable to the launched process, where VAR is formatted AAA=foo or just AAA for a null string value.




