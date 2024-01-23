# ИТЕРАТОРЫ И ГЕНЕРАТОРЫ
import math

# функция a-x-квадрат
def fx(x,a):
    return a*x*x

# Проверяет, делится ли num нацело на 3
def totally_div_by_three(num):
    return num % 3 == 0

# простейший список
lst = list ( range(1,11) )

for el in lst:
    print(el)

print()
for el in iter(lst):
    print('Элемент:',el)

# использование функции next()
iterator = iter(lst)
while True:
    try:
        element = next(iterator)
    except StopIteration:
        break
    else:
        print(f'>> {element} <<')

# вывод объекта, который вернула функция map()
print( map( math.factorial, lst ) )
# вывод списка в виде факториалов чисел из списка lst
print( list(map(math.factorial, lst)) )

x_list = list( range(5, 16) )
a_list = [10 for i in range(11)]

# расчитать и вывести результаты функции для массивов аргументов
print( list( map( fx, x_list, a_list ) ) )
print( list( map( lambda x, a: x*x*a, x_list, a_list ) ) )

# сформировать список чисел, которые нацело делятся на 3
# divisible_by_three = list( filter(totally_div_by_three, x_list) )
divisible_by_three = list( filter(lambda num: num % 3 == 0, x_list) )

print('Первоначальный список:')
print(x_list)
print('Отфильтрованный список:')
print(divisible_by_three)

# Оставить только строки, которые представляют из себя целые числа
print( list( filter( str.isdecimal, [ '12', '46-00', 'Автомобиль', '59', '3500', '356-200' ] ) ) )
print( list( filter( str.isdecimal, [ '12', '46-00', 'Автомобиль', '59', '3500', '356-200' ] ) ) )


