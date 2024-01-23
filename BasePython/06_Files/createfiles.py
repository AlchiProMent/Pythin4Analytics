import os
file_name = 'datas/van_rossum.txt'
# чтение файла
try:
    with open(file_name) as f:
        txt = f.read().encode('1251')
except FileNotFoundError:
    print('Файл не найден!')
except OSError:
    print('Ошибка при чтении файла.')
else:
    print(txt.decode())

# разделительная линия
print('~'*55)

# данные телефонной книги для сохранения в файл
phones = [ [ 'Игорь', '+7-123-987-12-23', 18, 'Староста группы' ],
           [ 'Ольга', '+7-123-345-12-00', 17, 'Познакомились в кафе' ],
           [ 'Анатолий Ефремович', '+7-123-600-89-25', 36, 'Препод по статистике' ],
           [ 'Саня', '+7-123-129-11-22', 18, 'Друг' ],
           [ 'Таня', '+7-123-904-22-33', 18, 'На море' ],
           [ 'Василий Алибабаевич', '+7-123-800-23-72', 49, 'Заправщик с бензоколонки' ],
           [ 'Людмила Прокофьевна', '+7-123-765-43-21', 36, 'Начальник' ]
        ]

# символ-разделитель
CH_DELIM = '\u007C'

# функция для преобразования последовательности в строку
def data2str(d):
    # получить длину последовательности (количество элементов)
    total = len(d)
    s = ''
    # сформировать строку
    for i in range(0, total):
        # на последней итерации вместо разделителя ставить символ новой строки
        s = '{0}{1}{2}'.format( s, d[i], ('\n',CH_DELIM)[i < total-1] )
    return s

# проверка преобразования последовательности в строку
# for item in phones:
#    print( data2str(item), end='' )

def save2file(datas, file_name='anyfile.txt', reg='w'):
    try:
        with open(file_name, reg) as fw:
            for d in datas:
                fw.write( data2str(d) )
    except:
        return -1
    else:
        return 0

# сохранить справочник в файл
phones_book = 'datas/phones.txt'

if ( save2file(phones, phones_book, 'w') == 0 ):
    print('Данные успешно сохранены')
else:
    print('Произошла ошибка при попытке сохранить данные!')


# построчное чтение из файла
def read_from_file(file_name):
    # создать пустой список
    datas = []
    try:
        with open(file_name) as f:
            # чтение первой строки
            line = f.readline()
            while line:
                # убрать в строке возможные пробелы
                line = line.strip()
                # разбить строаку на подстроки по символу-разделителю
                flds = line.split( CH_DELIM )
                # добавить полученные список flds в качестве элемиента в список datas
                datas.append(flds)
                # чтение очередной строки
                line = f.readline()
    except FileNotFoundError:
        print('Файл "{}" не найден!'.format(file_name))
    else:
        return datas

# очистить список
phones.clear()
# прочитать данные из файла в список
phones = read_from_file(phones_book)
# вывести список на консоль
print(*phones, sep='\n')

# фнукция формирования записей справочника в удобочитаемом виде
def view_phones(phones):
    print('\n\nТелефонный справочник')
    print('-'*40)
    for abonent in phones:
        print('Имя: {}'.format(abonent[0]))
        print('Телефон: {}'.format(abonent[1]))
        print('Возраст: {}'.format(abonent[2]))
        print('Комментарий: {}'.format(abonent[3]))
        print('-' * 40)

# вывести справочник
view_phones(phones)

# добавить новые записи в файл
phones.clear()
phones.append([ 'Жорж Милославский', '+7-123-687-23-77 (3-62)', 45, 'Артист Больших и Малых театров' ])
phones.append([ 'Аня', '+7-123-700-45-72', 22, 'Знакомая' ])

if ( save2file(phones, phones_book, 'a') == 0 ):
    print('Данные успешно добавлены')
else:
    print('Произошла ошибка при попытке сохранить данные!')

# очистить список
phones.clear()
# прочитать данные из файла в список
phones = read_from_file(phones_book)
# вывести справочник
view_phones(phones)
