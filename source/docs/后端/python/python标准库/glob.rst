================
glob
================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


glob --- Unix 风格路径名模式扩展

官网: `https://docs.python.org/zh-cn/3/library/glob.html`

glob 模块会按照 Unix shell 所使用的规则找出所有匹配特定模式的路径名称，但返回结果的顺序是不确定的。
波浪号扩展不会生效，但*, ? 以及用 [] 表示的字符范围将被正确地匹配。
这是通过配合使用 os.scandir() 和 fnmatch.fnmatch() 函数来实现的，而不是通过实际发起调用子 shell。

.. function:: glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

  如果 root_dir 不为 None，则它应当是指明要搜索的根目录的 path-like object。
  它用在 glob() 上与在调用它之前改变当前目录有相同的效果。 如果 pathname 为相对路径，结果将包含相对于 root_dir 的路径。

  本函数带有 dir_fd 参数，支持 基于目录描述符的相对路径。

  如果 recursive 为真值，则模式 "**" 将匹配目录中的任何文件以及零个或多个目录、子目录和符号链接。
  如果模式加了一个 os.sep 或 os.altsep 则将不匹配文件。

  If include_hidden is true, "**" pattern will match hidden directories.

  引发一个 审计事件 glob.glob 附带参数 pathname, recursive。

  引发一个 审计事件 glob.glob/2，附带参数 pathname, recursive, root_dir, dir_fd。

  备注 在一个较大的目录树中使用 "**" 模式可能会消耗非常多的时间。
  在 3.5 版更改: 支持使用 "**" 的递归 glob。

  在 3.10 版更改: 添加了 root_dir 和 dir_fd 形参。

  在 3.11 版更改: Added the include_hidden parameter.

.. function:: glob.iglob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

  返回一个 iterator，它会产生与 glob() 相同的结果，但不会实际地同时保存它们。

  引发一个 审计事件 glob.glob 附带参数 pathname, recursive。

  引发一个 审计事件 glob.glob/2，附带参数 pathname, recursive, root_dir, dir_fd。

  在 3.5 版更改: 支持使用 "**" 的递归 glob。

  在 3.10 版更改: 添加了 root_dir 和 dir_fd 形参。

  在 3.11 版更改: Added the include_hidden parameter.

.. function:: glob.escape(pathname)

  转义所有特殊字符 ('?', '*' 和 '[')。 这适用于当你想要匹配可能带有特殊字符的任意字符串字面值的情况。
  在 drive/UNC 共享点中的特殊字符不会被转义，
  例如在 Windows 上 escape('//?/c:/Quo vadis?.txt') 将返回 '//?/c:/Quo vadis[?].txt'。

3.4 新版功能.


