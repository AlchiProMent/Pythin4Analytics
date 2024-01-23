def unicodes(title='', begin_code=0, end_code=255, tab_cols=16):
    # вывод на консоль списка символов в виже таблиы размерностью rowsxtab_cols

    if (title != ''):
        print(title)

    # общее количество символов
    total_chars = end_code - begin_code + 1
    # всего строк
    rows = total_chars // tab_cols

    if (total_chars % tab_cols > 0):
        rows += 1

    # начальный код символа
    char_code = begin_code
    # строки
    for i in range(rows):
        s = ''
        # столбцы
        for j in range(tab_cols):
            # вычислить код символа
            s = s + '\t' + ('#' + str(char_code), chr(char_code))[char_code > 31]
            char_code += 1
        print(s)
    # прогон пустой строк
    print()


unicodes('Таблицы ASCII',0,255,32)
unicodes('Кириллица:',1040,1103,32)
unicodes('Разное:',9654,10062,16)