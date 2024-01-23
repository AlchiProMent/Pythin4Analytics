# поиск ошибки в программе

# список русских броненсоцев начала XX века
battleships = ['Бородино', 'Император Алексндр III', 'Орел', 'Князь Суворов', 'Слава']

# добавить в список два элемента
battleships.append('Князь Потемкин-Таврический')
battleships.append('Цесаревич')

# отсортировать список
battleships.sort()

# получить размерность списка
# len_list = len(battleships) - 1
len_list = len(battleships)

# вывести на консоль весь список
# for i in range(1, len_list):
for i in range(0, len_list):
    print(battleships[i])
