from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


ANIMALS_LIST = []
DICT_NUMS = {}

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")


i = 0
while True:
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        html_animals_list = soup.findAll('li')
        for tag in html_animals_list[2:202]:
            if ord(tag.text[0].lower()) > ord('я'):
                break
            ANIMALS_LIST.append(tag.text)
        driver.find_element_by_link_text('Следующая страница').click()
        i += 1
    except:
        break


letter = ord('а')


for animal in ANIMALS_LIST:
    DICT_NUMS[animal[0]] = []

for animal in ANIMALS_LIST:
    DICT_NUMS[animal[0]].append(animal)


for key, value in DICT_NUMS.items():
    print(f'{key}: {len(value)}')
