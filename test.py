from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

url = 'https://afipochtovaya.ru/plans/search'
print(time.localtime())
driver = webdriver.Chrome()

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.title)

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
    j.append(float(j[6])/float(j[5]))
    print(j)
