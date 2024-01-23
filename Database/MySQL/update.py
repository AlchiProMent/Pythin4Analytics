# обновить данные
from mysql_class import MySqlDriver
from init import db_name, host, user, password

if __name__ == '__main__':
    # создать объект и подключить к базе
    db = MySqlDriver(host, db_name, user, password)

    # если подключение состоялось
    if db.connected():
        query = 'UPDATE o_students SET FIO="Белоусова Д.А." WHERE ID=2'
        db.execute(query)
        db.commit()
        print('Изменения внесены')

    # закрыть подключение
    db.close()