======================
innosetup构建包
======================

:github地址::
    `jrsoftware/issrc <https://github.com/jrsoftware/issrc>`_

innosetup 是适用于windows的一个免费windows安装程序制作软件.

对于打好的包, 支持不关闭应用程序的静默安装等操作.

配置脚本
======================

innosetup 支持的配置文件为 iss 后缀的文件.

看到一个比较新的中文的配置教程: `Inno Setup打包程序 <https://elmagnifico.tech/2020/08/18/InnoSetup-python/>`_

截取了部分: innosetup_code_example_

支持的配置::

    [Setup] section
    [Setup] section directives
    [Types] section
    [Components] section
    [Tasks] section
    [Dirs] section
    [Files] section
    [Icons] section
    [INI] section
    [InstallDelete] section
    [Languages] section
    [Messages] section
    [CustomMessages] section
    [LangOptions] section
    [Registry] section
    [Run] section
    [UninstallDelete] section
    [UninstallRun] section

详情见官网: `setup script sections <https://jrsoftware.org/ishelp/index.php?topic=consts>`

自定义配置代码
======================

若需要加代码之类, 需要增加 ``[code]`` 小节, 在其中编码, 支持设置自己的参数.

如, vscode自定义了一个 ``/update`` 参数, 使用时候传入标志文件路径::

    VSCodeUserSetup-x64-1.76.0.exe /verysilent /update=VSCodeUserSetup-x64-1.76.0.flag /nocloseapplications /mergetasks=runcode,!desktopicon,!quicklaunchicon

在代码中获取 ``/update`` 的参数, 获取不到则为 false ::

    '{param:update|false}'

code部分编码语言参考 ``Pascal`` (上古语言)

安装包默认支持的参数
======================

:官网地址::
    `Setup Command Line Parameters <https://jrsoftware.org/ishelp/index.php?topic=scriptintro>`_

对于构建好的包, 启动时支持参数::

    /silent             静默安装，但如果又报错，还是会提示，并且有进度条
    /verysilent         强制静默安装，不管是否报错，都不会有任何提示(注意：如果需要重启电脑，它会不提示而直接重启)
    /suppressmsgboxes   由 suppress(抑制，镇压) 和 msgboxes(消息框)，组成，表示不提示消息框
    /norestart          结合 /verysilent 使用，避免无提示直接重启

    /HELP, /?           查看帮助文档
    /SP-                隐藏安装提示信息(setup prompt)
    /ALLUSERS           管理员身份安装
    /CURRENTUSER        非管理员身份安装
    /LOG="filename"     创建安装日志文件. 可不带参数, 则在用户的 Temp 目录下创建日志文件, debug的时候用处大
    /TASKS="comma separated list of task names"
                        执行定义的task
    /MERGETASKS="comma separated list of task names"
                        貌似于上一个一样

    ... 其他见官网



附件
======================

.. _innosetup_code_example:

innosetup 配置脚本例

.. literalinclude:: ../../../../resources/code/innosetup_config.iss

一些有点用的文档, 主要是还没来得及看, 先记录:

- python项目构建: `Python_Project_nuitka_inno_setup <https://www.cnblogs.com/chrisfang/p/17027553.html>`_
- `inno setup技巧篇 <https://blog.csdn.net/fuhanghang/article/details/128410009?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EAD_ESQUERY%7Eyljh-1-128410009-blog-108202454.pc_relevant_3mothn_strategy_and_data_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EAD_ESQUERY%7Eyljh-1-128410009-blog-108202454.pc_relevant_3mothn_strategy_and_data_recovery>`_
- `软件exe打包压缩常用静默安装参数 <https://blog.csdn.net/qq_37550440/article/details/86478287?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-86478287-blog-121375273.pc_relevant_3mothn_strategy_and_data_recovery&spm=1001.2101.3001.4242.1&utm_relevant_index=3>`_
- `常用软件的静默安装参数，双击自动安装 <https://cloud.tencent.com/developer/article/1538138>`_
- `常用软件打包类型及静默安装参数 <https://cloud.tencent.com/developer/article/1537821>`_

