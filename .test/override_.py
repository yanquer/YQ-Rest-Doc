#  coding: utf-8
#
#  Copyright (C) 2022-2022, Inc. All Rights Reserved
#
#  @Time    : 2022-12-29
#  @Author  : yan que
#  @Email   : yanquer@qq.com
#  @File    : override_.py
#  @Project : new_doc_rst
#

class Father(object):
	name = 'father'

	def eat(self, fruit: str):
		print(f'{self.name} eat {fruit}')


class SonOne(Father):
	name = 'son one'

	def eat(self, fruit: str):
		print(f'{self.name} eat {fruit}')


class SonTwo(Father):
	name = 'son two'

	def eat(self, fruit: str, other):
		print(f'{self.name} eat {fruit}, {other}')


class SonThree(Father):
	name = 'son three'

	def eat(self, fruit, other=None):
		print(f'{self.name} eat {fruit}, {other}')


def main():
	father = Father()
	son_one, son_two, son_three = SonOne(), SonTwo(), SonThree()

	father.eat('apple')             # father eat apple
	son_one.eat('apple')            # son one eat apple
	son_two.eat('apple', 'rice')    # son two eat apple, rice
	son_three.eat('apple', 'rice')  # son three eat apple, rice


if __name__ == '__main__':
	main()
