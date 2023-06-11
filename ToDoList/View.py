import sys


class View:
    def __init__(self, controller):
        self.controller = controller

        while True:
            self.controller.clear()
            print(
                '''
                    MENU
                    
                1. Add Task
                2. Show List
                3. Edit Task
                4. Delete Task
                5. Set Notification
                6. Save changes
                7. Quit
                ''')
            select = input('\nSelect option from 1 to 7: ')
            if select == '1':
                self.controller.clear()
                self.make_task_object()
            elif select == '2':
                self.controller.clear()
                self.controller.show_list()
                while True:
                    choice = input('\nPress Enter for Back to Menu or ID item for display task')
                    if choice == '':
                        break
                    elif choice.isdigit():
                        print()
                        print(controller.model.task_object_dictionary[int(choice)].name)
                        print(controller.model.task_object_dictionary[int(choice)].text)
            elif select =='4':
                self.delete_task_view()
            elif select == '3':
                self.controller.clear()
                self.edit_task_view()
            elif select == '5':
                pass
                # self.controller.clear()
                # self.set_notification()
            elif select == '6':
                self.controller.clear()
                self.controller.save_dictionary()

                # self.save_changes_callback()
            elif select == '7':
                sys.exit()
    def set_save_changes_callback(self, callback):
        self.save_changes_callback = callback


    def add_task_view(self):
        pass
    def make_task_object(self):
        name = input('\nType the name of Task: ')
        text = input('Type the text of Task: ')
        while True:
            priority = input('Chose One or Two. 1/2 ?:')
            if priority == '1' or priority == '2':
                break
            else:
                print('Priority must be One or Two . 1/ 2 .')
        task_object = self.controller.make_object(name, text, priority)
        self.controller.add_task(task_object)
    def edit_task_view(self):
        while True:
            self.controller.clear()
            print('\t\tEDIT TASK\n')
            self.controller.show_list()
            task_choice = int(input('\nType ID number for edit: '))
            task = self.controller.model.task_object_dictionary[task_choice]
            if task_choice not in self.controller.model.task_object_dictionary.keys():
                print('Unfortunately this ID does not exist. Press Enter to quit or Try again. ')
            else:
                self.controller.clear()
                print(f'''
                Edit item : {task_choice}. {task}
                Which value of task would you like to edit ?
                
                1. Name
                2. Text
                3. Priority
                4. Quit(back to menu)
                ''')
                choice = input('type number from 1 to 4: ')
                if choice == '1':
                    self.controller.clear()
                    while True:
                        new_name = input('Type new name of task : ')
                        if len(new_name.strip()) == 0 :
                            print('Can\'t be a empty record. Try again.')
                        else:
                            self.controller.set_name_task(task, new_name)
                            break
                elif choice == '2':
                    self.controller.clear()
                    while True:
                        text = input('Type new name of task : ')
                        if len(text.strip()) == 0 :
                            print('Can\'t be a empty record. Try again.')
                        else:
                            option = input('Would you like add to text to already exist text or delete old text and add new one? \n1. Add text, 2. New Text. select 1 or 2 : ')
                            if option == '1':
                                self.controller.set_append_text_task(task, text)
                            elif option =='2':
                                self.controller.set_new_text_task(task, text)
                            break
                elif choice == '3':
                    self.controller.clear()
                    while True:
                        priority = input('Type new number of priority : ')
                        if len(priority.strip()) == 0 :
                            print('Can\'t be a empty record. Try again.')
                        else:
                            self.controller.set_priority_task(task, priority)
                            break
                elif choice == '4':
                    break
            break

    def delete_task_view(self):
        while True:
            self.controller.clear()
            self.controller.show_list()
            delete_item = int(input('\nGive ID item for delete or press Q for quit : '))
            if delete_item not in self.controller.model.task_object_dictionary.keys():
                print('This Id number do not exist. Try again ')

            else:
                self.controller.delete_task(delete_item)
                self.controller.clear()
                self.controller.show_list()
                input('Press Enter to back Menu')
                break

