# добавить значения в справочники
import psycopg2
from init import db_name, port, user_name, passwrd, host


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

        # добавить данные

        data = [[0, 'нет', ''],
                [1, 'Корпус 1', 'ул.Синеухова, 23'],
                [2, 'Корпус 2', 'ул.Чипполино, 45'],
                [3, 'Корпус A', 'ул.Синеухова, 32']]
        query = 'INSERT INTO r_campuses (ID, CORPS, ADDRESS) VALUES (%s, %s, %s)'
        cursor.executemany(query, data)

        cursor = conn.cursor()
        data = [[1, 'Биологический', 'ФБ'],
                [2, 'Гуманитарных наук', 'ФГН'],
                [3, 'Информационных технологий', 'ФИТ'],
                [4, 'Прикладной арифметики', 'ФПА'],
                [5, 'Промышленной механики', 'ФПМ']]
        query = 'INSERT INTO r_faculties (ID, NAME, SHORT_NAME) VALUES (%s, %s, %s)'
        cursor.executemany(query, data)

        conn.commit()
        # закрыть соединение
        cursor.close()
        conn.close()