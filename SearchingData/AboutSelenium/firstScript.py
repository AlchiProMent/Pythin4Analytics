# Первый скрипт, иллюстрирующий работу с пакетом Selenium
#
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# получить драйвер
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# загрузить в браузер страницу
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
# установить задержку в 0,5 сек.
driver.implicitly_wait(0.5)

# получить строку ввода текста
text_box = driver.find_element(by=By.NAME, value='my-text')
# получить кнопку
button = driver.find_element(by=By.CSS_SELECTOR, value='button')

# симулировать ввод данных в поле
text_box.send_keys('Python')
# симулировать нажатие на кнопку Submit
button.click()

# получить ответно сообщение
message = driver.find_element(by=By.ID, value='message')
# вывести отзыв на экран
print(message.text)

driver.quit()
