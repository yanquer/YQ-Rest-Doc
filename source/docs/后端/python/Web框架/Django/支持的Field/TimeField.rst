=======================
TimeField
=======================

一个时间，在 Python 中用 datetime.time 实例表示。接受与 DateField 相同的自动填充选项::

  class TimeField(auto_now=False, auto_now_add=False, **options)

该字段默认的表单部件t是一个 TimeInput。管理中添加了一些 JavaScript 快捷方式。




