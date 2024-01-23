# расбота с JSON и словарями
import json

# рекурсивная функция для вывода JSON-объекта
def print_json(dct,level=0):
    # табуляция в зависимисоти от уровня вложенности
    tab='\t'*level
    for key, item in dct.items():
        # если текущий элемент – справочник
        if isinstance(item,(dict)):
            print('{}{}: {}'.format(tab, key,'{'))
            print_json(item,level+1)
            print(tab, '}')
        # если текущий элемент – список
        elif isinstance(item,(list)):
            print('{}{}: {}'.format(tab, key, '['))
            for list_item in item:
                print(tab, '{')
                print_json(list_item,level+1)
                print(tab, '}')
            print('{}{}'.format(tab, ']'))
        else:
            print('{}{}: {}'.format(tab,key,item))



file_name = 'beatles.json'
try:
    js = json.load( open(file_name, encoding='utf-8') )
except json.decoder.JSONDecodeError:
    print(f'Ошибка при чтении JSON из файла {file_name}')
except FileNotFoundError:
    print(f'Файл {file_name} не найден')
else:
    print_json(js)
    print(js['response'])
    print(js['response']['count'])
    print(js['response']['items'][1])
    print(js['response']['items'][2]['name'])

print()
input('\nДля окончания работы нажмитек ENTER...')


