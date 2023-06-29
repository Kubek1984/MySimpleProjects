import datetime
from enum import Enum


class Task_object:
    def __init__(self,name, text, priority, date=None, id=None):
        self.name = name
        self.text = text
        self.priority = priority
        self.date = date
        # self.notification = notification
        # self.state = state
        if self.date == None:
            date = datetime.datetime.now().date()
            self.date = date.strftime('%Y-%m-%d')
        self.id = id

    def __repr__(self):
        space_nr = 25 - len(self.name)
        if self.priority == 'High':
            return f'{self.name + (space_nr * " ")} \t {self.date} \tHigh Priority'
        elif self.priority == 'Medium':
            return f'{self.name + (space_nr * " ")} \t {self.date} \tMedium Priority'
        else:
            return f'{self.name + (space_nr * " ")} \t {self.date} \tLow Priority'

    # class Priority(Enum):
    #     HIGH = 'High'
    #     MEDIUM = 'Medium'
    #     LOW = 'Low'
