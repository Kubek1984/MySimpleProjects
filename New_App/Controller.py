from Model import *
from View import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def make_flashcard(self):
