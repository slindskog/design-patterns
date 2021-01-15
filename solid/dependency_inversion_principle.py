# DIP
# High level classes should not depend on lower level classes instead they should depend on abstractions
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # Low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # High-level module
    def __init__(self, browser):
        for name in browser.find_all_children_of('John'):
            print(f"John has a child called {name}.")

    # Bad init - depends on relations being a list
    # def __init__(self, relationships):
    #    relations = relationships.relations
    #    for r in relations:
    #        if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #            print(f"John has a child called {r[2].name}.")


if __name__ == '__main__':
    parent = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)
