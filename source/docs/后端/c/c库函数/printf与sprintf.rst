=============================
printf与sprintf
=============================


.. post:: 2023-02-20 22:06:49
  :tags: c, c库函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


sprintf和printf在用法和功能上存在以下区别

printf(data):
  将内容输出到屏幕
sprintf(var, data):
  将data赋值给var, data可以是不同类型变量的格式化;
  这就是与 strcpy 的差别, strcpy 只能操作字符串

strcpy(var1, var2):
  :ref:`Cstring_strcpy`

