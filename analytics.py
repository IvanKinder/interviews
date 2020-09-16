import openpyxl
import numpy as np
import matplotlib.pyplot as plt

wb = openpyxl.load_workbook('DDY.xlsx')

data_sheet = wb['данные за 2 кв.']

classes = {}
room_numbers = {}
for i in range(2, data_sheet.max_row):
    classes[data_sheet.cell(row=i, column=53).value] = [0]
    room_numbers[data_sheet.cell(row=i, column=11).value] = [0]

for i in range(2, data_sheet.max_row):
    if data_sheet.cell(row=i, column=53):
        classes[data_sheet.cell(row=i, column=53).value][0] += 1
    if data_sheet.cell(row=i, column=11):
        room_numbers[data_sheet.cell(row=i, column=11).value][0] += 1
print(classes)
print(room_numbers)

new_wb = openpyxl.Workbook()
n_sheet = new_wb.active
n_sheet.title = 'Лист1'

i = 2
n_sheet['A1'] = 'Комнатность'
n_sheet['B1'] = 'Куплено штук'
for key, value in room_numbers.items():
    if key is None:
        n_sheet.cell(row=i, column=1).value = 'Нет данных'
        n_sheet.cell(row=i, column=2).value = value[0]
    else:
        n_sheet.cell(row=i, column=1).value = key
        n_sheet.cell(row=i, column=2).value = value[0]
    i += 1

j = 2
n_sheet['E1'] = 'Класс'
n_sheet['F1'] = 'Куплено штук'
for key, value in classes.items():
    if key == 'Нет такого корпуса':
        n_sheet.cell(row=j, column=5).value = 'Нет данных'
        n_sheet.cell(row=j, column=6).value = value[0]
    else:
        n_sheet.cell(row=j, column=5).value = key
        n_sheet.cell(row=j, column=6).value = value[0]
    j += 1

new_wb.save('analytics.xlsx')
