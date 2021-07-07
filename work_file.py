import time
import random

rand_list = [random.randint(0, 100) for i in range(10000)]


def multidel(my_list):  # сложность O(n^2)
    new_list = []
    for el in my_list:
        if el not in new_list:
            new_list.append(el)
    return new_list


def multidel_v2(my_list):  # сложность O(n)
    my_dict = {}
    for el in my_list:
        my_dict[el] = 0
    return list(my_dict.keys())


if __name__ == "__main__":
    t1 = time.time()
    print(multidel(rand_list))
    t2 = time.time()
    print(f'func 1 time: {t2 - t1}')
    t1 = time.time()
    print(multidel_v2(rand_list))
    t2 = time.time()
    print(f'func 2 time: {t2 - t1}')
