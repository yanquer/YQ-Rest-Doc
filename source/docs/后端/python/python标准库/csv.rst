===================
csv
===================

官网: `csv - CSV 文件读写 <https://docs.python.org/zh-cn/3/library/csv.html>`_

CSV (Comma Separated Values) 格式是电子表格和数据库中最常见的输入、输出文件格式。

csv 模块实现了 CSV 格式表单数据的读写。
其提供了诸如“以兼容 Excel 的方式输出数据文件”或“读取 Excel 程序输出的数据文件”的功能，
程序员无需知道 Excel 所采用 CSV 格式的细节。
此模块同样可以用于定义其他应用程序可用的 CSV 格式或定义特定需求的 CSV 格式。

csv 模块中的 reader 类和 writer 类可用于读写序列化的数据。
也可使用 DictReader 类和 DictWriter 类以字典的形式读写数据。

提供的函数
===================

.. function:: csv.reader(csvfile, dialect='excel', **fmtparams)

  返回一个 reader 对象，该对象将逐行遍历 csvfile。
  csvfile 可以是任何对象，只要这个对象支持 iterator 协议并在每次调用 ``__next__()`` 方法时都返回字符串，
  文件对象 和列表对象均适用。

  csvfile:
    如果 csvfile 是文件对象，则打开它时应使用 ``newline=''`` 。
    如果没有指定 newline=''，则嵌入引号中的换行符将无法正确解析，
    并且在写入时，使用 ``\r\n`` 换行的平台会有多余的 ``\r`` 写入。
    由于 csv 模块会执行自己的（通用）换行符处理，因此指定 newline='' 应该总是安全的。
  dialect:
    可选参数 dialect 是用于不同的 CSV 变种的特定参数组。它可以是 Dialect_ 类的子类的实例，
    也可以是 list_dialects() 函数返回的字符串之一。
  fmtparams:
    另一个可选关键字参数 fmtparams 可以覆写当前变种格式中的单个格式设置。有关变种和格式设置参数的完整详细信息，
    请参见 变种与格式参数 部分。

  csv 文件的每一行都读取为一个由字符串组成的列表。除非指定了 QUOTE_NONNUMERIC 格式选项（在这种情况下，未加引号的字段会转换为浮点数），否则不会执行自动数据类型转换。

  一个简短的用法示例::

    >>>
    import csv
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
    Spam, Spam, Spam, Spam, Spam, Baked Beans
    Spam, Lovely Spam, Wonderful Spam

.. function:: csv.writer(csvfile, dialect='excel', **fmtparams)

  返回一个 writer 对象，该对象负责将用户的数据在给定的文件类对象上转换为带分隔符的字符串。 csvfile 可以是任何具有 write() 方法的对象。 如果 csvfile 是一个文件对象，则打开它时应使用 newline='' 1。 可以给出可选的 dialect 形参用来定义一组特定 CSV 变种专属的形参。 它可以是 Dialect 类的某个子类的实例或是 list_dialects() 函数所返回的字符串之一。 还可以给出另一个可选的 fmtparams 关键字参数来覆盖当前变种中的单个格式化形参。 有关各个变种和格式化形参的完整细节，请参阅 变种与格式参数 部分。 为了尽量简化与实现 DB API 的模块之间的接口，None 值会被当作空字符串写入。 虽然这个转换是不可逆的，但它可以简化 SQL NULL 数据值到 CSV 文件的转储而无需预处理从 cursor.fetch* 调用返回的数据。 在被写入之前所有其他非字符串数据都会先用 str() 来转转为字符串。

  一个简短的用法示例::

    import csv
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

.. function:: csv.register_dialect(name[, dialect[, **fmtparams]])

  将 dialect 与 name 关联起来。 name 必须是字符串。
  变种的指定可以通过传入一个 Dialect 的子类，或通过 fmtparams 关键字参数，或是两者同时传入，
  此时关键字参数会覆盖 dialect 形参。

  有关变种和格式化形参的完整细节，请参阅 变种与格式参数 部分。

.. function:: csv.unregister_dialect(name)

  从变种注册表中删除 name 对应的变种。如果 name 不是已注册的变种名称，则抛出 Error 异常。

.. function:: csv.get_dialect(name)

  返回 name 对应的变种。如果 name 不是已注册的变种名称，则抛出 Error 异常。该函数返回的是不可变的 Dialect 对象。

.. function:: csv.list_dialects()

  返回所有已注册变种的名称。

.. function:: csv.field_size_limit([new_limit])

  返回解析器当前允许的最大字段大小。如果指定了 new_limit，则它将成为新的最大字段大小。

提供的类
===================

- DictReader_
- DictWriter_
- Dialect_
- excel_
- excel_tab_
- unix_dialect_
- Sniffer_

DictReader
-------------------

