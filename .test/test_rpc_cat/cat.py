# coding: utf-8
from typing import Dict


class Cat(object):

    _name: str = 'cat'
    _age: int = 1
    _love: tuple = ('eat', 'play', 'drink', )
    _eat_food_once: Dict[str, float] = {
        'apple': 0.1,
        'rice': 0.3,
        'water': 0.1,
    }

    def name(self) -> str:
        return self._name

    def age(self) -> int:
        return self._age

    def love(self) -> tuple:
        return self._love

    def eat_food_once(self):
        return self._eat_food_once

    def get_attr_by_name(self, name: str):
        attr = getattr(self, f'_{name}', None)
        if attr:
            return attr

    def all_attr(self):
        return {
            'name': self._name,
            'age':  self._age,
            'love': self._love,
            'food_once': self._eat_food_once,
        }




