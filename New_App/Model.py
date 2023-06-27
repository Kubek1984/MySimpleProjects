from Objects import *


class Model:

    def __init__(self):
        self.main_dictionary = {}

    def load_dictionary(self):
        pass

    def make_flashcard_object(self, subject, topic, name, text):
        flashcard_object = FlashCard(subject, topic, name, text)
        print('Dziala')
        return flashcard_object

    def make_lesson_object(self, subject, topic, name, text):
        lesson_object = Lesson(subject, topic, name, text)
        return lesson_object

    def make_lesson_item_object(self, lesson_object, item_subject, item_topic, item_name, item_text, item_links):
        lesson_object.add_item( item_subject, item_topic, item_name, item_text, item_links)

    def add_object_to_dictionary(self, item_object):
        pass

    def save_dictionary(self):
        pass

    def edit_object(self):
        pass

    def delete_object(self):
        pass


