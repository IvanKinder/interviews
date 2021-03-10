import sys
import random
from history import History
from time import time


def test_history(obj):
    sequense = [random.randint(1, 10000) for i in range(random.randint(2, 100))]

    def random_score():
        return random.random()

    if random_score() != 0:
        obj.set_history(sequense, random_score())
    else:
        test_history(obj)


obj = History()
times = []

if __name__ == '__main__':
    while sys.getsizeof(obj.history_arr) / 1024 <= 100:
        t1 = time()
        test_history(obj)
        t2 = time()
        times.append(t2 - t1)
    print(f'Среднее время выполнения set_history: {sum(times) / len(times)}')
    print(f'Общее количество дубликатов: {obj.dubles}')
    obj.save_history('')
    obj.load_history('')
    times = []
    while sys.getsizeof(obj.history_arr) / 1024 <= 200:
        t1 = time()
        test_history(obj)
        t2 = time()
        times.append(t2 - t1)
    print(f'Среднее время выполнения set_history после загрузки: {sum(times) / len(times)}')
    print(f'Общее количество дубликатов: {obj.dubles}')
