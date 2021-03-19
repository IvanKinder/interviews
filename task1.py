"""Получение индекса списка сложность O(n)"""


def task(array):
    try:
        return array.index('0')
    except ValueError:
        return 'Нули не найдены'


print(task('11111111000'))
