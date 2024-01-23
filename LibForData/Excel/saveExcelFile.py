# Сохранение данных в Excel-файл
#
import pandas as pnd

NAME_FILE = 'test.xlsx'

# создать структуры для каждого листа
df1 = pnd.DataFrame({'city': ['Москва', 'Санкт-Петербург', 'Владимир', 'Рязань', 'Новгород'],
                     'area': [2561, 1439, 137, 224, 90],
                     'population': [13000, 5600, 349, 528, 224]})

df2 = pnd.DataFrame({'Имя': ['Бах, Иоганн Себастьян', 'Моцарт, Вольфганг Амадей', 'Рахманинов, Сергей Васильевич'],
                     'Страна': ['Тюрингия', 'Австрия', 'Россия'],
                     'Стиль': ['Оркестровая и камерная музыка, орган',
                               'Оперы, Скрипичные и фортепианные концерты',
                               'Фортепианные концерты']})

# создать словарь листов
sheets = {'Города':df1, 'Композиторы':df2}

try:
    with pnd.ExcelWriter(NAME_FILE, mode='a', if_sheet_exists='overlay') as writer:
        for sheet in sheets.keys():
            # одбавить лист в файл
            sheets[sheet].to_excel(writer, sheet_name=sheet, index=False)

except:
    print('Ошибка при попытке сохранить данные!')
else:
    print('Данные успещно сохранены.')
