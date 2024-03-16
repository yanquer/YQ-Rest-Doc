
================================
type
================================

.. post:: 2023-02-20 22:06:49
  :tags: python, 内置函数
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


一个参数
================================

一个参数返回类型


三个参数(或者大于1)
================================

以第一个参数为类名, 第二个参数为父类元祖, 第三个参数为赋值


用例:

.. code-block:: python

	# coding: utf-8

	class A(object):
		a = 1


	class B(object):
		b = 2


	def something():
		print('some')


	c = type(A), type(A())
	d = type('D', (A, B), {'something': something})

	print('一个参数', c)
	print('三个参数', d, d.__dict__, d.a, d.b)


	# 输出
	# 一个参数 (<class 'type'>, <class '__main__.A'>)
	# 三个参数 <class '__main__.D'> {'something': <function something at 0x109e410d0>, '__module__': '__main__', '__doc__': None} 1 2




