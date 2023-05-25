from tkinter import *

class View:
    def __init__(self):
        self.root = Tk()
        # self.root.geometry('1000x1000')
        # self.root.resizable(False, False)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_color = 'black'
        self.font_color = 'orange'
        self.root.configure(bg=self.bg_color)
        self.main_frame = self.welcome_frame()
        self.main_frame.grid()
        self.root.mainloop()
    def welcome_frame(self):
        self.clear_root()
        welcome_frame = Frame(self.root, bg='black')
        welcome_label = Label(welcome_frame,bg=self.bg_color, fg=self.font_color, text='Welcome Easy Learning App', font=('Arial', 22))
        welcome_label.grid()
        button_1 = Button(welcome_frame, text='text1')
        button_1.grid()
        button_2 = Button(welcome_frame, text='text2')
        button_2.grid()
        button_3 = Button(welcome_frame, text='text3')
        button_3.grid()
        return welcome_frame

    def clear_root(self):
        for child in self.root.winfo_children():
            child.destroy()
    def main_screen(self):
        self.main_screen_frame = Frame(self.root)
