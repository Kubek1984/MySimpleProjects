


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.category_list = ['Other']
        self.priority_list = ['Low', 'Medium', 'High', 'Extreme']

    def add_item_to_category_list(self, item):
        self.category_list.append(item)
    def import_category_list(self):
        pass
    def save_category_list(self):
        # with open('cat_list.txt', 'w') as fileobject:
            pass
    def selected_combobox_category(self, event):

        print('Working!!!', event)
        # print(self.controller.view.category_choice)

