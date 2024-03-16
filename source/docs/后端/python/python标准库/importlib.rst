========================
importlib
========================

官网: https://docs.python.org/zh-cn/3/library/importlib.html

实现了import部分功能及动态导入

这里仅介绍主要的几个

- import_module():导入模块,返回模块对象。
- find_loader():根据模块名称查找其加载器(loader),用于动态导入。
- load_module():使用加载器加载模块,返回模块对象。
- reload():重载已加载的模块。
- get_module():根据模块对象获取模块信息。

__import__
========================

.. function::importlib.__import__(name, globals=None, locals=None, fromlist=(), level=0)

  内置 __import__() 函数的实现。

.. note::

  程序式地导入模块应该使用 import_module() 而不是这个函数。

import_module
========================

.. function:: importlib.import_module(name, package=None)

  导入一个模块。

  name
    指定了以绝对或相对导入方式导入什么模块 (比如要么像这样 pkg.mod 或者这样 ..mod)。
    如果参数 name 使用相对导入的方式来指定，那么 package 参数必须设置为那个包名，
    这个包名作为解析这个包名的锚点 (比如 import_module('..mod', 'pkg.subpkg') 将会导入 pkg.mod)。

  import_module() 函数是一个对 importlib.__import__() 进行简化的包装器。
  这意味着该函数的所有语义都来自于 importlib.__import__()。
  这两个函数之间最重要的不同点在于 import_module() 返回指定的包或模块 (例如 pkg.mod)，
  而 __import__() 返回最高层级的包或模块 (例如 pkg)。

  如果动态导入一个自解释器开始执行以来被创建的模块（即创建了一个 Python 源代码文件），
  为了让导入系统知道这个新模块，可能需要调用 invalidate_caches()。

find_loader
========================

.. function:: importlib.find_loader(name, path=None)

  查找一个模块的加载器，可选择地在指定的 path 里面。
  如果这个模块是在 sys.modules，
  那么返回 sys.modules[name].__loader__ (除非这个加载器是 None 或者是没有被设置， 在这样的情况下，会引起 ValueError 异常）。
  否则使用 sys.meta_path 的一次搜索就结束。如果未发现加载器，则返回 None。

  点状的名称没有使得它父包或模块隐式地导入，因为它需要加载它们并且可能不需要。
  为了适当地导入一个子模块，需要导入子模块的所有父包并且使用正确的参数提供给 path。

  3.3 新版功能.

  在 3.4 版更改: 如果没有设置 __loader__，会引起 ValueError 异常，就像属性设置为 None 的时候一样。

  3.4 版后已移除: 使用 importlib.util.find_spec() 来代替。

invalidate_caches
========================

.. function:: importlib.invalidate_caches()

  使查找器存储在 sys.meta_path 中的内部缓存无效。
  如果一个查找器实现了 invalidate_caches()，那么它会被调用来执行那个无效过程。
  如果创建/安装任何模块，同时正在运行的程序是为了保证所有的查找器知道新模块的存在，那么应该调用这个函数。

reload
========================

.. function:: importlib.reload(module)

  重新加载之前导入的 module。
  那个参数必须是一个模块对象，所以它之前必须已经成功导入了。
  这在你已经使用外部编辑器编辑过了那个模块的源代码文件并且想在退出 Python 解释器之前试验这个新版本的模块的时候将很适用。
  函数的返回值是那个模块对象（如果重新导入导致一个不同的对象放置在 sys.modules 中，那么那个模块对象是有可能会不同）。

  当执行 reload() 的时候：

  Python 模块的代码会被重新编译并且那个模块级的代码被重新执行，
  通过重新使用一开始加载那个模块的 loader，定义一个新的绑定在那个模块字典中的名称的对象集合。
  扩展模块的``init``函数不会被调用第二次。
  与Python中的所有的其它对象一样，旧的对象只有在它们的引用计数为0之后才会被回收。
  模块命名空间中的名称重新指向任何新的或更改后的对象。
  其他旧对象的引用（例如那个模块的外部名称）不会被重新绑定到引用的新对象的，并且如果有需要，必须在出现的每个命名空间中进行更新。

  有一些其他注意事项：

  当一个模块被重新加载的时候，它的字典（包含了那个模块的全区变量）会被保留。
  名称的重新定义会覆盖旧的定义，所以通常来说这不是问题。
  如果一个新模块没有定义在旧版本模块中定义的名称，则将保留旧版本中的定义。
  这一特性可用于作为那个模块的优点，如果它维护一个全局表或者对象的缓存 —— 使用 try 语句，
  就可以测试表的存在并且跳过它的初始化，如果有需要的话::

    try:
        cache
    except NameError:
        cache = {}

  重新加载内置的或者动态加载模块，通常来说不是很有用处。
  不推荐重新加载"sys，__main__，builtins 和其它关键模块。
  在很多例子中，扩展模块并不是设计为不止一次的初始化，并且当重新加载时，可能会以任意方式失败。

  如果一个模块使用 from ... import ... 导入的对象来自另外一个模块，
  给其它模块调用 reload() 不会重新定义来自这个模块的对象 ——
  解决这个问题的一种方式是重新执行 from 语句，另一种方式是使用 import 和限定名称(module.name)来代替。

  如果一个模块创建一个类的实例，重新加载定义那个类的模块不影响那些实例的方法定义———它们继续使用旧类中的定义。
  对于子类来说同样是正确的。

  3.4 新版功能.

  在 3.7 版更改: 如果重新加载的模块缺少 ModuleSpec ，则会触发 ModuleNotFoundError 。

metadata
========================

metadata.entry_points
------------------------

位置::

  from importlib.metadata import entry_points

通过参数 group 或者 name, 找到所有匹配的已安装包的入口.

关于loader加载器
========================

在Python的importlib包中,加载器(Loader)是用来加载模块的对象。它包含了导入模块所需要的逻辑和信息。
主要有以下几种加载器:

- SourceFileLoader:从源文件(.py文件)加载模块。
- PyLoader:从编译好的模块文件(.pyc文件)加载模块。
- PackageLoader:从包中加载子模块。
- ExtensionFileLoader:从扩展模块(.so/.pyd文件)加载模块。
- ImpLoader:兼容Import模块的加载器,用于从已编译好的模块加载模块。

等等。

加载器具有以下方法:

- exec_module(module):执行模块的模块体代码,initialize模块对象。
- load_module(fullname):加载模块,返回模块对象。
- get_code(fullname):获取模块的代码对象。
- get_source(fullname):获取模块的源代码。
- is_package(fullname):判断模块是否是包。
- get_filename(fullname):获取模块的文件名。

通过这些方法,加载器实现了导入模块的主要逻辑。

例如,SourceFileLoader可以从源文件读取代码并执行,返回模块对象。
在importlib中,find_loader()函数通过模块名称找到相应的加载器。
然后我们可以调用加载器的load_module()方法加载该模块。例如::

  import importlib.util

  name = 'example'
  loader = importlib.util.find_loader(name)
  module = loader.load_module(name)

这里我们找到example模块的加载器loader,然后通过loader加载example模块,获得模块对象module。

eg, 模块导入::

  module = importlib.import_module('math')
  print(module.sqrt(16))  # 4.0

获取模块信息::

  name = 'os'
  loader = importlib.find_loader(name)
  module = loader.load_module(name)

  print(module.__file__)
  print(module.__package__)
