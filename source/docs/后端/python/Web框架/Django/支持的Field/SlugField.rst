==========================
SlugField
==========================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


Slug 是一个报纸术语。slug 是一个简短的标签，只包含字母、数字、下划线或连字符。它们一般用于 URL 中::

  class SlugField(max_length=50, **options)

像 CharField 一样，你可以指定 max_length （也请阅读那一节中关于数据库可移植性和 max_length 的说明）。
如果没有指定 max_length，Django 将使用默认长度 50。

意味着将 Field.db_index 设置为 True。

基于其他值的值自动预填充一个 SlugField 通常是很有用的。 你可以在管理中使用 prepopulated_fields 来自动完成。

它使用 validate_slug 或 validate_unicode_slug 进行验证。

SlugField.allow_unicode
  如果是 True，该字段除了接受 ASCII 字母外，还接受 Unicode 字母。默认值为 False。


