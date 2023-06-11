from Model import Model
from View import View

class Controller:
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def get_category_list(self):
        return self.model.category_list

    def on_select_category_combobox(self, event):
        # category = self.view.category_choice
        self.model.selected_combobox_category(event)

    def get_priority_list(self):
        return self.model.priority_list