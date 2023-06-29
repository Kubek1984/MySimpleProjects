from tkinter import *
from tkinter import ttk
from Task_object import *
import sys


class View:

    def __init__(self, controller):
        self.selected = None
        self.controller = controller
        self.root = Tk()
        self.root.geometry('550x550')
        self.root.config(bg='black')
        self.label_font = ('Verdana', 10, 'normal')
        self.label_font_color = 'white'
        self.button_font = ('Calibri', 11, 'normal')
        self.button_font_color = '#009999'
        self.bg = 'black'
        self.pad_x = 10
        self.pad_y = 10
        self.navigation: Frame = self.navigation_frame()
        self.navigation.grid(row=0, column=0)
        self.main_field: Frame = self.main_menu_frame()
        self.main_field.grid(row=0, column=1)
        self.current_selection_from_list = None

        self.root.mainloop()

    # ----------Frame's----------------#

    def navigation_frame(self):
        frame = Frame(self.root, width=200, height=500, bg=self.bg)
        show_list_button = Button(frame, text='Main Menu', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_main_menu)
        show_list_button.grid(pady=self.pad_y, padx=self.pad_x)
        add_task_button = Button(frame, text='Add Task', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_add_task)
        add_task_button.grid(pady=self.pad_y, padx=self.pad_x)
        # set_notification_button = Button(frame, text='Set Notification')
        # set_notification_button.grid()
        show_task_button = Button(frame, text='Show Task', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_show_task)
        show_task_button.grid(pady=self.pad_y, padx=self.pad_x)
        save_changes_button = Button(frame, text='Save changes', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_save_changes)
        save_changes_button.grid(pady=self.pad_y, padx=self.pad_x)
        quit_button = Button(frame, text='Quit', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_quit)
        quit_button.grid(pady=self.pad_y, padx=self.pad_x)
        return frame

    def add_task_frame(self):
        frame = Frame(self.root, width=200, height=500)
        task_label = Label(frame, text='Task name: ')
        task_label.grid(row=0, column=0)
        task_entry = Entry(frame)
        task_entry.grid(row=0, column=1)
        text_label = Label(frame, text='Text name: ')
        text_label.grid(row=1, column=0)
        text_field = Text(frame, width=20, height=20)
        text_field.grid(row=1, column=1)
        priority_label = Label(frame, text='Priority: ')
        priority_label.grid(row=2, column=0)
        values = self.controller.model.priority_list
        self.priority_combobox = ttk.Combobox(frame, values=values, state='readonly')
        self.priority_combobox.grid(row=2, column=1)
        self.priority_combobox.bind('<<ComboboxSelected>>', self.selected_item_from_combobox)
        submit_button = Button(frame, text='Submit', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0,
                               command=lambda: self.click_on_submit(task_entry.get(),
                                                                    text_field.get('1.0', 'end').strip(),
                                                                    self.selected))
        submit_button.grid(pady=self.pad_y, padx=self.pad_x)
        reset_button = Button(frame, text='Reset', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_add_task)
        reset_button.grid(pady=self.pad_y, padx=self.pad_x)
        return frame

    def main_menu_frame(self):
        frame = Frame(self.root, bg=self.bg)
        self.list_of_task = Listbox(frame, width=45, height=20, bg=self.bg, fg=self.label_font_color)
        for item in self.controller.model.task_object_dictionary.values():
            self.list_of_task.insert(END, item)
        self.list_of_task.grid()
        self.list_of_task.bind('<<ListboxSelect>>', self.select_item_from_listbox)
        edit_task_button = Button(frame, text='Edit Task', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_task_edit)
        edit_task_button.grid()
        delete_task_button = Button(frame, text='Delete Task', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_delete_task)
        delete_task_button.grid()
        return frame

    def task_edit_frame(self):
        frame = Frame(self.root, width=200, height=500)
        task_label = Label(frame, text='Task name: ')
        task_label.grid(row=0, column=0)
        task_entry = Entry(frame)
        task_entry.insert(END, self.current_selection_from_list.name)
        task_entry.grid(row=0, column=1)
        text_label = Label(frame, text='Text name: ')
        text_label.grid(row=1, column=0)
        text_field = Text(frame, width=20, height=20)
        text_field.insert(END, self.current_selection_from_list.text)
        text_field.grid(row=1, column=1)
        priority_label = Label(frame, text='Priority: ')
        priority_label.grid(row=2, column=0)
        values = self.controller.model.priority_list
        self.priority_combobox = ttk.Combobox(frame, values=values, state='readonly')
        self.priority_combobox.current(values.index(self.current_selection_from_list.priority))
        self.priority_combobox.grid(row=2, column=1)
        self.priority_combobox.bind('<<ComboboxSelected>>', self.selected_item_from_combobox)
        submit_edit_button = Button(frame, text='Submit', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0,
                                    command=lambda: self.click_on_submit_edit_task(self.current_selection_from_list,
                                                                                   task_entry.get(),
                                                                                   text_field.get('1.0', 'end').strip(),
                                                                                   self.selected))
        submit_edit_button.grid(padx=self.pad_x, pady=self.pad_y)
        reset_button = Button(frame, text='Reset', bg=self.bg, fg=self.button_font_color, font=self.button_font, borderwidth=4, highlightthickness=0, command=self.click_on_add_task)
        reset_button.grid(padx=self.pad_x, pady=self.pad_y)
        return frame

    def show_task_frame(self):
        frame = Frame(self.root, width=200, height=500)
        item = self.current_selection_from_list
        task_name = Label(frame, text=f'Task name : {item.name}\n')
        task_name.grid(padx=20, pady=20)
        task_text = Label(frame, text=f'Text : \n\t{item.text}\n\n')
        task_text.grid(padx=20, pady=20)
        data_label = Label(frame, text=f'Date : {item.date}\nPriority : {item.priority}')
        data_label.grid(pady=20, padx=20)

        return frame

    # ------------Click's on-------------------------#

    def click_on_add_task(self):
        # self.clear_main_field()
        self.main_field.grid_forget()
        self.main_field = self.add_task_frame()
        self.main_field.grid(row=0, column=1)

    def click_on_submit(self, name, text, priority):
        task_object = self.controller.make_object(name, text, priority)
        self.controller.save_object_in_database(task_object)
        self.controller.model.load_dictionary()
        # self.controller.add_task(task_object)
        # self.controller.save_dictionary()
        self.click_on_main_menu()

    def click_on_submit_edit_task(self, task_object, name, text, priority):
        self.submit_edit_task(task_object, name, text, priority)
        # self.controller.save_dictionary()
        self.click_on_main_menu()

    def click_on_main_menu(self):
        self.main_field.grid_forget()
        self.main_field = self.main_menu_frame()
        self.main_field.grid(row=0, column=1)

    def click_on_task_edit(self):
        self.main_field.grid_forget()
        self.main_field = self.task_edit_frame()
        self.main_field.grid(row=0, column=1)

    def click_on_delete_task(self):
        item = self.current_selection_from_list


        self.controller.delete_task(item.id)
        # self.controller.save_dictionary()
        self.click_on_main_menu()

    def click_on_show_task(self):
        self.main_field.grid_forget()
        self.main_field = self.show_task_frame()
        self.main_field.grid(row=0, column=1)

    def click_on_quit(self):
        save_or_not = self.controller.ask_save_changes_before_shut_down()
        if save_or_not == False:
            pass
            # Yes no alert
            # if yes:
            # save chcanges
        # self.root.after(3000, sys.exit)
        sys.exit()

    def click_on_save_changes(self):
        self.controller.save_dictionary()


    # ---------------Methods-------------------------#

    def clear_main_field(self):
        for child in self.main_field.winfo_children():
            child.destroy()

    def selected_item_from_combobox(self, event):
        if self.priority_combobox.get() == 'High':
            self.selected = 'High'
        elif self.priority_combobox.get() == 'Medium':
            self.selected = 'Medium'
        else:
            self.selected = 'Low'

    def select_item_from_listbox(self, event):

        # selected_index = self.list_of_task.curselection()
        # selected_item = self.list_of_task.get(selected_index)
        index_of_selected_item_in_list = self.list_of_task.curselection()[0]
        item = list(self.controller.model.task_object_dictionary.values())[index_of_selected_item_in_list]
        self.current_selection_from_list = item
        print(type(self.current_selection_from_list))

    def submit_edit_task(self, task_object, name, text, priority):
        if task_object.name != name:
            self.controller.set_name_task(task_object, name)
        if task_object.text != text:
            self.controller.set_text_task(task_object, text)
        if priority is not None and task_object.priority != priority:
            self.controller.set_priority_task(task_object, priority)
