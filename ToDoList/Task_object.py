import datetime

class Task_object:
    def __init__(self, name, text, priority, date = None):
        self.name = name
        self.text = text
        self.priority = priority
        self.date = date
        # self.notification = notification
        # self.state = state
        if self.date == None:
            self.date = datetime.datetime.now().date()

    def __repr__(self):
        space_nr = 25 - len(self.name)
        if self.priority == '1':
            return f'{self.name + (space_nr * " ")} \t {self.date} \tHIGH Priority'
        elif self.priority == '2':
            return f'{self.name + (space_nr * " ")} \t {self.date} \tLOW Priority'
        else:
            return f'{self.name + (space_nr * " ")} \t {self.date}'
