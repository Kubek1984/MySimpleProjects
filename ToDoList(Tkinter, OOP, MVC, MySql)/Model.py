from Task_object import *
import platform
import os
from DataBaseManager import *
class Model:
    def __init__(self, controller):
        self.controller = controller
        self.task_object_dictionary = {}
        self.load_dictionary()
        self.archive_task_dictionary ={}
        self.priority_list = ['Low', 'Medium', 'High']
    def set_name_task(self, task, new_name):
        sql_field = 'name'
        self.update_task_in_sql_database(task, sql_field, new_name)
        self.load_dictionary()


    def set_text_task(self, task, new_text):
        sql_field = 'text'
        self.update_task_in_sql_database(task, sql_field, new_text)
        self.load_dictionary()
    def update_task_in_sql_database(self, task,sql_field, update_parametr):
        db = DataBaseManager()
        db.execute(f'UPDATE task SET {sql_field}="{update_parametr}" WHERE id={task.id}')
        db.commit()
        db.close()
    def set_append_text_task(self, task, additional_text):
        task.text += ('\n' + additional_text)

    def set_priority_task(self, task, new_priority):
        sql_field = 'priority'
        self.update_task_in_sql_database(task, sql_field, new_priority)
        self.load_dictionary()

    # def add_task(self, task_object):
    #     if len(self.task_object_dictionary) > 0:
    #         id = self.highest_id_in_dictionary() + 1
    #     else:
    #         id = 1
    #     self.task_object_dictionary[id] = task_object
    def highest_id_in_dictionary(self):
        highest = 0
        for key in self.task_object_dictionary.keys():
            if key > highest:
                highest = key
        return highest
    def make_object(self, name, text, priority):
        task_object = Task_object(name, text, priority)
        return task_object

    def show_list(self):
        for key, value in self.task_object_dictionary.items():
            print(f'{key}: {value}.')

    def delete_task(self, task_id):
        db = DataBaseManager()
        db.execute(f'DELETE FROM `task` WHERE `task`.`id` = {task_id}')
        db.commit()
        db.close()
        self.load_dictionary()
    def save_object_in_data_base(self, object_for_saving):
        db = DataBaseManager()
        name = object_for_saving.name
        text = object_for_saving.text
        priority = object_for_saving.priority
        date = object_for_saving.date
        db.execute(f"INSERT INTO `task` (`id`, `name`, `text`, `priority`, `date`) VALUES (NULL, '{name}', '{text}', '{priority}', '{date}');")
        db.commit()
        db.close()
    def save_dictionary(self):
        # with open('DataBase.txt', 'w') as fileobject:
        #     for k, v in self.task_object_dictionary.items():
        #         format_string_date = v.date.strftime('%Y-%m-%d')
        #         text_without_new_lines = v.text.replace('\n', '$$$')
        #         fileobject.write(f'{k};;;{v.name};;;{text_without_new_lines};;;{v.priority};;;{format_string_date}\n')
        pass
    def load_dictionary(self):
        # self.task_object_dictionary.clear()
        # with open('DataBase.txt', 'r') as fileobject:
        #     for line in fileobject:
        #         object_list = line.split(';;;')
        #         if len(object_list) == 5:
        #             id = object_list[0].strip()
        #             name = object_list[1]
        #             unformated_text = object_list[2]
        #             text = unformated_text.replace('$$$', '\n')
        #             priority = object_list[3]
                    # if priority == 'Priority.HIGH':
                    #     priority = Task_object.Priority.HIGH
                    # elif priority == 'Priority.MEDIUM':
                    #     priority = Task_object.Priority.MEDIUM
                    # else:
                    #     priority = Task_object.Priority.LOW
        self.task_object_dictionary.clear()
        db = DataBaseManager()
        list_of_task_tuples_from_data_base = db.execute('SELECT * FROM task')
        for item in list_of_task_tuples_from_data_base:
            id = item[0]
            name = item[1]
            text = item[2]
            priority = item[3]
            date = item[4]

            task = Task_object(name.strip(), text.strip(), priority.strip(), date, id=id)
            self.task_object_dictionary[int(id)] = task

    def clear(self):
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def ask_save_changes_before_shut_down(self):
        new_dict = {}
        # with open('DataBase.txt', 'r') as fileobject:
        #     for line in fileobject:
        #         object_list = line.split(';;;')
        #         if len(object_list) == 5:
        #             id = object_list[0].strip()
        #             name = object_list[1]
        #             unformated_text = object_list[2]
        #             text = unformated_text.replace('$$$', '\n')
        #             priority = object_list[3]
                    # if priority == 'Priority.HIGH':
                    #     priority = Task_object.Priority.HIGH
                    # elif priority == 'Priority.MEDIUM':
                    #     priority = Task_object.Priority.MEDIUM
                    # else:
                    #     priority = Task_object.Priority.LOW
                    # date_str = datetime.datetime.strptime(object_list[4].strip(), '%Y-%m-%d').date()
                    # task = Task_object(name.strip(), text.strip(), priority.strip(), date = date_str)
                    # new_dict[int(id)] = task
        db = DataBaseManager()
        list_of_task_tuples_from_data_base = db.execute('SELECT * FROM task')
        for item in list_of_task_tuples_from_data_base:
            id = item[0]
            name = item[1]
            text = item[2]
            priority = item[3]
            date = item[4]

            task = Task_object(name.strip(), text.strip(), priority.strip(), date, id=id)
            new_dict[int(id)] = task


        return new_dict == self.task_object_dictionary
