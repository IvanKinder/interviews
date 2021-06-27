import csv


def export_to_csv(task, fields, titles, file_name):
    with open(f'{file_name}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

    if fields:
        headers = fields
        if titles:
            titles = titles
        else:
            titles = headers
    else:
        headers = []
        titles = headers

    writer.writerow(titles)
    data_to_export = [task.name, task.deadline, task.description, task.done, task.created_at, task.updated_at, task.is_active]
    writer.writerow(data_to_export)