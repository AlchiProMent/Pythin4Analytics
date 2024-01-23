# рекурсивные функции

def factorial(num):
    # факториал числа
    f = 1
    for n in range(1,num+1):
        f = f * n
    return f

# вывеси факториал числа
n = 6
print('Факториал', n, 'равно', factorial(n))

def rfactorial(num):
    # расчет факториала числа при помощи рекурсии
    if (num > 1):
        return num * rfactorial(num-1)
    else:
        return 1


# найти факториал числа при помощи рекурсии
n = 6
print('Факториал', n, 'равно', rfactorial(n))

