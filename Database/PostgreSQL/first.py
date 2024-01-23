# показать таблицы базы данных
import psycopg2
from init import db_name, port, user_name, passwrd, host


def view_table(tab_name):
    # вывести содержимое одной таблицы
    cursor.execute(f'SELECT * FROM {tab_name} ORDER BY id')
    rows = cursor.fetchall()
    print(tab_name)
    for row in rows:
        print(row)
    print()


if __name__ == '__main__':
    try:
        # подключение к базе данных
        conn = psycopg2.connect(dbname=db_name, port=port, user=user_name, password=passwrd, host=host)
    except Exception as e:
        # в случае ошибки вывести сообщение
        print(e)
    else:
        # создать курсор
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM INFORMATION_SCHEMA.TABLES')
        rows = cursor.fetchall()
        tables = []
        # сформировать список таблиц
        for row in rows:
            if row[1] == 'public':
                tables.append(row[2])

        # вывести содерижимое всех таблиц
        for tab in tables:
            view_table(tab)

        # закрыть соединение
        cursor.close()
        conn.close()