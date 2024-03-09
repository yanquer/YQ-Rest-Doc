================================
FieldFile
================================

此节仅说明与FileField关系, 并不存在这样一个列,
:doc:`/docs/后端/python/Web框架/Django/支持的Field/FileField` 和 FieldFile

当你访问一个模型上的 FileField 时，你会得到一个 FieldFile 的实例作为访问底层文件的代理::

  class FieldFile

FieldFile 的 API 与 File 的 API 相同，但有一个关键的区别。
该类所封装的对象不一定是 Python 内置文件对象的封装 相反，
它是 Storage.open() 方法结果的封装，该方法可能是 File 对象，也可能是自定义存储对 File API 的实现。

除了从 File 继承的 API，如 read() 和 write() 之外，FieldFile 还包括一些可以用来与底层文件交互的方法：

.. warning::

  该类的两个方法 save() 和 delete()，默认为将与相关 FieldFile 的模型对象保存在数据库中。

FieldFile.name
  文件名，包括从关联的 Storage 的根部开始的相对路径 FileField。
FieldFile.path
  一个只读属性，通过调用底层的 path() 方法，访问文件的本地文件系统路径。
FieldFile.size
  底层 Storage.size() 方法的结果。
FieldFile.url
  一个只读属性，通过调用底层 Storage 类的 Storage() 方法来访问文件的相对 URL。
FieldFile.open(mode='rb')
  以指定的 mode 打开或重新打开与该实例相关的文件。与标准的 Python open() 方法不同，它不返回一个文件描述符。

  因为在访问底层文件时，底层文件是隐式打开的，所以除了重置底层文件的指针或改变 mode 之外，可能没有必要调用这个方法。
FieldFile.close()
  类似于标准的 Python file.close() 方法，关闭与该实例相关的文件。
FieldFile.save(name, content, save=True)
  这个方法接收一个文件名和文件内容，并将它们传递给字段的存储类，然后将存储的文件与模型字段关联。
  如果你想手动将文件数据与模型上的 FileField 实例关联起来，那么 save() 方法用来持久化该文件数据。

  取两个必要的参数。name 是文件的名称，content 是包含文件内容的对象。 可选的 save 参数控制在与该字段相关联的文件被更改后是否保存模型实例。默认为 True。

  .. note::

    content 参数应该是 django.core.files.File 的实例，而不是 Python 内置的文件对象。
    你可以从现有的 Python 文件对象构造一个 File，像这样::

      from django.core.files import File

      Open an existing file using Python's built-in open()
      f = open('/path/to/hello.world')
      myfile = File(f)

    或者你可以从 Python 字符串中构建一个像这样的字符串::

      from django.core.files.base import ContentFile
      myfile = ContentFile("hello world")

    更多信息，请参见 管理文件。
FieldFile.delete(save=True)
  删除与此实例相关的文件，并清除字段的所有属性。
  注意：如果在调用 delete() 时，文件恰好被打开，本方法将关闭该文件。

  可选的 save 参数控制在删除与该字段相关的文件后是否保存模型实例。默认值为 True。

  .. note::

    当一个模型被删除时，相关文件不会被删除。
    如果你需要清理遗留文件，你需要自己处理（例如，使用自定义管理命令，可以手动运行或通过例如 cron 定期运行）。




