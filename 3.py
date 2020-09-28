reques = []
with open('input3.txt', 'r') as i_f:
    for line in i_f.readlines():
        reques.append(line.split())
wishes = []
dev_num = reques[0][0]
print(dev_num)
req_num = reques[1][0]
print(req_num)
reques.pop(0)
reques.pop(0)
roo_num = reques[int(dev_num[0])-3]
reques.pop(reques.index(roo_num))
roo_num = roo_num[0]
print(roo_num)
wishes.append(reques[:int(req_num)-1])



print(reques)
print(wishes)
