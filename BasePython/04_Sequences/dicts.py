# СЛОВАРИ

celebrity = {'name':'John Lennon','sex':1,'years':40,'work':'Musician','alive':False}
print(type(celebrity))
print(celebrity)

# распаковать словарь для вывода на консоль
print(*celebrity, sep='\n')

# вывод словаря в цикле
print()
for item in celebrity:
    print(item)

# в цикле просмотреть все ключи словаря и их значения
for key, val in celebrity.items():
    print('{} - {}'.format(key, val))

# доступ к значению по ключу
print(celebrity['name'])
print(celebrity['work'])

print()
# получить все ключи словаря
all_keys = celebrity.keys()
print(all_keys)

print()
# получить все значения словаря
all_vals = celebrity.values()
print(all_vals)

print()
# добавить новые элементы в словарь
celebrity.update({'wife':'Yoko Ono','mother':'Julia Lennon'})
# выдать на консоль
for key, val in celebrity.items():
    print('{} - {}'.format(key, val))

print()
# добавить список альбомов в виде вложенного словаря
celebrity.update({ 'albums':{'1971':'Imagine','1972':'Some Time In New York City',
                             '1974':'Walls And Bridges','1980':'Double Fantasy'} })
# выдать на консоль
for key, val in celebrity.items():
    print('{} - {}'.format(key, val))

print('\nДоступ по двум ключам:')
print(celebrity['albums']['1971'])

# удалить элемнет из списка
print()
years = celebrity.pop('years')
print(years)
# выдать на консоль
for key, val in celebrity.items():
    print('{} ~ {}'.format(key, val))

# полностью очистить словарь
print()
celebrity.clear()
print(celebrity)






