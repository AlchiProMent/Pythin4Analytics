# функция-генератор последовательности дробей
def limit(first,last):
    for num in range(first,last):
        yield 1/num

# генерация последовательности от first до last и далее снова до first
def updown(first,last):
    yield from range(first, last)
    yield from range(last, first-1, -1)


squares = [ x**2 for x in range(1,21) ]

print('Квадраты целых чисел от 1 до 20:')
print(squares)

# генерация кортежа, состоящагео из степеней числа 2
powers_of_two_tuple = tuple( 2**x for x in range(21) )
print('Степени числа 2 с 0-й по 20-ю:')
print(powers_of_two_tuple)

# генерация кубов чисел от 1 до 10
keys_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
w_dict = { keys_list[x-1]: x*x*x for x in range(1,11) }
print('Словарь кубов чисел от 1 до 10:')
print(w_dict)

# получить значения по ключу
print(w_dict['two'])
print(w_dict['four'])
print(w_dict['eight'])

# использование генератора списка
sum1 = sum([ x**x for x in range(10) ])
# использование выражения генератор
sum2 = sum( x**x for x in range(10) )

print(f'sum1 = {sum1}')
print(f'sum2 = {sum2}')

# генератор заглавных символов латинского алфавита
alphabets = (chr(code) for code in range(65,65+26))
print(alphabets)
# вывести последовательность заглавных литер
for ch in alphabets:
    print(ch, end=' ')

print()
# вывести уменьшающуюся последовательность дробей
print( list( limit(1,15) ) )

# использование функции-генератора для задания последовательности цикла
for n in limit(1,15):
    print(n)

print( list(updown(1,12)) )


