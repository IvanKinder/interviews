def sqr_sum(array):
    new_arr = []
    bad_arr = []
    flag = True
    for el in array:
        if type(el) in (int, float, complex):
            new_arr.append(el * el)
        elif el.isdigit():
            new_arr.append(float(el) * float(el))
        else:
            bad_arr.append(el)
            flag = False
    if flag:
        return sum(new_arr)
    else:
        for el in bad_arr:
            print(f'Некорректный элемент: {el}')
        return -1