.. function:: class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)

  创建一个对象，该对象在操作上类似于常规 reader，
  但是将每行中的信息映射到一个 dict，该 dict 的键由 fieldnames 可选参数给出。

  f:
    文件
  fieldnames:
    fieldnames 参数是一个 sequence。
    如果省略 fieldnames，则文件 f 第一行中的值将用作字段名。无论字段名是如何确定的，字典都将保留其原始顺序。
  restkey:
    如果某一行中的字段多于字段名，则剩余数据会被放入一个列表，并与 restkey 所指定的字段名 (默认为 None) 一起保存。
  restval:
    如果某个非空白行的字段少于字段名，则缺失的值会使用 restval 的值来填充 (默认为 None)。

  所有其他可选或关键字参数都传递给底层的 reader 实例。

  在 3.6 版更改: 返回的行现在的类型是 OrderedDict。

  在 3.8 版更改: 现在，返回的行是 dict 类型。

  一个简短的用法示例::

    >>>
    import csv
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])

    Eric Idle
    John Cleese

    print(row)
    {'first_name': 'John', 'last_name': 'Cleese'}

DictWriter
-------------------

.. function:: class csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)

  创建一个对象，该对象在操作上类似常规 writer，但会将字典映射到输出行。

  fieldnames:
    fieldnames 参数是由键组成的 序列，它指定字典中值的顺序，
    这些值会按指定顺序传递给 writerow() 方法并写入文件 f。
  restval:
    如果字典缺少 fieldnames 中的键，则可选参数 restval 用于指定要写入的值。
  extrasaction:
    如果传递给 writerow() 方法的字典的某些键在 fieldnames 中找不到，则可选参数 extrasaction 用于指定要执行的操作。
    如果将其设置为默认值 'raise'，则会引发 ValueError。
    如果将其设置为 'ignore'，则字典中的其他键值将被忽略。

  所有其他可选或关键字参数都传递给底层的 writer 实例。

  注意，与 DictReader_ 类不同，DictWriter_ 类的 fieldnames 参数不是可选参数。

  一个简短的用法示例::

    import csv

    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

Dialect
-------------------

