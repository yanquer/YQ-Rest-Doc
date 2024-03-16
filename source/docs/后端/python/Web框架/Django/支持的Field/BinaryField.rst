==============================
BinaryField
==============================


.. post:: 2023-02-20 22:06:49
  :tags: python, Web框架, Django, 支持的Field
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


一个用于存储原始二进制数据的字段。可以指定为 bytes、bytearray 或 memoryview。

默认情况下，BinaryField 将 ediditable` 设置为 False，在这种情况下，它不能被包含在 ModelForm 中。

BinaryField 有一个额外的可选参数：

BinaryField.max_length
  The maximum length (in bytes) of the field. The maximum length is enforced in Django's validation using MaxLengthValidator.

滥用 BinaryField
  虽然你可能会想到在数据库中存储文件，但考虑到这在99%的情况下是糟糕的设计。这个字段 不能 代替正确的 静态文件 处理。


