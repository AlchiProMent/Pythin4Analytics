# создать справочники
import psycopg2
from init import db_name, port, user_name, passwrd, host


def create_table(cursor, tab_name, fields_dict):
    # создать таблицу
    created = False
    fields = 'id integer PRIMARY KEY'
    # сгенерировать последовательность полей таблицы
    for name, fld_type in fields_dict.items():
        fields += f', {name} {fld_type}'
    query = f'CREATE TABLE {tab_name} ({fields})'
    try:
        cursor.execute(query)
    except:
        print(f'Ошибка при попытке создать таблицу {tab_name}')
    else:
        created = True
    return created


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
        create_table(cursor, 'r_campuses', {'CORPS':'text', 'ADDRESS':'text'})
        create_table(cursor, 'r_faculties', {'NAME':'text', 'SHORT_NAME':'text'})
        conn.commit()
        print('Базы данных созданы')

        # закрыть соединение
        cursor.close()
        conn.close()