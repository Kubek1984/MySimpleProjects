from Model import *
from View1 import *


class Controller:
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        # self.view.set_save_changes_callback(self.save_changes)

    def make_object(self, name, text, priority):
        task_object = self.model.make_object(name, text, priority)
        return task_object

    def save_dictionary(self):
        self.model.save_dictionary()

    def save_object_in_database(self, task):
        self.model.save_object_in_data_base(task)

    def set_name_task(self, task, new_name):
        self.model.set_name_task(task, new_name)

    def set_text_task(self, task, new_text):
        self.model.set_text_task(task, new_text)

    def set_priority_task(self, task, new_priority):
        self.model.set_priority_task(task, new_priority)

    def clear(self):
        self.model.clear()

    def delete_task(self, task_id):
        self.model.delete_task(task_id)

    def ask_save_changes_before_shut_down(self):
        compare = self.model.ask_save_changes_before_shut_down()
        return compare
