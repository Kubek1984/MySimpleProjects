from tkinter import *


class View:
    def __init__(self):

        self.root = Tk()
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_color = 'black'
        self.root.configure(bg=self.bg_color)
        self.menu_frame = self.menu_frame()
        self.menu_frame.grid(row=0, column=0)
        self.main_frame = self.main_frame()
        self.main_frame.grid(row=0, column=1)


        self.root.mainloop()

    #---------------------Frame's-----------------------#

    def menu_frame(self):
        frame = Frame(self.root,bg='blue', width=700, height=800)
        add_flashcard_button = Button(self.root, text= 'Add Flashcard', command=click_on_add_flashcard)
        add_flashcard_button.grid()
        return frame

    def main_frame(self):
        frame = Frame(self.root, bg='lightblue', width=700, height=800)
        return frame

    def flashcard_frame(self):
        frame = Frame(self.root, bg='lightblue', width=700, height=800)

        return frame

    #-------------------------Click_On-----------------------------------#

    def click_on_add_flashcard(self):

View()