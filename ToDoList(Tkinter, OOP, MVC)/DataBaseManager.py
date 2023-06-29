import mysql.connector
import datetime

class DataBaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='db4free.net', database='object_items', username='szogun', password='password1234')
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

# name = 'aaaaaa'
# text = 'aaaaaa'
# priority = 'aaaaa'
# date_now = datetime.datetime.now().date()
# # print(type(date_now))
# date_now_string = date_now.strftime('%Y-%m-%d')
# print(type(date_now_string))
x=DataBaseManager()
# x.execute(f'INSERT INTO task(name, text, priority, date) VALUES({name}, {text}, {priority}, {date_now_string});')

# query = f"INSERT INTO 'task' ('id', 'name', 'text', 'priority') VALUES (NULL, {name}, {text}, {priority});"
# x.execute(f"INSERT INTO `task` (`id`, `name`, `text`, `priority`, `date`) VALUES (NULL, '{name}', '{text}', '{priority}', '{date_now_string}');")

# x.execute(f"INSERT INTO `task` (`id`, `name`, `text`, `priority`) VALUES (NULL, 'sdsdf', 'dfsdf', 'dsfsdfsd');")
# "INSERT INTO `task` (`id`, `name`, `text`, `priority`, `date`) VALUES (NULL, 'Testing task', 'random text', 'High', '2023-06-27');"
# x.commit()
# result = x.execute("SELECT * FROM task;")
# print(result)
# x.execute('DELETE FROM `task` WHERE `task`.`id` = 3 ')
# x.commit()
result1 = x.execute("SELECT * FROM task;")
print(result1)
