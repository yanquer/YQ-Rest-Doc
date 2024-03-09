==========================
函数API
==========================


数值计算
==========================

.. function:: format(num, n)

	格式化为string，format($num, $n)， 四舍五入保留小数点后 n 位，
	并格式化用逗号隔开（每三位一个逗号）::

		select format(1000.1254);
		# 1,000.13

round(num, n)
	直接四舍五入，round($num, $n)，四舍五入保留 n 位小数

.. function:: truncate(num, n)

	截取数字的小数点后几位 truncate($num, $n)，不四舍五入::

		select truncate(100.1234, 2) as '1';

		# 100.12
		# 截取小数点后两位

.. function:: convert(num, ...)

	转型，会四舍五入::

		select convert(1478568.2457, DECIMAL(10,2));

		# 1478568.25
		# DECIMAL(10,2) 表示转换为 DECIMAL, 十进制, 保留2位

.. function:: ceiling(num, n)

	取整，个位加一::

		select CEILING(1478568.2457);   直接取整，个位+1
		# 1478569

.. function:: floor(n)

		向下取整::

			select FLOOR(1478568.2457);
			# 1478568

.. function:: rand([n])

		返回随机数, 0~1之间

		可设置随机种子参数, 保证结果一致

.. function:: random()

		随机数

字符串拼接
==========================

.. function:: cancat(a, b, c)

	将abc拼起来

.. function:: substr(data_str, start, length)

		截取字符串

		data_str: str
				需要截取的字符串
		start: int
				开始截取的下标(包含)
		length: int
				从起始位置的长度, 默认到结尾

.. function:: mid

		效果等价于substr

.. function:: left(data_str, length)

		从左边开始截取字符串指定长度

.. function:: ascii(data_str)

		获取ascii码, 字符串则获取首字母的ascii码

.. function:: ord(data_str)

		效果等价于ascii

.. function:: group_concat

		group_by 的时候, 如果有一对多的情况, 5.7 之后的mysql会报错.

		使用 group_concat(分组依据的字段名) 可以将多的情况拼接起来.

.. function:: updatexml(XML, xpath_str, new_value)

		...

.. function:: extractvalue(XML, xpath_str)

		...

.. function:: hex(char)

		查看字符的十六进制


