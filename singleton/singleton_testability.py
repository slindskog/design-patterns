import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        with open('capitols.txt', 'r') as fh:
            lines = fh.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = int(lines[i + 1].strip())
        print('Loading database')


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += DataBase().population[c]
        return result


# Do not want to use live database here
class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]


class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


class SingletonTests(unittest.TestCase):

    def test_is_singleton(self):
        db1 = DataBase()
        db2 = DataBase()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Tokyo', 'New Delhi']
        tp = rf.total_population(names)
        self.assertEqual(14200000 + 13929286, tp)

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(3, crf.total_population(['alpha', 'beta']))



if __name__ == '__main__':
    unittest.main()