# генераторы списков
from random import randint


# преобразовать строку в число, если она состоит только из цифр
def protect_int(sn):
    if sn.isdecimal():
        return int(sn)
    else:
        return sn


zero_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(zero_list)

another_zero_list = [0 for i in range(0, 100)]
print(another_zero_list)

new_list = [i for i in range(0, 100)]
print(new_list)

simple_list = list(range(0, 100))
print(simple_list)

# степени двойки
two_powers = [2 ** i for i in range(0, 10)]
print(two_powers)

another_list = [i * i for i in (2, 4, 8, 16, 32)]
print(another_list)

chars = [ch for ch in 'О сколько нам открытий чудных']
print(chars)

random_list = [randint(32, 65535) for i in range(100)]
print(random_list)

# создать список на основе random_list, оставив только числа, меньшие 5000
new_random = [element for element in random_list if element < 5000]
print(new_random)

# ввод списка чисел с клавиатуры
numbers = input('Введите числа через пробел: ').split()
print(numbers)

# преобразовать numbers в список целых чисел
# int_numbers = list( map(int, numbers) )
int_numbers = list(map(protect_int, numbers))
print(int_numbers)
numbers_lst = list(filter(lambda n: n % 2, list(map(lambda d: int(d) if d.isdecimal() else d, input('Снова введите числа: ').split()))))
print('При помощи lambda:')
print(numbers_lst)
