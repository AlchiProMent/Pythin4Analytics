# добавить таблицу для списка студентов
import psycopg2
from init import db_name, port, user_name, passwrd, host
from create_refs import create_table

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
        '''
        CREATE TABLE o_students(
                    id integer PRIMARY KEY,
                    fio text,
                    city_id integer REFERENCES r_cities(id),
                    camp_id integer REFERENCES r_campuses(id),
                    facult_id integer REFERENCES r_faculties(id)
        );
        '''
        if create_table(cursor, 'o_students', {'fio':'text',
                                               'city_id':'integer REFERENCES r_cities(id)',
                                               'camp_id':'integer REFERENCES r_campuses(id)',
                                               'facult_id':'integer REFERENCES r_faculties(id)'
                                               }):
            conn.commit()
            print('Таблица создана')
        else:
            print('При создании таблицы возникла ошибка!')

        # закрыть соединение
        cursor.close()
        conn.close()