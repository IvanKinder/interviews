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
