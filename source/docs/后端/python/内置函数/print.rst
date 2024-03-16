==============================
print
==============================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


这个本来不用说的, 但是想了想还是记录一下

.. note::

  其实大多属于字符串输出本身的

输出指定行长度, 可以使用 ``{:长度}`` 形式;
比如输出123, 长度为40::

  In [3]: "|{:40}|".format("123")
  Out[3]: '|123                                     |'

  In [4]: f"|{'123':40}|"
  Out[4]: '|123                                     |'

print与sys.stdout.write
==============================

``sys.stdout.write()``
  只能输出一个字符串str，而 ``print()`` 可以输出多个值，数据类型多样。
``print(obj)``
  实际上是调用 ``sys.stdout.write(obj+'\n')``，因此print在打印时会自动加个换行符。



