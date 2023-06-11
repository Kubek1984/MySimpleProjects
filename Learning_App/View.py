from tkinter import *
from tkinter import ttk

class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        # self.root.geometry('1000x1000')
        # self.root.resizable(False, False)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_color = 'black'
        self.font_color = 'orange'
        self.root.configure(bg=self.bg_color)
        self.frame_1 = self.welcome_frame()
        self.frame_1.grid(row=0, column=0)
        self.frame_2 = self.asside_frame()
        self.frame_2.grid(row=1, column=0)
        self.frame_3 = self.main_frame()
        self.frame_3.grid(row=0, column=1, rowspan=2)
        self.category_choice = None
        self.priority_choice = None
        self.root.mainloop()
    def welcome_frame(self):
        self.first_frame = Frame(self.root, bg='red', width=500, height=450)
        self.first_frame.grid_propagate(False)
        add_new_button = Button(self.first_frame, text='Add New Topic', width=50, command=self.click_on_add_new_topic)
        add_new_button.grid(padx=20, pady=20)

        return self.first_frame

    def click_on_add_new_topic(self):
        # self.clear_main_frame()
        self.frame_3.grid_forget()
        self.frame_4 = self.add_new_frame()
        self.frame_4.grid_propagate(False)
        self.frame_4.grid(row=0, column=1, rowspan=2)

    def add_new_frame(self):
        self.add_new = Frame(self.root, bg='blue', width=700, height=800)
        # self.add_new.grid_propagate(False)
        # self.add_new.grid(row=0, column=1, rowspan=2)
        self.category_label = Label(self.add_new, text='Category: ')
        self.category_label.grid(row=0, column=0, pady=10, padx=10)
        self.category_combo = ttk.Combobox(self.add_new, state="readonly", textvariable=self.category_choice, values=self.controller.get_category_list())
        self.category_combo.grid(row=0, column=1, pady=10, padx=10)
        self.category_combo.bind('<<ComboboxSelected>>', self.controller.on_select_category_combobox)
        self.category_label_2 = Label(self.add_new, text='Category: ')
        self.category_label_2.grid(row=1, column=0, pady=10, padx=10)
        self.category_label_2_entry = Entry(self.add_new)
        self.category_label_2_entry.grid(row=1, column=1, pady=10, padx=10)
        self.add_new_label = Label(self.add_new, text='Name: ')
        self.add_new_label.grid(row=3, column=0, pady=10, padx=10)
        self.add_new_entry = Entry(self.add_new)
        self.add_new_entry.grid(row=3, column=1, pady=10, padx=10)
        self.text_label = Label(self.add_new, text='Text: ')
        self.text_label.grid(row=4, column=0, pady=10, padx=10)
        self.text = Text(self.add_new, width=50, height=20)
        self.text.grid(row=4, column=1, pady=10, padx=10)
        self.flash_card_label = Label(self.add_new, text='Flashcard: ')
        self.flash_card_label.grid(row=5, column=0, pady=10, padx=10)
        self.flash_card = Text(self.add_new, width=50, height=6)
        self.flash_card.grid(row=5, column=1, pady=10, padx=10)
        self.priority_label = Label(self.add_new, text='Priority: ')
        self.priority_label.grid(row=6, column=0, pady=10, padx=10)
        self.priority_combo = ttk.Combobox(self.add_new, state="readonly", textvariable=self.priority_choice,
                                           values=self.controller.get_priority_list())
        self.priority_combo.grid(row=6, column=1, pady=10, padx=10)
        self.priority_combo.bind('<<ComboboxSelected>>', self.controller.on_select_category_combobox)


        return self.add_new
    def asside_frame(self):
        self.second_frame = Frame(self.root, bg='orange', width=500, height=450)
        self.second_frame.grid_propagate(False)
        # welcome_label = Label(welcome1_frame, bg=self.bg_color, fg=self.font_color, text='Welcome Easy Learning App',
        #                       font=('Arial', 22))
        # welcome_label.grid()

        return self.second_frame

    def main_frame(self):
        self.third_frame = Frame(self.root, bg='green', width=700, height=800)
        self.third_frame.grid_propagate(False)

        return self.third_frame

    def clear_root(self):
        for child in self.root.winfo_children():
            child.destroy()
    def clear_welcome_frame(self):
        for child in self.first_frame.winfo_children():
            child.destroy()

    def clear_asside_frame(self):
        for child in self.second_frame.winfo_children():
            child.destroy()

    def clear_main_frame(self):
        for child in self.third_frame.winfo_children():
            child.destroy()