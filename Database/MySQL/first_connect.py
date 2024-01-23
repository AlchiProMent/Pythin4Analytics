# демонстрация подключения
import mysql.connector
from init import db_name, host, user, password

if __name__ == '__main__':
    try:
        # подключение к базе данных
        con = mysql.connector.connect(user=user, password=password,host=host, database=db_name)
    except Exception as e:
        # вывести ошибку
        print(e)
    else:
        if con.is_connected():
            with con.cursor() as cursor:
                # запрос
                query = 'SELECT * FROM o_students'

                # выполнить запрос
                try:
                    result = cursor.execute(query)
                except:
                    print('Ошибка при выполнении запроса')
                else:
                    # получить результат запроса
                    rows = cursor.fetchall()
                    if len(rows) > 0:
                        # построчный вывод данных на экран
                        for row in rows:
                            print(row)
                    else:
                        print('Нет данных')
    finally:
        # закрыть подключение к базе данных
        con.close()

