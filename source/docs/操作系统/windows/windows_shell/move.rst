==========
move
==========

移动文件并重命名文件和目录。

要移动至少一个文件::

  MOVE [/Y | /-Y] [drive:][path]filename1[,...] destination

要重命名一个目录::

  MOVE [/Y | /-Y] [drive:][path]dirname1 dirname2

    [drive:][path]filename1 指定你想移动的文件位置和名称。
    destination             指定文件的新位置。目标可包含一个驱动器号
                            和冒号、一个目录名或组合。如果只移动一个文件
                            并在移动时将其重命名，你还可以包括文件名。
    [drive:][path]dirname1  指定要重命名的目录。
    dirname2                指定目录的新名称。

    /Y                      取消确认覆盖一个现有目标文件的提示。
    /-Y                     对确认覆盖一个现有目标文件发出提示。

命令行开关 /Y 可以出现在 COPYCMD 环境变量中。
这可以用命令行上的 /-Y 替代。
默认值是，除非 MOVE 命令是从一个批脚本内执行的，覆盖时都发出提示。


