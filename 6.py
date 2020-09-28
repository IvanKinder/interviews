workers = []
boths = {}
jobbers = {}
tmp = []
with open('input1.txt', 'r') as i_f:
    for line in i_f.readlines():
        workers.append(line.split())
for i in range(1, len(workers)):
    for k in range(int(workers[0][1])):
        print(workers[i])
        tmp = [a for a in workers[1:]*int(workers[0][1])]
    # for i in range(1, int(workers[0][0]) + 1):
    # for j in range(1, int(workers[0][0]) + 1):
    #     if str(workers[i]) != str(workers[j]):
    #         tmp = [workers[i], workers[j]]
    #         boths[str(tmp)] = tmp
print(tmp)
print(boths)
print(workers)
# for value in boths.values():
#     for i in range(int(workers[0][1]) - 1):
#         for j in range(int(workers[0][2])):
#             if int(value[i][j]) > int(value[i + 1][j]):
#                 value.append(int(value[i][j]))
#             else:
#                 value.append(int(value[i+1][j]))
#     value.append(0)
# for value in boths.values():
#     for i in value:
#         if type(i) is int:
#             value[-1] += i
#     value[-1] = value[-1]//2
# tmp = set()
# for value in boths.values():
#     tmp.add(value[-1])
# tmp = list(tmp)
# print(boths)
# tmp.sort(key=lambda x: -x)
# print(tmp)
# for key, value in boths.items():
#     if value[-1] == tmp[0]:
#         print(value[-1])
#         print(f'{workers.index(value[0])} {workers.index(value[1])}')
#         break