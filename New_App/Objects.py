import datetime
from abc import ABC
from enum import Enum


class MainObject(ABC):

    def __init__(self, subject, topic, name, text, date=None, class_type=None):
        self.class_type = class_type
        self.subject = subject
        self.topic = topic
        self.name = name
        self.text = text
        self.date = date
        if self.date is None:
            self.date = datetime.datetime.now().date()
        self.status = MainObject.Status.IN_PROGRESS
        self.end_date = None

    def end_object(self):
        self.status = MainObject.Status.DONE
        self.end_date = datetime.datetime.now().date()

    def __repr__(self):
        return f' {self.name} - {self.subject}'

    class Status(Enum):
        IN_PROGRESS = 'In progress'
        DONE = 'Done'


class Lesson(MainObject):

    def __init__(self, subject, topic, name, text):
        super().__init__(subject, topic, name, text)
        self.items = []

    class LessonItem(MainObject):

        def __init__(self, subject, topic, name, text, link=None):
            super().__init__(subject, topic, name, text)
            self.link = link

    def add_item(self, item_subject, item_topic, item_name, item_text, item_links):
        item = self.LessonItem(item_subject, item_topic, item_name, item_text, item_links)
        self.items.append(item)

    def percentage_progress(self):
        done_status_item = 0
        for item in self.items:
            if item.status == MainObject.Status.DONE:
                done_status_item += 1
        if done_status_item == 0:
            return 0
        else:
            return (done_status_item / len(self.items)) * 100


class FlashCard(MainObject):

    def __init__(self, subject, topic, name, text, read_once=None):
        super().__init__(subject, topic, name, text)
        self.read_once = read_once
        if self.read_once is None:
            self.read_once = 0
        if self.status == MainObject.Status.IN_PROGRESS:
            if self.read_once >= 10:
                self.status = MainObject.Status.DONE

    def mark_as_read(self):
        self.read_once += 1

    def reset(self):
        self.read_once = 0


class Task(MainObject):
    pass


obj = Lesson('tematPython', 'klasy i dziedziczenie', 'test1', 'dowolny text testowy')
obj.add_item('ItemSubject', 'ItemTopic', 'ItemName', 'ItemText', 'ItemLinks')
obj.add_item('ItemSubject22', 'ItemTopic22', 'ItemName22', 'ItemText22', 'ItemLinks22')
obj.items[0].end_object()

print(obj.percentage_progress())
print(obj.class_type)