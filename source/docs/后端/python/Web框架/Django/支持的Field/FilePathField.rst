================================
FilePathField
================================

一个 CharField，其选择仅限于文件系统中某个目录下的文件名。有一些特殊的参数，其中第一个参数是 必须的::

  class FilePathField(path='', match=None, recursive=False, allow_files=True, allow_folders=False, max_length=100,\ *\*options)

FilePathField.path
  必须的。一个目录的绝对文件系统路径，这个 FilePathField 应从该目录中获取其选择。例如："/home/images"。

  path 也可以是一个可调用对象，可以是在运行时动态设置路径的函数。例如::

    import os
    from django.conf import settings
    from django.db import models

    def images_path():
        return os.path.join(settings.LOCAL_FILE_DIR, 'images')

    class MyModel(models.Model):
        file = models.FilePathField(path=images_path)
FilePathField.matc
  可选。一个正则表达式，作为一个字符串， FilePathField 将用于过滤文件名。
  请注意，正则表达式将被应用于基本文件名，而不是完整的路径。例如："foo.*.txt$"，它将匹配名为 foo23.txt 的文件，但不匹配 bar.txt 或 foo23.png。
FilePathField.recursive
  可选。True 或 False。默认为 False。指定是否包含 path 的所有子目录。
FilePathField.allow_files
  可选。 True 或 False。 默认值是 True。 指定是否应该包含指定位置的文件。 这个或 allow_folders 必须是 True。
FilePathField.allow_folders
  可选。 True 或 False。 默认为 False。 指定是否应该包含指定位置的文件夹。 这个或 allow_files 必须是 True。

  一个潜在的问题是 match 适用于基本文件名，而不是完整的路径。所以，这个例子::

    FilePathField(path="/home/images", match="foo.*", recursive=True)

  将匹配 /home/images/foo.png，但不匹配 /home/images/foo/bar.png，因为 match 适用于基本文件名（ foo.png 和 bar.png ）。

FilePathField 实例在数据库中作为 varchar 列创建，默认最大长度为 100 个字符。
与其他字段一样，你可以使用 max_length 参数改变最大长度。





