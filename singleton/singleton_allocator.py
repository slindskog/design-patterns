import random


class DataBase:
    _instance = None

    def __init__(self):
        _id = random.randint(0, 100)
        # init always called after __new__
        print('id = ', _id)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataBase, cls)\
                .__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':

    d1 = DataBase()
    d2 = DataBase()
    print(d1 == d2)
