=================
gettext模块
=================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


:官网文档::
  `gettext <https://docs.python.org/zh-cn/3/library/gettext.html>`_

多语种国际化服务

为 Python 模块和应用程序提供国际化 (Internationalization, I18N)
和本地化 (Localization, L10N) 服务.

- 支持 GNU gettext 消息编目 API. GUN_gettext_API_
- 支持 高级的、基于类的 API. 可能更适合于 Python 文件

.. _GUN_gettext_API:

GNU gettext API
=================

使用该 API，将会对整个应用程序产生全局的影响。

如果你的应用程序支持多语种，而语言选择取决于用户的语言环境设置，这通常正是你所想要的。

而如果你正在本地化某个 Python 模块，或者你的应用程序需要在运行时切换语言，相反你或许想用基于类的API: api_base_class_ 。

API:

- bindtextdomain_
- textdomain_
- gettext_
- dgettext_
- ngettext_
- dngettext_
- pgettext_
- dpgettext_
- npgettext_
- dnpgettext_

bindtextdomain
-----------------

.. function:: gettext.bindtextdomain(domain, localedir=None)

  将 domain 绑定到本地目录 localedir。
  更具体地来说，模块 gettext 将使用路径 (在 Unix 系统中):
  localedir/language/LC_MESSAGES/domain.mo 查找二进制 .mo 文件，
  此处对应地查找 language 的位置是环境变量 LANGUAGE, LC_ALL, LC_MESSAGES 和 LANG 中。

  如果遗漏了 localedir 或者设置为 None，那么将返回当前 domain 所绑定的值 [1]_ .

textdomain
-----------------

.. function:: gettext.textdomain(domain=None)

  修改或查询当前的全局域。

  如果 domain 为 None，则返回当前的全局域，
  不为 None 则将全局域设置为 domain，并返回它。

gettext
-----------------

.. function:: gettext.gettext(message)

  返回 message 的本地化翻译，依据包括当前的全局域、语言和语言环境目录。本函数在本地命名空间中通常有别名 _() （参考下面的示例）。

dgettext
-----------------

.. function:: gettext.dgettext(domain, message)

  与 gettext() 类似，但在指定的 domain 中查找 message。

ngettext
-----------------

.. function:: gettext.ngettext(singular, plural, n)

  与 gettext() 类似，但考虑了复数形式。
  如果找到了翻译，则将 n 代入复数公式，然后返回得出的消息（某些语言具有两种以上的复数形式）。
  如果未找到翻译，则 n 为 1 时返回 singular，为其他数时返回 plural。

  复数公式取自编目头文件。
  它是 C 或 Python 表达式，有一个自变量 n，该表达式计算的是所需复数形式在编目中的索引号。
  关于在 .po 文件中使用的确切语法和各种语言的公式，请参阅 `GNU gettext <https://www.gnu.org/software/gettext/manual/gettext.html>`_ 文档 。

dngettext
-----------------

.. function:: gettext.dngettext(domain, singular, plural, n)

  与 ngettext() 类似，但在指定的 domain 中查找 message。

pgettext
-----------------

  .. function:: gettext.pgettext(context, message)

dpgettext
-----------------

.. function:: gettext.dpgettext(domain, context, message)

npgettext
-----------------

.. function:: gettext.npgettext(context, singular, plural, n)

dnpgettext
-----------------

.. function:: gettext.dnpgettext(domain, context, singular, plural, n)

  与前缀中没有 p 的相应函数类似（即 gettext(), dgettext(), ngettext(), dngettext() ），
  但是仅翻译给定的 message context。

  3.8 新版功能.

注意，GNU gettext 还定义了 dcgettext() 方法，但它被认为不实用，因此目前没有实现它。

这是该 API 的典型用法示例::

  import gettext
  gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
  gettext.textdomain('myapplication')
  _ = gettext.gettext
  # ...
  print(_('This is a translatable string.'))

.. _api_base_class:

基于类的 API
=================

与 GNU gettext API ( GUN_gettext_API_ ) 相比，gettext 模块的基于类的 API 提供了更多的灵活性和更强的便利性。
这是本地化 Python 应用程序和模块的推荐方法。
gettext 定义了一个 GNUTranslations 类，该类实现了 GNU .mo 格式文件的解析，并且具有用于返回字符串的方法。
本类的实例也可以将自身作为函数 _() 安装到内建命名空间中。

