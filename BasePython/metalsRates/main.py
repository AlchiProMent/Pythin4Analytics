# получение данных из веб-страницы
from urllib.request import urlopen
import re

# страница со стоимостью дграгоценных металлов
url = 'https://cbr.ru/hd_base/metall/metall_base_upto/'

# подключение к документу
response = urlopen(url)

# прочитать документ
webdoc = response.read()

# декодировать
html = webdoc.decode()

# регулярное выражение
pattern = r'(\d{2}\.\d{2}\.\d{4})\D+' \
          r'([\d\s]*\d{2,3},\d{4})\D+' \
          r'([\d\s]*\d{2,3},\d{4})\D+' \
          r'([\d\s]*\d{2,3},\d{4})\D+' \
          r'([\d\s]*\d{2,3},\d{4})'

# откомпилировать
regex = re.compile(pattern)

# получить данные
golds = regex.findall(html)

# вывести на консоль
line = '-'*55
print(line)
print('   Дата    |  Золото  | Серебро |   Платина  | Палладий')
print(line)
for gold in reversed(golds):
    print('{} | {} | {} | {} | {}'.format(gold[0],gold[1],gold[2],gold[3],gold[4]))
print(line)




