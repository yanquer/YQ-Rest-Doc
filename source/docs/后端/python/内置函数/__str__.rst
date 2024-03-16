=========================
__str__
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


当使用print输出对象的时候，只要自己定义了 ``__str__(self)``
方法，那么就会打印从在这个方法中return的数据

比如::

  class Cat:
      def __str__(self):
          return "猫"

  t = Cat()
  print(t)

  # 猫




