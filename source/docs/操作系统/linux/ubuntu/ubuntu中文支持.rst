===========================
ubuntu中文支持
===========================


.. post:: 2023-02-23 00:00:02
  :tags: linux, ubuntu
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


方式一: 图形化设置
===========================

在 Settings 下找到 Region&Language, 进入后点击 Manage Install Languages, 在
其中选择汉语即可.
这里若缺少包后会提示缺少相关语言包, 输入密码下载即可.

方式二: 命令行设置
===========================

安装中文包::

  apt update
  apt install language-pack-zh-hans

设置区域为中文::

  localectl set-locale LANG=zh_CN.utf8

然后重启::

  reboot

可以查看当前设置的区域语言::

  locale

其他指令
===========================

查看语言支持的字体::

  check-language-support

然后都可以装上(如果没装, 可能会存在乱码问题), 一般应该是这些::

  sudo apt install fonts-droid-fallback ttf-wqy-zenhei ttf-wqy-microhei fonts-arphic-ukai fonts-arphic-uming

安装等宽字体, 有一个比较好的等宽字体叫Inconsolata, 在ubuntu中可安装::

  sudo apt install fonts-inconsolata

若不是这名, 可以搜索一下::

  apt search inconsolata

设置为指定的字体
===========================

Ubuntu字体及配置说明: `https://wiki.ubuntu.org.cn/字体#.E9.85.8D.E7.BD.AE.fonts.conf`

.. 如设置上面的 inconsolata 字体, 编辑 `/etc/fonts/fonts.conf`:\:
  <fontconfig>
    <match target="pattern">
      <test qual="any" name="family">
        <string>monospace</string>
      </test>
      <edit name="family" mode="prepend" binding="strong">
        <string>inconsolata</string>
      </edit>
    </match>
  </fontconfig>

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
    </edit>
  </match>
  <match target="pattern">
    <test qual="any" name="family">
      <string>sans-serif</string>
    </test>
    <edit name="family" mode="prepend" binding="strong">
      <string>inconsolata</string>
    </edit>
  </match>
  </fontconfig>

表示把 `monospace` 等宽字体和,
`sans-serif` 无衬线体(对中文而言指的就是黑体) 都优先设置为 `inconsolata`.

这个时候查看默认字体与等宽字体都改变了::

  ~$ fc-match
  Inconsolata.otf: "Inconsolata" "Medium"
  ~$ fc-match monospace
  Inconsolata.otf: "Inconsolata" "Medium"

具体参考: :doc:`/docs/操作系统/linux/教程/debian-ubuntu字体说明`

.. 然后刷新字体缓存:\:

..   fc-cache -f -v

.. 实测无效, 靠



