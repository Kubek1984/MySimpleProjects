import mysql.connector

try:
    connection = mysql.connector.connect(host='db4free.net', database='carshop', user='newuser1234', password='password123')
    if connection.is_connected():
        cursor = connection.cursor()
        query = 'SELECT * FROM car;'
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        connection.close()
    else:
        print('something go wrong')
except:
    print('Error')


class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(host='db4free.net', database='carshop', user='newuser1234',password='password123')
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            self.connected = True
        else:
            self.connected = False

    def execute(self, query):
        if self.connected:
            self.cursor.execute(query)
            return self.cursor.fetchall()

    def stop(self):
        self.connection.close()

databaseManager = DatabaseManager()
cars = databaseManager.execute("SELECT * FROM car;")
print(cars)

databaseManager.stop()