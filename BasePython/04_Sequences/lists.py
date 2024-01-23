# список покупок
shopping_list = ['Хлеб', 'Молоко', 'Сахар', 'Соль', 'Торт']
print(shopping_list)
print(shopping_list[2])
print(shopping_list[-2])
print(shopping_list[1:4])
sub_list = shopping_list[1:3]
print(sub_list)

# вывести элементы списка построчно
print(*shopping_list, sep='\n')

# вывести элементы списка построчно в цикле
for item_list in shopping_list:
    print('\u2022 {}'.format(item_list))

# вывести список методов объекта shopping_list
# print(*dir(shopping_list), sep='\n')

print()
# отсортировать список и вывести на консоль
shopping_list.sort()
print(*shopping_list, sep='\n')

print()
# отсортировать список в обратном порядке и вывести на консоль
shopping_list.reverse()
print(*shopping_list, sep='\n')

print()
# добавить два элемента в список
shopping_list.append('Сок')
shopping_list.append('Печенье')
print(*shopping_list, sep='\n')

# вставиь элемент в список на первое место (0-й индекс)
print()
shopping_list.insert(0, 'Варенье')
print(*shopping_list, sep='\n')

# удалить элемент
print()
shopping_list.remove('Сахар')
print(*shopping_list, sep='\n')

# подсчет количества одинаковых элементов в списке
print( '\nВсего: {}'.format( [5,3,2,7,9,1,6,2,9,4,6,2].count(2) ) )

# проверка наличия элемента search_element в списке any_list
def item_exists(any_list,search_element):
    # возвращает True, если количество элементов в списке больше нуля
    return  (any_list.count(search_element) > 0)

print()
salt = 'Соль'
# проверка наличия элемента в списке при помощи оператора in
if (salt in shopping_list):
    print('{} надо купить - она в списке'.format(salt))
else:
    print('{} не надо покупать - ее нет в списке'.format(salt))

print()
# узнать индекс элемента
print('Индекс {}'.format( shopping_list.index('Молоко') ))

print()
xalva = 'Халва'
if item_exists(shopping_list,xalva):
    print('Индекс {}'.format(shopping_list.index(xalva)))
else:
    print('Элемент "{}" в списке отсутствует'.format(xalva))

print()
# очистить список
shopping_list.clear()
print(shopping_list)

# список из элементов разного типа
mixed_list = ['Солнце', 5100, True, 'Дождь', 3.1415]
print()
for item in mixed_list:
    print('\u2022 {}'.format(item))

# многомерный список (3D)
list_3d = ['Омега Центавра', ['Альфа Центавра','Проксима Центавра'],
           'Солнечная система', ['Меркурий',
                                 'Венера',
                                 'Земля',['Луна'],
                                 'Марс', ['Фобос','Деймос'],
                                 'Юпитер', ['Европа','Ио','Ганимед','Каллисто'],
                                 'Сатурн', ['Мимас','Энцелад','Тефия','Диона','Рея','Титан','Япет'],
                                 'Уран', ['Миранда','Ариэль','Умбриэль','Титания','Оберон'],
                                 'Нептун',['Тритон','Нереида','Протей'],
                                 'Загадочная девятая'],
           'Сириус', ['Сириус A','Сириус B'],
           'Процион' ]

def print_list(lst,level=0):
    # табуляция в зависимости от уровня вложенности
    tab = '\t'*level
    # маркер элемента
    mark = ( ('\u25AA','\u25CB')[level==1], '\u25CF') [level == 0]
    for item in lst:
        # если текущий элемент - список
        if isinstance(item,(list,tuple)):
            print_list(item,level+1)
        else:
            print('{}{} {}'.format(tab,mark,item))

print('\nНекоторые звезды, их планеты и спутники планет')
print('----------------------------------------------')
print_list(list_3d)

print('\n------------------ КОРТЕЖИ ------------------')
simple_tuple = ('Север', 'Юг', 'Восток', 'Запад')
print(simple_tuple)

print('Найдено: {}'.format( simple_tuple.count('Восток') ))
print('Индекс: {}'.format( simple_tuple.index('Север') ))

geo_tuple = ('Австралия',
                'Америка',('Бразилия',
                           'Канада',
                           'Мексика',
                           'США',('Айдахо',
                                  'Индиана',
                                  'Калифорния', ('Лос-Анджелес','Сакраменто','Сан-Франциско'),
                                  'Монтана',
                                  'Техас')),
                'Африка', ('Ангола','Ботсвана','Гвинея','Конго','Сомали','ЮАР'),
                'Евразия', ('Великобритания',
                            'Германия',
                            'Индия',
                            'Китай',
                            'Россия', ('Алтай',
                                       'Бурятия', ('Гусиноозерск','Кяхта','Улан-Удэ'),
                                       'Дагестан',
                                       'Коми',
                                       'Мордовия',
                                       'Москва',
                                       'Татарстан', ('Бугульма','Елабуга','Набережные Челны','Казань'),
                                       'Чечня',
                                       'Чувашия'),
                            'Франция',
                            'Япония') )

print_list(geo_tuple)
