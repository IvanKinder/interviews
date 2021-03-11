import sys
import random
from history import History
from time import time


def what_time(func):
    def wrapper():
        t1 = time()
        func()
        t2 = time()
        print(f'Общее время выполнения функции: {t2 - t1}')
    return wrapper


def test_history(obj):
    sequense = [random.randint(100, 10000000) for i in range(random.randint(10, 300000))]

    def random_score():
        return random.random()

    if random_score() != 0:
        obj.set_history(sequense, random_score())
    else:
        test_history(obj)


obj = History()


@what_time
def test_to_3_gb():
    print(sys.getsizeof(obj.history_arr) / 1024 / 1024 / 1024)
    times = []
    while sys.getsizeof(obj.history_arr) / 1024 / 1024 / 1024 < 3:
        t1 = time()
        test_history(obj)
        t2 = time()
        times.append(t2 - t1)
    obj.save_history('')
    print(f'Среднее время выполнения set_history: {sum(times) / len(times)}')
    print(f'Общее количество дубликатов: {obj.dubles}')


@what_time
def test_to_5_gb():
    obj = History.load_history('')
    times = []
    while sys.getsizeof(obj.history_arr) / 1024 / 1024 / 1024 < 5:
        t1 = time()
        test_history(obj)
        t2 = time()
        times.append(t2 - t1)
    obj.save_history('')
    print(f'Среднее время выполнения set_history после загрузки: {sum(times) / len(times)}')
    print(f'Общее количество дубликатов: {obj.dubles}')


if __name__ == '__main__':
    test_to_3_gb()
    test_to_5_gb()
