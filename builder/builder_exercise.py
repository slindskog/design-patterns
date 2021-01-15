import unittest
from unittest import TestCase


class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'self.{self.name} = {self.value}'


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = [f'class {self.name}:']
        if not self.fields:
            lines.append('    pass')
        else:
            lines.append('    def __init__(self):')
            for f in self.fields:
                lines.append(f'        {f}')
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, _type, name):
        self.__class.fields.append(Field(_type, name))
        return self

    def __str__(self):
        return self.__class.__str__()


class Evaluate(TestCase):
    @staticmethod
    def preprocess(s=''):
        return s.strip().replace('\r\n', '\n')

    def test_empty(self):
        cb = CodeBuilder('Foo')
        self.assertEqual(
            self.preprocess(str(cb)),
            'class Foo:\n  pass'
        )

    def test_person(self):
        cb = CodeBuilder('Person').add_field('name', '""') \
            .add_field('age', 0)
        self.assertEqual(
            self.preprocess(str(cb)),
            """class Person:
            def __init__(self):
            self.name = \"\"
            self.age = 0"""
        )


if __name__ == '__main__':
    cb = CodeBuilder('Person')\
        .add_field('name', '""')\
        .add_field('age', '0')
    print(cb)
