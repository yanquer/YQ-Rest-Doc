==============================
DateField
==============================

一个日期，在 Python 中用一个 datetime.date 实例表示。有一些额外的、可选的参数。

DateField.auto_now
  每次保存对象时，自动将该字段设置为现在。
  对于“最后修改”的时间戳很有用。请注意，当前日期 总是 被使用，而不仅仅是一个你可以覆盖的默认值。

  只有在调用 Model.save() 时，该字段才会自动更新。
  当以其他方式对其他字段进行更新时，如 QuerySet.update()，
  该字段不会被更新，尽管你可以在这样的更新中为该字段指定一个自定义值。
DateField.auto_now_add
  当第一次创建对象时，自动将该字段设置为现在。
  对创建时间戳很有用。请注意，当前日期是 始终 使用的；
  它不是一个你可以覆盖的默认值。因此，即使你在创建对象时为该字段设置了一个值，它也会被忽略。
  如果你想修改这个字段，可以设置以下内容来代替 auto_now_add=True ：

- 对于 DateField: default=date.today ——来自 datetime.date.today()
- 对于 DateTimeField: default=timezone.now ——来自 django.utils.timezone.now()

该字段的默认表单部件是一个 DateInput。管理中增加了一个 JavaScript 日历，
以及“今天”的快捷方式。包含一个额外的 invalid_date 错误信息键。

auto_now_add、auto_now 和 default 选项是相互排斥的。这些选项的任何组合都会导致错误。

.. note::

  目前，将 auto_now 或 auto_now_add 设置为 True，将导致该字段设置为 editable=False 和 blank=True。

  auto_now 和 auto_now_add 选项将始终使用创建或更新时 默认时区 的日期。
  如果你需要一些不同的东西，你可能需要考虑使用你自己的可调用的默认值，或者覆盖 save()
  而不是使用 auto_now 或 auto_now_add ；
  或者使用 DateTimeField 而不是 DateField，并决定如何在显示时间处理从日期时间到日期的转换。


