==================================
XPath 运算符
==================================


.. post:: 2023-03-01 22:50:22
  :tags: python, 教程, xpath
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


XPath 表达式可返回节点集、字符串、逻辑值以及数字。

XPath 运算符

下面列出了可用在 XPath 表达式中的运算符：

=========== ====================== ====================== ============================================
运算符        描述                  实例                    返回值
=========== ====================== ====================== ============================================
``|``          计算两个节点集        ``//book | //cd``        返回所有拥有 book 和 cd 元素的节点集
\+              加法                    6 + 4                  10
\-              减法                    6 - 4                  2
\*              乘法                    6 * 4                  24
div            除法                    8 div 4                2
=              等于                    price=9.80           如果 price 是 9.80，则返回 true。
                                                            如果 price 是 9.90，则返回 false。

!=            不等于                  price!=9.80           几乎同上
<             小于                    price<9.80            几乎同上
<=            小于或等于              price<=9.80           几乎同上
>             大于                    price>9.80            几乎同上
>=            大于或等于              price>=9.80           几乎同上

or            或                      price=9.80 or         几乎同上
                                      price=9.70
and           与                      price>9.00 and        几乎同上
                                      price<9.90
mod           计算除法的余数          5 mod 2                1

contains      包含, 主要用于属性      contains(@class,      以为例::
                                      "c2")
                                                              <div class="c2 c3">Direct Child Div 1</div>

                                                            表示匹配 class 包含 c2

count         子元素数量              count(a)              a标签数量
=========== ====================== ====================== ============================================

.. _XpathContain:

contain的使用
==================================

如::

  *[contains(concat(' ', normalize-space(@class), ' '), ' someclass ')]
                      获取class 包含 someclass的元素
                      最繁琐

  @class='someclass'  获取class 仅为 someclass的元素
                      可能会漏选
  contains(@class, 'someclass')
                      获取class 包含 someclass的元素
                      但是可能会多选一些元素






