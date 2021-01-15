

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class DataBase:
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    # Only calls initializer once
    d1 = DataBase()
    d2 = DataBase()
    print(d1 == d2)
