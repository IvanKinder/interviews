import csv

from openpyxl import Workbook, load_workbook


# утилита для экспорта данных задачи в файл
def export_to_file(task, fields, file_name):
    wb = Workbook()
    ws = wb.active
    ws.title = "Task"
    wb.save(filename=f'{file_name}.xlsx')

    filename = f'{file_name}.xlsx'
    wb = load_workbook(filename)
    file = wb.active

    file.append(fields)
    file.append([task.name, task.deadline, task.description, task.done, task.created_at, task.updated_at, task.is_active])

    wb.save(filename=filename)
