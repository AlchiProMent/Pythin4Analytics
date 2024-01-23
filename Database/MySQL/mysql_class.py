# класс для работы с базой данных
import mysql.connector

class MySqlDriver:
    def __init__(self, host, db_name, user_name, user_pass):
        # подключение к базе во время создания объекта
        try:
            # подключиться к базе данных
            self.__cnx = mysql.connector.connect(user=user_name, password=user_pass,
                                          host=host, database=db_name)
        except Exception as ex:
            self.__error = ex
            self._connected = False
        else:
            self.__error = ''
            self.__connected = self.__cnx.is_connected()
            if self.__connected:
                self.__cursor = self.__cnx.cursor()
            else:
                self.__cursor = None

    def close(self):
        # закрыть соединение
        self.__cnx.close()

    def error(self):
        # сообщение об ошибке (если есть)
        return self.__error

    def connected(self):
        # сообшает, что имеется подключение
        return self.__connected

    def execute(self, query):
        # выполнить запрос
        rows = []
        if self.__connected:
            try:
                result = self.__cursor.execute(query)
            except Exception as ex:
                self.__error = ex
            else:
                rows = self.__cursor.fetchall()
        return rows

    def executemany(self, query, data):
        # множественное добавление
        rows = []
        if self.__connected:
            try:
                result = self.__cursor.executemany(query, data)
            except Exception as ex:
                self.__error = ex
            else:
                self.commit()
        return rows


    def commit(self):
        self.__cnx.commit()



