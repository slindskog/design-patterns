

class Person:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name


class PersonFactory:

    id = 0

    @staticmethod
    def create_person(name):
        person = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return person
