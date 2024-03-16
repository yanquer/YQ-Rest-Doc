===========================
debian/ubuntu字体说明
===========================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 教程
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


Ubuntu字体及配置说明: `https://wiki.ubuntu.org.cn/字体#.E9.85.8D.E7.BD.AE.fonts.conf`

参考: `https://catcat.cc/post/2020-10-31/`

Linux 桌面程序使用字体的方式，受 fontconfig 的影响和控制。

一个字体文件，可以提供多个字体族名 (family)。
比如 Arch Linux 用户在 安装 wqy-microhei 后，
系统端增加了 wqy-microhei.ttc 这个 字体文件，
分别提供「WenQuanYi Micro Hei」「文泉驛微米黑」,「文泉驿微米黑」 三个字体族名，
它们是一个意思。可以运行 fontconfig 提供的命令行工具 fc-list
去查看系统上 已安装的字体已经它们对应的字体族名。

至于 sans-serif，serif，monospace，则是三个通用字体族名 (generic family)，
它们不是真实存在的字体，而是分别指示程序去使用无衬线、衬线、等宽字体。
那么桌面程序又是如何知道具体使用哪些字体呢？
它只需要去查询 fontconfig 就行了。
由于它们必定要经过 fontconfig 的查询流程后才能使用字体，
所以我们可以通过 fontconfig 的配置去精准控制程序使用的字体。

配置文件流向
===========================

fontconfig 主要读取

* ``/etc/fonts/fonts.conf``
* ``/etc/fonts/conf.d/*.conf``
* ``~/.config/fontconfig/fonts.conf``
* ``~/config/fontconfig/conf.d/*.conf``
* 至于那些历史遗留的目录位置 ``~/.fonts.conf.d/*.conf`` 和 ``~/.fonts.conf`` ， 由于不遵守 XDG 规范，我们就不要再使用它们了。

fontconfig 并非固定读取这些位置，它首先读取 /etc/fonts/fonts.conf，该文件中有句::

  <include ignore_missing="yes">conf.d</include>

表示将 `/etc/fonts/conf.d/` 目录中的文件纳入读取中,
在这个目录中的配置文件，按照文件名前的数字的顺序进行读取。
而当读取到50-user.conf的时候，其中的语句::

  <include ignore_missing="yes" prefix="xdg">fontconfig/conf.d</include>
  <include ignore_missing="yes" prefix="xdg">fontconfig/fonts.conf</include>
  <include ignore_missing="yes" deprecated="yes">~/.fonts.conf.d</include>
  <include ignore_missing="yes" deprecated="yes">~/.fonts.conf</include>

指示 fontconfig 开始读取用户家目录下的配置文件。
语句中的属性值prefix="xdg"，代表 XDG_CONFIG_HOME 目录， 默认是我们熟悉的~/.config/目录。

字体文件位置
===========================

fontconfig 的很多配置文件是先从/etc/fonts/fonts.conf引入的。
其实，fontconfig 获取字体文件的位置，也是该文件定义的。
你会发现 该文件的开头就在指定字体目录::

  <dir>/usr/share/fonts</dir>
  <dir>/usr/local/share/fonts</dir>
  <dir prefix="xdg">fonts</dir>
  <!-- the following element will be removed in the future -->
  <dir>~/.fonts</dir>

当我们安装字体软件包时，软件包把字体文件放在了/usr/share/fonts/目录下

配置自己的规则
===========================

比如我已经提前安装好了 `inconsolata` 字体,
然后在家目录下设置了配置文件,
新建文件 `~/.config/fontconfig/fonts.conf`::

  <?xml version="1.0"?>
  <!DOCTYPE fontconfig SYSTEM "/etc/fonts/conf.d/fonts.dtd">
  <fontconfig>
  <match target="pattern">
    <test qual="any" name="family">
      <string>monospace</string>
    </test>
    <edit name="family" mode="prepend" binding="strong">
      <string>inconsolata</string>
      <string>Iosevka Custom</string>
      <string>Noto Sans Mono CJK SC</string>
      <string>Blobmoji</string>
      <string>Symbols Nerd Font</string>
    </edit>
  </match>
  </fontconfig>

这个时候查询等宽字体的结果就是我设置的这个::

  $ fc-match "monospace"
  Inconsolata.otf: "Inconsolata" "Medium"

解释一下这里配置含义

fontconfig
  表示是一个字体查询配置
match
  匹配规则, ``<match target="pattern">``，被操作对象是 font pattern;

  如果是 ``<match target="font">``, 则是对单个字体的操作
test
  定义匹配规则, 可选的测试条件。只有当满足测试条件的时候，才执行<edit>;

  这里表示匹配 `monospace` 家族
edit
  表示匹配的字体结果

  此处完整含义::

    在这里，test 语句针对了 font pattern 中的 monospace。
    也就是说， 接下来的 edit 语句就在 font pattern 的 monospace 这个位置上进行操作。
    mode="prepend"的意思是在 monospace 前添加四个字体：
    等宽字体 inconsolata，
    英文等宽字体 Iosevka Custom，
    中文字体 Noto Sans Mono CJK SC，
    以及通用字体族名 emoji。
    binding="strong"，是强绑定的意思， 它会影响 font pattern 的排序结果，

  - name="family" 表明被操作对象是是 font pattern 中的 family。
  - mode="prepend" 表示在结果之前插入;
    如果是 mode="assign" , 表示对test中的String修改替换.

    如向 fc-match 传入的 font pattern 是可以有多个字体的。 现在我们要运行::

      FC_DEBUG=4 fc-match 'cantarell, WenQuanYi Micro Hei'

    经过这段配置会变成什么呢::

      <match target="pattern">
        <test name="family">
          <string>Cantarell</string>
        </test>
        <edit name="family" mode="assign" binding="strong">
          <string>Noto Sans</string>
        </edit>
      </match>

    这里的mode="assign"，表示 将 font pattern 中的 Cantarell 修改成 Noto Sans。
    没有对 WenQuanYi Micro Hei 的操作，所以结果是::

      family: "Noto Sans"(s) "WenQuanYi Micro Hei"(s)

  - binding="strong" 表示强绑定

  下面的 String 的内容的是结果列表, 支持多个

  先后顺序就是设置的优先使用的字体顺序。
  最先尝试使用 `inconsolata` 字体作为英文等宽字体,
  然后才是 `Iosevka` ， 中日韩字体使用 `Noto Sans Mono CJK SC`，
  剩下的 `emoji` 和特殊符号 优先使用 `Blobmoji` 和 `Nerd font`。

完整属性说明可参考: `https://www.cnblogs.com/jacker1979/p/4695169.html`

.. note::

  旧版是使用的alias::

    <match>...<test>...<edit name="family" mode="prepend">...

    等价于

    <alias>...<family>...<prefer>...

