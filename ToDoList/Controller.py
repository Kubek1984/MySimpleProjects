from Model import *
from View import *

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
    def add_task(self, task_object):
        self.model.add_task(task_object)
    def show_list(self):
        self.model.show_list()

    def set_notification_task(self, task, message):
        self.model.set_notification(task, message)

    def set_name_task(self, task, new_name):
        self.model.set_name_task(task, new_name)

    def set_append_text_task(self, task, additional_text):
        self.model.set_append_text_task(task, additional_text)

    def set_new_text_task(self, task, new_text):
        self.model.set_new_text_task(task, new_text)

    def set_priority_task(self, task, new_priority):
        self.model.set_priority_task(task, new_priority)

    def clear(self):
        self.model.clear()

    def delete_task(self, task_id):
        self.model.delete_task(task_id)


