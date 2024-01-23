# добавление записей
from mysql_class import MySqlDriver
from init import db_name, host, user, password

if __name__ == '__main__':
    # создать объект и подключить к базе
    db = MySqlDriver(host, db_name, user, password)

    # если подключение состоялось
    if db.connected():
        data = [['Химический','ХФ'], ['Философский','ФиФ'], ['Астрономический','АФ']]
        query = "INSERT INTO r_faculties (NAME, SHORT_NAME) VALUES (%s, %s)"
        # выполнить запрос с множественным добавлением
        print('Выполняется добавление...')
        db.executemany(query, data)

        if db.error() == '':
            print('Данные успешно обновлены')
        else:
            print(db.error())

    # закрыть подключение
    db.close()