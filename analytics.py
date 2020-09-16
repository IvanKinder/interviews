import openpyxl
import numpy

wb = openpyxl.load_workbook('DDY.xlsx')
data_sheet = wb['данные за 2 кв.']

classes = {}
room_numbers = {}
for i in range(2, data_sheet.max_row + 1):
    classes[data_sheet.cell(row=i, column=53).value] = 0
    room_numbers[data_sheet.cell(row=i, column=11).value] = 0
for i in range(2, data_sheet.max_row + 1):
    if data_sheet.cell(row=i, column=53):
        classes[data_sheet.cell(row=i, column=53).value] += 1
    if data_sheet.cell(row=i, column=11):
        room_numbers[data_sheet.cell(row=i, column=11).value] += 1

room_s = {}
for i in range(2, data_sheet.max_row + 1):
    room_s[str(data_sheet.cell(row=i, column=53).value) + ' ' + str(data_sheet.cell(row=i, column=11).value)] = [0]
for i in range(2, data_sheet.max_row + 1):
    if data_sheet.cell(row=i, column=53) and data_sheet.cell(row=i, column=11):
        if str(data_sheet.cell(row=i, column=11).value) != 'None' and str(data_sheet.cell(row=i, column=53).value) != 'Нет такого корпуса':
            room_s[str(data_sheet.cell(row=i, column=53).value) + ' ' + str(data_sheet.cell(row=i, column=11).value)][0] += 1
            room_s[str(data_sheet.cell(row=i, column=53).value) + ' ' + str(data_sheet.cell(row=i, column=11).value)].append(data_sheet.cell(row=i, column=10).value)

print(f'Классы: {classes}')
print(f'Комнатность: {room_numbers}')
print(f'Комнатность по классам: {room_s}')

new_wb = openpyxl.Workbook()
n_sheet = new_wb.active
n_sheet.title = 'Лист1'

i = 2
n_sheet['A1'] = 'Комнатность'
n_sheet['B1'] = 'Куплено штук'
for key, value in room_numbers.items():
    if key is None:
        n_sheet.cell(row=i, column=1).value = 'Нет данных'
        n_sheet.cell(row=i, column=2).value = value
    else:
        n_sheet.cell(row=i, column=1).value = key
        n_sheet.cell(row=i, column=2).value = value
    i += 1

j = 2
n_sheet['E1'] = 'Класс'
n_sheet['F1'] = 'Куплено штук'
for key, value in classes.items():
    if key == 'Нет такого корпуса':
        n_sheet.cell(row=j, column=5).value = 'Нет данных'
        n_sheet.cell(row=j, column=6).value = value
    else:
        n_sheet.cell(row=j, column=5).value = key
        n_sheet.cell(row=j, column=6).value = value
    j += 1

k = 2
n_sheet['I1'] = 'Класс + комнатность'
n_sheet['J1'] = 'Куплено штук'
n_sheet['K1'] = 'Средняя площадь'
for key, value in room_s.items():
    if value[0] != 0 and key:
        n_sheet.cell(row=k, column=9).value = key
        n_sheet.cell(row=k, column=10).value = str(value[0])
        n_sheet.cell(row=k, column=11).value = str(round(numpy.mean(value[1:]), 1))
        k += 1

new_wb.save('analytics.xlsx')
