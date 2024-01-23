s = 'Строковый тип'
def view_list(*args):
    print()
    for a_s in args:
        print(a_s)

view_list('Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье')
view_list(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
view_list('Север',2020,200.5,True,'Арбуз')

def view_n_list(**kwargs):
    print()
    for key, val in kwargs.items():
        print(key,': [',val,']')

view_n_list(brand='Sony',year=2018,price=1000.50)

vacuum_cleaner_brand = 'AnyName'
discount = 0.15
price = 10000.00
print('На пылесосы {0} действует скидка {1}% Стоимость пылесоса со скидкой: {2}'.
      format(vacuum_cleaner_brand,
             round(discount*100),
             price*(1-discount)))

s = 'Строка'
n = 12345
f = 200.55
b = True
full_str = 'булев: {3}, строковый: {0}, дробный: {2}, целочисленный: {1}'.format(s,n,f,b)
print(full_str)

print('{0}, {0}, {0}, {0}, {0}'.format(123))
print('{}, {}, {}, {}, {}'.format(1,2,'Три',True,'Пять'))
print('{}{}'.format('Строка1','Строка2'))


print()
# форматирование матрицы степеней чисел
for i in range(1,11):
    for j in range(1,11):
        print('{:>12}'.format(i**j),end=('\n',' ')[j<10])

print('десятичный:{0:d}\nдвоичный:{0:b}\n8-ричный:{0:o}\n16-ричный:{0:X}\nс плавающей точкой:{0:10.2f}'.format(32767))

# расчет зарплаты на руки с  учетом налога
income = 50000.00   # сумма без вычета налога
tax = 0.13          # процент налога
amount_in_hand = income * (1.0-tax)

print('\nДоход: {:,.2f}\nНалог: {:.2%}\nСумма на руки: {:,.2f}'.format(income,tax,amount_in_hand))

# таблица умножения
horizontal_line = '-'*73
print('\n{:^73}\n'.format('Таблица умножения'))
# формирование строк
for i in range(0,11):
    # формирование одной строки
    for j in range(0,11):
        # одна итерация цикла формирует одну ячейку таблицы
        if (i==0):
            # формирование строки с номерами столбцов
            print(('{:>6}'.format(j), ' '*3)[j == 0], end=('\n', ' ')[j < 10])
        else:
            if (j > 0):
                # формирование ячейки для результата умножения номера строки на номер столбца
                print('{:>6}'.format(j*i),end=('\n', ' ')[j < 10])
            else:
                # формирвоание очередного номера строки в левом столбце
                print('{:>2}'.format(i), end=' ')
    if (i == 0):
        # верхняя разделительная линия
        print(horizontal_line)
# нижняя разделительная линия
print(horizontal_line)
