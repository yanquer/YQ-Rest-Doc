===============================
shell的变量替换
===============================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 教程, shell语法规范
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


几种特殊的替换结构
===============================

四种::

  ${var:-string}
  ${var:+string}
  ${var:=string}
  ${var:?string}

``${var:-string}`` 和 ``${var:=string}`` :
  若变量var为空，则用在命令行中用string来替换${var:-string}，
  否则变量var不为空时，则用变量var的值来替换${var:-string}；

  对于${var:=string}的替换规则和${var:-string}是一样的，
  所不同之处是${var:=string}若var为空时，用string替换${var:=string}的同时，把string赋给变量var;

  ${var:=string}很常用的一种用法是，判断某个变量是否赋值，没有的话则给它赋上一个默认值
``${var:+string}``
  替换规则和上面的相反，即只有当var不是空的时候才替换成string，
  若var为空时则不替换或者说是替换成变量 var的值，
  即空值。(因为变量var此时为空，所以这两种说法是等价的)
``${var:?string}``
  若变量var不为空，则用变量var的值来替换${var:?string}；
  若变量var为空，则把string输出到标准错误中，并从脚本中退出。
  我们可利用此特性来检查是否设置了变量的值。

.. note::

  上面这四种替换结构中string不一定是常值的，可用另外一个变量的值或是一种命令的输出。

四种模式匹配替换结构
===============================

模式匹配记忆方法：

- ``#`` 是去掉左边(在键盘上#在$之左边)
- ``%`` 是去掉右边(在键盘上%在$之右边)
- ``#`` 和 ``%`` 中的单一符号是最小匹配，两个相同符号是最大匹配。

也是四种::

  ${var%pattern}
  ${var%%pattern}
  ${var#pattern}
  ${var##pattern}

第一种模式: ${variable%pattern}
  shell在variable中查找，看它是否一给的模式pattern结尾，
  如果是，就从命令行把variable中的内容去掉右边最短的匹配模式
第二种模式: ${variable%%pattern}
  shell在variable中查找，看它是否一给的模式pattern结尾，
  如果是，就从命令行把variable中的内容去掉右边最长的匹配模式
第三种模式: ${variable#pattern}
  shell在variable中查找，看它是否一给的模式pattern开始，
  如果是，就从命令行把variable中的内容去掉左边最短的匹配模式
第四种模式: ${variable##pattern}
  shell在variable中查找，看它是否一给的模式pattern结尾，
  如果是，就从命令行把variable中的内容去掉右边最长的匹配模式

.. note::

  这四种模式中都不会改变variable的值，
  其中, **只有在pattern中使用了 ``*`` 匹配符号时** , %和%%，#和##才有区别.

  结构中的pattern支持通配符,

  - ``*`` 表示零个或多个任意字符;
  - ``?`` 表示仅与一个任意字符匹配;
  - ``[...]`` 表示匹配中括号里面的字符;
  - ``[!...]`` 表示不匹配中括号里面的字符.

示例::

  var=testcase

  echo $var
  #testcase

去掉右边的se::

  echo ${var%s*e}     #testca
  echo $var           #testcase

去掉s..e::

  echo ${var%%s*e}    #te

去掉左边第一个e之前的（包括自己）::

  echo ${var#?e}      #stcase

去掉se::

  echo ${var##?e}     #stcase

去自己::

  echo ${var##*e}     #

去的就剩个e::

  echo ${var##*s}     #e

去test::

  echo ${var##test}   #case



