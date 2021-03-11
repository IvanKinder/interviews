import sys
import random
from history import History
from time import time


def test_history(obj):
    sequense = [random.randint(1000000, 100000000) for i in range(random.randint(100, 10000))]

    def random_score():
        return random.random()

    if random_score() != 0:
        obj.set_history(sequense, random_score())
    else:
        test_history(obj)


obj = History()
obj.history_arr = [i for i in range(10000000)]


def test_to_3_gb():
    times = []
    while sys.getsizeof(obj.history_arr) / 1024 / 1024 / 1024 < 3:
        print(sys.getsizeof(obj.history_arr) / 1024 / 1024 / 1024)
        for i in range(10000000):
            obj.history_arr.append(i)
        t1 = time()
        test_history(obj)
        t2 = time()
        times.append(t2 - t1)
        obj.save_history('')
    print(f'Среднее время выполнения set_history: {sum(times) / len(times)}')
    print(f'Общее количество дубликатов: {obj.dubles}')


def test_to_5_gb():
    obj = History.load_history('')
    times = []
    while sys.getsizeof(obj.history_arr) / 1024 / 1024 / 1024 < 5:
        print(sys.getsizeof(obj.history_arr) / 1024 / 1024 / 1024)
        for i in range(10000000):
            obj.history_arr.append(i)
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
