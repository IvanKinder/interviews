from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import re
import csv

url = 'https://afipochtovaya.ru/plans/search'
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

data = []
data1 = []
finally_data = []
for tag in soup.findAll('tr'):
    data.append(str(tag))

for d in data:
    if re.search('targ="\d', d):
        i = d.index('№')
        d = d[i:]
    tmp = ''
    for l in d:
        if l.isdigit() or l in ['c', ',']:
            if l == ',':
                tmp += '.'
            else:
                tmp += l
    data1.append(tmp)
data1.pop(0)
for d in data1:
    finally_data.append(d.split('c'))
for j in finally_data:
    while '' in j:
        j.remove('')
    if len(j) > 7:
        j.pop(-1)
    else:
        j.append(j[-1])
    j.append(int(float(j[6]) / float(j[5])))
    j.append(int(float(j[7]) / float(j[5])))

finally_data.insert(0, [soup.title.text])
finally_data.insert(0, [str(datetime.datetime.today())])
with open('1.csv', "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    for line in finally_data:
        writer.writerow(line)

for l in finally_data:
    print(l)
