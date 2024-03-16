=====================
datetime
=====================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


与 :doc:`/docs/后端/python/python标准库/time` 类似,
区别如下

- time: 提供了与时间有关的函数和类型，包括获取当前时间、将时间戳转换为人类可读格式等
- datetime: 提供了更灵活和强大的日期和时间操作功能，包括日期算术、日期格式化等。

示例::

  import datetime

  # 获取当前日期和时间
  now = datetime.datetime.now()
  print(now)

  # 格式化日期字符串
  date_str = now.strftime('%Y-%m-%d %H:%M:%S')
  print(date_str)



