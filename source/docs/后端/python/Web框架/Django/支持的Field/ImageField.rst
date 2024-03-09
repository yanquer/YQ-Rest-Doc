===============================
ImageField
===============================

继承 FileField 的所有属性和方法，但也验证上传的对象是有效的图像::

  class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, \*\*options)

除了 FileField 的特殊属性外， ImageField 也有 height 和 width 属性。

为了方便查询这些属性，ImageField 有两个额外的可选参数。

ImageField.height_field
  模型字段的名称，每次保存模型实例时将自动填充图像的高度。
ImageField.width_field
  模型字段的名称，每次保存模型实例时将自动填充图像的宽度。

需要 Pillow 库。

ImageField 实例在数据库中创建为 varchar 列，默认最大长度为 100 个字符。与其他字段一样，你可以使用 max_length 参数改变最大长度。

该字段的默认表单部件是一个 ClearableFileInput。

