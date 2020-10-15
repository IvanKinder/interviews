import time
import random

rand_list = [random.randint(0, 100) for i in range(1000)]

def multidel(my_list):  # сложность n^2
    new_list = []
    for el in my_list:
        if el not in new_list:
            new_list.append(el)
    return new_list

def multidel_v2(my_list):
    i = 0
    while True:
        if my_list[i] not in my_list[0:i]:
            print(i)
        else:
            break

    return my_list

t1 = time.time()
print(multidel(rand_list))
t2 = time.time()
print(f'func 1: {t2 - t1}')
t1 = time.time()
print(multidel_v2(rand_list))
t2 = time.time()
print(f'func 2: {t2 - t1}')