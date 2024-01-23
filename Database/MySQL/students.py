# список студентов
from mysql_class import MySqlDriver
from init import db_name, host, user, password

def table_list(db, table_name, title):
    # вывести таблицу
    query = f'SELECT * FROM {table_name}'
    rows = db.execute(query)
    print(title)
    for row in rows:
        print(row)
    print()

if __name__ == '__main__':
    # создать объект и подключить к базе
    db = MySqlDriver(host, db_name, user, password)

    # если подключение состоялось
    if db.connected():
        query = '''
        SELECT
            o_students.ID,
            o_students.FIO,
            r_faculties.SHORT_NAME,
            r_cities.Name,
            r_campuses.Corps,
            r_campuses.Address
        FROM o_students
        INNER JOIN r_cities ON o_students.CITY_ID = r_cities.ID    
        INNER JOIN r_faculties ON o_students.FACULTY_ID = r_faculties.ID
        INNER JOIN r_campuses ON o_students.CAMPUS_ID = r_campuses.ID
        '''

        # выполнить запрос
        rows = db.execute(query)
        if len(rows) > 0:
            title = ' # :         ФИО          :Факультет: Место проживания : Общежитие  :       Адрес'
            line = '-' * 87
            print('Список студентов')
            print(line)
            print(title)
            print(line)
            for row in rows:
                print(f'{row[0]:>2} : {row[1]:<20} : {row[2]:<7} : {row[3]:<16} : {row[4]:<10} : {row[5]:<30}')
            print(line)
        else:
            print('Нет данных, удовлетворяющих запросу')
            print(db.error())

    table_list(db, 'r_cities', 'Города')
    table_list(db, 'r_campuses', 'Общежития')
    table_list(db, 'r_faculties', 'Факультеты')

    # закрыть подключение
    db.close()