from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


ANIMALS_LIST = []
DICT_NUMS = {}

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")

flag = True

while flag:
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        html_animals_list = soup.findAll('li')
        for tag in html_animals_list[2:202]:
            if ord(tag.text[0].lower()) > 1105:
                continue
            if tag.text[0] == 'A':
                flag = False
            ANIMALS_LIST.append(tag.text)
        driver.find_element_by_link_text('Следующая страница').click()
    except:
        break

driver.close()

for animal in ANIMALS_LIST:
    if 1072 <= ord(animal[0].lower()) <= 1105:
        DICT_NUMS[animal[0]] = []

for animal in ANIMALS_LIST:
    if 1072 <= ord(animal[0].lower()) <= 1105:
        DICT_NUMS[animal[0]].append(animal)

alphabet = [chr(i) for i in range(1072, 1104)]

for letter in alphabet:
    try:
        if letter == 'ж' and ('Ё' in DICT_NUMS.keys()):
            print(f'Ё: {len(DICT_NUMS["Ё"])}')
        print(f'{letter.capitalize()}: {len(DICT_NUMS[letter.capitalize()])}')
    except KeyError:
        pass
