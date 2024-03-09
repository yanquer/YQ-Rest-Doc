#  coding: utf-8
#
#  Copyright (C) 2022-2022, Inc. All Rights Reserved
#
#  @Time    : 2022-12-22
#  @Author  : yan que
#  @Email   : yanquer@qq.com
#  @File    : t_cerberus.py
#  @Project : rst-document

from cerberus import Validator


def main():
	# 定义模版校验规则
	schema = {
		"user_name": {"type": "string"},
		"password": {"type": "string"},
		"properties": {
			"type": "dict",
			"require_all": True,
			"schema": {"address": {"type": "string"}},
		},
	}
	v = Validator(schema)
	document = {"user_name": "bob", "test": '', 'properties': {}}
	result = v.validate(document)
	print(result)  # 打印 False
	print(v.errors)  # 打印 {'properties': [{'address': ['required field']}], 'test': ['unknown field']}


if __name__ == '__main__':
	main()
