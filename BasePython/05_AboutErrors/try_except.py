# обработка исключительных ситуаций при помощи try

# делимое
dividend = 1000.00
# делитель
divider = 4**3 - 64

try:
    # частное
    quotient = dividend / divider
except ZeroDivisionError:
    print('На ноль делить нельзя!')

# проверка ввода
total = 0
min_val = 100
try:
    # total = int ( input('Введите целое число, большее {}: '.format(min_val)) )
    total = 500
except ValueError:
    print('Надо ввести число!')
else:
    if (total > min_val):
        print('Вы ввели корректное число.')
    else:
        print('Надо ввести число, большее {}'.format(min_val))

# вложенные try
week = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
try:
    # ind = int( input('Введите номер дня недели: ') )
    ind = 1
    # человек вводит номер, начиная от 1, а Python начинает счет с 0
    ind = ind - 1

    # проверка индекса
    try:
        print( week [ind] )
    except IndexError:
        print('Вы ввели неверный номер!')

except ValueError:
    print('Надо ввести номер!')

print()
solar_system = ['Меркурий','Венера','Земля','Марс','Юпитер','Сатурн','Уран','Нептун']
try:
    # ind = int ( input('Введите номер планеты: ') )
    ind = 3
    ind = ind - 1
    print(solar_system[ind])
    print(100/ind)
except IndexError:
    print('Планет всего восемь!')
except ValueError:
    print('Надо ввести номер!')
except:
    print('Другая ошибка')


# использование секции finally
try:
    pass
finally:
    solar_system.clear()

# функция, в которой инициируется прерывание
def any_func(v1=1,v2=20):
    if (v2 > v1):
        raise ValueError ('Второй параметр не должен быть больше первого!')
    return ( v1 - v2 )

print()
try:
    print( any_func(50,100) )
except ValueError as e:
    # print(*e.args, sep=' ')
    print(e.args[0])


