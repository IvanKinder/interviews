mas = []
tablets = {}
tab_mas = []
boxes = []
days = []
with open('input.txt', 'r') as i_f:
    for line in i_f.readlines():
        if line[-1] == '\n':
            mas.append(line[:-1].split())
        else:
            mas.append(line.split())
mas.pop(0)
for i in range(len(mas)):
    tablets[mas[i][0]] = [mas[i][1]]
for key, value in tablets.items():
    value.append(int(key) - 1)
def check(box, days, lost_days):
    if 0 < days <= lost_days:
        boxes.append(box)
        # print(lost_days)

for key, value in tablets.items():
    days.append(value[1])
days.sort(key=lambda x: -x)
iter = int(days[0])
for i in range(len(days)):
    for key, value in tablets.items():
        if value[1] == days[i] and (iter - int(value[1])) >= 0:
            check(key, value[1], days[i])
            # print(iter)
            # print(days[i])
for i in range(len(mas)):
    for j in boxes:
        if j in mas[i][0]:
            # print((mas[i]))
            print(mas.index(mas[i]))

# print(f'mas: {mas}')
# print(f'tablets: {tablets}')
# print(f'boxes: {boxes}')
# print(f'days: {days}')
