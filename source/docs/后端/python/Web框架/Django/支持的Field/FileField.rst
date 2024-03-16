=========================
FileField
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


一个文件上传字段::

  class FileField(upload_to=None, max_length=100, \*\*options)

.. note::

  primary_key 参数不支持，如果使用，会引起错误。

有两个可选参数：

FileField.upload_to
  这个属性提供了一种设置上传目录和文件名的方式，可以有两种设置方式。在这两种情况下，值都会传递给 Storage.save() 方法。

  如果你指定一个字符串值或一个 Path，它可能包含 strftime() 格式，
  它将被文件上传的日期／时间所代替（这样上传的文件就不会填满指定的目录）。例如::

    class MyModel(models.Model):
        # file will be uploaded to MEDIA_ROOT/uploads
        upload = models.FileField(upload_to='uploads/')
        # or...
        # file will be saved to MEDIA_ROOT/uploads/2015/01/30
        upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

  如果你使用的是默认的 FileSystemStorage，这个字符串的值将被附加到你的 MEDIA_ROOT 路径后面，
  形成本地文件系统中上传文件的存储位置。
  如果你使用的是不同的存储系统，请检查该存储系统的文档，看看它是如何处理 upload_to 的。

  upload_to 也可以是一个可调用对象，如函数。这个函数将被调用以获得上传路径，包括文件名。
  这个可调用对象必须接受两个参数，并返回一个 Unix 风格的路径（带斜线），以便传给存储系统。这两个参数是：

  instance
    定义 FileField 的模型实例。更具体地说，这是附加当前文件的特定实例。

    在大多数情况下，这个对象还没有被保存到数据库，所以如果它使用默认的 AutoField，它的主键字段可能还没有一个值。
  filename
    最初给文件的文件名。在确定最终目标路径时，可能会考虑到，也可能不会考虑到。

  例子::

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    class MyModel(models.Model):
        upload = models.FileField(upload_to=user_directory_path)
FileField.storage
  一个存储对象，或是一个返回存储对象的可调用对象。它处理你的文件的存储和检索。参见 管理文件，了解如何提供这个对象。

Changed in Django 3.1:
  增加了提供可调用对象的能力。

该字段的默认表单部件是一个 ClearableFileInput。

在模型中使用 FileField 或 ImageField （见下文）需要几个步骤：

- 在你的配置文件中，你需要定义 MEDIA_ROOT 作为你希望 Django 存储上传文件的目录的完整路径。
  （为了保证性能，这些文件不存储在数据库中。）
  定义 MEDIA_URL 作为该目录的基本公共 URL。确保这个目录是 Web 服务器的用户账号可以写的。
- 将 FileField 或 ImageField 添加到你的模型中，定义 upload_to 选项，指定 MEDIA_ROOT 的子目录，用于上传文件。
- 所有这些将被存储在你的数据库中的是一个文件的路径（相对于 MEDIA_ROOT ）。
  你很可能要使用 Django 提供的方便的 url 属性。
  例如，如果你的 ImageField 叫做 mug_shot，你可以在模板中使用 {{ object.mug_shot.url }} 获取图片的绝对路径。

例如，你的 MEDIA_ROOT 设置为 '/home/media'，
upload_to 设置为 'photos/%Y/%m/%d'。
upload_to 中的 '%Y/%m/%d' 部分是 strftime() 格式化，
'%Y' 是四位数的年，'%m' 是两位数的月，'%d' 是两位数的日。
如果你在 2007 年 1 月 15 日上传了一个文件，它将被保存在 /home/media/photos/2007/01/15 目录下。

如果你想检索上传文件的盘上文件名，或者文件的大小，可以分别使用 name 和 size 属性；关于可用属性和方法的更多信息，
请参见 File 类参考和 管理文件 主题指南。

.. note::

  文件在数据库中作为保存模型的一部分，因此在模型被保存之前，不能依赖磁盘上使用的实际文件名。

上传的文件的相对 URL 可以通过 url 属性获得。内部调用底层 Storage 类的 store() 方法。

需要注意的是，无论何时处理上传的文件，你都应该密切关注你上传的文件在哪里，
是什么类型的文件，以避免安全漏洞。对所有上传的文件进行验证，这样你才能确定文件是你认为的那样。
例如，如果你盲目地让别人上传文件，不经过验证，就上传文件到你的 Web 服务器的文档根目录下，
那么有人就可以上传一个 CGI 或 PHP 脚本，并通过访问它的 URL 在你的网站上执行该脚本。不要允许这种情况发生。

另外要注意的是，即使是上传的 HTML 文件，由于可以被浏览器执行（虽然不能被服务器执行），也会造成相当于 XSS 或 CSRF 攻击的安全威胁。

FileField 实例在数据库中被创建为 varchar 列，默认最大长度为 100 个字符。与其他字段一样，你可以使用 max_length 参数改变最大长度。




