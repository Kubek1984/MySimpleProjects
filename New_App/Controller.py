from Model import *
from View import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view.set_making_flashcard_callback(self.make_flashcard)
        self.view.confirm()
    def make_flashcard(self, subject, topic, name, text):
        return self.model.make_flashcard_object(subject, topic, name, text)
