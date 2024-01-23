rows = 8    # всего строка
cols = 32   # всего столбцов
# строки
for i in range(rows):
    s = ''
    # столбцы
    for j in range(cols):
        # вычислить код символа
        char_code = i * cols + j
        s = s + '\t' + ('#' + str(char_code), chr(char_code))[char_code > 31]
    print(s)

