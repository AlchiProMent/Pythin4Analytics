# лямбда-выражения и лямбда-функции

def exp_cube(num):
    # возведение числа в куб
    return num * num * num

# проверить результат возведения в куб
print( exp_cube(2) )
print( exp_cube(4) )
print( exp_cube(12) )
print( exp_cube(121) )

print('Расчет при помощи лямбда-выражения:')
print( (lambda num: num*num*num)(2) )

print('Расчет при помощи лямбда-функции:')
l_cube = lambda num: num*num*num

print( l_cube(2) )
print( l_cube(4) )
print( l_cube(12) )
print( l_cube(121) )

# список чисел Фибоначчи
fibo_list = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946 ]

def divisible_by_five (num):
    # возвращает True, если число нацело делится на пять
    return num % 5 == 0

print('На 5 без остатка делятся числа Фибоначчи:')
print( list ( filter (divisible_by_five, fibo_list) ) )

print('На 5 без остатка делятся числа Фибоначчи (лямбда-выражение):')
print( list ( filter (lambda x: (x % 5 == 0), fibo_list) ) )


