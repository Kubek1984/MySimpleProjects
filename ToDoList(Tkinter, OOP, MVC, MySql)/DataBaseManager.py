import mysql.connector
import datetime


class DataBaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='db4free.net', database='object_items', username='szogun',
                                                      password='password1234')
            if self.connection.is_connected():
                self.connected = True
                print('Connection working properly')
                self.cursor = self.connection.cursor()
            else:
                self.connected = False
        except:
            print('Connection Failed')

    def close(self):
        self.connection.close()

    def execute(self, query):
        if self.connected:
            self.cursor.execute(query)
            # self.connection.commit()
            return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