API:

- find_
- translation_
- install_

find
-----------------

.. function:: gettext.find(domain, localedir=None, languages=None, all=False)

  本函数实现了标准的 .mo 文件搜索算法。它接受一个 domain，它与 textdomain() 接受的域相同。
  可选参数 localedir 与 bindtextdomain() 中的相同。
  可选参数 languages 是多条字符串的列表，其中每条字符串都是一种语言代码。

  - 如果没有传入 localedir，则使用默认的系统语言环境目录 [1]_
  - 如果没有传入 languages，则搜索以下环境变量：LANGUAGE、LC_ALL、LC_MESSAGES 和 LANG。
    从这些变量返回的第一个非空值将用作 languages 变量。
    环境变量应包含一个语言列表，由冒号分隔，该列表会被按冒号拆分，以产生所需的语言代码字符串列表。

  find() 将扩展并规范化 language，然后遍历它们，搜索由这些组件构建的现有文件::

    localedir/language/LC_MESSAGES/domain.mo

  find() 返回找到类似的第一个文件名。如果找不到这样的文件，则返回 None。如果传入了 all，它将返回一个列表，包含所有文件名，并按它们在语言列表或环境变量中出现的顺序排列。

translation
-----------------

.. function:: gettext.translation(domain, localedir=None, languages=None, class_=None, fallback=False)

  languages: list
    默认为空则使用系统当前的LANG环境变量的值;
    不为空, 如 ``['en']`` , 表示自定义设置语言.

  根据 domain、localedir 和 languages，返回 \*Translations 实例，
  首先应将前述参数传入 find() 以获取关联的 .mo 文件路径的列表。名
  字与 .mo 文件名相同的实例将被缓存。如果传入 class\_，它将是实际被实例化的类，否则实例化 GNUTranslations。
  类的构造函数必须只接受一个 文件对象 参数。
  如果传入 codeset，那么在 lgettext() 和 lngettext() 方法中，对翻译后的字符串进行编码的字符集将被改变。

  如果找到多个文件，后找到的文件将用作先前文件的替补。
  为了设置替补，将使用 copy.copy() 从缓存中克隆每个 translation 对象。
  实际的实例数据仍在缓存中共享。

  如果 .mo 文件未找到，且 fallback 为 false（默认值），则本函数引发 OSError 异常，
  如果 fallback 为 true，则返回一个 NullTranslations 实例。

  在 3.3 版更改: 曾经是 IOError 被引发而不是 OSError 。

  在 3.11 版更改: codeset parameter is removed.

install
-----------------

.. function:: gettext.install(domain, localedir=None, *, names=None)

  This installs the function _() in Python's builtins namespace, based on domain and localedir which are passed to the function translation().

  通过 translation_ , 安装 ``_()`` 到 Python 命名空间 **全局性更改**

  names 参数的信息请参阅 translation 对象的 install() 方法的描述。

  如下所示，通常将字符串包括在 _() 函数的调用中，以标记应用程序中待翻译的字符串，就像这样:

  print(_('This string will be translated.'))
  为了方便，一般将 _() 函数安装在 Python 内建命名空间中，以便在应用程序的所有模块中轻松访问它。

  在 3.11 版更改: names is now a keyword-only parameter.


本地化
=================

部分本地化::

  import gettext
  t = gettext.translation('spam', '/usr/share/locale')
  _ = t.gettext

全局本地化::

  import gettext

  lang1 = gettext.translation('myapplication', languages=['en'])
  lang2 = gettext.translation('myapplication', languages=['fr'])
  lang3 = gettext.translation('myapplication', languages=['de'])

  # start by using language1
  lang1.install()

  # ... time goes by, user selects language 2
  lang2.install()

  # ... more time goes by, user selects language 3
  lang3.install()





.. [1] 不同系统的默认语言环境目录是不同的；
  比如在 RedHat Linux 上是 /usr/share/locale，
  在 Solaris 上是 /usr/lib/locale。
  gettext 模块不会支持这些基于不同系统的默认值；
  而它的默认值为 sys.base_prefix/share/locale （请参阅 sys.base_prefix）。
  基于上述原因，最好每次都在应用程序的开头使用明确的绝对路径来调用 bindtextdomain_ 。