.. function:: class csv.Dialect

  Dialect 类是一个容器类，其属性包含有如何处理双引号、空白符、分隔符等的信息。
  由于缺少严格的 CSV 规格描述，不同的应用程序会产生略有差别的 CSV 数据。
  Dialect 实例定义了 reader 和 writer 实例将具有怎样的行为。

  所有可用的 Dialect 名称会由 list_dialects() 返回，
  并且它们可由特定的 reader 和 writer 类通过它们的初始化函数 ( ``__init__`` ) 来注册，例如::

    import csv

    with open('students.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='unix')
                                  ^^^^^^^^^^^^^^

excel
-------------------

.. function:: class csv.excel

  excel 类定义了 Excel 生成的 CSV 文件的常规属性。它在变种注册表中的名称是 'excel'。

excel_tab
-------------------

.. function:: class csv.excel_tab

  excel_tab 类定义了 Excel 生成的、制表符分隔的 CSV 文件的常规属性。它在变种注册表中的名称是 'excel-tab'。

unix_dialect
-------------------

.. function:: class csv.unix_dialect

  unix_dialect 类定义了在 UNIX 系统上生成的 CSV 文件的常规属性，即使用 '\n' 作为换行符，且所有字段都有引号包围。
  它在变种注册表中的名称是 'unix'。

  3.2 新版功能.

Sniffer
-------------------

.. function:: class csv.Sniffer

  Sniffer 类用于推断 CSV 文件的格式。

  Sniffer 类提供了两个方法：

  .. function:: sniff(sample, delimiters=None)

    分析给定的 sample 并返回一个 Dialect 子类，该子类中包含了分析出的格式参数。
    如果给出可选的 delimiters 参数，则该参数会被解释为字符串，该字符串包含了可能的有效定界符。

  .. function:: has_header(sample)

    分析 sample 文本（假定为 CSV 格式），如果发现其首行为一组列标题则返回 True。
    在检查每一列时，将考虑是否满足两个关键标准之一来估计 sample 是否包含标题:

    第二至第 n 行包含数字值
    第二至第 n 行包含字符串值，其中至少有一个值的长度与该列预期标题的长度不同。
    会对第一行之后的二十行进行采样；如果有超过一半的列 + 行符合标准，则返回 True。
    备注 此方法是一个粗略的启发式方式，有可能产生错误的真值和假值。

  使用 Sniffer 的示例::

    with open('example.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        # ... process CSV file contents here ...

提供的常量
===================

csv.QUOTE_ALL:
  指示 writer 对象给所有字段加上引号。
csv.QUOTE_MINIMAL:
  指示 writer 对象仅为包含特殊字符（例如 定界符、引号字符 或 行结束符 中的任何字符）的字段加上引号。
csv.QUOTE_NONNUMERIC:
  指示 writer 对象为所有非数字字段加上引号。

  指示 reader 将所有未用引号引出的字段转换为 float 类型。
csv.QUOTE_NONE:
  指示 writer 对象不使用引号引出字段。
  当 定界符 出现在输出数据中时，其前面应该有 转义符。
  如果未设置 转义符，则遇到任何需要转义的字符时，writer 都会抛出 Error 异常。

  指示 reader 不对引号字符进行特殊处理。

变种与格式参数
===================

为了更容易指定输入和输出记录的格式, **特定的一组格式参数组合为一个 dialect（变种）**

一个 dialect 是一个 Dialect_ 类的子类，
它具有一组特定的方法和一个 validate() 方法。
创建 reader 或 writer 对象时，程序员可以将某个字符串或 Dialect 类的子类指定为 dialect 参数。
要想补充或覆盖 dialect 参数，程序员还可以单独指定某些格式参数，这些参数的名称与下面 Dialect 类定义的属性相同。

Dialect支持属性
===================

Dialect_ 类支持以下属性:

Dialect.delimiter:
  一个用于分隔字段的单字符，默认为 ','。
Dialect.doublequote:
  控制出现在字段中的 引号字符 本身应如何被引出。
  当该属性为 True 时，双写引号字符。
  如果该属性为 False，则在 引号字符 的前面放置 转义符。默认值为 True。

  在输出时，如果 doublequote 是 False，且 转义符 未指定，且在字段中发现 引号字符 时，会抛出 Error 异常。
Dialect.escapechar:
  一个用于 writer 的单字符，用来在 quoting 设置为 QUOTE_NONE 的情况下转义 定界符，
  在 doublequote 设置为 False 的情况下转义 引号字符。
  在读取时，escapechar 去除了其后所跟字符的任何特殊含义。该属性默认为 None，表示禁用转义。

  在 3.11 版更改: An empty escapechar is not allowed.
Dialect.lineterminator:
  放在 writer 产生的行的结尾，默认为 '\r\n'。

  备注 reader 经过硬编码，会识别 '\r' 或 '\n' 作为行尾，并忽略 lineterminator。未来可能会更改这一行为。
Dialect.quotechar:
  一个单字符，用于包住含有特殊字符的字段，特殊字符如 定界符 或 引号字符 或换行符。默认为 '"'。

  在 3.11 版更改: An empty quotechar is not allowed.
Dialect.quoting:
  控制 writer 何时生成引号，以及 reader 何时识别引号。
  该属性可以等于任何 QUOTE\_\* 常量（参见 模块内容 段落），默认为 QUOTE_MINIMAL。
Dialect.skipinitialspace:
  When True, spaces immediately following the delimiter are ignored.
  The default is False.
Dialect.strict:
  如果为 True，则在输入错误的 CSV 时抛出 Error 异常。默认值为 False。

Reader 对象
===================

Reader 对象 (DictReader_ 实例和 reader() 函数返回的对象) 具有以下公开方法：

.. function:: csvreader.__next__()

  返回 reader 的可迭代对象的下一行，
  它可以是一个列表（如果对象是由 reader() 返回）或字典（如果是一个 DictReader 实例），
  根据当前 Dialect 来解析。

  通常你应当以 next(reader) 的形式来调用它。

Reader 对象具有以下公开属性：

csvreader.dialect:
  变种描述，只读，供解析器使用。
csvreader.line_num:
  源迭代器已经读取了的行数。它与返回的记录数不同，因为记录可能跨越多行。

DictReader_ 对象具有以下公开属性：

DictReader.fieldnames:
  字段名称。如果在创建对象时未传入字段名称，则首次访问时或从文件中读取第一条记录时会初始化此属性。

Writer 对象
===================

Writer 对象（DictWriter 实例和 writer() 函数返回的对象）具有下面的公开方法。
对于 Writer 对象，行 必须是（一组可迭代的）字符串或数字。
对于 DictWriter 对象，行 必须是一个字典，这个字典将字段名映射为字符串或数字（数字要先经过 str() 转换类型）。
请注意，输出的复数会有括号包围。这样其他程序读取 CSV 文件时可能会有一些问题（假设它们完全支持复数）。

.. function:: csvwriter.writerow(row)

  将 row 形参写入到 writer 的文件对象，根据当前 Dialect 进行格式化。 返回对下层文件对象的 write 方法的调用的返回值。

  在 3.5 版更改: 开始支持任意类型的迭代器。

.. function:: csvwriter.writerows(rows)

  将 rows\*（即能迭代出多个上述 \*row 对象的迭代器）中的所有元素写入 writer 的文件对象，并根据当前设置的变种进行格式化。

Writer 对象具有以下公开属性：

csvwriter.dialect:
  变种描述，只读，供 writer 使用。

DictWriter_ 对象具有以下公开方法：

.. function:: DictWriter.writeheader()

  在 writer 的文件对象中，写入一行字段名称（字段名称在构造函数中指定），并根据当前设置的变种进行格式化。
  本方法的返回值就是内部使用的 csvwriter.writerow() 方法的返回值。

  3.2 新版功能.

  在 3.8 版更改: 现在 writeheader() 也返回其内部使用的 csvwriter.writerow() 方法的返回值。



