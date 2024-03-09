===================
configparser
===================

介绍
===================

configparser 模块主要是用来读写配置文件的, 比如 *ini* 类型的文件.

读取结果以节的形式展示, 每一个节下含选项字典

用例
===================

.. code-block:: ini
	:caption: 初始文件内容

	[default]
	a = 1
	b = 2
	c = 3

	[dev]
	a = 11
	b = 22
	c = 33

	[test]
	a = 111
	b = 222
	c = 333

.. code-block:: python
	:caption: 自定义配置操作类

	#  coding: utf-8
	#
	#  Copyright (C) 2022-2022, Inc. All Rights Reserved
	#
	#  @Time    : 2022/12/14 下午1:41
	#  @Author  : yan que
	#  @Email   : yanquer@qq.com
	#  @File    : t_configparser.py
	#  @Project : mytest

	import configparser
	from typing import Dict, List


	class MyConfig(object):
		_config_path: str
		_config_parser = configparser.ConfigParser()

		def _write_file(self):
			with open(self._config_path, 'w') as f:
				self._config_parser.write(f)

		def save(self):
			self._write_file()

		def _read_file(self):
			self._config_parser.read(self._config_path, encoding='utf-8')

		def __init__(self, config_path: str):
			self._config_path = config_path
			self._read_file()

		@property
		def config_parser(self):
			return self._config_parser

		@property
		def selections(self):
			return self._config_parser.sections()

		def has_selection(self, name: str):
			return self._config_parser.has_section(name)

		def has_option(self, selection: str, option: str):
			return self._config_parser.has_option(selection, option)

		def add_selection(self, name: str):
			if not self.has_selection(name):
				self._config_parser.add_section(name)

		def add_options(self, selection: str, data: Dict[str, str]):
			if self.has_selection(selection):
				for k, v in data.items():
					self._config_parser.set(selection, k, v)

		def remove_selection(self, name: str):
			self._config_parser.remove_section(name)

		def remove_option(self, selection: str, data: List[str]):
			if self.has_selection(selection):
				for option in data:
					self._config_parser.remove_option(selection, option)

.. code-block:: python
	:caption: 操作

	def main():
		my_config = MyConfig(config_path='./setting.ini')

		# 获取所有的节
		print('获取所有的节', my_config.selections)

		# 判断是否存在 dev 节
		print('判断是否存在 dev 节', my_config.has_selection('dev'))

		# 判断是否存在 tt 节
		print('判断是否存在 tt 节', my_config.has_selection('tt'))

		# 判断 dev 节是否存在 a 选项
		print('判断 dev 节是否存在 a 选项', my_config.has_option('dev', 'a'))

		# 判断 dev 节是否存在 aa 选项
		print('判断 dev 节是否存在 aa 选项', my_config.has_option('dev', 'aa'))

		# 添加一个 tt 节
		print('添加一个 tt 节', my_config.add_selection('tt'), my_config.selections)

		# tt节添加选项
		my_config.add_options('tt', {
			'a': '123',
			'b': '123',
			'c': '123',
		})

		# 读取一个节
		print('读取 dev 节所有选项', my_config.config_parser.options('dev'))

		# 读取一个节的某个选项
		print('读取 dev 节 a 选项', my_config.config_parser.get('dev', 'a'))
		print('读取 dev 节 a 选项', my_config.config_parser.getint('dev', 'a'))

		# 读取一个节所有配置
		print('读取 dev 节所有配置', my_config.config_parser.items('dev'))

		# 支持直接以字典的形式写入
		my_config.config_parser['DEFAULT'] = {
			'ServerAliveInterval': '45',
			'Compression': 'yes',
			'CompressionLevel': '9'}

		# 保存, 只有保存才会持久化写入到硬盘
		my_config.save()

.. code-block:: none
	:caption: 结果

	获取所有的节 ['default', 'dev', 'test', 'tt']
	判断是否存在 dev 节 True
	判断是否存在 tt 节 True
	判断 dev 节是否存在 a 选项 True
	判断 dev 节是否存在 aa 选项 False
	添加一个 tt 节 None ['default', 'dev', 'test', 'tt']
	读取 dev 节所有选项 ['a', 'b', 'c']
	读取 dev 节 a 选项 11
	读取 dev 节 a 选项 11
	读取 dev 节所有配置 [('a', '11'), ('b', '22'), ('c', '33')]

.. code-block:: ini
	:caption: 最终的文件内容

	[DEFAULT]
	serveraliveinterval = 45
	compression = yes
	compressionlevel = 9

	[default]
	a = 1
	b = 2
	c = 3

	[dev]
	a = 11
	b = 22
	c = 33

	[test]
	a = 111
	b = 222
	c = 333

	[tt]
	a = 123
	b = 123
	c = 123

