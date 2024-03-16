=============================
locale-gen
=============================


.. post:: 2023-02-24 22:59:42
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn



默认情况下，为基于 libc 的程序的本地化提供基本支持的 locale 包不包含每种支持语言的可用本地化文件。
由于此类文件的巨大大小以及 libc 支持的大量语言，此限制变得必要。
因此，Debian 使用了一种特殊的机制，我们在目标主机上准备实际的本地化文件并仅分发它们的模板。

**locale-gen** 是一个程序，它读取文件 **/etc/locale.gen** 并为所选的本地化配置文件调用 **localedef**。
修改 **/etc/locale.gen** 文件后运行 **locale-gen**。

**/etc/locale.gen**
  主配置文件，具有简单的格式：每行不为空且不以 # 开头的行都被视为要构建的语言环境定义。
**/var/lib/locales/supported.d/**
  包含语言包提供的 locale.gen 片段的目录。不要手动编辑这些，它们将在包升级时被覆盖。

名字::

  locale-gen - 编译本地定义文件的一个列表

简介::

  locale-gen [options] [locale] [language]

描述:
  编译本地文件需要50M的磁盘容量，并却大部分用户仅需要很少的locales.
  为了节省磁盘容量，编译的locale 文件不在Locales包中发布，
  但是当这些包通过运行locale-gen程序安装的时候，可选的locales是自动产生的。

  如果languages和locales的一个列表被具体到一个参数，
  那么locale-gen 仅仅产生这些具体的locales，
  并添加新的一些到/var/lib/locales/supported.d/local文件中。
  否则产生所有的支持的locales.

  locale 数据文件可以存储在一个单一的二进制文件（/usr/lib/locale/locale-archive） ，
  或者在一个更深的树形结构下的个人文件/usr/lib/locale/<locale_name>/LC_*.
  但是不像locales包，当运行locale-gen时，编译的locale definitions不被移除，
  如果locale源代码文件修改了，locales 才可以在一次编译。

选项, 这些选项覆盖了/etc/belocs/locale-gen.conf下的设置

--help
  一些帮助信息和退出
--purge
  在运行之前，移除所有存在的locales
--no-purge
  与上相反
--archive
  当这个选项被设置，Locale数据是被存储在单一的文档/usr/lib/locale/locale-archive
--no-archive
  .
--aliases=<FILE locale>
  别名从FILE文件中读出

文件：
  /var/lib/locales/supported.d/*  列出了所有要产生的Locales。文件格式和/usr/share/i18n/SUPPORTED 相似。

  /etc/belocs/locale-gen.conf 自定义编译的locale文件怎么存储到磁盘上。

  /usr/lib/locale/<locale-name>/LC_* 编译Locale数据

  /usr/lib/locale/locale-archive 产生包含编译的locale数据的归档，如果--archive 被设置

  /var/lib/belocs 用于追踪在Locale源码文件变化的目录

环境变量：
  这些环境变量影响到每一个对所有的locale-aware程序的Locale类别

  LC_CTYPE
    Character classification and case conversion.
  LC_COLLATE
    Collation order.
  LC_TIME
    Date and time formats.
  LC_NUMERIC
    Non-monetary numeric formats.
  LC_MONETARY
    Monetary formats.
  LC_MESSAGES
    Formats of informative and diagnostic messages and interactive responses.
  LC_PAPER
    Paper size.
  LC_NAME
    Name formats.
  LC_ADDRESS
    Address formats and location information.
  LC_TELEPHONE
    Telephone number formats.
  LC_MEASUREMENT
    Measurement units (Metric or Other).
  LC_IDENTIFICATION
    Metadata about the locale information.

    This environment variable can switch against multiple locale database:
  LOCPATH
    The directory where locale data is stored. By default, /usr/lib/locale is used.


