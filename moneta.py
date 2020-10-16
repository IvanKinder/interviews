from scipy.stats import variation

arr = []


# N = int(input('Введите число подбрасываний: '))
def func(N):
    x = N / 2.1
    reshka = x
    orel = 1.1 * x
    for i in range(int(reshka)):
        arr.append(-1)
    for j in range(int(orel)):
        arr.append(1)
    return arr


print(arr)
N = 2
while variation(func(N), axis=0) <= 33:
    print(f'{variation(func(N), axis=0)} --- {N}')
    N += 500000
