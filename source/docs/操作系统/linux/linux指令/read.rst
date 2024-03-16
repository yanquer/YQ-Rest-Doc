=====================
read
=====================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


功能
=====================

从键盘读取输入

使用: ``read [-options] [ variables ]``

选项
=====================

.. csv-table:: 选项参数
	:header: 选项, 含义

	-p,				输入提示信息
	-r,				不转义读取
	-n num,			"仅读取 num 个字符串, 而非整行"
	-a array,		"把读取的数据赋值给数组 array，从下标 0 开始。"
	-d delimiter,	"用字符串 delimiter 指定读取结束的位置，而不是一个换行符（读取到的数据不包括 delimiter）。"
	-e,				"在获取用户输入的时候，对功能键进行编码转换，不会直接显式功能键对应的字符。"
	-p prompt,		"显示提示信息，提示内容为 prompt 。"
	-s,				"静默模式（ Silent mode ），不会在屏幕上显示输入的字符。当输入密码和其它确认信息的时候，这是很有必要的。"
	-t seconds,		"设置超时时间，单位为秒。如果用户没有在指定时间内输入完成，那么 read 将会返回一个非 0 的退出状态，表示读取失败。"
	-u fd,			"使用文件描述符 fd 作为输入源，而不是标准输入，类似于重定向。"

示例
====================

.. code-block:: sh
	:caption: 直到用户输入y, 否则一直循环

	#!/bin/bash
	tip='n'

	while [ "${tip}" != 'y' ]; do
		read -p "添加成功后输入 y 确认 >" -r tip
	done

