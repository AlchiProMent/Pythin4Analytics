# пример работы с поисковиком
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

GOOGLE_URL = 'https://www.google.com'

# ПРИМЕЧАНИЕ ОКТЯБРЯ 2023 года.
# Google обновила драйвер главной страницы и теперь результаты поиска выводятся не постранично, а подгружаются по мере
# прокрутки страницы вниз. В связи с этим фрагмент даной программы, в которой ищется ссылка на следующую страницу
# по ID=pnnext, будет приводить к ошибке. В связи с чем я сделал новый модуль - goSearchNew.py, в котором устранил
# данную проблему путем прокрутки страницы вниз.


def print_links(urls, index):
    # вывести ссылки на консоль
    print(f'[ {index} ]')
    for link in urls:
        # получить URL
        url = link.get_attribute('href')
        # вывести адрес на консоль
        print(url)

def go_search(query_text, make_scr=False):
    # создать объект для настройки опций
    opts = Options()
    # установить стратегию загрузки
    opts.page_load_strategy = 'normal'
    # создать драйвер
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    # загрущить страницу
    driver.get(GOOGLE_URL)

    # получить строку ввода
    text_box = driver.find_element(by=By.NAME, value='q')
    # поместить запрос в строку ввода
    text_box.send_keys(query_text)
    # нажать на ENTER (RETURN)
    text_box.send_keys(Keys.RETURN)

    for i in range(1, 11):
        # задержка в 3 секунды
        driver.implicitly_wait(3)
        # сделать скриншот страницы
        if make_scr:
            driver.save_screenshot(f'scr/screen_{i:02}.png')
        # все ссылки, который Google выдал по запросу
        links = driver.find_elements(by=By.XPATH, value='//*[@class="yuRUbf"]/a')
        # вывести все ссыфлки страницы
        print_links(links, i)

                # получить ссылку на следующую страницу
        next_link = driver.find_element(by=By.ID, value='pnnext').get_attribute('href')
        # загрузить эту страницу
        driver.get(next_link)


    # закрыть драйвер и выйти
    driver.close()
    driver.quit()
if __name__ == '__main__':
    query_text = 'Алхимия'
    go_search(query_text, True)