#  coding: utf-8
#
#  Copyright (C) 2022-2022, Inc. All Rights Reserved
#
#  @Time    : 2022-12-22
#  @Author  : yan que
#  @Email   : yanquer@qq.com
#  @File    : t_cerberus_person.py
#  @Project : rst-document

from cerberus import Validator
from dataclasses import dataclass


@dataclass
class Person:
	name: str
	age: int


class PersonValidator(Validator):

	def validate_person(self, obj):
		return self.validate(obj.__dict__)


def main():
	schema = {
		'name': {'type': 'string', 'minlength': 2},
		'age': {'type': 'integer', 'min': 18, 'max': 65}
	}

	v = PersonValidator(schema)

	p = Person('John Doe', 2)

	if v.validate_person(p):
		print('valid data')
	else:
		print('invalid data')
		print(v.errors)


if __name__ == '__main__':
	main()
