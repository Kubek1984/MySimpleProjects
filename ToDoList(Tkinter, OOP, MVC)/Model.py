from Task_object import *
import platform
import os
class Model:
    def __init__(self, controller):
        self.controller = controller
        self.task_object_dictionary = {}
        self.load_dictionary()
        self.archive_task_dictionary ={}
        self.priority_list = [item for item in Task_object.Priority]

    def set_name_task(self, task, new_name):
        task.name = new_name

    def set_notification(self, task, message):
        task.notification = message

    def set_new_text_task(self, task, new_text):
        task.text = new_text

    def set_append_text_task(self, task, additional_text):
        task.text += ('\n' + additional_text)

    def set_priority_task(self, task, new_priority):
        task.priority = new_priority

    def add_task(self, task_object):
        if len(self.task_object_dictionary) > 0:
            id = self.highest_id_in_dictionary() + 1
        else:
            id = 1
        self.task_object_dictionary[id] = task_object
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
        self.task_object_dictionary.pop(task_id)

    def save_dictionary(self):
        with open('DataBase.txt', 'w') as fileobject:
            for k, v in self.task_object_dictionary.items():
                format_string_date = v.date.strftime('%Y-%m-%d')
                text_without_new_lines = v.text.replace('\n', '$$$')
                fileobject.write(f'{k};;;{v.name};;;{text_without_new_lines};;;{v.priority};;;{format_string_date}\n')

    def load_dictionary(self):
        self.task_object_dictionary.clear()
        with open('DataBase.txt', 'r') as fileobject:
            for line in fileobject:
                object_list = line.split(';;;')
                if len(object_list) == 5:
                    id = object_list[0].strip()
                    name = object_list[1]
                    unformated_text = object_list[2]
                    text = unformated_text.replace('$$$', '\n')
                    priority = object_list[3]
                    if priority == 'Priority.HIGH':
                        priority = Task_object.Priority.HIGH
                    elif priority == 'Priority.MEDIUM':
                        priority = Task_object.Priority.MEDIUM
                    else:
                        priority = Task_object.Priority.LOW
                    date_str = datetime.datetime.strptime(object_list[4].strip(), '%Y-%m-%d').date()
                    task = Task_object(name.strip(), text.strip(), priority, date = date_str)
                    self.task_object_dictionary[int(id)] = task

    def clear(self):
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def ask_save_changes_before_shut_down(self):
        new_dict = {}
        with open('DataBase.txt', 'r') as fileobject:
            for line in fileobject:
                object_list = line.split(';;;')
                if len(object_list) == 5:
                    id = object_list[0].strip()
                    name = object_list[1]
                    unformated_text = object_list[2]
                    text = unformated_text.replace('$$$', '\n')
                    priority = object_list[3]
                    if priority == 'Priority.HIGH':
                        priority = Task_object.Priority.HIGH
                    elif priority == 'Priority.MEDIUM':
                        priority = Task_object.Priority.MEDIUM
                    else:
                        priority = Task_object.Priority.LOW
                    date_str = datetime.datetime.strptime(object_list[4].strip(), '%Y-%m-%d').date()
                    task = Task_object(name.strip(), text.strip(), priority, date = date_str)
                    new_dict[int(id)] = task
        # print(new_dict == self.task_object_dictionary)
        return new_dict == self.task_object_dictionary
