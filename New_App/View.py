from tkinter import *


class View:
    def __init__(self):

        self.root = Tk()
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_color = 'black'
        self.root.configure(bg=self.bg_color)
        self.menu_frame = self.menu_frame()
        self.menu_frame.grid(row=0, column=0)
        self.main_frame = self.main_window_frame()
        self.main_frame.grid(row=0, column=1)


        # self.root.mainloop()

    #---------------------Frame's-----------------------#

    def menu_frame(self):
        frame = Frame(self.root,bg='blue', width=700, height=800)
        add_flashcard_button = Button(self.root, text= 'Add Flashcard', command=self.click_on_add_flashcard)
        add_flashcard_button.grid()
        return frame

    def main_window_frame(self):
        frame = Frame(self.root, bg='lightblue', width=700, height=800)
        return frame

    def flashcard_frame(self):
        frame = Frame(self.root, bg='lightblue', width=700, height=800)
        name_label = Label(frame, text='Name : ')
        name_label.grid(row=0, column=0)
        name_entry = Entry(frame)
        name_entry.grid(row=0, column=1)
        text_label = Label(frame, text='Text : ')
        text_label.grid(row=1, column=0)
        text_entry = Text(frame)
        text_entry.grid(row=1, column=1)
        topic_label = Label(frame, text='Topic : ')
        topic_label.grid(row=2, column=0)
        topic_entry = Entry(frame)
        topic_entry.grid(row=2, column=1)
        subject_label = Label(frame, text='Subject : ')
        subject_label.grid(row=3, column=0)
        subject_entry = Entry(frame)
        subject_entry.grid(row=3, column=1)
        submit_button = Button(frame, text='Submit', command=lambda : self.click_on_submit_flashcard(subject_entry.get(), topic_entry.get(), name_entry.get(), text_entry.get('1.0', END)))
        submit_button.grid()
        return frame

    #-------------------------Click_On-----------------------------------#

    def click_on_add_flashcard(self):
        self.main_frame.grid_forget()
        self.main_frame = self.flashcard_frame()
        self.main_frame.grid(row=0, column=1)

    def click_on_submit_flashcard(self, subject, topic, name, text):
        self.make_flashcard_callback(subject, topic, name, text)




    #--------------callback's--------------------

    def set_making_flashcard_callback(self, callback):
        self.make_flashcard_callback = callback

    def confirm(self):
        self.root.mainloop()